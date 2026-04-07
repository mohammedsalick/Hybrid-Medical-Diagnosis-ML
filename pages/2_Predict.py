import streamlit as st
from utils import load_artifacts, build_input_vector, get_top_predictions
from knowledge.rules import evaluate_rules
from knowledge.advice import get_advice
from ui_components import inject_global_css, render_pipeline_animation, hero_markdown

st.set_page_config(page_title="Predict Disease", page_icon="🩺", layout="wide")

inject_global_css()

st.markdown(
    hero_markdown(
        "Clinical inference workspace",
        "Map symptoms through the hybrid stack: vectorization, the ML brain, the knowledge base, and rule-based explanations — with a live pipeline animation.",
    ),
    unsafe_allow_html=True,
)

if "prediction" not in st.session_state:
    st.session_state.prediction = None

model, label_encoder, symptom_columns = load_artifacts()

left, right = st.columns([1.05, 1], gap="large")

with left:
    st.markdown(
        '<div class="hybrid-card"><p style="margin:0 0 0.75rem 0;color:#94a3b8;font-size:0.9rem;">Step 1 — Symptom capture</p></div>',
        unsafe_allow_html=True,
    )
    selected_symptoms = st.multiselect(
        "Select every symptom that applies",
        options=sorted(symptom_columns),
        placeholder="Type or pick symptoms — the pipeline reacts as you select",
        label_visibility="collapsed",
    )

    n = len(selected_symptoms)
    if n:
        chips = "".join(
            f'<span class="sym-chip">{s.replace("_", " ")}</span>' for s in selected_symptoms[:18]
        )
        more = f'<span class="sym-chip dim">+{n - 18} more</span>' if n > 18 else ""
        st.markdown(
            f"""
<style>
.sym-row {{
  display: flex; flex-wrap: wrap; gap: 0.45rem; margin: 0.75rem 0 1rem 0;
}}
.sym-chip {{
  display: inline-block;
  padding: 0.35rem 0.75rem;
  border-radius: 999px;
  font-size: 0.78rem;
  font-weight: 600;
  color: #ecfdf5;
  background: linear-gradient(135deg, rgba(45,212,191,0.25), rgba(99,102,241,0.2));
  border: 1px solid rgba(45,212,191,0.35);
  animation: chipIn 0.45s cubic-bezier(0.22, 1, 0.36, 1) both;
}}
.sym-chip.dim {{ opacity: 0.75; border-style: dashed; }}
@keyframes chipIn {{
  from {{ opacity: 0; transform: translateY(8px) scale(0.92); }}
  to {{ opacity: 1; transform: translateY(0) scale(1); }}
}}
</style>
<div class="sym-row">{chips}{more}</div>
            """,
            unsafe_allow_html=True,
        )

    run = st.button("Run hybrid diagnosis", type="primary", use_container_width=True)

with right:
    st.markdown(
        '<div class="hybrid-card"><p style="margin:0 0 0.5rem 0;color:#94a3b8;font-size:0.9rem;">Live data flow</p>'
        "<p style=\"margin:0;color:#64748b;font-size:0.8rem;\">Symptoms → preprocess → ML brain → knowledge → rules & output</p></div>",
        unsafe_allow_html=True,
    )

pred = st.session_state.prediction
pred_complete = pred is not None
disease_for_anim = pred["disease"] if pred else None
conf_for_anim = pred["confidence"] if pred else None

anim_key = f"pipe_{n}_{int(pred_complete)}_{hash(tuple(selected_symptoms)) % 10**9}"

render_pipeline_animation(
    symptom_count=n,
    prediction_complete=pred_complete,
    disease=disease_for_anim,
    confidence=conf_for_anim,
    height=360,
    component_key=anim_key,
)

if run:
    if not selected_symptoms:
        st.warning("Choose at least one symptom to run the pipeline.")
        st.session_state.prediction = None
    else:
        input_vector = build_input_vector(selected_symptoms, symptom_columns)
        top_predictions = get_top_predictions(model, label_encoder, input_vector, top_n=3)
        predicted_disease = top_predictions[0][0]
        confidence = top_predictions[0][1]
        matched_rules, warnings = evaluate_rules(selected_symptoms)
        advice = get_advice(predicted_disease)
        st.session_state.prediction = {
            "disease": predicted_disease,
            "confidence": confidence,
            "top": top_predictions,
            "rules": matched_rules,
            "warnings": warnings,
            "advice": advice,
        }
        st.rerun()

pred = st.session_state.prediction

if pred:
    st.markdown("---")
    st.markdown("### Diagnosis output")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Primary hypothesis", pred["disease"])
    with c2:
        st.metric("Model confidence", f"{pred['confidence']:.1f}%")
    with c3:
        st.metric("Expert rules fired", len(pred["rules"]))

    a, b = st.columns(2, gap="large")
    with a:
        st.markdown("#### Ranked alternatives")
        max_score = max(s for _, s in pred["top"]) or 1.0
        for i, (name, score) in enumerate(pred["top"], start=1):
            st.caption(f"{i}. {name}")
            st.progress(min(1.0, float(score) / 100.0))
            st.caption(f"{score:.2f}%")

    with b:
        st.markdown("#### Expert system")
        if pred["rules"]:
            for rule in pred["rules"]:
                st.success(rule)
        else:
            st.info("No handcrafted rule fired — interpretation leans on the Random Forest model.")

        if pred["warnings"]:
            st.markdown("##### Alerts")
            for w in pred["warnings"]:
                st.error(w)

    st.markdown("#### Care suggestions")
    for tip in pred["advice"]:
        st.markdown(f"- {tip}")

    st.markdown("---")
    st.caption(
        "Educational decision-support only — not a substitute for licensed medical care."
    )
