"""
Shared UI: global Streamlit styling and animated hybrid pipeline diagram (HTML).
"""
import html
import json
import streamlit.components.v1 as components


def inject_global_css() -> None:
    import streamlit as st

    st.markdown(
        """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,600;0,9..40,700;1,9..40,400&family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,700;1,9..144,600&display=swap');

html, body, [class*="css"] {
  font-family: 'DM Sans', system-ui, sans-serif;
}

h1, h2, h3 {
  font-family: 'Fraunces', Georgia, serif !important;
  letter-spacing: -0.02em;
}

/* Page background */
.stApp {
  background: radial-gradient(1200px 800px at 10% -10%, rgba(45, 212, 191, 0.08), transparent 50%),
              radial-gradient(900px 600px at 100% 0%, rgba(99, 102, 241, 0.1), transparent 45%),
              linear-gradient(165deg, #070b12 0%, #0c1220 40%, #0a0f18 100%) !important;
}

[data-testid="stHeader"] { background: rgba(7, 11, 18, 0.85); backdrop-filter: blur(12px); }
[data-testid="stToolbar"] { background: transparent; }

.block-container { padding-top: 1.25rem !important; max-width: 1200px; }

[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] label {
  color: #cbd5e1 !important;
}
.stMarkdown p, .stMarkdown li { color: #e2e8f0; }
small, .stCaption { color: #94a3b8 !important; }

/* Cards */
.hybrid-card {
  background: linear-gradient(145deg, rgba(26, 35, 50, 0.85) 0%, rgba(15, 23, 42, 0.92) 100%);
  border: 1px solid rgba(148, 163, 184, 0.12);
  border-radius: 16px;
  padding: 1.25rem 1.5rem;
  margin-bottom: 1rem;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.35), inset 0 1px 0 rgba(255,255,255,0.04);
  backdrop-filter: blur(10px);
}

/* Multiselect: focus + selection pulse */
div[data-testid="stMultiSelect"] [data-baseweb="select"] > div {
  border-radius: 12px !important;
  border: 1px solid rgba(148, 163, 184, 0.25) !important;
  background: rgba(15, 23, 42, 0.6) !important;
  transition: border-color 0.35s ease, box-shadow 0.35s ease, transform 0.2s ease !important;
}
div[data-testid="stMultiSelect"]:focus-within [data-baseweb="select"] > div,
div[data-testid="stMultiSelect"] [data-baseweb="select"]:focus-within > div {
  border-color: rgba(45, 212, 191, 0.65) !important;
  box-shadow: 0 0 0 3px rgba(45, 212, 191, 0.2), 0 8px 32px rgba(45, 212, 191, 0.12) !important;
}

/* Primary button */
.stButton > button[kind="primary"],
button[kind="primary"] {
  background: linear-gradient(135deg, #14b8a6 0%, #6366f1 100%) !important;
  border: none !important;
  border-radius: 12px !important;
  font-weight: 600 !important;
  letter-spacing: 0.02em;
  padding: 0.55rem 1.35rem !important;
  transition: transform 0.2s ease, box-shadow 0.25s ease !important;
  box-shadow: 0 4px 20px rgba(99, 102, 241, 0.35) !important;
}
.stButton > button[kind="primary"]:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 28px rgba(45, 212, 191, 0.35) !important;
}

/* Metrics / success / info boxes */
div[data-testid="stSuccess"] {
  background: rgba(16, 185, 129, 0.12) !important;
  border: 1px solid rgba(16, 185, 129, 0.35) !important;
  border-radius: 12px !important;
}
div[data-testid="stInfo"] {
  background: rgba(99, 102, 241, 0.12) !important;
  border: 1px solid rgba(99, 102, 241, 0.35) !important;
  border-radius: 12px !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #0f172a 0%, #0c1220 100%) !important;
  border-right: 1px solid rgba(148, 163, 184, 0.1) !important;
}

/* Progress bars (top 3) */
.stProgress > div > div > div > div {
  background: linear-gradient(90deg, #14b8a6, #6366f1) !important;
  border-radius: 6px !important;
}

/* Guided flow stepper */
.flow-bar-wrap {
  margin: 0 0 1rem 0;
  padding: 0.85rem 1.1rem;
  background: rgba(15, 23, 42, 0.72);
  border: 1px solid rgba(148, 163, 184, 0.14);
  border-radius: 14px;
  backdrop-filter: blur(8px);
}
.flow-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 0.35rem 0.5rem;
}
.flow-step {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  flex: 1 1 140px;
  min-width: 120px;
}
.flow-num {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.82rem;
  flex-shrink: 0;
}
.flow-step.done .flow-num {
  background: rgba(45, 212, 191, 0.18);
  border: 2px solid #2dd4bf;
  color: #5eead4;
}
.flow-step.active .flow-num {
  background: linear-gradient(135deg, #14b8a6, #6366f1);
  color: #fff;
  border: 2px solid transparent;
  box-shadow: 0 0 18px rgba(45, 212, 191, 0.45);
}
.flow-step.todo .flow-num {
  background: rgba(30, 41, 59, 0.8);
  border: 2px solid #475569;
  color: #64748b;
}
.flow-text { min-width: 0; }
.flow-title {
  display: block;
  font-weight: 600;
  color: #f1f5f9;
  font-size: 0.88rem;
  line-height: 1.2;
}
.flow-sub {
  display: block;
  font-size: 0.7rem;
  color: #64748b;
  margin-top: 0.1rem;
}
.flow-line {
  flex: 1 1 32px;
  min-width: 20px;
  max-width: 80px;
  height: 3px;
  border-radius: 2px;
  background: #334155;
  align-self: center;
}
.flow-line.done {
  background: linear-gradient(90deg, #2dd4bf, #6366f1);
  opacity: 0.95;
}
.flow-line.partial {
  background: linear-gradient(90deg, #2dd4bf 0%, #334155 85%);
}
.flow-line.todo { opacity: 0.45; }

.nav-rail-wrap {
  margin: 0 0 1.25rem 0;
  padding-bottom: 0.25rem;
  border-bottom: 1px solid rgba(148, 163, 184, 0.1);
}
.nav-rail-label {
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: #64748b !important;
  margin: 0 0 0.5rem 0 !important;
}
/* Page link buttons: full-width rail */
.nav-rail-wrap [data-testid="stPageLink-NavLink"] {
  border-radius: 10px !important;
  border: 1px solid rgba(148, 163, 184, 0.15) !important;
  background: rgba(15, 23, 42, 0.5) !important;
  padding: 0.45rem 0.65rem !important;
  transition: border-color 0.2s, background 0.2s !important;
}
.nav-rail-wrap [data-testid="stPageLink-NavLink"]:hover {
  border-color: rgba(45, 212, 191, 0.35) !important;
  background: rgba(45, 212, 191, 0.08) !important;
}

.journey-card {
  border-left: 3px solid #2dd4bf;
  padding-left: 1rem;
  margin: 0.5rem 0 1rem 0;
}
</style>
        """,
        unsafe_allow_html=True,
    )


