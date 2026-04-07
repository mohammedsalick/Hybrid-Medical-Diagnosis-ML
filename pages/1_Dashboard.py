import streamlit as st
from ui_components import (
    hero_markdown,
    inject_global_css,
    render_flow_stepper,
    render_nav_rail,
    render_sidebar_journey,
)

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")

inject_global_css()
render_sidebar_journey()

render_flow_stepper("dashboard")
render_nav_rail("dashboard")

st.markdown(
    hero_markdown(
        "Step 2 — System dashboard",
        "How the hybrid stack fits together: ML for pattern completion, rules for explainability, and classical reasoning patterns you can cite in reports. When you are ready, go to **Predict** to run a case.",
    ),
    unsafe_allow_html=True,
)

tab1, tab2, tab3 = st.tabs(["Overview & architecture", "ML & expert brains", "Chaining & flow"])

with tab1:
    st.markdown(
        """
<div class="hybrid-card">
<p style="color:#94a3b8;margin:0 0 0.75rem 0;">This system is a <strong style="color:#e2e8f0;">Hybrid Medical Diagnosis</strong> stack: <strong style="color:#2dd4bf;">Part A — ML brain</strong> plus <strong style="color:#a5b4fc;">Part B — expert rules</strong>. Together they predict from symptoms and surface human-readable reasons.</p>
</div>
        """,
        unsafe_allow_html=True,
    )
    st.code(
        """
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
        """,
        language=None,
    )

with tab2:
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        st.markdown(
            """
<div class="hybrid-card">
<h4 style="margin:0 0 0.5rem 0;color:#2dd4bf;">Part A — ML brain</h4>
<ol style="margin:0;padding-left:1.2rem;color:#cbd5e1;line-height:1.7;">
<li>Load <code>Training.csv</code> / <code>Testing.csv</code></li>
<li>Binary symptom features</li>
<li>Train <strong>Random Forest</strong></li>
<li>Output: top class + probabilities</li>
</ol>
</div>
            """,
            unsafe_allow_html=True,
        )
        st.code("Dataset → Train → Patterns → Predict", language=None)
    with c2:
        st.markdown(
            """
<div class="hybrid-card">
<h4 style="margin:0 0 0.5rem 0;color:#a5b4fc;">Part B — Expert shell</h4>
<ul style="margin:0;padding-left:1.2rem;color:#cbd5e1;line-height:1.7;">
<li><strong>Knowledge base</strong> — IF–THEN rules</li>
<li><strong>Inference</strong> — symptom subset matching</li>
<li><strong>Explanation</strong> — fired rules + warnings</li>
</ul>
<p style="margin:0.75rem 0 0 0;color:#64748b;font-size:0.9rem;">Example: IF high_fever AND chills AND sweating THEN malaria-like pattern.</p>
</div>
            """,
            unsafe_allow_html=True,
        )
        st.code("Symptoms → Rules → Match → Explanation", language=None)

with tab3:
    st.markdown("##### Forward chaining (data-driven)")
    st.write(
        "Start from **facts** (symptoms), apply rules forward toward **conclusions** (disease hypotheses)."
    )
    st.code("Symptoms → Match rules → Fire rule → Conclusion", language=None)
    st.markdown("##### Backward chaining (goal-driven)")
    st.write(
        "Start from a **goal** (e.g. “flu?”), check whether required symptoms are present."
    )
    st.code("Hypothesis → Required signs → Confirm / reject", language=None)
    st.markdown("##### SLD-style resolution")
    st.write(
        "Treat the diagnosis as a **goal literal**, resolve it against rule bodies (symptom literals) until proved or failed."
    )
    st.code(
        """
Goal: Diagnose(Flu)
   ↓ Check Fever, Cough, Fatigue
   ↓ All satisfied → PROVEN
        """,
        language=None,
    )
    st.markdown("##### End-to-end")
    st.code(
        """
Patient Symptoms → [Form] → [Binary vector]
     ├─► ML brain → scores
     └─► Knowledge / rules → explanations
              └─► Combined output
        """,
        language=None,
    )

st.markdown("---")
st.markdown("##### Continue the flow")
p, n = st.columns(2, gap="medium")
with p:
    st.page_link("app.py", label="Back to Home", icon="🏠", use_container_width=True)
with n:
    st.page_link(
        "pages/2_Predict.py",
        label="Next: Predict",
        icon="🩺",
        use_container_width=True,
    )
