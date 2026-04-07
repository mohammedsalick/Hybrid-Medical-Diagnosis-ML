import html
import streamlit as st
from utils import load_artifacts, build_input_vector, get_top_predictions
from knowledge.rules import evaluate_rules
from knowledge.advice import get_advice
from ui_components import (
    hero_markdown,
    inject_global_css,
    render_flow_stepper,
    render_nav_rail,
    render_pipeline_animation,
    render_sidebar_journey,
)

st.set_page_config(page_title="Predict Disease", page_icon="🩺", layout="wide", initial_sidebar_state="collapsed")

inject_global_css()
render_sidebar_journey()

render_flow_stepper("predict")
render_nav_rail("predict")

st.markdown(
    hero_markdown(
        "Step 3 — Clinical inference",
        "Add symptoms, run the hybrid pipeline, then read ranked hypotheses, expert rules, and precautions. The diagram below mirrors data moving through preprocessing → ML → knowledge → rules.",
    ),
    unsafe_allow_html=True,
)

if "prediction" not in st.session_state:
    st.session_state.prediction = None
if "symptoms" not in st.session_state:
    st.session_state.symptoms = []

model, label_encoder, symptom_columns = load_artifacts()

SYM_PLACEHOLDER = "— Pick a symptom, then click Add —"

left, right = st.columns([1.05, 1], gap="large")

with left:
    st.markdown(
        '<div class="hybrid-card"><p style="margin:0 0 0.75rem 0;color:#94a3b8;font-size:0.9rem;">Step 1 — Add symptoms one at a time</p></div>',
        unsafe_allow_html=True,
    )

    available = sorted(s for s in symptom_columns if s not in st.session_state.symptoms)
    picker_options = [SYM_PLACEHOLDER] + available

    def _fmt_sym(x: str) -> str:
        if x == SYM_PLACEHOLDER:
            return SYM_PLACEHOLDER
        return x.replace("_", " ").title()

    col_pick, col_add = st.columns([1, 0.35], gap="small")
    with col_pick:
        choice = st.selectbox(
            "Symptom to add",
            options=picker_options,
            format_func=_fmt_sym,
            label_visibility="collapsed",
            disabled=len(available) == 0,
            key="one_by_one_symptom_picker",
        )
    with col_add:
        st.markdown('<div style="height:0.35rem"></div>', unsafe_allow_html=True)
        add_clicked = st.button("Add", use_container_width=True, type="secondary")

    if add_clicked:
        if choice == SYM_PLACEHOLDER:
            st.warning("Choose a symptom in the list, then press **Add**.")
        elif choice in st.session_state.symptoms:
            st.warning("That symptom is already in your list.")
        else:
            st.session_state.symptoms.append(choice)
            st.rerun()

    if not available and st.session_state.symptoms:
        st.caption("All dataset symptoms are already selected.")
    elif not available and not st.session_state.symptoms:
        st.error("No symptoms available from the model — check `data/` and retrain.")

    n = len(st.session_state.symptoms)
    selected_symptoms = list(st.session_state.symptoms)

    if n:
        st.markdown(
            '<p style="color:#94a3b8;font-size:0.82rem;margin:0.75rem 0 0.4rem 0;">Selected symptoms <span style="color:#64748b;">(remove any row before running)</span></p>',
            unsafe_allow_html=True,
        )
        for i, s in enumerate(selected_symptoms):
            r1, r2 = st.columns([5, 1], gap="small")
            with r1:
                st.markdown(
                    f'<div class="sym-line">{i + 1}. <strong style="color:#e2e8f0;">{html.escape(s.replace("_", " ").title())}</strong> <span style="color:#475569;font-size:0.8rem;">({html.escape(s)})</span></div>',
                    unsafe_allow_html=True,
                )
            with r2:
                if st.button("Remove", key=f"rm_sym_{i}", use_container_width=True):
                    st.session_state.symptoms.pop(i)
                    st.rerun()

        chips = "".join(
            f'<span class="sym-chip" style="animation-delay:{i * 0.04}s">{html.escape(s.replace("_", " "))}</span>'
            for i, s in enumerate(selected_symptoms[:20])
        )
        more = f'<span class="sym-chip dim">+{n - 20} more</span>' if n > 20 else ""
        st.markdown(
            f"""
<style>
.sym-line {{ padding: 0.15rem 0; }}
.sym-row {{
  display: flex; flex-wrap: wrap; gap: 0.45rem; margin: 0.6rem 0 0.9rem 0;
}}
.sym-chip {{
  display: inline-block;
  padding: 0.3rem 0.65rem;
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 600;
  color: #ecfdf5;
  background: linear-gradient(135deg, rgba(45,212,191,0.22), rgba(99,102,241,0.18));
  border: 1px solid rgba(45,212,191,0.3);
  animation: chipIn 0.4s cubic-bezier(0.22, 1, 0.36, 1) both;
}}
.sym-chip.dim {{ opacity: 0.75; border-style: dashed; }}
@keyframes chipIn {{
  from {{ opacity: 0; transform: translateY(6px) scale(0.95); }}
  to {{ opacity: 1; transform: translateY(0) scale(1); }}
}}
</style>
<div class="sym-row">{chips}{more}</div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.info("Use the dropdown to add your first symptom.")

    row_run, row_clear = st.columns([1, 1], gap="small")
    with row_run:
        run = st.button("Run hybrid diagnosis", type="primary", use_container_width=True)
    with row_clear:
        clear_output = st.button("Clear output", use_container_width=True, type="secondary")

    if st.button("Clear all symptoms", use_container_width=True):
        st.session_state.symptoms = []
        st.session_state.prediction = None
        st.rerun()

with right:
    st.markdown(
        '<div class="hybrid-card"><p style="margin:0 0 0.5rem 0;color:#94a3b8;font-size:0.9rem;">Live data flow</p>'
        "<p style=\"margin:0;color:#64748b;font-size:0.8rem;\">The animated pipeline appears below after you interact. Add symptoms to light the path; run diagnosis to play the full hybrid tour.</p></div>",
        unsafe_allow_html=True,
    )

if clear_output:
    st.session_state.prediction = None
    st.rerun()

if run:
    if not selected_symptoms:
        st.warning("Add at least one symptom before running.")
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
pred_complete = pred is not None
disease_for_anim = pred["disease"] if pred else None
conf_for_anim = pred["confidence"] if pred else None

st.markdown(
    '<p style="color:#94a3b8;font-size:0.85rem;margin:1rem 0 0.35rem 0;">Hybrid inference pipeline</p>',
    unsafe_allow_html=True,
)
render_pipeline_animation(
    symptom_count=n,
    prediction_complete=pred_complete,
    disease=disease_for_anim,
    confidence=conf_for_anim,
    height=400,
)

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

st.markdown("---")
st.markdown("##### Other pages")
ex1, ex2 = st.columns(2, gap="medium")
with ex1:
    st.page_link("pages/1_Dashboard.py", label="Back to Dashboard", icon="📊", use_container_width=True)
with ex2:
    st.page_link("app.py", label="Back to Home", icon="🏠", use_container_width=True)