def render_pipeline_animation(
    symptom_count: int,
    prediction_complete: bool,
    disease: str | None = None,
    confidence: float | None = None,
    height: int = 340,
) -> None:
    """Embeds an animated SVG pipeline: inputs → preprocess → ML → KB → rules → output."""
    conf_str = f"{confidence:.1f}%" if confidence is not None else "—"

    config = {
        "symptomCount": int(symptom_count),
        "complete": bool(prediction_complete),
        "disease": disease or "",
        "confidence": conf_str,
    }
    config_json = json.dumps(config)
    # Bust iframe cache when inputs change (Streamlit may reuse component instance)
    cache_bust = hash(config_json) & 0xFFFFFFFF

    html_doc = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <style>
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: 'DM Sans', system-ui, sans-serif;
      background: transparent;
      color: #e2e8f0;
      overflow: hidden;
    }}
    .wrap {{
      width: 100%;
      min-height: {height}px;
      padding: 8px 4px;
    }}
    svg {{
      width: 100%;
      height: auto;
      max-height: {height - 20}px;
    }}
    .edge {{
      fill: none;
      stroke: #334155;
      stroke-width: 2.5;
      stroke-linecap: round;
      opacity: 0.55;
    }}
    .edge.glow {{
      stroke: url(#gradLine);
      stroke-width: 3;
      opacity: 0.95;
      filter: drop-shadow(0 0 6px rgba(45,212,191,0.5));
    }}
    .edge.dash {{
      stroke-dasharray: 10 8;
      animation: dashmove 1.2s linear infinite;
    }}
    @keyframes dashmove {{
      to {{ stroke-dashoffset: -36; }}
    }}
    .node-bg {{
      fill: #1e293b;
      stroke: #475569;
      stroke-width: 2;
      transition: stroke 0.45s ease, fill 0.45s ease, filter 0.45s ease;
    }}
    .node-bg.hot {{
      stroke: #2dd4bf;
      fill: #0f2724;
      filter: drop-shadow(0 0 14px rgba(45,212,191,0.55));
    }}
    .node-bg.done {{
      stroke: #818cf8;
      fill: #1e1b3a;
      filter: drop-shadow(0 0 12px rgba(129,140,248,0.45));
    }}
    .node-label {{
      fill: #f1f5f9;
      font-size: 11px;
      font-weight: 600;
      text-anchor: middle;
      pointer-events: none;
    }}
    .node-sub {{
      fill: #94a3b8;
      font-size: 9px;
      text-anchor: middle;
    }}
    .packet {{
      fill: #2dd4bf;
      filter: drop-shadow(0 0 8px #2dd4bf);
      opacity: 0;
    }}
    .status {{
      text-align: center;
      font-size: 12px;
      color: #94a3b8;
      margin-top: 6px;
      min-height: 18px;
    }}
    .status strong {{ color: #2dd4bf; }}
  </style>
</head>
<body>
  <!-- v={cache_bust} -->
  <div class="wrap">
    <svg viewBox="0 0 920 200" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="gradLine" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" style="stop-color:#2dd4bf"/>
          <stop offset="100%" style="stop-color:#818cf8"/>
        </linearGradient>
      </defs>

      <!-- Edges -->
      <path id="p0" class="edge" d="M 118 100 L 218 100"/>
      <path id="p1" class="edge" d="M 318 100 L 418 100"/>
      <path id="p2" class="edge" d="M 518 100 L 618 100"/>
      <path id="p3" class="edge" d="M 718 100 L 818 100"/>
      <path id="p4" class="edge" d="M 118 100 Q 320 28 518 100"/>
      <path id="p5" class="edge" d="M 318 100 Q 520 172 718 100"/>

      <!-- Nodes: x centers at 68, 268, 468, 668, 868 -->
      <g class="node" data-i="0" transform="translate(68,100)">
        <circle class="node-bg" r="36"/>
        <text class="node-label" y="6">Symptoms</text>
        <text class="node-sub" y="20">Your input</text>
      </g>
      <g class="node" data-i="1" transform="translate(268,100)">
        <circle class="node-bg" r="36"/>
        <text class="node-label" y="6">Vector</text>
        <text class="node-sub" y="20">Preprocess</text>
      </g>
      <g class="node" data-i="2" transform="translate(468,100)">
        <circle class="node-bg" r="40"/>
        <text class="node-label" y="6">ML Brain</text>
        <text class="node-sub" y="20">Random Forest</text>
      </g>
      <g class="node" data-i="3" transform="translate(668,100)">
        <circle class="node-bg" r="36"/>
        <text class="node-label" y="6">Knowledge</text>
        <text class="node-sub" y="20">Base</text>
      </g>
      <g class="node" data-i="4" transform="translate(868,100)">
        <circle class="node-bg" r="38"/>
        <text class="node-label" y="6">Rules +</text>
        <text class="node-sub" y="20">Output</text>
      </g>

      <circle id="pkt" class="packet" r="6" cx="0" cy="0"/>
    </svg>
    <div class="status" id="status"></div>
  </div>
  <script>
    const CFG = {config_json};

    const edges = ['p0','p1','p2','p3'];
    const nodes = () => document.querySelectorAll('.node-bg');
    const pkt = document.getElementById('pkt');
    const statusEl = document.getElementById('status');

    function setStatus(text, html) {{
      statusEl.innerHTML = html || text;
    }}

    function activateNode(i, cls) {{
      nodes().forEach((n, j) => {{
        n.classList.remove('hot', 'done');
        if (j === i) n.classList.add(cls || 'hot');
      }});
    }}

    function pathLength(id) {{
      const p = document.getElementById(id);
      try {{ return p.getTotalLength(); }} catch(e) {{ return 200; }}
    }}

    function pointOnPath(id, t) {{
      const p = document.getElementById(id);
      const len = p.getTotalLength();
      return p.getPointAtLength(Math.min(len * t, len - 0.01));
    }}

    let animId = null;
    let t0 = performance.now();

    function clearAnim() {{
      if (animId) cancelAnimationFrame(animId);
      animId = null;
    }}

    function pulseEdges(activeCount) {{
      edges.forEach((id, i) => {{
        const el = document.getElementById(id);
        el.classList.remove('glow', 'dash');
        if (i < activeCount) {{
          el.classList.add('glow', 'dash');
        }}
      }});
    }}

    /* Continuous subtle flow when user has selected symptoms */
    function loopInputFlow() {{
      clearAnim();
      const paths = ['p0','p1'];
      let phase = 0;
      function frame(now) {{
        const t = ((now - t0) / 1800) % 1;
        const pathId = paths[Math.floor((now / 900) % 2)];
        const pt = pointOnPath(pathId, t);
        pkt.setAttribute('cx', pt.x);
        pkt.setAttribute('cy', pt.y);
        pkt.style.opacity = CFG.symptomCount > 0 ? '0.95' : '0';
        pulseEdges(CFG.symptomCount > 0 ? 2 : 0);
        if (CFG.symptomCount > 0) {{
          activateNode(t < 0.5 ? 0 : 1, 'hot');
        }} else {{
          nodes().forEach(n => n.classList.remove('hot','done'));
        }}
        if (!CFG.complete) animId = requestAnimationFrame(frame);
      }}
      animId = requestAnimationFrame(frame);
    }}

    function escHtml(s) {{
      const d = document.createElement('div');
      d.textContent = String(s || '');
      return d.innerHTML;
    }}

    /* Full pipeline tour after prediction */
    function playCompleteTour() {{
      clearAnim();
      pulseEdges(4);
      const seq = [
        {{ node: 0, path: 'p0', dur: 550 }},
        {{ node: 1, path: 'p1', dur: 550 }},
        {{ node: 2, path: 'p2', dur: 650 }},
        {{ node: 3, path: 'p3', dur: 550 }},
        {{ node: 4, path: null, dur: 450 }}
      ];
      let step = 0;
      let stepStart = performance.now();

      function finishTour() {{
        nodes().forEach(n => n.classList.add('done'));
        const d = escHtml(CFG.disease || 'Result');
        const c = escHtml(CFG.confidence || '—');
        setStatus('', 'Pipeline complete → <strong>' + d + '</strong> · confidence <strong>' + c + '</strong>');
        pkt.style.opacity = '0.35';
      }}

      function runStep(now) {{
        if (step >= seq.length) {{
          finishTour();
          return;
        }}
        const s = seq[step];
        const elapsed = now - stepStart;
        activateNode(s.node, 'hot');
        if (s.path) {{
          const t = Math.min(1, elapsed / s.dur);
          const pt = pointOnPath(s.path, t);
          pkt.setAttribute('cx', pt.x);
          pkt.setAttribute('cy', pt.y);
          pkt.style.opacity = '1';
        }} else {{
          pkt.style.opacity = '0.85';
        }}
        if (elapsed >= s.dur) {{
          const list = document.querySelectorAll('.node-bg');
          list[s.node].classList.remove('hot');
          list[s.node].classList.add('done');
          step++;
          stepStart = now;
        }}
        animId = requestAnimationFrame(runStep);
      }}
      animId = requestAnimationFrame(runStep);
    }}

    if (CFG.complete) {{
      setStatus('Running full hybrid pipeline…', '');
      setTimeout(playCompleteTour, 120);
    }} else if (CFG.symptomCount > 0) {{
      setStatus('Signals flowing to preprocessing… (<strong>' + CFG.symptomCount + '</strong> symptom' + (CFG.symptomCount === 1 ? '' : 's') + ')', '');
      loopInputFlow();
    }} else {{
      setStatus('Select symptoms to animate the path toward the <strong>ML Brain</strong>.', '');
      loopInputFlow();
    }}
  </script>
</body>
</html>
    """

    components.html(html_doc, height=height, scrolling=False)


def hero_markdown(title: str, subtitle: str) -> str:
    return f"""
<div style="
  background: linear-gradient(135deg, rgba(20, 184, 166, 0.15) 0%, rgba(99, 102, 241, 0.12) 50%, transparent 100%);
  border: 1px solid rgba(148, 163, 184, 0.15);
  border-radius: 20px;
  padding: 2rem 2.25rem;
  margin-bottom: 1.5rem;
  position: relative;
  overflow: hidden;
">
  <div style="position:absolute; inset:-40% -20% auto auto; width:55%; height:120%; background: radial-gradient(circle, rgba(99,102,241,0.18), transparent 65%); pointer-events:none; animation: heroGlow 8s ease-in-out infinite alternate;"></div>
  <style>@keyframes heroGlow {{ from {{ opacity: 0.5; transform: translate(0,0); }} to {{ opacity: 1; transform: translate(-20px, 10px); }} }}</style>
  <h1 style="font-family: 'Fraunces', Georgia, serif; font-size: clamp(1.75rem, 4vw, 2.35rem); margin: 0 0 0.5rem 0; color: #f8fafc; line-height: 1.15;">{html.escape(title)}</h1>
  <p style="margin: 0; font-size: 1.05rem; color: #94a3b8; max-width: 52ch; line-height: 1.55;">{subtitle}</p>
</div>
"""


def render_flow_stepper(current: str) -> None:
    """Shows Home → Dashboard → Predict with active / done / upcoming states."""
    import streamlit as st

    order = ("home", "dashboard", "predict")
    if current not in order:
        current = "home"
    idx = order.index(current)

    steps = [
        ("1", "Home", "Orientation", "home"),
        ("2", "Dashboard", "How the system works", "dashboard"),
        ("3", "Predict", "Symptoms & diagnosis", "predict"),
    ]

    chunks: list[str] = []
    for i, (num, title, sub, key) in enumerate(steps):
        if i < idx:
            state = "done"
        elif i == idx:
            state = "active"
        else:
            state = "todo"
        sub_esc = html.escape(sub)
        title_esc = html.escape(title)
        chunks.append(
            f'<div class="flow-step {state}"><span class="flow-num">{num}</span>'
            f'<div class="flow-text"><span class="flow-title">{title_esc}</span>'
            f'<span class="flow-sub">{sub_esc}</span></div></div>'
        )
        if i < len(steps) - 1:
            if i < idx:
                ln = "done"
            elif i == idx:
                ln = "partial"
            else:
                ln = "todo"
            chunks.append(f'<div class="flow-line {ln}"></div>')

    inner = "".join(chunks)
    st.markdown(
        f'<div class="flow-bar-wrap"><div class="flow-bar">{inner}</div></div>',
        unsafe_allow_html=True,
    )


def render_nav_rail(current: str) -> None:
    """Primary navigation: same three pages, highlights current via disabled link."""
    import streamlit as st

    st.markdown('<div class="nav-rail-wrap">', unsafe_allow_html=True)
    st.markdown(
        '<p class="nav-rail-label">Go to page</p>',
        unsafe_allow_html=True,
    )
    a, b, c = st.columns(3)
    with a:
        st.page_link("app.py", label="Home", icon="🏠", disabled=(current == "home"))
    with b:
        st.page_link(
            "pages/1_Dashboard.py",
            label="Dashboard",
            icon="📊",
            disabled=(current == "dashboard"),
        )
    with c:
        st.page_link(
            "pages/2_Predict.py",
            label="Predict",
            icon="🩺",
            disabled=(current == "predict"),
        )
    st.markdown("</div>", unsafe_allow_html=True)


def render_sidebar_journey() -> None:
    """Short sidebar hint so the default page list has context."""
    import streamlit as st

    with st.sidebar:
        st.markdown(
            """
<div style="padding:0.5rem 0 0.25rem 0;">
  <p style="margin:0;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.1em;color:#64748b;">Flow</p>
  <p style="margin:0.35rem 0 0 0;font-size:0.85rem;color:#94a3b8;line-height:1.45;">
    <strong style="color:#cbd5e1;">1</strong> Home →
    <strong style="color:#cbd5e1;">2</strong> Dashboard →
    <strong style="color:#cbd5e1;">3</strong> Predict
  </p>
</div>
            """,
            unsafe_allow_html=True,
        )
