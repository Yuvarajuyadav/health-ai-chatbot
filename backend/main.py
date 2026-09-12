from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()
# ==========================================
# REQUEST MODEL
# ==========================================

class ChatRequest(BaseModel):
    message: str
    language: str = "english"


# ==========================================
# CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================
# HEALTH DATA
# ==========================================


health_data = {

    # ======================================
    # 1. HEADACHE
    # ======================================

    "headache": {
        "keywords": {
            "english": ["headache", "head pain"],
            "hindi": ["सिरदर्द", "सर दर्द"],
            "telugu": ["తలనొప్పి"],
            "french": ["mal de tête", "céphalée"]
        },

        "english": {
            "title": "Headache",
            "response": "Headaches can have many causes such as stress, dehydration, lack of sleep, or eye strain.",
            "precautions": [
                "Drink enough water",
                "Get adequate rest",
                "Take breaks from screens",
                "Avoid skipping meals"
            ]
        },

        "hindi": {
            "title": "सिरदर्द",
            "response": "सिरदर्द के कई कारण हो सकते हैं, जैसे तनाव, पानी की कमी, नींद की कमी या आंखों पर अधिक दबाव।",
            "precautions": [
                "पर्याप्त पानी पिएं",
                "पर्याप्त आराम करें",
                "स्क्रीन से बीच-बीच में ब्रेक लें",
                "भोजन न छोड़ें"
            ]
        },

        "telugu": {
            "title": "తలనొప్పి",
            "response": "తలనొప్పికి ఒత్తిడి, నీటి కొరత, నిద్రలేమి లేదా కళ్లపై ఒత్తిడి వంటి అనేక కారణాలు ఉండవచ్చు.",
            "precautions": [
                "తగినంత నీరు తాగండి",
                "తగినంత విశ్రాంతి తీసుకోండి",
                "స్క్రీన్ నుండి మధ్యలో విరామం తీసుకోండి",
                "భోజనం మానేయకండి"
            ]
        },

        "french": {
            "title": "Mal de tête",
            "response": "Les maux de tête peuvent avoir plusieurs causes, notamment le stress, la déshydratation, le manque de sommeil ou la fatigue visuelle.",
            "precautions": [
                "Buvez suffisamment d'eau",
                "Reposez-vous suffisamment",
                "Faites des pauses devant les écrans",
                "Évitez de sauter des repas"
            ]
        }
    },


    # ======================================
    # 2. FEVER
    # ======================================

    "fever": {
        "keywords": {
            "english": ["fever", "high temperature"],
            "hindi": ["बुखार", "बुखार होना"],
            "telugu": ["జ్వరం"],
            "french": ["fièvre"]
        },

        "english": {
            "title": "Fever",
            "response": "Fever is often a sign that the body is fighting an infection.",
            "precautions": [
                "Drink plenty of fluids",
                "Get enough rest",
                "Wear comfortable clothing",
                "Monitor your temperature"
            ]
        },

        "hindi": {
            "title": "बुखार",
            "response": "बुखार अक्सर इस बात का संकेत होता है कि शरीर किसी संक्रमण से लड़ रहा है।",
            "precautions": [
                "भरपूर पानी और तरल पदार्थ पिएं",
                "पर्याप्त आराम करें",
                "आरामदायक कपड़े पहनें",
                "अपने शरीर का तापमान जांचते रहें"
            ]
        },

        "telugu": {
            "title": "జ్వరం",
            "response": "జ్వరం తరచుగా శరీరం ఏదైనా ఇన్ఫెక్షన్‌తో పోరాడుతున్నదనే సంకేతం.",
            "precautions": [
                "తగినంత ద్రవాలు తీసుకోండి",
                "తగినంత విశ్రాంతి తీసుకోండి",
                "సౌకర్యవంతమైన దుస్తులు ధరించండి",
                "మీ శరీర ఉష్ణోగ్రతను గమనించండి"
            ]
        },

        "french": {
            "title": "Fièvre",
            "response": "La fièvre est souvent un signe que le corps lutte contre une infection.",
            "precautions": [
                "Buvez beaucoup de liquides",
                "Reposez-vous suffisamment",
                "Portez des vêtements confortables",
                "Surveillez votre température"
            ]
        }
    },


    # ======================================
    # 3. COMMON COLD
    # ======================================

    "cold": {
        "keywords": {
            "english": ["cold", "common cold"],
            "hindi": ["सर्दी", "जुकाम", "सर्दी जुकाम"],
            "telugu": ["జలుబు"],
            "french": ["rhume", "refroidissement"]
        },

        "english": {
            "title": "Common Cold",
            "response": "A common cold can cause a runny nose, sneezing, sore throat, cough, and mild tiredness.",
            "precautions": [
                "Drink warm fluids",
                "Get adequate rest",
                "Wash your hands regularly",
                "Avoid close contact with sick people"
            ]
        },

        "hindi": {
            "title": "सर्दी-जुकाम",
            "response": "सर्दी-जुकाम के कारण नाक बहना, छींकना, गले में खराश, खांसी और हल्की थकान हो सकती है।",
            "precautions": [
                "गर्म तरल पदार्थ पिएं",
                "पर्याप्त आराम करें",
                "अपने हाथ नियमित रूप से धोएं",
                "बीमार लोगों के करीब जाने से बचें"
            ]
        },

        "telugu": {
            "title": "జలుబు",
            "response": "జలుబు వల్ల ముక్కు కారడం, తుమ్ములు, గొంతు నొప్పి, దగ్గు మరియు స్వల్ప అలసట రావచ్చు.",
            "precautions": [
                "వెచ్చని ద్రవాలు తాగండి",
                "తగినంత విశ్రాంతి తీసుకోండి",
                "చేతులను క్రమం తప్పకుండా కడుక్కోండి",
                "అనారోగ్యంతో ఉన్నవారికి దూరంగా ఉండండి"
            ]
        },

        "french": {
            "title": "Rhume",
            "response": "Un rhume peut provoquer un nez qui coule, des éternuements, un mal de gorge, une toux et une légère fatigue.",
            "precautions": [
                "Buvez des boissons chaudes",
                "Reposez-vous suffisamment",
                "Lavez régulièrement vos mains",
                "Évitez le contact rapproché avec les personnes malades"
            ]
        }
    },


    # ======================================
    # 4. COUGH
    # ======================================

    "cough": {
        "keywords": {
            "english": ["cough"],
            "hindi": ["खांसी"],
            "telugu": ["దగ్గు"],
            "french": ["toux"]
        },

        "english": {
            "title": "Cough",
            "response": "A cough can occur due to a cold, allergies, throat irritation, or other respiratory conditions.",
            "precautions": [
                "Drink plenty of fluids",
                "Avoid smoke and dust",
                "Get enough rest",
                "Keep the air comfortably humid"
            ]
        },

        "hindi": {
            "title": "खांसी",
            "response": "खांसी सर्दी, एलर्जी, गले में जलन या अन्य श्वसन समस्याओं के कारण हो सकती है।",
            "precautions": [
                "भरपूर तरल पदार्थ पिएं",
                "धुएं और धूल से बचें",
                "पर्याप्त आराम करें",
                "हवा में उचित नमी बनाए रखें"
            ]
        },

        "telugu": {
            "title": "దగ్గు",
            "response": "దగ్గు జలుబు, అలర్జీలు, గొంతు చికాకు లేదా ఇతర శ్వాస సంబంధిత సమస్యల వల్ల రావచ్చు.",
            "precautions": [
                "తగినంత ద్రవాలు తాగండి",
                "పొగ మరియు దుమ్మును నివారించండి",
                "తగినంత విశ్రాంతి తీసుకోండి",
                "గాలిలో తగినంత తేమ ఉండేలా చూసుకోండి"
            ]
        },

        "french": {
            "title": "Toux",
            "response": "La toux peut être causée par un rhume, des allergies, une irritation de la gorge ou d'autres problèmes respiratoires.",
            "precautions": [
                "Buvez beaucoup de liquides",
                "Évitez la fumée et la poussière",
                "Reposez-vous suffisamment",
                "Maintenez une humidité confortable dans l'air"
            ]
        }
    },


    # ======================================
    # 5. SORE THROAT
    # ======================================

    "sore_throat": {
        "keywords": {
            "english": ["sore throat", "throat pain", "throat ache"],
            "hindi": ["गले में खराश", "गले में दर्द"],
            "telugu": ["గొంతు నొప్పి", "గొంతు మంట"],
            "french": ["mal de gorge", "gorge irritée"]
        },

        "english": {
            "title": "Sore Throat",
            "response": "A sore throat can be caused by infections, allergies, dry air, or irritation.",
            "precautions": [
                "Drink warm fluids",
                "Rest your voice",
                "Avoid smoke and other irritants",
                "Stay hydrated"
            ]
        },

        "hindi": {
            "title": "गले में खराश",
            "response": "गले में खराश संक्रमण, एलर्जी, सूखी हवा या जलन के कारण हो सकती है।",
            "precautions": [
                "गर्म तरल पदार्थ पिएं",
                "अपनी आवाज को आराम दें",
                "धुएं और जलन पैदा करने वाली चीजों से बचें",
                "पर्याप्त पानी पिएं"
            ]
        },

        "telugu": {
            "title": "గొంతు నొప్పి",
            "response": "గొంతు నొప్పి ఇన్ఫెక్షన్లు, అలర్జీలు, పొడి గాలి లేదా చికాకు వల్ల రావచ్చు.",
            "precautions": [
                "వెచ్చని ద్రవాలు తాగండి",
                "మీ గొంతుకు విశ్రాంతి ఇవ్వండి",
                "పొగ మరియు ఇతర చికాకులను నివారించండి",
                "తగినంత నీరు తాగండి"
            ]
        },

        "french": {
            "title": "Mal de gorge",
            "response": "Un mal de gorge peut être causé par des infections, des allergies, l'air sec ou une irritation.",
            "precautions": [
                "Buvez des boissons chaudes",
                "Reposez votre voix",
                "Évitez la fumée et les irritants",
                "Restez bien hydraté"
            ]
        }
    },


    # ======================================
    # 6. STOMACH ACHE
    # ======================================

    "stomach_ache": {
        "keywords": {
            "english": ["stomach ache", "stomach pain", "abdominal pain"],
            "hindi": ["पेट दर्द", "पेट में दर्द"],
            "telugu": ["కడుపు నొప్పి", "పొట్ట నొప్పి"],
            "french": ["mal au ventre", "douleur abdominale"]
        },

        "english": {
            "title": "Stomach Ache",
            "response": "Stomach pain can have many causes, including indigestion, gas, infections, or other digestive problems.",
            "precautions": [
                "Drink enough water",
                "Eat light meals",
                "Avoid foods that irritate your stomach",
                "Get adequate rest"
            ]
        },

        "hindi": {
            "title": "पेट दर्द",
            "response": "पेट दर्द के कई कारण हो सकते हैं, जैसे अपच, गैस, संक्रमण या अन्य पाचन संबंधी समस्याएं।",
            "precautions": [
                "पर्याप्त पानी पिएं",
                "हल्का भोजन करें",
                "पेट को परेशान करने वाले खाद्य पदार्थों से बचें",
                "पर्याप्त आराम करें"
            ]
        },

        "telugu": {
            "title": "కడుపు నొప్పి",
            "response": "కడుపు నొప్పికి అజీర్ణం, గ్యాస్, ఇన్ఫెక్షన్లు లేదా ఇతర జీర్ణ సమస్యలు వంటి అనేక కారణాలు ఉండవచ్చు.",
            "precautions": [
                "తగినంత నీరు తాగండి",
                "తేలికపాటి ఆహారం తీసుకోండి",
                "కడుపుకు ఇబ్బంది కలిగించే ఆహారాలను నివారించండి",
                "తగినంత విశ్రాంతి తీసుకోండి"
            ]
        },

        "french": {
            "title": "Mal au ventre",
            "response": "Les douleurs abdominales peuvent avoir plusieurs causes, notamment l'indigestion, les gaz, les infections ou d'autres problèmes digestifs.",
            "precautions": [
                "Buvez suffisamment d'eau",
                "Mangez des repas légers",
                "Évitez les aliments qui irritent l'estomac",
                "Reposez-vous suffisamment"
            ]
        }
    },


    # ======================================
    # 7. DIARRHEA
    # ======================================

    "diarrhea": {
        "keywords": {
            "english": ["diarrhea", "diarrhoea", "loose motion"],
            "hindi": ["दस्त", "पतले दस्त", "लूज मोशन"],
            "telugu": ["విరేచనాలు", "నీళ్ల విరేచనాలు"],
            "french": ["diarrhée"]
        },

        "english": {
            "title": "Diarrhea",
            "response": "Diarrhea can cause frequent loose stools and may lead to dehydration.",
            "precautions": [
                "Drink plenty of fluids",
                "Consider oral rehydration fluids",
                "Eat light foods",
                "Get enough rest"
            ]
        },

        "hindi": {
            "title": "दस्त",
            "response": "दस्त के कारण बार-बार पतला मल हो सकता है और शरीर में पानी की कमी हो सकती है।",
            "precautions": [
                "भरपूर तरल पदार्थ पिएं",
                "ओआरएस जैसे पुनर्जलीकरण तरल लें",
                "हल्का भोजन करें",
                "पर्याप्त आराम करें"
            ]
        },

        "telugu": {
            "title": "విరేచనాలు",
            "response": "విరేచనాల వల్ల తరచుగా పలుచని మలం రావచ్చు మరియు శరీరంలో నీరు తగ్గే అవకాశం ఉంది.",
            "precautions": [
                "తగినంత ద్రవాలు తాగండి",
                "ORS వంటి పునర్జలీకరణ ద్రవాలు తీసుకోండి",
                "తేలికపాటి ఆహారం తీసుకోండి",
                "తగినంత విశ్రాంతి తీసుకోండి"
            ]
        },

        "french": {
            "title": "Diarrhée",
            "response": "La diarrhée peut provoquer des selles fréquentes et liquides et peut entraîner une déshydratation.",
            "precautions": [
                "Buvez beaucoup de liquides",
                "Prenez des solutions de réhydratation orale",
                "Mangez des aliments légers",
                "Reposez-vous suffisamment"
            ]
        }
    },


    # ======================================
    # 8. VOMITING
    # ======================================

    "vomiting": {
        "keywords": {
            "english": ["vomiting", "vomit", "throwing up"],
            "hindi": ["उल्टी", "वमन"],
            "telugu": ["వాంతులు", "వాంతి"],
            "french": ["vomissements", "vomir"]
        },

        "english": {
            "title": "Vomiting",
            "response": "Vomiting can occur because of infections, food-related problems, motion sickness, or other conditions.",
            "precautions": [
                "Take small sips of fluids",
                "Avoid heavy meals temporarily",
                "Rest adequately",
                "Watch for signs of dehydration"
            ]
        },

        "hindi": {
            "title": "उल्टी",
            "response": "उल्टी संक्रमण, भोजन से जुड़ी समस्याओं, यात्रा के दौरान होने वाली परेशानी या अन्य कारणों से हो सकती है।",
            "precautions": [
                "थोड़ी-थोड़ी मात्रा में तरल पदार्थ पिएं",
                "कुछ समय के लिए भारी भोजन से बचें",
                "पर्याप्त आराम करें",
                "पानी की कमी के लक्षणों पर ध्यान दें"
            ]
        },

        "telugu": {
            "title": "వాంతులు",
            "response": "వాంతులు ఇన్ఫెక్షన్లు, ఆహార సంబంధిత సమస్యలు, ప్రయాణంలో కలిగే అసౌకర్యం లేదా ఇతర కారణాల వల్ల రావచ్చు.",
            "precautions": [
                "కొద్దికొద్దిగా ద్రవాలు తాగండి",
                "కొంతకాలం భారమైన ఆహారాన్ని నివారించండి",
                "తగినంత విశ్రాంతి తీసుకోండి",
                "నీరు తగ్గే లక్షణాలను గమనించండి"
            ]
        },

        "french": {
            "title": "Vomissements",
            "response": "Les vomissements peuvent être causés par des infections, des problèmes alimentaires, le mal des transports ou d'autres problèmes.",
            "precautions": [
                "Buvez de petites quantités de liquide",
                "Évitez temporairement les repas lourds",
                "Reposez-vous suffisamment",
                "Surveillez les signes de déshydratation"
            ]
        }
    },


    # ======================================
    # 9. NAUSEA
    # ======================================

    "nausea": {
        "keywords": {
            "english": ["nausea", "feeling sick", "queasy"],
            "hindi": ["मतली", "जी मिचलाना", "उबकाई"],
            "telugu": ["వికారం", "వాంతి భావన"],
            "french": ["nausée", "envie de vomir"]
        },

        "english": {
            "title": "Nausea",
            "response": "Nausea is a feeling of discomfort in the stomach that may make you feel like vomiting.",
            "precautions": [
                "Take small sips of water",
                "Eat small and light meals",
                "Avoid strong smells",
                "Get adequate rest"
            ]
        },

        "hindi": {
            "title": "मतली",
            "response": "मतली पेट में होने वाली असहजता है जिससे उल्टी जैसा महसूस हो सकता है।",
            "precautions": [
                "थोड़ी-थोड़ी मात्रा में पानी पिएं",
                "थोड़ा और हल्का भोजन करें",
                "तेज गंध से बचें",
                "पर्याप्त आराम करें"
            ]
        },

        "telugu": {
            "title": "వికారం",
            "response": "వికారం అనేది కడుపులో కలిగే అసౌకర్యం, దీనివల్ల వాంతి రావాలనిపించవచ్చు.",
            "precautions": [
                "కొద్దికొద్దిగా నీరు తాగండి",
                "చిన్న మొత్తంలో తేలికపాటి ఆహారం తీసుకోండి",
                "తీవ్రమైన వాసనలను నివారించండి",
                "తగినంత విశ్రాంతి తీసుకోండి"
            ]
        },

        "french": {
            "title": "Nausée",
            "response": "La nausée est une sensation d'inconfort dans l'estomac qui peut donner envie de vomir.",
            "precautions": [
                "Buvez de petites quantités d'eau",
                "Mangez de petits repas légers",
                "Évitez les odeurs fortes",
                "Reposez-vous suffisamment"
            ]
        }
    },


    # ======================================
    # 10. BACK PAIN
    # ======================================

    "back_pain": {
        "keywords": {
            "english": ["back pain", "backache", "lower back pain"],
            "hindi": ["कमर दर्द", "पीठ दर्द", "पीठ में दर्द"],
            "telugu": ["వెన్నునొప్పి", "నడుము నొప్పి"],
            "french": ["mal de dos", "douleur au dos"]
        },

        "english": {
            "title": "Back Pain",
            "response": "Back pain can be related to muscle strain, poor posture, prolonged sitting, or other causes.",
            "precautions": [
                "Maintain good posture",
                "Avoid lifting heavy objects",
                "Take regular breaks from sitting",
                "Get adequate rest"
            ]
        },

        "hindi": {
            "title": "कमर दर्द",
            "response": "कमर दर्द मांसपेशियों में खिंचाव, खराब मुद्रा, लंबे समय तक बैठने या अन्य कारणों से हो सकता है।",
            "precautions": [
                "सही मुद्रा बनाए रखें",
                "भारी वस्तुएं उठाने से बचें",
                "लंबे समय तक बैठने से बीच-बीच में ब्रेक लें",
                "पर्याप्त आराम करें"
            ]
        },

        "telugu": {
            "title": "వెన్నునొప్పి",
            "response": "వెన్నునొప్పి కండరాలపై ఒత్తిడి, తప్పు భంగిమ, ఎక్కువసేపు కూర్చోవడం లేదా ఇతర కారణాల వల్ల రావచ్చు.",
            "precautions": [
                "సరైన భంగిమను పాటించండి",
                "భారీ వస్తువులను ఎత్తడం నివారించండి",
                "ఎక్కువసేపు కూర్చుంటే మధ్యలో విరామం తీసుకోండి",
                "తగినంత విశ్రాంతి తీసుకోండి"
            ]
        },

        "french": {
            "title": "Mal de dos",
            "response": "Le mal de dos peut être lié à une tension musculaire, une mauvaise posture, une position assise prolongée ou d'autres causes.",
            "precautions": [
                "Maintenez une bonne posture",
                "Évitez de soulever des objets lourds",
                "Faites des pauses régulières lorsque vous êtes assis",
                "Reposez-vous suffisamment"
            ]
        }
    },


    # ======================================
    # 11. TOOTHACHE
    # ======================================

    "toothache": {
        "keywords": {
            "english": ["toothache", "tooth pain"],
            "hindi": ["दांत दर्द", "दांत में दर्द"],
            "telugu": ["పంటి నొప్పి", "దంత నొప్పి"],
            "french": ["mal de dent", "douleur dentaire"]
        },

        "english": {
            "title": "Toothache",
            "response": "Toothache can be caused by tooth decay, gum problems, sensitivity, or other dental issues.",
            "precautions": [
                "Maintain good oral hygiene",
                "Rinse your mouth with clean water",
                "Avoid very hot or cold foods",
                "See a dentist if the pain continues"
            ]
        },

        "hindi": {
            "title": "दांत दर्द",
            "response": "दांत दर्द दांतों में सड़न, मसूड़ों की समस्या, संवेदनशीलता या अन्य दंत समस्याओं के कारण हो सकता है।",
            "precautions": [
                "मुंह की अच्छी सफाई रखें",
                "साफ पानी से मुंह धोएं",
                "बहुत गर्म या ठंडे भोजन से बचें",
                "दर्द जारी रहने पर दंत चिकित्सक से मिलें"
            ]
        },

        "telugu": {
            "title": "పంటి నొప్పి",
            "response": "పంటి నొప్పి పళ్లలో క్షయం, చిగుళ్ల సమస్యలు, సున్నితత్వం లేదా ఇతర దంత సమస్యల వల్ల రావచ్చు.",
            "precautions": [
                "నోటి పరిశుభ్రతను పాటించండి",
                "శుభ్రమైన నీటితో నోరు కడుక్కోండి",
                "చాలా వేడి లేదా చల్లని ఆహారాన్ని నివారించండి",
                "నొప్పి కొనసాగితే దంత వైద్యుడిని సంప్రదించండి"
            ]
        },

        "french": {
            "title": "Mal de dent",
            "response": "Le mal de dent peut être causé par une carie, des problèmes de gencives, une sensibilité ou d'autres problèmes dentaires.",
            "precautions": [
                "Maintenez une bonne hygiène bucco-dentaire",
                "Rincez votre bouche avec de l'eau propre",
                "Évitez les aliments très chauds ou très froids",
                "Consultez un dentiste si la douleur continue"
            ]
        }
    },


    # ======================================
    # 12. EARACHE
    # ======================================

    "earache": {
        "keywords": {
            "english": ["earache", "ear pain"],
            "hindi": ["कान दर्द", "कान में दर्द"],
            "telugu": ["చెవి నొప్పి"],
            "french": ["mal d'oreille", "douleur à l'oreille"]
        },

        "english": {
            "title": "Earache",
            "response": "Ear pain can have several causes, including infections, irritation, pressure changes, or other ear problems.",
            "precautions": [
                "Keep the ear dry",
                "Avoid putting objects inside the ear",
                "Avoid loud sounds",
                "See a doctor if pain persists"
            ]
        },

        "hindi": {
            "title": "कान दर्द",
            "response": "कान में दर्द संक्रमण, जलन, दबाव में बदलाव या कान की अन्य समस्याओं के कारण हो सकता है।",
            "precautions": [
                "कान को सूखा रखें",
                "कान के अंदर कोई वस्तु न डालें",
                "तेज आवाज से बचें",
                "दर्द जारी रहने पर डॉक्टर से मिलें"
            ]
        },

        "telugu": {
            "title": "చెవి నొప్పి",
            "response": "చెవి నొప్పి ఇన్ఫెక్షన్, చికాకు, ఒత్తిడిలో మార్పులు లేదా ఇతర చెవి సమస్యల వల్ల రావచ్చు.",
            "precautions": [
                "చెవిని పొడిగా ఉంచండి",
                "చెవిలో వస్తువులను పెట్టవద్దు",
                "పెద్ద శబ్దాలను నివారించండి",
                "నొప్పి కొనసాగితే వైద్యుడిని సంప్రదించండి"
            ]
        },

        "french": {
            "title": "Mal d'oreille",
            "response": "La douleur à l'oreille peut avoir plusieurs causes, notamment une infection, une irritation, des changements de pression ou d'autres problèmes.",
            "precautions": [
                "Gardez l'oreille sèche",
                "N'introduisez pas d'objets dans l'oreille",
                "Évitez les sons très forts",
                "Consultez un médecin si la douleur persiste"
            ]
        }
    },


    # ======================================
    # 13. ALLERGY
    # ======================================

    "allergy": {
        "keywords": {
            "english": ["allergy", "allergic"],
            "hindi": ["एलर्जी", "एलर्जिक"],
            "telugu": ["అలర్జీ", "అలెర్జీ"],
            "french": ["allergie", "allergique"]
        },

        "english": {
            "title": "Allergy",
            "response": "Allergies can cause symptoms such as sneezing, itching, runny nose, or skin reactions.",
            "precautions": [
                "Avoid known triggers",
                "Keep your surroundings clean",
                "Wash your hands regularly",
                "Seek medical advice for severe symptoms"
            ]
        },

        "hindi": {
            "title": "एलर्जी",
            "response": "एलर्जी के कारण छींक, खुजली, नाक बहना या त्वचा संबंधी प्रतिक्रियाएं हो सकती हैं।",
            "precautions": [
                "ज्ञात एलर्जी के कारणों से बचें",
                "अपने आसपास सफाई रखें",
                "अपने हाथ नियमित रूप से धोएं",
                "गंभीर लक्षण होने पर डॉक्टर से सलाह लें"
            ]
        },

        "telugu": {
            "title": "అలర్జీ",
            "response": "అలర్జీ వల్ల తుమ్ములు, దురద, ముక్కు కారడం లేదా చర్మంపై ప్రతిచర్యలు రావచ్చు.",
            "precautions": [
                "అలర్జీ కలిగించే కారణాలను నివారించండి",
                "మీ పరిసరాలను శుభ్రంగా ఉంచండి",
                "చేతులను క్రమం తప్పకుండా కడుక్కోండి",
                "తీవ్రమైన లక్షణాలు ఉంటే వైద్యుడిని సంప్రదించండి"
            ]
        },

        "french": {
            "title": "Allergie",
            "response": "Les allergies peuvent provoquer des éternuements, des démangeaisons, un nez qui coule ou des réactions cutanées.",
            "precautions": [
                "Évitez les déclencheurs connus",
                "Gardez votre environnement propre",
                "Lavez régulièrement vos mains",
                "Consultez un médecin en cas de symptômes sévères"
            ]
        }
    },


    # ======================================
    # 14. ASTHMA
    # ======================================

    "asthma": {
        "keywords": {
            "english": ["asthma", "asthmatic"],
            "hindi": ["अस्थमा", "दमा"],
            "telugu": ["ఆస్తమా", "ఉబ్బసం"],
            "french": ["asthme"]
        },

        "english": {
            "title": "Asthma",
            "response": "Asthma is a condition that can cause breathing difficulties, wheezing, coughing, or chest tightness.",
            "precautions": [
                "Avoid known triggers",
                "Avoid smoke and strong irritants",
                "Follow your doctor's asthma plan",
                "Seek urgent help for severe breathing difficulty"
            ]
        },

        "hindi": {
            "title": "अस्थमा",
            "response": "अस्थमा एक ऐसी स्थिति है जिसमें सांस लेने में कठिनाई, घरघराहट, खांसी या सीने में जकड़न हो सकती है।",
            "precautions": [
                "ज्ञात कारणों से बचें",
                "धुएं और तेज जलन पैदा करने वाली चीजों से बचें",
                "डॉक्टर द्वारा दी गई योजना का पालन करें",
                "सांस लेने में गंभीर कठिनाई होने पर तुरंत मदद लें"
            ]
        },

        "telugu": {
            "title": "ఆస్తమా",
            "response": "ఆస్తమా వల్ల శ్వాస తీసుకోవడంలో ఇబ్బంది, గురక, దగ్గు లేదా ఛాతిలో బిగుతుగా అనిపించడం ఉండవచ్చు.",
            "precautions": [
                "తెలిసిన ట్రిగ్గర్లను నివారించండి",
                "పొగ మరియు చికాకు కలిగించే పదార్థాలను నివారించండి",
                "వైద్యుడు సూచించిన ఆస్తమా ప్రణాళికను పాటించండి",
                "తీవ్రమైన శ్వాస ఇబ్బంది ఉంటే వెంటనే సహాయం పొందండి"
            ]
        },

        "french": {
            "title": "Asthme",
            "response": "L'asthme peut provoquer des difficultés respiratoires, une respiration sifflante, une toux ou une oppression thoracique.",
            "precautions": [
                "Évitez les déclencheurs connus",
                "Évitez la fumée et les irritants",
                "Suivez le plan contre l'asthme recommandé par votre médecin",
                "Demandez une aide urgente en cas de difficulté respiratoire sévère"
            ]
        }
    },


    # ======================================
    # 15. MIGRAINE
    # ======================================

    "migraine": {
        "keywords": {
            "english": ["migraine"],
            "hindi": ["माइग्रेन", "आधा सिर दर्द"],
            "telugu": ["మైగ్రేన్", "పార్శ్వపు తలనొప్పి"],
            "french": ["migraine"]
        },

        "english": {
            "title": "Migraine",
            "response": "Migraine can cause moderate to severe headache and may be associated with nausea or sensitivity to light and sound.",
            "precautions": [
                "Rest in a quiet and dark room",
                "Drink enough water",
                "Maintain regular sleep",
                "Avoid known migraine triggers"
            ]
        },

        "hindi": {
            "title": "माइग्रेन",
            "response": "माइग्रेन में मध्यम से तेज सिरदर्द हो सकता है और इसके साथ मतली या रोशनी और आवाज के प्रति संवेदनशीलता हो सकती है।",
            "precautions": [
                "शांत और अंधेरे कमरे में आराम करें",
                "पर्याप्त पानी पिएं",
                "नियमित नींद लें",
                "माइग्रेन के ज्ञात कारणों से बचें"
            ]
        },

        "telugu": {
            "title": "మైగ్రేన్",
            "response": "మైగ్రేన్ వల్ల మితమైన లేదా తీవ్రమైన తలనొప్పి రావచ్చు. వికారం లేదా వెలుగు మరియు శబ్దానికి సున్నితత్వం కూడా ఉండవచ్చు.",
            "precautions": [
                "నిశ్శబ్దమైన చీకటి గదిలో విశ్రాంతి తీసుకోండి",
                "తగినంత నీరు తాగండి",
                "క్రమం తప్పకుండా నిద్రపోండి",
                "మైగ్రేన్‌కు కారణమయ్యే అంశాలను నివారించండి"
            ]
        },

        "french": {
            "title": "Migraine",
            "response": "La migraine peut provoquer un mal de tête modéré à intense et peut être associée à des nausées ou à une sensibilité à la lumière et au bruit.",
            "precautions": [
                "Reposez-vous dans une pièce calme et sombre",
                "Buvez suffisamment d'eau",
                "Gardez un sommeil régulier",
                "Évitez les déclencheurs connus de la migraine"
            ]
        }
    },


    # ======================================
    # 16. FLU
    # ======================================

    "flu": {
        "keywords": {
            "english": ["flu", "influenza"],
            "hindi": ["फ्लू", "इन्फ्लुएंजा"],
            "telugu": ["ఫ్లూ", "ఇన్ఫ్లుయెంజా"],
            "french": ["grippe", "influenza"]
        },

        "english": {
            "title": "Flu",
            "response": "Flu can cause fever, cough, sore throat, body aches, tiredness, and other symptoms.",
            "precautions": [
                "Get plenty of rest",
                "Drink enough fluids",
                "Wash your hands regularly",
                "Avoid close contact with others when sick"
            ]
        },

        "hindi": {
            "title": "फ्लू",
            "response": "फ्लू के कारण बुखार, खांसी, गले में खराश, शरीर में दर्द और थकान जैसे लक्षण हो सकते हैं।",
            "precautions": [
                "भरपूर आराम करें",
                "पर्याप्त तरल पदार्थ पिएं",
                "अपने हाथ नियमित रूप से धोएं",
                "बीमार होने पर दूसरों के करीबी संपर्क से बचें"
            ]
        },

        "telugu": {
            "title": "ఫ్లూ",
            "response": "ఫ్లూ వల్ల జ్వరం, దగ్గు, గొంతు నొప్పి, శరీర నొప్పులు మరియు అలసట వంటి లక్షణాలు రావచ్చు.",
            "precautions": [
                "తగినంత విశ్రాంతి తీసుకోండి",
                "తగినంత ద్రవాలు తాగండి",
                "చేతులను క్రమం తప్పకుండా కడుక్కోండి",
                "అనారోగ్యంగా ఉన్నప్పుడు ఇతరులతో సన్నిహితంగా ఉండటాన్ని నివారించండి"
            ]
        },

        "french": {
            "title": "Grippe",
            "response": "La grippe peut provoquer de la fièvre, une toux, un mal de gorge, des courbatures, de la fatigue et d'autres symptômes.",
            "precautions": [
                "Reposez-vous suffisamment",
                "Buvez suffisamment de liquides",
                "Lavez régulièrement vos mains",
                "Évitez les contacts rapprochés avec les autres lorsque vous êtes malade"
            ]
        }
    },


    # ======================================
    # 17. CONSTIPATION
    # ======================================

    "constipation": {
        "keywords": {
            "english": ["constipation", "constipated"],
            "hindi": ["कब्ज", "कब्ज़"],
            "telugu": ["మలబద్ధకం"],
            "french": ["constipation"]
        },

        "english": {
            "title": "Constipation",
            "response": "Constipation can involve infrequent bowel movements or difficulty passing stool.",
            "precautions": [
                "Drink enough water",
                "Eat fiber-rich foods",
                "Stay physically active",
                "Maintain regular bathroom habits"
            ]
        },

        "hindi": {
            "title": "कब्ज",
            "response": "कब्ज में मल त्याग कम होना या मल त्याग करने में कठिनाई हो सकती है।",
            "precautions": [
                "पर्याप्त पानी पिएं",
                "फाइबर युक्त भोजन खाएं",
                "शारीरिक रूप से सक्रिय रहें",
                "नियमित शौच की आदत बनाए रखें"
            ]
        },

        "telugu": {
            "title": "మలబద్ధకం",
            "response": "మలబద్ధకం వల్ల మల విసర్జన తక్కువగా జరగడం లేదా మలం విసర్జించడంలో ఇబ్బంది ఉండవచ్చు.",
            "precautions": [
                "తగినంత నీరు తాగండి",
                "ఫైబర్ అధికంగా ఉన్న ఆహారం తీసుకోండి",
                "శారీరకంగా చురుకుగా ఉండండి",
                "నియమితమైన మల విసర్జన అలవాటును పాటించండి"
            ]
        },

        "french": {
            "title": "Constipation",
            "response": "La constipation peut entraîner des selles moins fréquentes ou des difficultés à aller à la selle.",
            "precautions": [
                "Buvez suffisamment d'eau",
                "Mangez des aliments riches en fibres",
                "Restez physiquement actif",
                "Gardez des habitudes régulières pour aller aux toilettes"
            ]
        }
    },


    # ======================================
    # 18. ACIDITY
    # ======================================

    "acidity": {
        "keywords": {
            "english": ["acidity", "heartburn", "acid reflux"],
            "hindi": ["एसिडिटी", "अम्लता", "सीने में जलन"],
            "telugu": ["ఆమ్లత్వం", "ఎసిడిటీ", "గుండెల్లో మంట"],
            "french": ["acidité", "brûlures d'estomac", "reflux acide"]
        },

        "english": {
            "title": "Acidity",
            "response": "Acidity or heartburn can cause a burning feeling in the chest or upper abdomen, sometimes after eating.",
            "precautions": [
                "Avoid overeating",
                "Avoid foods that trigger your symptoms",
                "Eat meals at regular times",
                "Avoid lying down immediately after eating"
            ]
        },

        "hindi": {
            "title": "एसिडिटी",
            "response": "एसिडिटी या सीने में जलन के कारण छाती या पेट के ऊपरी हिस्से में जलन महसूस हो सकती है, खासकर भोजन के बाद।",
            "precautions": [
                "बहुत अधिक भोजन करने से बचें",
                "ऐसे भोजन से बचें जो लक्षण बढ़ाते हैं",
                "समय पर भोजन करें",
                "भोजन के तुरंत बाद न लेटें"
            ]
        },

        "telugu": {
            "title": "ఎసిడిటీ",
            "response": "ఎసిడిటీ లేదా గుండెల్లో మంట వల్ల ఛాతి లేదా పై పొత్తికడుపులో మంటగా అనిపించవచ్చు, ముఖ్యంగా భోజనం తర్వాత.",
            "precautions": [
                "అతిగా తినడం నివారించండి",
                "లక్షణాలను పెంచే ఆహారాన్ని నివారించండి",
                "సమయానికి భోజనం చేయండి",
                "భోజనం చేసిన వెంటనే పడుకోకండి"
            ]
        },

        "french": {
            "title": "Acidité",
            "response": "L'acidité ou les brûlures d'estomac peuvent provoquer une sensation de brûlure dans la poitrine ou le haut de l'abdomen, parfois après avoir mangé.",
            "precautions": [
                "Évitez de trop manger",
                "Évitez les aliments qui déclenchent vos symptômes",
                "Prenez vos repas à heures régulières",
                "Évitez de vous allonger immédiatement après avoir mangé"
            ]
        }
    },


    # ======================================
    # 19. INDIGESTION
    # ======================================

    "indigestion": {
        "keywords": {
            "english": ["indigestion", "upset stomach"],
            "hindi": ["अपच", "बदहजमी", "पेट खराब"],
            "telugu": ["అజీర్ణం", "జీర్ణక్రియ సమస్య"],
            "french": ["indigestion", "troubles digestifs"]
        },

        "english": {
            "title": "Indigestion",
            "response": "Indigestion can cause discomfort, fullness, bloating, or burning in the upper abdomen after eating.",
            "precautions": [
                "Eat smaller meals",
                "Eat slowly",
                "Avoid foods that trigger discomfort",
                "Drink enough water"
            ]
        },

        "hindi": {
            "title": "अपच",
            "response": "अपच के कारण भोजन के बाद पेट के ऊपरी हिस्से में असहजता, भारीपन, पेट फूलना या जलन हो सकती है।",
            "precautions": [
                "कम मात्रा में भोजन करें",
                "धीरे-धीरे भोजन करें",
                "ऐसे भोजन से बचें जिससे परेशानी बढ़ती है",
                "पर्याप्त पानी पिएं"
            ]
        },

        "telugu": {
            "title": "అజీర్ణం",
            "response": "అజీర్ణం వల్ల భోజనం తర్వాత పై పొత్తికడుపులో అసౌకర్యం, కడుపు నిండిన భావన, ఉబ్బరం లేదా మంట ఉండవచ్చు.",
            "precautions": [
                "తక్కువ పరిమాణంలో భోజనం చేయండి",
                "నెమ్మదిగా భోజనం చేయండి",
                "అసౌకర్యాన్ని కలిగించే ఆహారాన్ని నివారించండి",
                "తగినంత నీరు తాగండి"
            ]
        },

        "french": {
            "title": "Indigestion",
            "response": "L'indigestion peut provoquer une gêne, une sensation de satiété, des ballonnements ou des brûlures dans le haut de l'abdomen après avoir mangé.",
            "precautions": [
                "Mangez de petites quantités",
                "Mangez lentement",
                "Évitez les aliments qui provoquent une gêne",
                "Buvez suffisamment d'eau"
            ]
        }
    },


    # ======================================
    # 20. DIZZINESS
    # ======================================

    "dizziness": {
        "keywords": {
            "english": ["dizziness", "dizzy"],
            "hindi": ["चक्कर", "चक्कर आना"],
            "telugu": ["తల తిరగడం", "తల తిరుగుట"],
            "french": ["vertiges", "étourdissement"]
        },

        "english": {
            "title": "Dizziness",
            "response": "Dizziness can have many possible causes, including dehydration, standing up quickly, illness, or other conditions.",
            "precautions": [
                "Sit or lie down if you feel dizzy",
                "Drink enough water",
                "Stand up slowly",
                "Seek medical advice if dizziness is severe or repeated"
            ]
        },

        "hindi": {
            "title": "चक्कर आना",
            "response": "चक्कर आने के कई संभावित कारण हो सकते हैं, जैसे पानी की कमी, अचानक खड़ा होना, बीमारी या अन्य स्थितियां।",
            "precautions": [
                "चक्कर आने पर बैठ जाएं या लेट जाएं",
                "पर्याप्त पानी पिएं",
                "धीरे-धीरे खड़े हों",
                "चक्कर तेज या बार-बार आने पर डॉक्टर से सलाह लें"
            ]
        },

        "telugu": {
            "title": "తల తిరగడం",
            "response": "తల తిరగడానికి నీటి కొరత, ఒక్కసారిగా నిలబడటం, అనారోగ్యం లేదా ఇతర కారణాలు ఉండవచ్చు.",
            "precautions": [
                "తల తిరిగితే కూర్చోండి లేదా పడుకోండి",
                "తగినంత నీరు తాగండి",
                "నెమ్మదిగా నిలబడండి",
                "తీవ్రంగా లేదా తరచుగా తల తిరిగితే వైద్యుడిని సంప్రదించండి"
            ]
        },

        "french": {
            "title": "Vertiges",
            "response": "Les vertiges peuvent avoir plusieurs causes possibles, notamment la déshydratation, le fait de se lever rapidement, une maladie ou d'autres problèmes.",
            "precautions": [
                "Asseyez-vous ou allongez-vous si vous avez des vertiges",
                "Buvez suffisamment d'eau",
                "Levez-vous lentement",
                "Consultez un médecin si les vertiges sont importants ou répétés"
            ]
        }
    },


    # ======================================
    # 21. FATIGUE
    # ======================================

    "fatigue": {
        "keywords": {
            "english": ["fatigue", "tiredness", "tired"],
            "hindi": ["थकान", "थकावट"],
            "telugu": ["అలసట", "నీరసం"],
            "french": ["fatigue", "épuisement"]
        },

        "english": {
            "title": "Fatigue",
            "response": "Fatigue means feeling unusually tired or lacking energy. It can be related to poor sleep, stress, dehydration, or other health conditions.",
            "precautions": [
                "Get enough sleep",
                "Drink enough water",
                "Eat balanced meals",
                "Take regular rest breaks"
            ]
        },

        "hindi": {
            "title": "थकान",
            "response": "थकान का मतलब असामान्य रूप से थका हुआ या ऊर्जा की कमी महसूस करना है। यह कम नींद, तनाव, पानी की कमी या अन्य स्वास्थ्य समस्याओं से संबंधित हो सकती है।",
            "precautions": [
                "पर्याप्त नींद लें",
                "पर्याप्त पानी पिएं",
                "संतुलित भोजन करें",
                "नियमित रूप से आराम करें"
            ]
        },

        "telugu": {
            "title": "అలసట",
            "response": "అలసట అంటే సాధారణం కంటే ఎక్కువగా అలసిపోయినట్లు లేదా శక్తి తగ్గినట్లు అనిపించడం. ఇది నిద్రలేమి, ఒత్తిడి, నీటి కొరత లేదా ఇతర ఆరోగ్య సమస్యలతో సంబంధం కలిగి ఉండవచ్చు.",
            "precautions": [
                "తగినంత నిద్రపోండి",
                "తగినంత నీరు తాగండి",
                "సమతుల్యమైన ఆహారం తీసుకోండి",
                "క్రమం తప్పకుండా విశ్రాంతి తీసుకోండి"
            ]
        },

        "french": {
            "title": "Fatigue",
            "response": "La fatigue correspond à une sensation inhabituelle de manque d'énergie. Elle peut être liée au manque de sommeil, au stress, à la déshydratation ou à d'autres problèmes de santé.",
            "precautions": [
                "Dormez suffisamment",
                "Buvez suffisamment d'eau",
                "Mangez de manière équilibrée",
                "Prenez régulièrement des pauses"
            ]
        }
    },


    # ======================================
    # 22. INSOMNIA
    # ======================================

    "insomnia": {
        "keywords": {
            "english": ["insomnia", "can't sleep", "cannot sleep", "sleep problem"],
            "hindi": ["अनिद्रा", "नींद नहीं आना", "नींद की समस्या"],
            "telugu": ["నిద్రలేమి", "నిద్ర రావడం లేదు", "నిద్ర సమస్య"],
            "french": ["insomnie", "difficulté à dormir", "problème de sommeil"]
        },

        "english": {
            "title": "Insomnia",
            "response": "Insomnia refers to difficulty falling asleep, staying asleep, or getting restful sleep. Stress, irregular sleep schedules, and excessive screen use can contribute to sleep problems.",
            "precautions": [
                "Maintain a regular sleep schedule",
                "Avoid screens before bedtime",
                "Keep your bedroom quiet and comfortable",
                "Avoid caffeine close to bedtime"
            ]
        },

        "hindi": {
            "title": "अनिद्रा",
            "response": "अनिद्रा का मतलब सोने, सोते रहने या अच्छी नींद लेने में कठिनाई होना है। तनाव, अनियमित नींद और अधिक स्क्रीन उपयोग नींद की समस्या में योगदान कर सकते हैं।",
            "precautions": [
                "नियमित समय पर सोएं",
                "सोने से पहले स्क्रीन का उपयोग कम करें",
                "कमरे को शांत और आरामदायक रखें",
                "सोने से पहले कैफीन से बचें"
            ]
        },

        "telugu": {
            "title": "నిద్రలేమి",
            "response": "నిద్రలేమి అంటే నిద్రపోవడంలో, నిద్ర కొనసాగించడంలో లేదా ప్రశాంతమైన నిద్ర పొందడంలో ఇబ్బంది కలగడం. ఒత్తిడి, క్రమం లేని నిద్ర సమయం మరియు ఎక్కువ స్క్రీన్ ఉపయోగం నిద్ర సమస్యలకు కారణం కావచ్చు.",
            "precautions": [
                "ప్రతిరోజూ ఒకే సమయానికి నిద్రపోండి",
                "నిద్రకు ముందు స్క్రీన్ ఉపయోగాన్ని తగ్గించండి",
                "పడకగదిని ప్రశాంతంగా మరియు సౌకర్యవంతంగా ఉంచండి",
                "నిద్రకు ముందు కెఫీన్‌ను నివారించండి"
            ]
        },

        "french": {
            "title": "Insomnie",
            "response": "L'insomnie désigne une difficulté à s'endormir, à rester endormi ou à avoir un sommeil réparateur. Le stress, des horaires de sommeil irréguliers et l'utilisation excessive des écrans peuvent contribuer aux troubles du sommeil.",
            "precautions": [
                "Gardez des horaires de sommeil réguliers",
                "Évitez les écrans avant de dormir",
                "Gardez la chambre calme et confortable",
                "Évitez la caféine avant le coucher"
            ]
        }
    },


    # ======================================
    # 23. DEHYDRATION
    # ======================================

    "dehydration": {
        "keywords": {
            "english": ["dehydration", "dehydrated"],
            "hindi": ["निर्जलीकरण", "पानी की कमी"],
            "telugu": ["డీహైడ్రేషన్", "నీటి కొరత"],
            "french": ["déshydratation", "déshydraté"]
        },

        "english": {
            "title": "Dehydration",
            "response": "Dehydration happens when the body loses more fluids than it takes in. It may cause thirst, dry mouth, tiredness, or dizziness.",
            "precautions": [
                "Drink water regularly",
                "Drink extra fluids during hot weather",
                "Replace fluids after heavy sweating",
                "Avoid excessive alcohol and caffeine"
            ]
        },

        "hindi": {
            "title": "निर्जलीकरण",
            "response": "निर्जलीकरण तब होता है जब शरीर में जाने वाले तरल पदार्थ की तुलना में अधिक तरल पदार्थ बाहर निकल जाता है। इससे प्यास, मुंह का सूखना, थकान या चक्कर आ सकते हैं।",
            "precautions": [
                "नियमित रूप से पानी पिएं",
                "गर्म मौसम में अधिक तरल पदार्थ लें",
                "बहुत पसीना आने के बाद तरल पदार्थ लें",
                "अधिक शराब और कैफीन से बचें"
            ]
        },

        "telugu": {
            "title": "డీహైడ్రేషన్",
            "response": "శరీరం తీసుకునే ద్రవాల కంటే ఎక్కువ ద్రవాలను కోల్పోయినప్పుడు డీహైడ్రేషన్ ఏర్పడుతుంది. దీనివల్ల దాహం, నోరు పొడిబారడం, అలసట లేదా తల తిరగడం రావచ్చు.",
            "precautions": [
                "క్రమం తప్పకుండా నీరు తాగండి",
                "వేడి వాతావరణంలో ఎక్కువ ద్రవాలు తీసుకోండి",
                "ఎక్కువగా చెమట పట్టిన తర్వాత ద్రవాలు తీసుకోండి",
                "అధిక ఆల్కహాల్ మరియు కెఫీన్‌ను నివారించండి"
            ]
        },

        "french": {
            "title": "Déshydratation",
            "response": "La déshydratation se produit lorsque le corps perd plus de liquides qu'il n'en reçoit. Elle peut provoquer de la soif, une bouche sèche, de la fatigue ou des étourdissements.",
            "precautions": [
                "Buvez régulièrement de l'eau",
                "Buvez davantage par temps chaud",
                "Remplacez les liquides après une forte transpiration",
                "Évitez l'excès d'alcool et de caféine"
            ]
        }
    },


    # ======================================
    # 24. MUSCLE PAIN
    # ======================================

    "muscle_pain": {
        "keywords": {
            "english": ["muscle pain", "muscle ache", "sore muscles"],
            "hindi": ["मांसपेशियों में दर्द", "मांसपेशी दर्द"],
            "telugu": ["కండరాల నొప్పి", "కండరాల నొప్పులు"],
            "french": ["douleur musculaire", "douleurs musculaires", "courbatures"]
        },

        "english": {
            "title": "Muscle Pain",
            "response": "Muscle pain can occur after physical activity, muscle strain, stress, or some infections.",
            "precautions": [
                "Rest the affected muscles",
                "Stay hydrated",
                "Avoid strenuous activity for a while",
                "Use gentle stretching if comfortable"
            ]
        },

        "hindi": {
            "title": "मांसपेशियों में दर्द",
            "response": "मांसपेशियों में दर्द शारीरिक गतिविधि, मांसपेशियों पर अधिक दबाव, तनाव या कुछ संक्रमणों के बाद हो सकता है।",
            "precautions": [
                "प्रभावित मांसपेशियों को आराम दें",
                "पर्याप्त पानी पिएं",
                "कुछ समय तक अधिक मेहनत वाले काम से बचें",
                "आरामदायक होने पर हल्की स्ट्रेचिंग करें"
            ]
        },

        "telugu": {
            "title": "కండరాల నొప్పి",
            "response": "కండరాల నొప్పి శారీరక శ్రమ, కండరాలపై ఎక్కువ ఒత్తిడి, ఒత్తిడి లేదా కొన్ని ఇన్ఫెక్షన్ల తర్వాత రావచ్చు.",
            "precautions": [
                "నొప్పి ఉన్న కండరాలకు విశ్రాంతి ఇవ్వండి",
                "తగినంత నీరు తాగండి",
                "కొంతకాలం ఎక్కువ శారీరక శ్రమను నివారించండి",
                "సౌకర్యంగా ఉంటే తేలికపాటి స్ట్రెచింగ్ చేయండి"
            ]
        },

        "french": {
            "title": "Douleur musculaire",
            "response": "Les douleurs musculaires peuvent apparaître après une activité physique, une tension musculaire, un stress ou certaines infections.",
            "precautions": [
                "Reposez les muscles concernés",
                "Restez bien hydraté",
                "Évitez les activités physiques intenses pendant un certain temps",
                "Faites des étirements doux si cela est confortable"
            ]
        }
    },


    # ======================================
    # 25. JOINT PAIN
    # ======================================

    "joint_pain": {
        "keywords": {
            "english": ["joint pain", "joint ache", "painful joints"],
            "hindi": ["जोड़ों में दर्द", "जोड़ का दर्द"],
            "telugu": ["కీళ్ల నొప్పి", "కీళ్లలో నొప్పి"],
            "french": ["douleur articulaire", "douleurs articulaires"]
        },

        "english": {
            "title": "Joint Pain",
            "response": "Joint pain can have many causes, including overuse, injuries, inflammation, or other health conditions.",
            "precautions": [
                "Rest the affected joint",
                "Avoid activities that increase the pain",
                "Maintain a healthy body weight",
                "Use gentle movement when comfortable"
            ]
        },

        "hindi": {
            "title": "जोड़ों में दर्द",
            "response": "जोड़ों में दर्द के कई कारण हो सकते हैं, जैसे अधिक उपयोग, चोट, सूजन या अन्य स्वास्थ्य समस्याएं।",
            "precautions": [
                "प्रभावित जोड़ को आराम दें",
                "ऐसी गतिविधियों से बचें जिनसे दर्द बढ़ता है",
                "स्वस्थ शरीर का वजन बनाए रखें",
                "आरामदायक होने पर हल्की गतिविधि करें"
            ]
        },

        "telugu": {
            "title": "కీళ్ల నొప్పి",
            "response": "కీళ్ల నొప్పికి ఎక్కువగా ఉపయోగించడం, గాయాలు, వాపు లేదా ఇతర ఆరోగ్య సమస్యలు వంటి అనేక కారణాలు ఉండవచ్చు.",
            "precautions": [
                "నొప్పి ఉన్న కీళ్లకు విశ్రాంతి ఇవ్వండి",
                "నొప్పిని పెంచే కార్యకలాపాలను నివారించండి",
                "ఆరోగ్యకరమైన శరీర బరువును కొనసాగించండి",
                "సౌకర్యంగా ఉంటే తేలికపాటి కదలికలు చేయండి"
            ]
        },

        "french": {
            "title": "Douleur articulaire",
            "response": "Les douleurs articulaires peuvent avoir de nombreuses causes, notamment la surutilisation, les blessures, l'inflammation ou d'autres problèmes de santé.",
            "precautions": [
                "Reposez l'articulation concernée",
                "Évitez les activités qui augmentent la douleur",
                "Maintenez un poids corporel sain",
                "Faites des mouvements doux si cela est confortable"
            ]
        }
    },


    # ======================================
    # 26. SKIN RASH
    # ======================================

    "skin_rash": {
        "keywords": {
            "english": ["skin rash", "rash", "skin irritation"],
            "hindi": ["त्वचा पर दाने", "चकत्ते", "त्वचा में जलन"],
            "telugu": ["చర్మంపై దద్దుర్లు", "దద్దుర్లు", "చర్మం చికాకు"],
            "french": ["éruption cutanée", "éruption", "irritation de la peau"]
        },

        "english": {
            "title": "Skin Rash",
            "response": "A skin rash can have many causes, including allergies, irritation, infections, or other skin conditions.",
            "precautions": [
                "Keep the affected area clean",
                "Avoid products that irritate the skin",
                "Avoid scratching the affected area",
                "Seek medical advice if the rash is severe or spreading"
            ]
        },

        "hindi": {
            "title": "त्वचा पर दाने",
            "response": "त्वचा पर दाने एलर्जी, जलन, संक्रमण या अन्य त्वचा संबंधी समस्याओं के कारण हो सकते हैं।",
            "precautions": [
                "प्रभावित जगह को साफ रखें",
                "त्वचा में जलन पैदा करने वाले उत्पादों से बचें",
                "प्रभावित जगह को खुजलाने से बचें",
                "यदि दाने गंभीर हों या फैल रहे हों तो डॉक्टर से सलाह लें"
            ]
        },

        "telugu": {
            "title": "చర్మంపై దద్దుర్లు",
            "response": "చర్మంపై దద్దుర్లు అలర్జీలు, చికాకు, ఇన్ఫెక్షన్లు లేదా ఇతర చర్మ సమస్యల వల్ల రావచ్చు.",
            "precautions": [
                "ప్రభావిత ప్రాంతాన్ని శుభ్రంగా ఉంచండి",
                "చర్మానికి చికాకు కలిగించే ఉత్పత్తులను నివారించండి",
                "ప్రభావిత ప్రాంతాన్ని గోకడం నివారించండి",
                "దద్దుర్లు తీవ్రంగా ఉంటే లేదా వ్యాపిస్తుంటే వైద్యుడిని సంప్రదించండి"
            ]
        },

        "french": {
            "title": "Éruption cutanée",
            "response": "Une éruption cutanée peut avoir de nombreuses causes, notamment des allergies, une irritation, des infections ou d'autres problèmes de peau.",
            "precautions": [
                "Gardez la zone concernée propre",
                "Évitez les produits qui irritent la peau",
                "Évitez de gratter la zone concernée",
                "Consultez un professionnel de santé si l'éruption est sévère ou s'étend"
            ]
        }
    },


    # ======================================
    # 27. ITCHING
    # ======================================

    "itching": {
        "keywords": {
            "english": ["itching", "itchy skin", "itch"],
            "hindi": ["खुजली", "त्वचा में खुजली"],
            "telugu": ["దురద", "చర్మం దురద"],
            "french": ["démangeaisons", "démangeaison", "peau qui gratte"]
        },

        "english": {
            "title": "Itching",
            "response": "Itching can be caused by dry skin, allergies, insect bites, irritation, or various skin conditions.",
            "precautions": [
                "Keep your skin moisturized",
                "Avoid known irritants",
                "Take a cool shower if helpful",
                "Avoid scratching the skin"
            ]
        },

        "hindi": {
            "title": "खुजली",
            "response": "खुजली सूखी त्वचा, एलर्जी, कीड़े के काटने, जलन या विभिन्न त्वचा संबंधी समस्याओं के कारण हो सकती है।",
            "precautions": [
                "त्वचा को मॉइस्चराइज रखें",
                "ज्ञात जलन पैदा करने वाली चीजों से बचें",
                "जरूरत होने पर ठंडे पानी से नहाएं",
                "त्वचा को खुजलाने से बचें"
            ]
        },

        "telugu": {
            "title": "దురద",
            "response": "దురద పొడి చర్మం, అలర్జీలు, పురుగులు కుట్టడం, చికాకు లేదా వివిధ చర్మ సమస్యల వల్ల రావచ్చు.",
            "precautions": [
                "చర్మాన్ని తేమగా ఉంచండి",
                "చికాకు కలిగించే వస్తువులను నివారించండి",
                "ఉపయోగకరంగా అనిపిస్తే చల్లని నీటితో స్నానం చేయండి",
                "చర్మాన్ని గోకడం నివారించండి"
            ]
        },

        "french": {
            "title": "Démangeaisons",
            "response": "Les démangeaisons peuvent être causées par une peau sèche, des allergies, des piqûres d'insectes, une irritation ou diverses affections cutanées.",
            "precautions": [
                "Hydratez régulièrement votre peau",
                "Évitez les irritants connus",
                "Prenez une douche fraîche si cela vous soulage",
                "Évitez de gratter la peau"
            ]
        }
    },


    # ======================================
    # 28. EYE STRAIN
    # ======================================

    "eye_strain": {
        "keywords": {
            "english": ["eye strain", "tired eyes", "eye fatigue"],
            "hindi": ["आंखों में थकान", "आंखों पर तनाव", "आंखों की थकान"],
            "telugu": ["కళ్ల అలసట", "కళ్లపై ఒత్తిడి", "కంటి అలసట"],
            "french": ["fatigue oculaire", "yeux fatigués", "fatigue des yeux"]
        },

        "english": {
            "title": "Eye Strain",
            "response": "Eye strain can happen after prolonged screen use, reading, or activities that require intense visual focus.",
            "precautions": [
                "Take regular breaks from screens",
                "Keep a comfortable viewing distance",
                "Adjust screen brightness",
                "Get enough sleep"
            ]
        },

        "hindi": {
            "title": "आंखों की थकान",
            "response": "लंबे समय तक स्क्रीन देखने, पढ़ने या लगातार ध्यान केंद्रित करने वाले काम के बाद आंखों में थकान हो सकती है।",
            "precautions": [
                "स्क्रीन से नियमित ब्रेक लें",
                "स्क्रीन से उचित दूरी बनाए रखें",
                "स्क्रीन की चमक को आरामदायक स्तर पर रखें",
                "पर्याप्त नींद लें"
            ]
        },

        "telugu": {
            "title": "కళ్ల అలసట",
            "response": "ఎక్కువసేపు స్క్రీన్ చూడటం, చదవడం లేదా ఎక్కువగా దృష్టిని కేంద్రీకరించే పనుల తర్వాత కళ్ల అలసట రావచ్చు.",
            "precautions": [
                "స్క్రీన్ నుండి క్రమం తప్పకుండా విరామం తీసుకోండి",
                "స్క్రీన్‌కు సౌకర్యవంతమైన దూరం ఉంచండి",
                "స్క్రీన్ ప్రకాశాన్ని సర్దుబాటు చేయండి",
                "తగినంత నిద్రపోండి"
            ]
        },

        "french": {
            "title": "Fatigue oculaire",
            "response": "La fatigue oculaire peut apparaître après une utilisation prolongée des écrans, la lecture ou des activités nécessitant une concentration visuelle importante.",
            "precautions": [
                "Faites régulièrement des pauses devant les écrans",
                "Gardez une distance confortable avec l'écran",
                "Réglez la luminosité de l'écran",
                "Dormez suffisamment"
            ]
        }
    },


    # ======================================
    # 29. ANXIETY
    # ======================================

    "anxiety": {
        "keywords": {
            "english": ["anxiety", "anxious", "worry", "nervous"],
            "hindi": ["चिंता", "घबराहट", "बेचैनी"],
            "telugu": ["ఆందోళన", "కంగారు", "భయం"],
            "french": ["anxiété", "angoisse", "inquiétude", "nerveux"]
        },

        "english": {
            "title": "Anxiety",
            "response": "Anxiety can involve feelings of worry, nervousness, or uneasiness. Occasional anxiety is common, but persistent or severe anxiety may need professional support.",
            "precautions": [
                "Practice slow and deep breathing",
                "Get regular physical activity",
                "Maintain a regular sleep schedule",
                "Talk to someone you trust"
            ]
        },

        "hindi": {
            "title": "चिंता",
            "response": "चिंता में लगातार चिंता, घबराहट या बेचैनी की भावना हो सकती है। कभी-कभी चिंता सामान्य होती है, लेकिन लगातार या गंभीर चिंता के लिए पेशेवर सहायता की आवश्यकता हो सकती है।",
            "precautions": [
                "धीमी और गहरी सांस लेने का अभ्यास करें",
                "नियमित शारीरिक गतिविधि करें",
                "नियमित नींद का समय बनाए रखें",
                "किसी भरोसेमंद व्यक्ति से बात करें"
            ]
        },

        "telugu": {
            "title": "ఆందోళన",
            "response": "ఆందోళనలో ఎక్కువగా ఆలోచించడం, కంగారు లేదా అసౌకర్యంగా అనిపించడం ఉండవచ్చు. అప్పుడప్పుడు ఆందోళన సాధారణమే, కానీ నిరంతరంగా లేదా తీవ్రంగా ఉంటే నిపుణుల సహాయం అవసరం కావచ్చు.",
            "precautions": [
                "నెమ్మదిగా మరియు లోతుగా శ్వాస తీసుకోవడం సాధన చేయండి",
                "క్రమం తప్పకుండా శారీరక వ్యాయామం చేయండి",
                "క్రమమైన నిద్ర సమయాన్ని పాటించండి",
                "మీరు నమ్మే వ్యక్తితో మాట్లాడండి"
            ]
        },

        "french": {
            "title": "Anxiété",
            "response": "L'anxiété peut se manifester par des inquiétudes, de la nervosité ou un sentiment de malaise. Une anxiété occasionnelle est courante, mais une anxiété persistante ou sévère peut nécessiter un soutien professionnel.",
            "precautions": [
                "Pratiquez une respiration lente et profonde",
                "Faites régulièrement de l'activité physique",
                "Gardez des horaires de sommeil réguliers",
                "Parlez à une personne de confiance"
            ]
        }
    },


    # ======================================
    # 30. NASAL CONGESTION
    # ======================================

    "congestion": {
        "keywords": {
            "english": [
                "congestion",
                "nasal congestion",
                "stuffy nose",
                "blocked nose",
                "runny nose"
            ],
            "hindi": [
                "नाक बंद",
                "नाक जाम",
                "नाक बहना",
                "नाक में जकड़न"
            ],
            "telugu": [
                "ముక్కు మూసుకుపోవడం",
                "ముక్కు దిబ్బడ",
                "ముక్కు కారడం"
            ],
            "french": [
                "congestion nasale",
                "nez bouché",
                "nez qui coule"
            ]
        },

        "english": {
            "title": "Nasal Congestion",
            "response": "Nasal congestion can happen with a common cold, allergies, or irritation of the nasal passages.",
            "precautions": [
                "Drink plenty of fluids",
                "Get enough rest",
                "Use a humidifier if the air is dry",
                "Avoid smoke and other irritants"
            ]
        },

        "hindi": {
            "title": "नाक बंद होना",
            "response": "नाक बंद होना सामान्य सर्दी, एलर्जी या नाक के अंदर जलन के कारण हो सकता है।",
            "precautions": [
                "भरपूर तरल पदार्थ पिएं",
                "पर्याप्त आराम करें",
                "हवा सूखी होने पर ह्यूमिडिफायर का उपयोग करें",
                "धुएं और अन्य जलन पैदा करने वाली चीजों से बचें"
            ]
        },

        "telugu": {
            "title": "ముక్కు దిబ్బడ",
            "response": "ముక్కు దిబ్బడ సాధారణ జలుబు, అలర్జీలు లేదా ముక్కు లోపల చికాకు వల్ల రావచ్చు.",
            "precautions": [
                "తగినంత ద్రవాలు తాగండి",
                "తగినంత విశ్రాంతి తీసుకోండి",
                "గాలి పొడిగా ఉంటే హ్యూమిడిఫైయర్ ఉపయోగించండి",
                "పొగ మరియు ఇతర చికాకు కలిగించే వాటిని నివారించండి"
            ]
        },

        "french": {
            "title": "Congestion nasale",
            "response": "La congestion nasale peut survenir avec un rhume, des allergies ou une irritation des voies nasales.",
            "precautions": [
                "Buvez beaucoup de liquides",
                "Reposez-vous suffisamment",
                "Utilisez un humidificateur si l'air est sec",
                "Évitez la fumée et les autres irritants"
            ]
        }
    }

}


    # ==========================================
