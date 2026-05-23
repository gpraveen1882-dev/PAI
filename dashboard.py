import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json, os

st.set_page_config(
    page_title="Mentors International — Partnership Growth Framework",
    page_icon="🌍",
    layout="wide"
)

# ── UCLA COLORS ───────────────────────────────────────────────────────────────
BLUE    = "#2774AE"
DBLUE   = "#003B5C"
GOLD    = "#FFD100"
LGOLD   = "#FFE566"
LBLUE   = "#C8E0F4"
WHITE   = "#FFFFFF"
OFFWH   = "#F8F9FA"
MGREY   = "#6C757D"
DGREY   = "#343A40"
GREEN   = "#28A745"
AMBER   = "#FD7E14"
RED     = "#DC3545"

# ── TIER ASSIGNMENTS ──────────────────────────────────────────────────────────
TIER_MAP = {
    "Colombia":"Tier 1","Peru":"Tier 1","Kenya":"Tier 1","Dominican Republic":"Tier 1",
    "Cambodia":"Tier 2","Ghana":"Tier 2","Mexico":"Tier 2","Honduras":"Tier 2",
    "Guatemala":"Tier 3","Nicaragua":"Tier 3","Malawi":"Tier 3","Cape Verde":"Tier 3",
    "Brazil":"Expansion","Ecuador":"Expansion","South Africa":"Expansion",
}
TIER_COLOR = {"Tier 1":GREEN,"Tier 2":AMBER,"Tier 3":RED,"Expansion":BLUE}
TIER_LABEL = {
    "Tier 1":"🟢 Tier 1 — Invest & Scale",
    "Tier 2":"🟡 Tier 2 — Targeted Investment",
    "Tier 3":"🔴 Tier 3 — Monitor / Stabilize",
    "Expansion":"🔵 Expansion — Future Opportunity",
}

# ── DATA ──────────────────────────────────────────────────────────────────────
@st.cache_data
def load_scores():
    rows = [
        dict(country="Colombia",          c1=9.17,c2=8.26,c3=8.82,c4=7.66,c5=5.55,c6=6.77,score=7.94),
        dict(country="Peru",              c1=7.25,c2=7.04,c3=8.36,c4=7.50,c5=6.07,c6=6.93,score=7.23),
        dict(country="Kenya",             c1=7.95,c2=8.17,c3=9.60,c4=6.37,c5=2.62,c6=5.99,score=7.22),
        dict(country="Dominican Republic",c1=7.71,c2=8.12,c3=3.45,c4=8.93,c5=8.29,c6=7.20,score=7.15),
        dict(country="Cambodia",          c1=8.68,c2=6.67,c3=7.18,c4=7.04,c5=2.83,c6=5.31,score=6.50),
        dict(country="Ghana",             c1=4.09,c2=4.61,c3=9.39,c4=7.06,c5=8.78,c6=6.54,score=6.44),
        dict(country="Mexico",            c1=5.74,c2=5.21,c3=7.52,c4=9.24,c5=6.26,c6=4.80,score=6.21),
        dict(country="Honduras",          c1=8.29,c2=5.20,c3=6.61,c4=5.33,c5=4.07,c6=5.33,score=5.92),
        dict(country="Guatemala",         c1=4.31,c2=4.71,c3=6.87,c4=5.84,c5=4.71,c6=6.04,score=5.29),
        dict(country="Nicaragua",         c1=4.93,c2=4.61,c3=5.87,c4=4.38,c5=2.81,c6=3.00,score=4.46),
        dict(country="Malawi",            c1=4.03,c2=3.21,c3=6.18,c4=1.54,c5=4.60,c6=5.41,score=4.22),
        dict(country="Cape Verde",        c1=1.00,c2=1.00,c3=1.19,c4=6.40,c5=10.0,c6=6.84,score=3.42),
    ]
    df = pd.DataFrame(rows)
    df['tier'] = df['country'].map(TIER_MAP)
    return df

@st.cache_data
def load_expansion():
    rows = [
        dict(country="Brazil",       c1=15.22,c2=13.44,c3=9.89,c4=9.99,c5=6.71,c6=6.07,score=11.04),
        dict(country="Ecuador",      c1=9.91, c2=9.04, c3=6.76,c4=7.54,c5=6.72,c6=5.29,score=7.90),
        dict(country="South Africa", c1=8.76, c2=7.03, c3=8.15,c4=8.52,c5=7.21,c6=7.80,score=7.81),
    ]
    df = pd.DataFrame(rows)
    df['tier'] = "Expansion"
    return df

@st.cache_data
def load_eco():
    df = pd.read_csv('eco_db.csv')
    df['align_n'] = pd.to_numeric(df['align_n'], errors='coerce')
    df['scale_n'] = pd.to_numeric(df['scale_n'], errors='coerce')
    df['urban_n'] = pd.to_numeric(df['urban_n'], errors='coerce')
    return df

@st.cache_data
def load_pp():
    return pd.read_csv('priority_partners.csv')

scores     = load_scores()
expansion  = load_expansion()
eco        = load_eco()
pp         = load_pp()
all_scores = pd.concat([scores, expansion], ignore_index=True)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown(f"""
<style>
[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, {DBLUE} 0%, #002040 100%);
    border-right: 3px solid {GOLD};
}}
[data-testid="stSidebar"] * {{ color: {WHITE} !important; }}
[data-testid="stSidebar"] .stRadio > label {{ display:none; }}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {{
    color: #CADCFC !important; font-size:0.86rem; padding:4px 0;
}}
#MainMenu {{ visibility:hidden; }}
footer {{ visibility:hidden; }}
header[data-testid="stHeader"] {{ display:none; }}
.block-container {{ padding-top:0.8rem !important; padding-bottom:2rem; max-width:1280px; }}
h1,h2,h3 {{ color:{DBLUE}; }}

.page-header {{
    background: linear-gradient(135deg, {DBLUE} 0%, #003D70 100%);
    padding: 1rem 1.6rem 0.9rem;
    margin-bottom: 1.2rem;
    border-bottom: 4px solid {GOLD};
}}
.kpi-card {{
    background:{WHITE}; border-radius:10px; padding:1rem 0.8rem;
    text-align:center; box-shadow:0 2px 8px rgba(0,0,0,0.08);
    border-top: 4px solid {BLUE};
}}
.kpi-val {{ font-size:2rem; font-weight:800; color:{DBLUE}; line-height:1.1; }}
.kpi-lab {{ font-size:0.75rem; color:{MGREY}; margin-top:4px; line-height:1.3; }}
.card {{
    background:{WHITE}; border-radius:10px; padding:1rem 1.2rem;
    box-shadow:0 2px 8px rgba(0,0,0,0.07); margin-bottom:0.75rem;
    border-left: 4px solid {BLUE};
}}
.card-gold {{ background:#FFFBF0; border-left:4px solid {GOLD};
    border-radius:10px; padding:1rem 1.2rem; margin-bottom:0.75rem; }}
.card-green {{ background:#F0FAF4; border-left:4px solid {GREEN};
    border-radius:10px; padding:1rem 1.2rem; margin-bottom:0.75rem; }}
.pill-t1 {{ background:{GREEN}; color:white; border-radius:20px;
    padding:3px 12px; font-size:0.75rem; font-weight:700; display:inline-block; }}
.pill-t2 {{ background:{AMBER}; color:white; border-radius:20px;
    padding:3px 12px; font-size:0.75rem; font-weight:700; display:inline-block; }}
.pill-t3 {{ background:{RED}; color:white; border-radius:20px;
    padding:3px 12px; font-size:0.75rem; font-weight:700; display:inline-block; }}
.pill-ex {{ background:{BLUE}; color:white; border-radius:20px;
    padding:3px 12px; font-size:0.75rem; font-weight:700; display:inline-block; }}
.crit-card {{
    background:{OFFWH}; border-radius:8px; padding:0.9rem 1rem;
    margin-bottom:0.5rem; border-left:4px solid {BLUE};
}}
</style>
""", unsafe_allow_html=True)

