def get_advice(disease):
    advice_map = {
        "Fungal infection": [
            "Maintain hygiene",
            "Keep affected area dry",
            "Consult a dermatologist if needed"
        ],
        "Allergy": [
            "Avoid allergens",
            "Drink water",
            "Consult a doctor if severe"
        ],
        "GERD": [
            "Avoid spicy foods",
            "Eat small meals",
            "Do not lie down immediately after eating"
        ],
        "Chronic cholestasis": [
            "Consult a liver specialist",
            "Avoid oily food",
            "Follow prescribed medication"
        ],
        "Drug Reaction": [
            "Stop suspected medicine only after doctor consultation",
            "Seek medical help if severe"
        ],
        "Peptic ulcer diseae": [
            "Avoid spicy food",
            "Take meals on time",
            "Consult doctor for treatment"
        ],
        "AIDS": [
            "Seek specialist consultation",
            "Follow prescribed therapy"
        ],
        "Diabetes ": [
            "Monitor blood sugar",
            "Maintain healthy diet",
            "Exercise regularly"
        ],
        "Gastroenteritis": [
            "Drink ORS / fluids",
            "Eat light food",
            "Rest well"
        ],
        "Bronchial Asthma": [
            "Avoid dust and smoke",
            "Use inhaler if prescribed",
            "Consult doctor if breathing worsens"
        ],
        "Hypertension ": [
            "Reduce salt intake",
            "Exercise regularly",
            "Monitor BP"
        ],
        "Migraine": [
            "Rest in a dark room",
            "Avoid stress",
            "Stay hydrated"
        ],
        "Dengue": [
            "Drink plenty of fluids",
            "Monitor temperature",
            "Consult doctor immediately"
        ],
        "Malaria": [
            "Get blood test confirmation",
            "Consult doctor immediately",
            "Stay hydrated"
        ],
        "Jaundice": [
            "Take rest",
            "Drink water",
            "Consult doctor"
        ],
        "Typhoid": [
            "Take complete rest",
            "Eat light food",
            "Consult doctor"
        ],
        "Common Cold": [
            "Drink warm fluids",
            "Rest well",
            "Monitor symptoms"
        ],
        "Pneumonia": [
            "Consult doctor immediately",
            "Take rest",
            "Monitor breathing"
        ]
    }

    return advice_map.get(disease, [
        "Take adequate rest",
        "Stay hydrated",
        "Consult a doctor if symptoms worsen"
    ])
