import streamlit as st
from ui_components import (
    hero_markdown,
    inject_global_css,
    render_flow_stepper,
    render_nav_rail,
    render_sidebar_journey,
)

st.set_page_config(
    page_title="Hybrid Medical Diagnosis System",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_global_css()
render_sidebar_journey()

render_flow_stepper("home")
render_nav_rail("home")

st.markdown(
    hero_markdown(
        "Hybrid Medical Diagnosis System",
        "Follow the flow: orient yourself here, read how ML and rules work on Dashboard, then run a case on Predict.",
    ),
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="journey-card">
  <p style="margin:0 0 0.35rem 0;color:#94a3b8;font-size:0.9rem;"><strong style="color:#e2e8f0;">Suggested path</strong> (about 5–10 minutes)</p>
  <ol style="margin:0;padding-left:1.2rem;color:#cbd5e1;line-height:1.75;font-size:0.95rem;">
    <li><strong style="color:#f8fafc;">Home</strong> — you are here: scope and disclaimer.</li>
    <li><strong style="color:#f8fafc;">Dashboard</strong> — architecture, ML vs expert system, chaining & flow.</li>
    <li><strong style="color:#f8fafc;">Predict</strong> — add symptoms, run the hybrid pipeline, read results.</li>
  </ol>
</div>
    """,
    unsafe_allow_html=True,
)

st.markdown("##### Next step")
next_col, rest_col = st.columns([1, 2])
with next_col:
    st.page_link(
        "pages/1_Dashboard.py",
        label="Open Dashboard",
        icon="📊",
        use_container_width=True,
    )
with rest_col:
    st.caption("Read the system design before running predictions — it makes the demo easier to explain.")

st.markdown("---")

c1, c2 = st.columns(2, gap="large")
with c1:
    st.markdown(
        """
<div class="hybrid-card">
  <h3 style="margin:0 0 0.5rem 0;color:#f8fafc;font-size:1.05rem;">Dashboard</h3>
  <p style="margin:0 0 0.85rem 0;color:#94a3b8;line-height:1.55;">Diagrams, Part A vs Part B, forward / backward chaining, and end-to-end flow in tabs.</p>
</div>
        """,
        unsafe_allow_html=True,
    )
    st.page_link(
        "pages/1_Dashboard.py",
        label="Go to Dashboard",
        icon="📊",
        use_container_width=True,
    )

with c2:
    st.markdown(
        """
<div class="hybrid-card">
  <h3 style="margin:0 0 0.5rem 0;color:#f8fafc;font-size:1.05rem;">Predict</h3>
  <p style="margin:0 0 0.85rem 0;color:#94a3b8;line-height:1.55;">Add symptoms one by one, run the model, see top-3 classes, rules, and precautions.</p>
</div>
        """,
        unsafe_allow_html=True,
    )
    st.page_link(
        "pages/2_Predict.py",
        label="Go to Predict",
        icon="🩺",
        use_container_width=True,
    )

st.info(
    "Educational and decision-support use only — not a substitute for professional medical diagnosis."
)
