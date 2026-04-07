import streamlit as st

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

st.title("📊 System Dashboard")
st.subheader("How the Hybrid Medical Diagnosis System Works")

st.markdown("---")

# Overview
st.header("🔍 Project Overview")
st.write("""
This system is a **Hybrid Medical Diagnosis Prediction System** that combines:

- **Part A: Machine Learning Brain**
- **Part B: Expert System Brain**

The goal is to predict diseases from symptoms and explain the reasoning behind the prediction.
""")

st.markdown("---")

# Architecture
st.header("🏗️ System Architecture")
st.code("""
User selects symptoms
        ↓
Input Preprocessing
        ↓
 ┌─────────────────────────────┐
 │                             │
 ▼                             ▼
Part A: Machine Learning Brain   Part B: Expert System Brain
(Random Forest Model)            (Rules + Inference Engine)
        │                             │
        ▼                             ▼
Disease Prediction              Rule Matching / Reasoning
        │                             │
        └──────────────┬──────────────┘
                       ▼
              Explanation Module
                       ▼
                Final Output
""")

st.markdown("---")

# Part A
st.header("🧠 Part A — Machine Learning Brain")
st.write("""
This module learns disease patterns from the Kaggle dataset.

### It works like this:
1. Read dataset (`Training.csv`, `Testing.csv`)
2. Convert symptoms into features
3. Train a **Random Forest model**
4. Predict the most likely disease from user symptoms

### Output:
- Predicted disease
- Top 3 predictions
- Confidence score
""")

st.code("""
Dataset → Train Model → Learn Patterns → Predict Disease
""")

st.markdown("---")

# Part B
st.header("📚 Part B — Expert System Brain")
st.write("""
This module adds **reasoning and explanation** to the system.

### It contains:
- **Knowledge Base** → Medical IF–THEN rules
- **Inference Engine** → Matches rules with symptoms
- **Explanation Module** → Explains why prediction happened

### Example Rule:
IF fever AND cough AND fatigue THEN Flu likely
""")

st.code("""
User Symptoms → Check Rules → Match Conditions → Explanation
""")

st.markdown("---")

# Forward Chaining
st.header("➡️ Forward Chaining")
st.write("""
Forward Chaining is **data-driven reasoning**.

It starts from the **patient symptoms (facts)** and moves toward the **disease (conclusion)**.

### Example:
Facts:
- Fever = True
- Cough = True
- Fatigue = True

Rule:
IF Fever AND Cough AND Fatigue THEN Flu

Conclusion:
Flu predicted
""")

st.code("""
Symptoms → Match Rules → Fire Rule → Disease
""")

st.markdown("---")

# Backward Chaining
st.header("⬅️ Backward Chaining")
st.write("""
Backward Chaining is **goal-driven reasoning**.

It starts from a **disease hypothesis** and checks whether required symptoms are present.

### Example:
Goal:
Does patient have Flu?

Checks:
- Fever? ✔
- Cough? ✔
- Fatigue? ✔

Conclusion:
Flu confirmed
""")

st.code("""
Disease Hypothesis → Check Required Symptoms → Confirm / Reject
""")

st.markdown("---")

# SLD Resolution
st.header("🧩 SLD Resolution")
st.write("""
SLD Resolution is a **logical proof process** used in rule-based systems.

It proves a diagnosis by breaking it into smaller symptom checks.

### Example:
Goal:
Diagnose(Flu)

Rule:
Diagnose(Flu) :- Fever, Cough, Fatigue

Resolution:
1. Check Fever
2. Check Cough
3. Check Fatigue

If all are true → diagnosis is proven
""")

st.code("""
Goal: Diagnose(Flu)
        ↓
Check Fever?
        ↓
Check Cough?
        ↓
Check Fatigue?
        ↓
PROVEN
""")

st.markdown("---")

# End to End Flow
st.header("🔄 End-to-End Flow")
st.code("""
Patient Symptoms
     │
     ▼
[Symptom Input Form]
     │
     ▼
[Preprocessing Layer]
(Convert symptoms into binary vector)
     │
     ├──────────────► [Machine Learning Brain]
     │                 (Random Forest Model)
     │                          │
     │                          ▼
     │               [Predicted Disease + Probability]
     │
     └──────────────► [Knowledge Base]
                       (Rules / Facts / Advice)
                                  │
                                  ▼
                        [Inference Engine]
                       (Rule Matching / Explanation)
                                  │
                                  ▼
                    [Final Diagnosis Support Output]
""")

st.success("✅ Dashboard ready — use the Predict page to test the system.")