def page_header(title, sub=None):
    sub_html = f'<div style="font-size:0.8rem;color:#CADCFC;margin-top:3px;">{sub}</div>' if sub else ""
    st.markdown(f"""
<div class="page-header">
  <div style="display:flex;justify-content:space-between;align-items:center;">
    <div>
      <div style="font-size:0.65rem;color:{GOLD};letter-spacing:2px;font-weight:700;margin-bottom:4px;">
        MENTORS INTERNATIONAL · GROWTH STRATEGY
      </div>
      <div style="font-size:1.2rem;font-weight:800;color:white;">{title}</div>
      {sub_html}
    </div>
    <div style="text-align:right;">
      <div style="font-size:0.65rem;color:#CADCFC;font-weight:600;">UCLA Anderson SICC</div>
      <div style="font-size:0.62rem;color:#64748B;">Spring 2026</div>
    </div>
  </div>
</div>""", unsafe_allow_html=True)

def kpi(val, label, color=None):
    color = color or DBLUE
    return f'<div class="kpi-card" style="border-top-color:{color};"><div class="kpi-val" style="color:{color};">{val}</div><div class="kpi-lab">{label}</div></div>'

def tier_pill(tier):
    cls = {"Tier 1":"pill-t1","Tier 2":"pill-t2","Tier 3":"pill-t3","Expansion":"pill-ex"}.get(tier,"pill-t3")
    return f'<span class="{cls}">{TIER_LABEL.get(tier,tier)}</span>'

def score_bar(val, max_val=10, color=BLUE):
    pct = min(100, val/max_val*100)
    return f"""
<div style="display:flex;align-items:center;gap:8px;">
  <div style="flex:1;background:#E9ECEF;border-radius:4px;height:10px;">
    <div style="width:{pct:.0f}%;background:{color};height:10px;border-radius:4px;"></div>
  </div>
  <div style="font-size:0.82rem;font-weight:700;color:{DBLUE};width:30px;text-align:right;">{val:.1f}</div>
</div>"""

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
st.sidebar.markdown(f"""
<div style="padding:1.2rem 0.6rem 0.8rem;text-align:center;">
  <div style="font-size:1.4rem;font-weight:900;color:white;line-height:1.1;">Mentors</div>
  <div style="font-size:1.4rem;font-weight:900;color:{GOLD};line-height:1.1;margin-bottom:8px;">International</div>
  <div style="height:2px;background:linear-gradient(90deg,{GOLD},{BLUE},transparent);margin:0 0 8px;border-radius:2px;"></div>
  <div style="font-size:0.62rem;color:#CADCFC;letter-spacing:1.5px;font-weight:600;">PARTNERSHIP GROWTH FRAMEWORK</div>
  <div style="font-size:0.6rem;color:#445566;margin-top:3px;">UCLA Anderson SICC · Spring 2026</div>
</div>""", unsafe_allow_html=True)

page = st.sidebar.radio("", [
    "🏠  Overview",
    "📐  Framework",
    "🌍  Country Briefs",
    "🔭  Future Partnerships",
    "🤝  Partner Pipeline",
    "📊  Ecosystem Analysis",
    "💡  Recommendations",
    "📎  Appendix",
])

