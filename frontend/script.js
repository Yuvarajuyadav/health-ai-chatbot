const API_URL = "http://127.0.0.1:8000/chat"; 
 
const input = document.getElementById("messageInput"); 
const chatBox = document.getElementById("chatBox"); 
const languageSelect = document.getElementById("language"); 
const voiceStatus = document.getElementById("voiceStatus"); 
 
 
// ========================================== 
// LANGUAGE CODES 
// ========================================== 
 
const speechLanguages = { 
    english: "en-IN", 
    hindi: "hi-IN", 
    telugu: "te-IN", 
    french: "fr-FR" 
}; 
 
 
// ========================================== 
// SEND MESSAGE 
// ========================================== 
 
async function sendMessage() { 
 
    const message = input.value.trim(); 
 
    if (message === "") { 
        return; 
    } 
 
    // Show user message 
    addUserMessage(message); 
 
    // Clear input 
    input.value = ""; 
 
    try { 
 
        const response = await fetch(API_URL, { 
 
            method: "POST", 
 
            headers: { 
                "Content-Type": "application/json; charset=UTF-8" 
            }, 
 
            body: JSON.stringify({ 
 
                message: message, 
 
                // Used mainly for voice recognition. 
                // Backend detects typed-message language. 
                language: languageSelect.value 
            }) 
        }); 
 
 
        // ========================================== 
        // CHECK SERVER RESPONSE 
        // ========================================== 
 
        if (!response.ok) { 
            throw new Error( 
                `Server returned ${response.status}` 
            ); 
        } 
 
 
        const data = await response.json(); 
 
 
        // ========================================== 
        // SUCCESS 
        // ========================================== 
 
        if (data.success) { 
 
            // Display bot response 
            addBotResponse(data); 
 
            // Speak response in detected language 
            speakText( 
                data.response, 
                data.language 
            ); 
 
        } 
 
 
        // ========================================== 
        // SYMPTOM NOT FOUND 
        // ========================================== 
 
        else { 
 
            addBotMessage( 
                data.response || 
                getNotFoundMessage(languageSelect.value) 
            ); 
 
        } 
 
    } 
 
    // ========================================== 
    // CONNECTION ERROR 
    // ========================================== 
 
    catch (error) { 
 
        console.error("Error:", error); 
 
        addBotMessage( 
            "⚠️ Unable to connect to the Health AI server. Please make sure FastAPI is running." 
        ); 
    } 
} 
 
 
// ========================================== 
// USER MESSAGE 
// ========================================== 
 
function addUserMessage(message) { 
 
    const div = document.createElement("div"); 
 
    div.className = "user message"; 
 
    div.innerHTML = ` 
        <strong>👤 You:</strong> 
        <p>${escapeHTML(message)}</p> 
    `; 
 
    chatBox.appendChild(div); 
 
    scrollToBottom(); 
} 
 
 
// ========================================== 
// SIMPLE BOT MESSAGE 
// ========================================== 
 
function addBotMessage(message) { 
 
    const div = document.createElement("div"); 
 
    div.className = "bot message"; 
 
    div.innerHTML = ` 
        <strong>🤖 Bot:</strong> 
        <p>${escapeHTML(message)}</p> 
    `; 
 
    chatBox.appendChild(div); 
 
    scrollToBottom(); 
} 
 
 
// ========================================== 
// FULL BOT RESPONSE 
// ========================================== 
 
function addBotResponse(data) { 
 
    const div = document.createElement("div"); 
 
    div.className = "bot message"; 
 
 
    let precautionsHTML = ""; 
 
 
    if ( 
        data.precautions && 
        data.precautions.length > 0 
    ) { 
 
        precautionsHTML = ` 
 
            <strong>⚠️ Precautions:</strong> 
 
            <ul class="precautions"> 
 
                ${data.precautions 
                    .map( 
                        item => 
                            `<li>${escapeHTML(item)}</li>` 
                    ) 
                    .join("")} 
 
            </ul> 
        `; 
    } 
 
 
    div.innerHTML = ` 
 
        <strong>🤖 Bot:</strong> 
 
        <h3> 
            ${escapeHTML(data.title)} 
        </h3> 
 
        <p> 
            ${escapeHTML(data.response)} 
        </p> 
 
        ${precautionsHTML} 
 
    `; 
 
 
    chatBox.appendChild(div); 
 
    scrollToBottom(); 
} 
 
 
// ========================================== 
// TEXT TO SPEECH 
// ========================================== 
 
