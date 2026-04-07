def evaluate_rules(selected_symptoms):
    symptoms = set(selected_symptoms)
    matched_rules = []
    warnings = []

    rules = [
        {
            "name": "Flu Rule",
            "conditions": {"fever", "cough", "fatigue"},
            "result": "Symptoms strongly match Flu / Viral Fever"
        },
        {
            "name": "Malaria Rule",
            "conditions": {"high_fever", "chills", "sweating"},
            "result": "Symptoms strongly match Malaria-like infection"
        },
        {
            "name": "Gastroenteritis Rule",
            "conditions": {"vomiting", "diarrhoea", "dehydration"},
            "result": "Symptoms suggest Gastroenteritis / stomach infection"
        },
        {
            "name": "Respiratory Infection Rule",
            "conditions": {"cough", "breathlessness", "chest_pain"},
            "result": "Symptoms suggest Respiratory or Lung-related infection"
        },
        {
            "name": "Migraine Rule",
            "conditions": {"headache", "nausea", "dizziness"},
            "result": "Symptoms suggest Migraine-like condition"
        },
    ]

    for rule in rules:
        if rule["conditions"].issubset(symptoms):
            matched_rules.append(rule["result"])

    # emergency warnings
    if {"chest_pain", "breathlessness"}.issubset(symptoms):
        warnings.append("⚠️ Urgent medical attention recommended.")

    if {"high_fever", "vomiting", "dehydration"}.issubset(symptoms):
        warnings.append("⚠️ Risk of severe infection / dehydration. Consult doctor immediately.")

    return matched_rules, warnings