# CHAT API
# ==========================================

@app.post("/chat")
def chat(request: ChatRequest):

    user_message = request.message.strip().lower()

    # Search symptoms
    for symptom, data in health_data.items():

        # Search all languages
        for detected_language, keywords in data["keywords"].items():

            # Search all keywords
            for keyword in keywords:

                keyword = keyword.lower().strip()

                if keyword in user_message:

                    result = data[detected_language]

                    return {
                        "success": True,
                        "symptom": symptom,
                        "language": detected_language,
                        "title": result["title"],
                        "response": result["response"],
                        "precautions": result["precautions"]
                    }

    # ======================================
    # NO SYMPTOM FOUND
    # ======================================

    messages = {
        "english": "Sorry, I don't have information about that symptom yet.",
        "hindi": "क्षमा करें, मेरे पास अभी इस लक्षण की जानकारी नहीं है।",
        "telugu": "క్షమించండి, ఈ లక్షణం గురించి నా దగ్గర ఇంకా సమాచారం లేదు.",
        "french": "Désolé, je n'ai pas encore d'informations sur ce symptôme."
    }

    return {
        "success": False,
        "language": request.language,
        "response": messages.get(
            request.language,
            messages["english"]
        )
    }


# ==========================================
# HOME
# ==========================================

@app.get("/")
def home():

    return {
        "message": "Health AI Chatbot FastAPI Backend is running!"
    }