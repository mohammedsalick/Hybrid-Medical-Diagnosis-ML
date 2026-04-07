import joblib
import numpy as np
from pathlib import Path

MODEL_PATH = Path("models/random_forest_model.pkl")
LABEL_ENCODER_PATH = Path("models/label_encoder.pkl")
SYMPTOMS_PATH = Path("models/symptom_columns.pkl")


def load_artifacts():
    model = joblib.load(MODEL_PATH)
    label_encoder = joblib.load(LABEL_ENCODER_PATH)
    symptom_columns = joblib.load(SYMPTOMS_PATH)
    return model, label_encoder, symptom_columns


def build_input_vector(selected_symptoms, symptom_columns):
    input_vector = np.zeros(len(symptom_columns))
    for symptom in selected_symptoms:
        if symptom in symptom_columns:
            idx = symptom_columns.index(symptom)
            input_vector[idx] = 1
    return input_vector.reshape(1, -1)


def get_top_predictions(model, label_encoder, input_vector, top_n=3):
    probabilities = model.predict_proba(input_vector)[0]
    top_indices = np.argsort(probabilities)[::-1][:top_n]

    results = []
    for idx in top_indices:
        disease = label_encoder.inverse_transform([idx])[0]
        confidence = round(float(probabilities[idx]) * 100, 2)
        results.append((disease, confidence))

    return results