st.sidebar.markdown(f"""
<hr style="border-color:#1A3A5C;margin:0.5rem 0;">
<div style="font-size:0.7rem;color:#CADCFC;padding:0 0.3rem;line-height:1.9;">
  <div style="color:{GOLD};font-weight:700;margin-bottom:3px;">Project Summary</div>
  ✅ Framework: 8 criteria scored<br>
  ✅ Countries: 12 assessed<br>
  ✅ Ecosystem: 242 orgs researched<br>
  ✅ Priority Partners: {len(pp)} identified<br>
  ✅ Expansion: 3 countries analyzed<br>
  <div style="margin-top:6px;color:#445566;font-style:italic;">Final delivery: June 10, 2026</div>
</div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — OVERVIEW
# ══════════════════════════════════════════════════════════════════════════════
if "Overview" in page:
    page_header("Overview", "Who Mentors International is and what this project set out to achieve")

    # Mission
    st.markdown(f"""
<div style="background:linear-gradient(135deg,{DBLUE} 0%,#003D70 100%);border-radius:12px;
            padding:1.4rem 1.8rem;margin-bottom:1rem;border-left:5px solid {GOLD};">
  <div style="font-size:0.65rem;color:{GOLD};letter-spacing:2px;font-weight:700;margin-bottom:6px;">MISSION</div>
  <div style="font-size:1.3rem;font-weight:700;color:white;line-height:1.4;">
    Lifting families around the world from poverty to prosperity through entrepreneurship and one-on-one mentoring.
  </div>
</div>""", unsafe_allow_html=True)

    # Theory of Change
    st.markdown(f"""
<div class="card-gold">
  <div style="font-size:0.65rem;color:{DBLUE};letter-spacing:2px;font-weight:700;margin-bottom:6px;">THEORY OF CHANGE</div>
  <div style="font-size:1rem;color:{DGREY};line-height:1.75;">
    Because <strong>poverty traps families not from lack of effort but lack of knowledge</strong>,
    Mentors International works across <strong>12 countries</strong> to help micro-entrepreneurs
    grow stable businesses through one-on-one mentoring,
    in order to <strong>reach 100,000 families out of poverty by 2030</strong>.
  </div>
</div>""", unsafe_allow_html=True)

    # Logic Model — simplified visual
    st.markdown(f"<div style='font-weight:700;color:{DBLUE};margin:1rem 0 0.5rem;font-size:1rem;'>How the Model Works</div>", unsafe_allow_html=True)
    cols = st.columns(5)
    steps = [
        ("Partner","NGO, MFI or govt\nsources entrepreneurs",GOLD),
        ("Mentor","Trained local coach\nassigned to each socio",BLUE),
        ("Visit","Twice a month at\ntheir business",DBLUE),
        ("Skill","1 lesson/visit from\n28 certified modules","#5C6BC0"),
        ("Outcome","Income ↑  Savings ↑\nDebt ↓",GREEN),
    ]
    for col, (label, desc, color) in zip(cols, steps):
        col.markdown(f"""
<div style="background:white;border-radius:10px;padding:0.9rem 0.6rem;text-align:center;
            box-shadow:0 2px 8px rgba(0,0,0,0.08);border-top:4px solid {color};">
  <div style="font-size:1rem;font-weight:800;color:{color};">{label}</div>
  <div style="font-size:0.75rem;color:{MGREY};margin-top:5px;line-height:1.4;">{desc}</div>
</div>""", unsafe_allow_html=True)

    st.markdown(f"""
<div style="background:{OFFWH};border-radius:8px;padding:8px 14px;margin-top:8px;
            border-left:3px solid {BLUE};font-size:0.82rem;color:{DBLUE};">
  <strong>Key rule:</strong> Partners source entrepreneurs. Mentors International always delivers the program.
</div>""", unsafe_allow_html=True)

    st.markdown("---")

    # KPIs
    st.markdown(f"<div style='font-weight:700;color:{DBLUE};margin-bottom:10px;'>FY2025 Impact at a Glance</div>", unsafe_allow_html=True)
    k1,k2,k3,k4,k5 = st.columns(5)
    for col, val, label, color in [
        (k1,"43,160","Entrepreneurs served FY25",BLUE),
        (k2,"12","Countries operating",DBLUE),
        (k3,"+79%","Volume growth vs FY24",GREEN),
        (k4,"$150","Cost per family / year",AMBER),
        (k5,"$5","Economic return per $1",GOLD),
    ]:
        col.markdown(f'<div>{kpi(val,label,color)}</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Project goal
    st.markdown(f"""
<div class="card-green">
  <div style="font-size:0.65rem;color:{GREEN};letter-spacing:2px;font-weight:700;margin-bottom:6px;">PROJECT OBJECTIVE</div>
  <div style="font-size:1.05rem;color:{DGREY};line-height:1.65;">
    Develop a <strong>structured, data-driven framework</strong> to identify, prioritize, and scale
    high-impact partnerships that enable Mentors International to reach their
    <strong>2030 target of 100,000 socios per year</strong>.
  </div>
</div>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""<div class="card">
<div style="font-weight:700;color:{DBLUE};margin-bottom:8px;">The Core Problem</div>
<div style="font-size:0.85rem;color:{DGREY};line-height:1.65;">
~50% of current volume comes from a <strong>single partner</strong> (Bancolombia, Colombia).
That volume is already declining — 20,875 socios (FY25) → ~16,000 (FY26).
Outside Colombia, 97% of funding comes from individual donors.
No systematic framework for partnership growth existed before this project.
</div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""<div class="card">
<div style="font-weight:700;color:{DBLUE};margin-bottom:8px;">What We Built</div>
<div style="font-size:0.85rem;color:{DGREY};line-height:1.65;">
An <strong>8-criterion scoring framework</strong> grounded in real data sources (World Bank, GSMA, Freedom House).
A <strong>242-organization ecosystem database</strong> across all 12 countries.
<strong>Priority partner lists</strong> for Tier 1 countries.
An <strong>expansion analysis</strong> for 3 future markets.
</div></div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — FRAMEWORK
# ══════════════════════════════════════════════════════════════════════════════
elif "Framework" in page:
    page_header("The Framework", "8 criteria used to score and prioritize countries for partnership investment")

    st.markdown(f"""
<div class="card-gold">
  <strong>How to read this framework:</strong>
  <span style="font-size:0.85rem;color:{DGREY};">
  Each criterion is scored on a 0–10 scale using real data sources.
  Criteria 1–6 are fully scored. Criteria 7 (CD Strength) and 8 (Program Standardization)
  require qualitative judgment and are noted separately.
  The overall country score is the weighted average of Criteria 1–6.
  </span>
</div>""", unsafe_allow_html=True)

    criteria = [
        dict(num="C1", name="Mission Alignment", type="Market Opportunity", weight="15%",
             weight_ex="19%",
             goal="Assess the quality and strength of potential partners in each country ecosystem",
             oneliner="How well do potential partners in this country align with Mentors International's model?",
             metrics=["Number of high-fit partners (score 4–5) in the ecosystem database",
                      "Number of ideal partners (score 5) in the ecosystem database",
                      "Volume-adjusted alignment score — weighted by organization size",
                      "% of total ecosystem that is high-fit (4 or 5)"],
             source="Ecosystem Database — Alignment with MI (1–5) column"),
        dict(num="C2", name="Volume Potential", type="Market Opportunity", weight="23%",
             weight_ex="28%",
             goal="Identify whether a country can realistically get MI to scale",
             oneliner="Can this country realistically deliver 500+ socios per year through partnerships?",
             metrics=["Number of organizations with scale rating 4–5 (500+ reach)",
                      "Number of organizations with scale rating 5 (1,000+ reach)",
                      "Volume-weighted alignment score",
                      "% of ecosystem that is large-scale"],
             source="Ecosystem Database — Scale Potential (1–5) column"),
        dict(num="C3", name="Socio Profile Fit & Density", type="Market Opportunity", weight="15%",
             weight_ex="19%",
             goal="Assess the size and serviceability of the urban micro-entrepreneur target population",
             oneliner="Is there a sufficient density of urban micro-entrepreneurs who match Mentors' target profile?",
             metrics=["Urban population size (World Bank)",
                      "Multidimensional Poverty Index — urban population in need",
                      "Informal self-employment rate",
                      "% of workforce in urban micro-enterprise"],
             source="World Bank, MPI Index, ILO labor statistics"),
        dict(num="C4", name="Digital Readiness", type="Market Opportunity", weight="5%",
             weight_ex="9%",
             goal="Determine whether MI can scale virtually in each country",
             oneliner="Is the country's digital infrastructure strong enough to support virtual mentoring at scale?",
             metrics=["Mobile connectivity rate (GSMA Mobile Index)",
                      "Internet usage rate (World Bank)",
                      "Mobile money adoption (Findex)",
                      "4G/LTE coverage %"],
             source="GSMA Mobile Connectivity Index, World Bank Digital Development"),
        dict(num="C5", name="Political and Operating Risk", type="Market Opportunity", weight="10%",
             weight_ex="14%",
             goal="Assess the level of political and operational risk for NGO activities",
             oneliner="How stable and enabling is the political environment for a US-based NGO to operate?",
             metrics=["Fragile States Index score (Fund for Peace)",
                      "Freedom House political freedom score",
                      "NGO operational freedom — legal and regulatory environment",
                      "Historical US NGO operating risk in country"],
             source="Fund for Peace Fragile States Index, Freedom House"),
        dict(num="C6", name="Legal & Structural Constraints", type="Market Opportunity", weight="7%",
             weight_ex="11%",
             goal="Determine whether MI can operate and generate revenue without complex legal structures",
             oneliner="Can Mentors International collect revenue from partners without major legal barriers?",
             metrics=["Nonprofit registration requirements",
                      "Ability to receive foreign funding",
                      "Revenue-generating restrictions on NGOs",
                      "Ease of establishing local legal entity"],
             source="Country legal research, NGO Law Monitor"),
        dict(num="C7", name="CD Strength & Leadership", type="Operational Readiness",
             weight="15%", weight_ex="N/A (excluded from score)",
             goal="Assess whether in-country leadership can execute, build partnerships, and drive scale independently",
             oneliner="Does the country director have the capability and capacity to build and manage partnerships?",
             metrics=["Years of experience as CD",
                      "Track record of partnership development",
                      "Quality of existing partner relationships",
                      "Full-time vs part-time commitment"],
             source="CD interviews, HQ assessment — qualitative rubric"),
        dict(num="C8", name="Program Standardization", type="Operational Readiness",
             weight="10%", weight_ex="N/A (excluded from score)",
             goal="Assess whether MI's program can be delivered consistently, measured reliably, and scaled across partners",
             oneliner="Is the program sufficiently standardized to be delivered consistently across multiple partners?",
             metrics=["Socio Connect adoption and data quality",
                      "Mentor certification rate",
                      "Curriculum adherence rate",
                      "Impact data completeness"],
             source="Socio Connect platform data, program records — qualitative rubric"),
    ]

    # Weights bar chart
    c1, c2 = st.columns([2,3])
    with c1:
        wt_df = pd.DataFrame([
            {"Criterion": f"{c['num']}: {c['name']}", "Weight": float(c['weight'].replace('%',''))}
            for c in criteria if c['weight_ex'] != "N/A (excluded from score)"
        ])
        fig_w = px.bar(wt_df, x="Weight", y="Criterion", orientation="h",
            color="Weight", color_continuous_scale=[[0,"#C8E0F4"],[1,DBLUE]],
            labels={"Weight":"Weight (%)","Criterion":""},
            title="Criterion Weights (C1–C6)", height=320)
        fig_w.update_layout(plot_bgcolor=WHITE, coloraxis_showscale=False,
            margin=dict(l=0,r=0,t=40,b=0))
        fig_w.update_xaxes(gridcolor="#F0F0F0", ticksuffix="%")
        fig_w.update_yaxes(showgrid=False)
        st.plotly_chart(fig_w, use_container_width=True)

    with c2:
        st.markdown(f"<div style='font-weight:700;color:{DBLUE};margin-bottom:8px;'>All 8 Criteria — Goals & Metrics</div>",
                    unsafe_allow_html=True)
        for c in criteria:
            excluded = "N/A" in c['weight_ex']
            badge_color = "#5C6BC0" if c['type'] == "Operational Readiness" else BLUE
            with st.expander(f"**{c['num']}: {c['name']}** — {c['oneliner'][:60]}..."):
                col_a, col_b = st.columns([1,1])
                with col_a:
                    st.markdown(f"**Type:** {c['type']}")
                    st.markdown(f"**Weight (all 8):** {c['weight']}")
                    st.markdown(f"**Weight (C1–6 only):** {c['weight_ex']}")
                    st.markdown(f"**Goal:** {c['goal']}")
                    st.markdown(f"**Data source:** {c['source']}")
                with col_b:
                    st.markdown("**Metrics used:**")
                    for m in c['metrics']:
                        st.markdown(f"- {m}")
                if excluded:
                    st.info("⚠️ C7 and C8 require qualitative assessment and are excluded from the quantitative country score. They are assessed separately through CD interviews and program data review.")

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 3 — COUNTRY BRIEFS
# ══════════════════════════════════════════════════════════════════════════════
elif "Country Briefs" in page:
    page_header("Country Briefs", "Framework scores and tier assignment for all 12 current operating countries")

    CRIT_NAMES = {
        "c1":"C1: Mission Alignment","c2":"C2: Volume Potential",
        "c3":"C3: Socio Profile Fit","c4":"C4: Digital Readiness",
        "c5":"C5: Political Risk","c6":"C6: Legal Structure",
    }

    # Summary table
    st.markdown(f"<div style='font-weight:700;color:{DBLUE};margin-bottom:8px;'>All Countries — Score Summary</div>",
                unsafe_allow_html=True)
    disp = scores[['country','c1','c2','c3','c4','c5','c6','score','tier']].copy()
    disp.columns = ['Country','C1','C2','C3','C4','C5','C6','Score (C1–6)','Tier']
    disp = disp.sort_values('Score (C1–6)', ascending=False)
    st.dataframe(disp.style.format({'C1':'{:.2f}','C2':'{:.2f}','C3':'{:.2f}',
                         'C4':'{:.2f}','C5':'{:.2f}','C6':'{:.2f}','Score (C1–6)':'{:.2f}'}),
                 use_container_width=True, hide_index=True)

    st.markdown("---")
    sel = st.selectbox("Select a country for detailed view",
                       scores.sort_values('score', ascending=False)['country'].tolist())
    r = scores[scores['country'] == sel].iloc[0]
    tier = TIER_MAP.get(sel, "Tier 3")

    # Header
    st.markdown(f"""
<div style="background:linear-gradient(135deg,{DBLUE} 0%,#003D70 100%);border-radius:12px;
            padding:1rem 1.4rem;margin-bottom:1rem;border-bottom:4px solid {GOLD};
            display:flex;justify-content:space-between;align-items:center;">
  <div>
    <div style="font-size:1.4rem;font-weight:800;color:white;">{sel}</div>
    <div style="font-size:0.8rem;color:#CADCFC;margin-top:3px;">{TIER_LABEL.get(tier,tier)}</div>
  </div>
  <div style="font-size:2.5rem;font-weight:900;color:{GOLD};">{r['score']:.2f}<span style="font-size:1rem;color:#CADCFC;">/10</span></div>
</div>""", unsafe_allow_html=True)

    col1, col2 = st.columns([2,3])
    with col1:
        st.markdown(f"<div style='font-weight:700;color:{DBLUE};margin-bottom:8px;'>Criterion Scores</div>",
                    unsafe_allow_html=True)
        for key, name in CRIT_NAMES.items():
            val = r[key]
            color = GREEN if val >= 7 else AMBER if val >= 5 else RED
            st.markdown(f"""
<div style="margin-bottom:6px;">
  <div style="font-size:0.8rem;color:{DGREY};margin-bottom:3px;">{name}</div>
  {score_bar(val, 10, color)}
</div>""", unsafe_allow_html=True)

    with col2:
        # Radar chart
        fig_r = go.Figure(go.Scatterpolar(
            r=[r['c1'],r['c2'],r['c3'],r['c4'],r['c5'],r['c6'],r['c1']],
            theta=["Mission\nAlignment","Volume\nPotential","Socio\nProfile",
                   "Digital\nReadiness","Political\nRisk","Legal\nStructure","Mission\nAlignment"],
            fill='toself', fillcolor=f"rgba(39,116,174,0.15)",
            line=dict(color=BLUE, width=2),
            name=sel
        ))
        fig_r.update_layout(
            polar=dict(radialaxis=dict(range=[0,10], showticklabels=True,
                                       tickfont=dict(size=9))),
            showlegend=False, height=340,
            margin=dict(l=30,r=30,t=30,b=30)
        )
        st.plotly_chart(fig_r, use_container_width=True)

    # Country-specific partners
    c_pp = pp[pp['Country'] == sel] if 'Country' in pp.columns else pd.DataFrame()
    if len(c_pp):
        st.markdown(f"<div style='font-weight:700;color:{DBLUE};margin:0.5rem 0 0.5rem;'>Priority Partners for {sel}</div>",
                    unsafe_allow_html=True)
        st.dataframe(c_pp[['Organization Name','Why Priority','Partnership Type',
                           'Estimated Reach','Cities of Overlap with MI']].rename(
            columns={'Organization Name':'Organization','Why Priority':'Why a Priority',
                     'Partnership Type':'Type','Estimated Reach':'Scale',
                     'Cities of Overlap with MI':'Cities'}),
            use_container_width=True, hide_index=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 4 — FUTURE PARTNERSHIPS
# ══════════════════════════════════════════════════════════════════════════════
elif "Future" in page:
    page_header("Future Partnerships", "How to use this framework to evaluate potential expansion markets")

    st.markdown(f"""
<div class="card-gold">
  <strong>How to use this page:</strong>
  <span style="font-size:0.85rem;color:{DGREY};">
  This page demonstrates how Mentors International can apply the same 8-criterion framework
  to evaluate any new country or market — beyond the current 12. The three countries shown
  (Brazil, Ecuador, South Africa) have been scored using the same methodology and data sources.
  This is how the framework continues to create value after this project ends.
  </span>
</div>""", unsafe_allow_html=True)

    # Comparison: current Tier 1 vs expansion
    st.markdown(f"<div style='font-weight:700;color:{DBLUE};margin:1rem 0 0.5rem;'>How Expansion Countries Compare to Current Tier 1</div>",
                unsafe_allow_html=True)

    tier1 = scores[scores['tier']=='Tier 1'].copy()
    tier1['group'] = 'Current Tier 1'
    exp = expansion.copy()
    exp['group'] = 'Expansion Candidate'
    combined = pd.concat([tier1, exp], ignore_index=True)

    fig_comp = px.bar(combined.sort_values('score', ascending=False),
        x='country', y='score', color='group',
        color_discrete_map={'Current Tier 1':BLUE, 'Expansion Candidate':GOLD},
        labels={'score':'Framework Score (C1–6, out of 10)','country':'','group':''},
        height=360)
    fig_comp.update_layout(plot_bgcolor=WHITE, margin=dict(l=0,r=0,t=10,b=0),
        legend=dict(orientation="h",y=1.1))
    fig_comp.update_yaxes(gridcolor="#F0F0F0", range=[0,12])
    fig_comp.update_xaxes(showgrid=False)
    fig_comp.add_hline(y=7, line_dash="dot", line_color="#999",
                       annotation_text="Tier 1 threshold (7.0)")
    st.plotly_chart(fig_comp, use_container_width=True)

    # Expansion country detail
    sel_exp = st.selectbox("Explore an expansion country",
                           ["Brazil","Ecuador","South Africa"])
    r = expansion[expansion['country']==sel_exp].iloc[0]

    st.markdown(f"""
<div style="background:linear-gradient(135deg,{DBLUE} 0%,#003D70 100%);border-radius:12px;
            padding:1rem 1.4rem;margin:0.5rem 0 1rem;border-bottom:4px solid {GOLD};
            display:flex;justify-content:space-between;align-items:center;">
  <div>
    <div style="font-size:1.3rem;font-weight:800;color:white;">{sel_exp}</div>
    <div style="font-size:0.78rem;color:#CADCFC;margin-top:3px;">Expansion candidate — framework applied</div>
  </div>
  <div style="font-size:2.2rem;font-weight:900;color:{GOLD};">{r['score']:.2f}<span style="font-size:1rem;color:#CADCFC;">/10</span></div>
</div>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    CRIT_NAMES = {
        "c1":"C1: Mission Alignment","c2":"C2: Volume Potential",
        "c3":"C3: Socio Profile Fit","c4":"C4: Digital Readiness",
        "c5":"C5: Political Risk","c6":"C6: Legal Structure",
    }
    with col1:
        for key, name in CRIT_NAMES.items():
            val = r[key]
            color = GREEN if val >= 7 else AMBER if val >= 5 else RED
            st.markdown(f"""
<div style="margin-bottom:6px;">
  <div style="font-size:0.8rem;color:{DGREY};margin-bottom:3px;">{name}</div>
  {score_bar(val, max(10, val+1), color)}
</div>""", unsafe_allow_html=True)
    with col2:
        insight = {
            "Brazil": "Brazil scores the highest of any country evaluated — including all 12 current markets. Strong ecosystem, massive urban micro-entrepreneur population, and good digital infrastructure. The main constraint is legal complexity and the scale of entry investment required.",
            "Ecuador": "Ecuador scores at Tier 1 level (7.90) — comparable to Peru and Kenya. Strong mission alignment and volume potential. Shares cultural and linguistic similarities with Colombia and Peru, making program adaptation straightforward.",
            "South Africa": "South Africa scores 7.81 — Tier 1 equivalent. Strong ecosystem, high digital readiness, and good legal structure. The primary consideration is the urban poverty geography — operations would need to focus on township markets in Johannesburg and Cape Town.",
        }
        st.markdown(f"""<div class="card">
<div style="font-weight:700;color:{DBLUE};margin-bottom:8px;">Strategic Assessment</div>
<div style="font-size:0.88rem;color:{DGREY};line-height:1.65;">{insight[sel_exp]}</div>
</div>""", unsafe_allow_html=True)

        # Ecosystem orgs for expansion country if available
        eco_exp = eco[eco['Country']==sel_exp] if sel_exp in eco['Country'].values else pd.DataFrame()
        if len(eco_exp):
            st.markdown(f"**{len(eco_exp)} organizations researched in {sel_exp}**")
            st.dataframe(eco_exp[['Organization Name','Category','align_n','scale_n','Status']].rename(
                columns={'Organization Name':'Organization','align_n':'Alignment /5','scale_n':'Scale /5'}
            ).sort_values('Alignment /5',ascending=False),
            use_container_width=True, hide_index=True)
        else:
            st.info(f"Ecosystem research for {sel_exp} is in progress.")

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 5 — PARTNER PIPELINE
# ══════════════════════════════════════════════════════════════════════════════
elif "Partner Pipeline" in page:
    page_header("Partner Pipeline", "242 organizations researched across all 12 countries — source: Caleigh Hernandez, Anderson Library databases")

    col1, col2, col3 = st.columns(3)
    all_countries = ["All"] + sorted(eco['Country'].dropna().unique())
    country_f = col1.selectbox("Country", all_countries)
    align_f   = col2.selectbox("Min Alignment Score", [1,2,3,4,5], index=2)
    status_f  = col3.selectbox("Status", ["All"] + sorted(eco['Status'].dropna().unique()))

    filtered = eco.copy()
    if country_f != "All": filtered = filtered[filtered['Country']==country_f]
    filtered = filtered[filtered['align_n'] >= align_f]
    if status_f != "All": filtered = filtered[filtered['Status']==status_f]

    m1,m2,m3,m4 = st.columns(4)
    m1.metric("Organizations shown", len(filtered))
    m2.metric("Score 5 — Excellent Fit", len(filtered[filtered['align_n']==5]))
    m3.metric("Score 4 — Very Good Fit", len(filtered[filtered['align_n']==4]))
    m4.metric("Countries represented", filtered['Country'].nunique())

    st.dataframe(
        filtered[['Country','Organization Name','Status','Category',
                  'Alignment with MI (1-5)','Scale Potential (1-5)',
                  'Urban Relevance (1-5)','Website','Notes']].rename(
            columns={'Organization Name':'Organization',
                     'Alignment with MI (1-5)':'Alignment',
                     'Scale Potential (1-5)':'Scale',
                     'Urban Relevance (1-5)':'Urban Relevance'}
        ).sort_values(['Country','Alignment'], ascending=[True,False]),
        use_container_width=True, hide_index=True, height=480
    )

    st.caption("Source: Anderson Library databases, NGO registries, MFI directories, Factiva. Research by Caleigh Hernandez.")

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 6 — ECOSYSTEM ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
elif "Ecosystem" in page:
    page_header("Ecosystem Analysis", "Partner landscape across all 12 countries — alignment, scale, and market opportunity")

    tab1, tab2, tab3 = st.tabs(["📊 Alignment Overview","🗺️ Market vs Readiness","🏆 Country Rankings"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            a5 = eco[eco['align_n']==5].groupby('Country').size().reset_index(name='n')
            fig1 = px.bar(a5.sort_values('n'), x='n', y='Country', orientation='h',
                color_discrete_sequence=[BLUE],
                labels={'n':'# of 5-Alignment Organizations','Country':''},
                title='Top Mission-Aligned Partners (Score 5) per Country', height=380)
            fig1.update_layout(plot_bgcolor=WHITE, margin=dict(l=0,r=0,t=40,b=0))
            fig1.update_xaxes(gridcolor="#F0F0F0", dtick=1)
            fig1.update_yaxes(showgrid=False)
            st.plotly_chart(fig1, use_container_width=True)
        with col2:
            avg_a = eco.groupby('Country')['align_n'].mean().reset_index()
            avg_a.columns = ['Country','avg']
            fig2 = px.bar(avg_a.sort_values('avg'), x='avg', y='Country', orientation='h',
                color='avg', color_continuous_scale=[[0,"#C8E0F4"],[0.5,BLUE],[1,DBLUE]],
                labels={'avg':'Average Alignment Score','Country':''},
                title='Average Alignment Score by Country', height=380)
            fig2.update_layout(plot_bgcolor=WHITE, coloraxis_showscale=False,
                margin=dict(l=0,r=0,t=40,b=0))
            fig2.update_xaxes(gridcolor="#F0F0F0", range=[0,5.5])
            fig2.update_yaxes(showgrid=False)
            st.plotly_chart(fig2, use_container_width=True)

        # Scale
        avg_s = eco.groupby('Country')['scale_n'].mean().reset_index()
        avg_s.columns = ['Country','avg_scale']
        fig3 = px.bar(avg_s.sort_values('avg_scale'), x='avg_scale', y='Country', orientation='h',
            color='avg_scale',
            color_continuous_scale=[[0,"#FFF3CD"],[0.5,AMBER],[1,"#7D3F00"]],
            labels={'avg_scale':'Average Scale Score','Country':''},
            title='Average Scale Potential by Country', height=380)
        fig3.update_layout(plot_bgcolor=WHITE, coloraxis_showscale=False,
            margin=dict(l=0,r=0,t=40,b=0))
        fig3.update_xaxes(gridcolor="#F0F0F0", range=[0,5.5])
        fig3.update_yaxes(showgrid=False)
        st.plotly_chart(fig3, use_container_width=True)

    with tab2:
        fig4 = px.scatter(scores, x='score', y='c1',
            color='tier', size='score', size_max=50,
            hover_name='country',
            hover_data={'c1':True,'c2':True,'c3':True,'score':True,'tier':False},
            color_discrete_map={"Tier 1":GREEN,"Tier 2":AMBER,"Tier 3":RED},
            labels={'score':'Overall Framework Score (C1–6)','c1':'Mission Alignment (C1)','tier':'Tier'},
            title='Market Opportunity (Score) vs Mission Alignment', height=480)
        fig4.update_layout(plot_bgcolor=WHITE)
        fig4.update_xaxes(gridcolor="#F0F0F0")
        fig4.update_yaxes(gridcolor="#F0F0F0")
        st.plotly_chart(fig4, use_container_width=True)

        # Country portfolio
        st.markdown(f"<div style='font-weight:700;color:{DBLUE};margin-bottom:8px;'>Country Portfolio — All Criteria</div>",
                    unsafe_allow_html=True)
        fig5 = go.Figure()
        tier_order = ["Tier 1","Tier 2","Tier 3"]
        colors_by_tier = {"Tier 1":GREEN,"Tier 2":AMBER,"Tier 3":RED}
        crit_labels = ["C1: Mission","C2: Volume","C3: Socio Fit","C4: Digital","C5: Political","C6: Legal","C1: Mission"]
        for tier in tier_order:
            t_df = scores[scores['tier']==tier]
            for _, row in t_df.iterrows():
                vals = [row.c1,row.c2,row.c3,row.c4,row.c5,row.c6,row.c1]
                fig5.add_trace(go.Scatterpolar(
                    r=vals, theta=crit_labels, name=row.country,
                    line=dict(color=colors_by_tier[tier], width=1.5),
                    opacity=0.7
                ))
        fig5.update_layout(
            polar=dict(radialaxis=dict(range=[0,10])),
            showlegend=True, height=520,
            title="Country Portfolio — Criterion Profile",
            legend=dict(orientation="v", x=1.05)
        )
        st.plotly_chart(fig5, use_container_width=True)

    with tab3:
        st.markdown(f"""<div class="card-gold">
<strong>Ranking methodology:</strong> Countries are ranked by their weighted framework score
across Criteria 1–6. Criteria 7 (CD Strength) and 8 (Program Standardization) are excluded
from the quantitative score as they require qualitative judgment. The tier assignment reflects
both the quantitative score and qualitative assessment.
</div>""", unsafe_allow_html=True)

        rank_df = scores[['country','c1','c2','c3','c4','c5','c6','score','tier']].copy()
        rank_df = rank_df.sort_values('score', ascending=False).reset_index(drop=True)
        rank_df.insert(0,'Rank', range(1,len(rank_df)+1))
        rank_df.columns = ['Rank','Country','C1','C2','C3','C4','C5','C6','Score (C1–6)','Tier']
        rank_df['C7: CD Strength'] = '⏳ Assessed qualitatively'
        rank_df['C8: Program Std'] = '⏳ Assessed qualitatively'

        st.dataframe(rank_df.style.format({'C1':'{:.2f}','C2':'{:.2f}','C3':'{:.2f}',
                    'C4':'{:.2f}','C5':'{:.2f}','C6':'{:.2f}','Score (C1–6)':'{:.2f}'}),
            use_container_width=True, hide_index=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 7 — RECOMMENDATIONS
# ══════════════════════════════════════════════════════════════════════════════
elif "Recommendations" in page:
    page_header("Final Recommendations", "Tier structure, priority partners, and strategic next steps for Mentors International")

    st.markdown(f"""
<div style="background:linear-gradient(135deg,{DBLUE} 0%,#003D70 100%);border-radius:12px;
            padding:1.3rem 1.6rem;margin-bottom:1rem;border-bottom:4px solid {GOLD};">
  <div style="font-size:0.65rem;color:{GOLD};letter-spacing:2px;font-weight:700;margin-bottom:4px;">THE GOAL</div>
  <div style="font-size:1rem;color:white;line-height:1.7;">
    Because poverty traps families not from lack of effort but lack of knowledge,
    Mentors International works across 12 countries to help micro-entrepreneurs grow stable businesses
    through one-on-one mentoring, in order to reach
    <span style="color:{GOLD};font-weight:800;">100,000 families out of poverty by 2030</span>.
  </div>
</div>""", unsafe_allow_html=True)

    # Tier structure
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div style="background:#F0FAF4;border-radius:10px;padding:10px 14px;border-top:4px solid {GREEN};margin-bottom:8px;font-weight:700;color:{GREEN};">🟢 Tier 1 — Invest & Scale</div>', unsafe_allow_html=True)
        t1_countries = scores[scores['tier']=='Tier 1'].sort_values('score',ascending=False)
        for _, r in t1_countries.iterrows():
            c_pp = pp[pp['Country']==r['country']] if 'Country' in pp.columns else pd.DataFrame()
            with st.expander(f"**{r['country']}** — Score: {r['score']:.2f}"):
                st.markdown(f"**Framework score (C1–6):** {r['score']:.2f}/10")
                if len(c_pp):
                    st.markdown(f"**Priority partners identified:** {len(c_pp)}")
                    for _, p_row in c_pp.iterrows():
                        st.markdown(f"- **{p_row['Organization Name']}** — {p_row['Why Priority']}")
    with col2:
        st.markdown(f'<div style="background:#FFF9EC;border-radius:10px;padding:10px 14px;border-top:4px solid {AMBER};margin-bottom:8px;font-weight:700;color:{AMBER};">🟡 Tier 2 — Targeted Investment</div>', unsafe_allow_html=True)
        t2_countries = scores[scores['tier']=='Tier 2'].sort_values('score',ascending=False)
        for _, r in t2_countries.iterrows():
            c_pp = pp[pp['Country']==r['country']] if 'Country' in pp.columns else pd.DataFrame()
            with st.expander(f"**{r['country']}** — Score: {r['score']:.2f}"):
                st.markdown(f"**Framework score (C1–6):** {r['score']:.2f}/10")
                if len(c_pp):
                    st.markdown(f"**Priority partners identified:** {len(c_pp)}")
                    for _, p_row in c_pp.iterrows():
                        st.markdown(f"- **{p_row['Organization Name']}** — {p_row['Why Priority']}")
    with col3:
        st.markdown(f'<div style="background:#FFF5F5;border-radius:10px;padding:10px 14px;border-top:4px solid {RED};margin-bottom:8px;font-weight:700;color:{RED};">🔴 Tier 3 — Monitor / Stabilize</div>', unsafe_allow_html=True)
        t3_countries = scores[scores['tier']=='Tier 3'].sort_values('score',ascending=False)
        for _, r in t3_countries.iterrows():
            with st.expander(f"**{r['country']}** — Score: {r['score']:.2f}"):
                st.markdown(f"**Framework score (C1–6):** {r['score']:.2f}/10")
                st.markdown("Priority partner research pending or not applicable at this stage.")

    st.markdown("---")

    # Priority partners full table
    st.markdown(f"<div style='font-weight:700;color:{DBLUE};margin-bottom:8px;'>Priority Partners — Full List</div>",
                unsafe_allow_html=True)
    st.caption("This list will be updated by Caleigh as additional partner research is completed.")
    if len(pp):
        st.dataframe(pp.rename(columns={
            'Organization Name':'Organization','Why Priority':'Why a Priority',
            'Partnership Type':'Type','Estimated Reach':'Estimated Reach',
            'Cities of Overlap with MI':'Cities'
        }), use_container_width=True, hide_index=True)
    else:
        st.info("Priority partner list will be populated as research progresses.")

    st.markdown("---")

    # Top 5 recommendations
    st.markdown(f"<div style='font-weight:700;color:{DBLUE};margin-bottom:10px;'>Top Strategic Recommendations</div>",
                unsafe_allow_html=True)
    recs = [
        (AMBER,"🚨","Diversify Colombia — Immediately",
         "~50% of global volume comes from Bancolombia alone — and it is already declining. Research which Colombian banks have the same financial education compliance obligations. Pursue Bancamía, Banco Mundo Mujer, and Interactuar this quarter."),
        (RED,"👤","Resolve Kenya CD Commitment — One Decision Unlocks Everything",
         "Kenya has the best NGO ecosystem in Africa and an 82% socio graduation rate. But the CD holds a part-time job elsewhere. Full-time commitment or replacement — this one decision unlocks 3,000–5,000 additional socios per year."),
        (BLUE,"🌐","Pursue Millicom / TIGO at Corporate Level",
         "The TIGO Nicaragua flywheel is the best partnership model in the network. Millicom (TIGO's parent) operates in 9 LATAM+Africa countries. One corporate conversation could replicate that model across multiple markets simultaneously."),
        (DBLUE,"⛪","Approach LDS Humanitarian Program",
         "Mentors uses only the LDS Welfare arm (10% of budget, members only). The Humanitarian Program = 90% of the LDS budget and serves anyone regardless of faith. It has never been approached."),
        (GREEN,"📄","Build the Partner Evidence Brief",
         "Every CD interview surfaced the same gap. CDs walk into partner meetings without a crisp evidence document. A 2-page brief — Bancolombia -40% loan default, +53% income, $5 return per $1 — changes every country director conversation immediately."),
    ]
    for color, icon, title, body in recs:
        st.markdown(f"""<div class="card" style="border-left-color:{color};">
<div style="font-weight:700;color:{DBLUE};font-size:0.95rem;">{icon} {title}</div>
<div style="font-size:0.83rem;color:{MGREY};margin-top:5px;line-height:1.6;">{body}</div>
</div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 8 — APPENDIX
# ══════════════════════════════════════════════════════════════════════════════
elif "Appendix" in page:
    page_header("Appendix", "Additional research, data sources, and framework limitations")

    tab1, tab2, tab3 = st.tabs(["📚 Data Sources & Methodology","⚠️ Limitations","🔬 Sector Benchmarks"])

    with tab1:
        sources = [
            ("World Bank", "Urban population data, poverty headcount ratios, self-employment rates, internet usage", "world bank open data"),
            ("GSMA Mobile Connectivity Index", "Mobile connectivity, 4G coverage, and digital readiness scores by country", "gsma.com/mobileconnectivityindex"),
            ("Fund for Peace — Fragile States Index", "Political stability, government effectiveness, and security scores", "fragilestatesindex.org"),
            ("Freedom House", "Political rights and civil liberties — NGO operating environment", "freedomhouse.org"),
            ("Anderson Library Databases", "Organization research, MFI directories, NGO databases, Factiva", "UCLA Library"),
            ("Country NGO Registries", "Local NGO registration databases used by Eric (Kenya) and country directors", "Country-specific"),
            ("Ecosystem Database (Caleigh)", "242 organizations scored across 12 countries on alignment, scale, and urban relevance", "Internal research"),
            ("CD Interviews", "Ghana (Week 4), Kenya (Week 5), Mexico (Week 5), HQ: Ana Peña + Peter Sturgeon", "Primary research"),
        ]
        for name, desc, src in sources:
            st.markdown(f"""<div class="card">
<div style="font-weight:700;color:{DBLUE};">{name}</div>
<div style="font-size:0.82rem;color:{DGREY};margin-top:3px;">{desc}</div>
<div style="font-size:0.75rem;color:{MGREY};margin-top:2px;font-style:italic;">{src}</div>
</div>""", unsafe_allow_html=True)

    with tab2:
        limitations = [
            ("C7 and C8 excluded from quantitative score","CD Strength and Program Standardization require qualitative judgment based on interviews and program data. They are assessed separately and are not included in the numerical score to maintain objectivity."),
            ("Ecosystem research depth varies by country","Countries with more available data (Colombia, Kenya, Dominican Republic) have more organizations in the ecosystem database. Smaller or less-documented markets may have fewer entries."),
            ("Geography not captured in scoring","The framework does not account for the difficulty of traveling between cities within a country. A single country score does not reflect operational complexity across multiple cities."),
            ("Self-reported outcome data","Mentors International's impact outcomes (+53% income, +65% savings) are self-reported by participants and have not been independently verified. This is flagged throughout the framework."),
            ("Expansion country data gaps","Brazil, Ecuador, and South Africa have been scored on C1–C5 only. C6 (Legal Structure) data for these countries requires additional research."),
            ("Framework reflects a point in time","Country scores reflect data available as of May 2026. Political environments, partner landscapes, and economic conditions change — the framework should be reviewed annually."),
        ]
        for title, body in limitations:
            with st.expander(f"⚠️ {title}"):
                st.markdown(body)

    with tab3:
        bm = pd.DataFrame({
            "Organization":["Mentors International","BRAC Graduation Approach","Opportunity International","TechnoServe"],
            "Income Increase":["53% (Year 1)*","38% (over 4 years)","~25% (Year 1)","~20% (Year 1)"],
            "Cost / Year":["$150","$300–500","$400–600","$200–400"],
            "Countries":["12","14","30+","25+"],
            "Data Type":["Self-reported*","Independently verified","Partner-delivered","Technical assistance"],
        })
        st.dataframe(bm, use_container_width=True, hide_index=True)
        st.caption("* Mentors International outcomes are self-reported for FY2025 and have not been independently verified. Independent verification would significantly strengthen the partner evidence brief and unlock institutional funding conversations.")

    st.markdown("---")
    st.caption(f"UCLA Anderson SICC · Spring 2026 · Mentors International Growth Strategy Project · Final delivery June 10, 2026 · Team: Praveen Gangaraju · Caleigh Hernandez · Morgan Ikemiya · Sydney Kyle · Advisor: Prof. Gayle Northrop")
