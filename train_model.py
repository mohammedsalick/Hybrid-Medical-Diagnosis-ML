import pandas as pd
import joblib
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# Create models folder if not exists
os.makedirs("models", exist_ok=True)

# Load dataset (drop trailing-comma "Unnamed" columns from some CSV exports)
train_df = pd.read_csv("data/Training.csv")
test_df = pd.read_csv("data/Testing.csv")
train_df = train_df.loc[:, [c for c in train_df.columns if not str(c).startswith("Unnamed")]]
test_df = test_df.loc[:, [c for c in test_df.columns if not str(c).startswith("Unnamed")]]

# Features and target
X_train = train_df.drop("prognosis", axis=1)
y_train = train_df["prognosis"]

X_test = test_df.drop("prognosis", axis=1).reindex(columns=X_train.columns, fill_value=0)
y_test = test_df["prognosis"]

# Encode target labels
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.transform(y_test)

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train_encoded)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test_encoded, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:\n")
print(classification_report(y_test_encoded, y_pred))

# Save model and metadata
joblib.dump(model, "models/random_forest_model.pkl")
joblib.dump(label_encoder, "models/label_encoder.pkl")
joblib.dump(list(X_train.columns), "models/symptom_columns.pkl")

print("\nModel and artifacts saved successfully in models/")