function speakText(text, language) { 
 
    if (!("speechSynthesis" in window)) { 
        return; 
    } 
 
 
    const speech = 
        new SpeechSynthesisUtterance(text); 
 
 
    // Backend detected language 
    speech.lang = 
        speechLanguages[language] || "en-IN"; 
 
 
    speech.rate = 0.9; 
 
    speech.pitch = 1; 
 
 
    // Stop previous speech 
    window.speechSynthesis.cancel(); 
 
    window.speechSynthesis.speak(speech); 
} 
 
 
// ========================================== 
// VOICE RECOGNITION 
// ========================================== 
 
function startVoiceRecognition() { 
 
    const SpeechRecognition = 
        window.SpeechRecognition || 
        window.webkitSpeechRecognition; 
 
 
    if (!SpeechRecognition) { 
 
        voiceStatus.textContent = 
            "❌ Voice recognition is not supported in this browser."; 
 
        return; 
    } 
 
 
    const recognition = 
        new SpeechRecognition(); 
 
 
    // ========================================== 
    // MICROPHONE LANGUAGE 
    // ========================================== 
 
    recognition.lang = 
        speechLanguages[languageSelect.value]; 
 
 
    recognition.continuous = false; 
 
    recognition.interimResults = false; 
 
 
    voiceStatus.textContent = 
        "🎤 Listening..."; 
 
 
    recognition.start(); 
 
 
    // ========================================== 
    // VOICE RESULT 
    // ========================================== 
 
    recognition.onresult = function(event) { 
 
        const transcript = 
            event.results[0][0].transcript; 
 
 
        input.value = transcript; 
 
 
        voiceStatus.textContent = 
            "✅ Voice captured"; 
 
 
        // Automatically send 
        sendMessage(); 
    }; 
 
 
    // ========================================== 
    // VOICE ERROR 
    // ========================================== 
 
    recognition.onerror = function(event) { 
 
        console.error( 
            "Voice error:", 
            event.error 
        ); 
 
 
        voiceStatus.textContent = 
            "❌ Voice recognition failed."; 
    }; 
 
 
    // ========================================== 
    // VOICE END 
    // ========================================== 
 
    recognition.onend = function() { 
 
        setTimeout(() => { 
 
            voiceStatus.textContent = ""; 
 
        }, 2000); 
    }; 
} 
 
 
// ========================================== 
// ENTER KEY 
// ========================================== 
 
function handleEnter(event) { 
 
    if (event.key === "Enter") { 
 
        event.preventDefault(); 
 
        sendMessage(); 
    } 
} 
 
 
// ========================================== 
// SCROLL CHAT 
// ========================================== 
 
function scrollToBottom() { 
 
    chatBox.scrollTop = 
        chatBox.scrollHeight; 
} 
 
 
// ========================================== 
// NOT FOUND MESSAGE 
// ========================================== 
 
function getNotFoundMessage(language) { 
 
    const messages = { 
 
        english: 
            "Sorry, I don't have information about that symptom yet.", 
 
        hindi: 
            "क्षमा करें, मेरे पास अभी उस लक्षण के बारे में जानकारी नहीं है।", 
 
        telugu: 
            "క్షమించండి, ఆ లక్షణం గురించి నా దగ్గర ఇంకా సమాచారం లేదు.", 
 
        french: 
            "Désolé, je n'ai pas encore d'informations sur ce symptôme." 
    }; 
 
 
    return messages[language] || messages.english; 
} 
 
 
// ========================================== 
// SECURITY 
// ========================================== 
 
function escapeHTML(text) { 
 
    const div = 
        document.createElement("div"); 
 
    div.textContent = text; 
 
    return div.innerHTML; 
}