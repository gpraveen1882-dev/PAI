import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Mentors International — Partnership Growth Framework",
    page_icon="🌍", layout="wide"
)

# ── UCLA COLORS ───────────────────────────────────────────────────────────────
BLUE  = "#2774AE"
DBLUE = "#003B5C"
GOLD  = "#FFD100"
LBLUE = "#C8E0F4"
WHITE = "#FFFFFF"
OFFWH = "#F8F9FA"
MGREY = "#6C757D"
DGREY = "#343A40"
GREEN = "#28A745"
AMBER = "#FD7E14"
RED   = "#DC3545"

TIER_MAP = {
    "Colombia":"Tier 1","Peru":"Tier 1","Kenya":"Tier 1","Dominican Republic":"Tier 1",
    "Cambodia":"Tier 2","Ghana":"Tier 2","Mexico":"Tier 2","Honduras":"Tier 2",
    "Guatemala":"Tier 3","Nicaragua":"Tier 3","Malawi":"Tier 3","Cape Verde":"Tier 3",
    "Brazil":"Expansion","Ecuador":"Expansion","South Africa":"Expansion",
}
TIER_COLOR  = {"Tier 1":GREEN,"Tier 2":AMBER,"Tier 3":RED,"Expansion":BLUE}
TIER_LABEL  = {
    "Tier 1":"🟢 Tier 1 — Invest & Scale",
    "Tier 2":"🟡 Tier 2 — Targeted Investment",
    "Tier 3":"🔴 Tier 3 — Monitor / Stabilize",
    "Expansion":"🔵 Expansion — Future Opportunity",
}
CRIT_NAMES = {
    "c1":"C1: Mission Alignment",
    "c2":"C2: Volume Potential",
    "c3":"C3: Socio Profile Fit",
    "c4":"C4: Digital Readiness",
    "c5":"C5: Political Risk",
    "c6":"C6: Legal Structure",
}
CRIT_DESC = {
    "c1":"Quality & strength of potential partners in the country ecosystem",
    "c2":"Whether the country can realistically get MI to scale (500+ socios/yr)",
    "c3":"Density of urban micro-entrepreneurs matching MI's target profile",
    "c4":"Digital infrastructure strength to support virtual mentoring",
    "c5":"Political & operational risk level for a US-based NGO",
    "c6":"Ability to collect revenue without complex legal structures",
}
CITIES = {
    "Kenya":"Nairobi","Ghana":"Accra, Tamale","Cape Verde":"Praia",
    "Cambodia":"Phnom Penh, Siem Reap, Kampong Cham, Battambang",
    "Dominican Republic":"Santo Domingo","Mexico":"Mérida, Tuxtla",
    "Guatemala":"Guatemala City","Honduras":"San Pedro Sula",
    "Nicaragua":"Managua","Colombia":"Countrywide (Bogotá base)",
    "Peru":"Trujillo","Malawi":"Lilongwe",
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
        dict(country="Brazil",      c1=15.22,c2=13.44,c3=9.89,c4=9.99,c5=6.71,c6=6.07,score=11.04),
        dict(country="Ecuador",     c1=9.91, c2=9.04, c3=6.76,c4=7.54,c5=6.72,c6=5.29,score=7.90),
        dict(country="South Africa",c1=8.76, c2=7.03, c3=8.15,c4=8.52,c5=7.21,c6=7.80,score=7.81),
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

scores    = load_scores()
expansion = load_expansion()
eco       = load_eco()
pp        = load_pp()

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown(f"""
<style>
[data-testid="stSidebar"] {{
    background:linear-gradient(180deg,{DBLUE} 0%,#002040 100%);
    border-right:3px solid {GOLD};
}}
[data-testid="stSidebar"] * {{ color:{WHITE} !important; }}
[data-testid="stSidebar"] .stRadio > label {{ display:none; }}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {{
    color:#CADCFC !important; font-size:0.86rem; padding:4px 0;
}}
#MainMenu {{ visibility:hidden; }}
footer {{ visibility:hidden; }}
header[data-testid="stHeader"] {{ display:none; }}
.block-container {{ padding-top:0.8rem !important; padding-bottom:2rem; max-width:1280px; }}
h1,h2,h3 {{ color:{DBLUE}; }}

.page-header {{
    background:linear-gradient(135deg,{DBLUE} 0%,#005080 100%);
    padding:1rem 1.6rem 0.9rem;
    margin-bottom:1.2rem;
    border-bottom:4px solid {GOLD};
}}
.kpi-card {{
    background:{WHITE}; border-radius:10px; padding:1rem 0.8rem;
    text-align:center; box-shadow:0 2px 8px rgba(0,0,0,0.08);
    border-top:4px solid {BLUE};
}}
.kpi-val {{ font-size:1.9rem; font-weight:800; color:{BLUE}; line-height:1.1; }}
.kpi-lab {{ font-size:0.75rem; color:{MGREY}; margin-top:4px; line-height:1.3; }}
.card {{
    background:{WHITE}; border-radius:10px; padding:1rem 1.2rem;
    box-shadow:0 2px 8px rgba(0,0,0,0.07); margin-bottom:0.75rem;
    border-left:4px solid {BLUE};
}}
.card-gold {{
    background:#FFFDF0; border-left:4px solid {GOLD};
    border-radius:10px; padding:1rem 1.2rem; margin-bottom:0.75rem;
}}
.card-green {{
    background:#F0FAF4; border-left:4px solid {GREEN};
    border-radius:10px; padding:1rem 1.2rem; margin-bottom:0.75rem;
}}
.card-blue {{
    background:#EEF5FC; border-left:4px solid {BLUE};
    border-radius:10px; padding:1rem 1.2rem; margin-bottom:0.75rem;
}}
.section-label {{
    font-size:0.65rem; font-weight:700; letter-spacing:2px;
    color:{BLUE}; text-transform:uppercase; margin-bottom:6px; display:block;
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
        MENTORS INTERNATIONAL · PARTNERSHIP GROWTH FRAMEWORK
      </div>
      <div style="font-size:1.2rem;font-weight:800;color:{WHITE};">{title}</div>
      {sub_html}
    </div>
    <div style="text-align:right;">
      <div style="font-size:0.65rem;color:#CADCFC;font-weight:600;">UCLA Anderson SICC</div>
      <div style="font-size:0.62rem;color:#AABBCC;">Spring 2026</div>
    </div>
  </div>
</div>""", unsafe_allow_html=True)

def kpi(val, label, color=BLUE):
    return f'<div class="kpi-card" style="border-top-color:{color};"><div class="kpi-val" style="color:{color};">{val}</div><div class="kpi-lab">{label}</div></div>'

def score_bar(val, max_val=10, color=BLUE):
    pct = min(100, val/max_val*100)
    return f"""<div style="display:flex;align-items:center;gap:8px;margin-bottom:4px;">
  <div style="flex:1;background:#E9ECEF;border-radius:4px;height:10px;">
    <div style="width:{pct:.0f}%;background:{color};height:10px;border-radius:4px;"></div>
  </div>
  <div style="font-size:0.82rem;font-weight:700;color:{DBLUE};width:30px;text-align:right;">{val:.1f}</div>
</div>"""

def tier_pill(tier):
    c = TIER_COLOR.get(tier, MGREY)
    return f'<span style="background:{c};color:white;border-radius:20px;padding:3px 12px;font-size:0.75rem;font-weight:700;">{TIER_LABEL.get(tier,tier)}</span>'

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
st.sidebar.markdown(f"""
<div style="padding:1.2rem 0.6rem 0.8rem;text-align:center;">
  <div style="font-size:1.4rem;font-weight:900;color:{WHITE};line-height:1.1;">Mentors</div>
  <div style="font-size:1.4rem;font-weight:900;color:{GOLD};line-height:1.1;margin-bottom:8px;">International</div>
  <div style="height:2px;background:linear-gradient(90deg,{GOLD},{BLUE},transparent);margin:0 0 8px;border-radius:2px;"></div>
  <div style="font-size:0.62rem;color:#CADCFC;letter-spacing:1.5px;font-weight:600;">PARTNERSHIP GROWTH FRAMEWORK</div>
  <div style="font-size:0.6rem;color:#7A8EA0;margin-top:3px;">UCLA Anderson SICC · Spring 2026</div>
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
  ✅ Ecosystem: 183 orgs researched<br>
  ✅ Priority Partners identified<br>
  ✅ Expansion: 3 countries analyzed<br>
  <div style="margin-top:6px;color:#556677;font-style:italic;">Final delivery: June 10, 2026</div>
</div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — OVERVIEW
# ══════════════════════════════════════════════════════════════════════════════
if "Overview" in page:
    page_header("Overview", "Mentors International · Partnership Growth Strategy · Spring 2026")

    # Mission only — no Theory of Change
    st.markdown(f"""
<div style="background:linear-gradient(135deg,{DBLUE} 0%,#005080 100%);border-radius:12px;
            padding:1.4rem 1.8rem;margin-bottom:1rem;border-left:5px solid {GOLD};">
  <div style="font-size:0.65rem;color:{GOLD};letter-spacing:2px;font-weight:700;margin-bottom:6px;">MISSION</div>
  <div style="font-size:1.3rem;font-weight:700;color:{WHITE};line-height:1.5;">
    Lifting families around the world from poverty to prosperity through entrepreneurship and one-on-one mentoring.
  </div>
</div>""", unsafe_allow_html=True)

    st.markdown("---")

    # FY25 KPIs
    st.markdown(f'<span class="section-label">FY2025 Impact</span>', unsafe_allow_html=True)
    k1,k2,k3,k4,k5 = st.columns(5)
    for col, val, label, color in [
        (k1,"43,160","Entrepreneurs served",BLUE),
        (k2,"12","Countries operating",DBLUE),
        (k3,"+79%","Volume growth vs FY24",GREEN),
        (k4,"$150","Cost per family / year",AMBER),
        (k5,"$5","Economic return per $1",GOLD),
    ]:
        col.markdown(f'<div>{kpi(val,label,color)}</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Project objective + what we built
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""<div class="card-green">
<span class="section-label">PROJECT OBJECTIVE</span>
<div style="font-size:1rem;color:{DGREY};line-height:1.7;margin-top:4px;">
Develop a <strong>structured, data-driven framework</strong> to identify, prioritize, and scale
high-impact partnerships that enable Mentors International to reach their
<strong>2030 target of 100,000 socios per year</strong>.
</div></div>""", unsafe_allow_html=True)

    with col2:
        st.markdown(f"""<div class="card-blue">
<span class="section-label">WHAT WE BUILT</span>
<div style="font-size:0.88rem;color:{DGREY};line-height:1.75;margin-top:4px;">
An <strong>8-criterion scoring framework</strong> based off interviews, using real data sources
(World Bank, GSMA, Freedom House, etc.).<br><br>
A <strong>183-organization ecosystem database</strong> across all 12 countries of operation
and 3 potential expansion countries.<br><br>
<strong>Priority partners</strong> for all 12 countries of operation.<br><br>
An <strong>expansion analysis</strong> for 3 future markets.
</div></div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — FRAMEWORK
# ══════════════════════════════════════════════════════════════════════════════
elif "Framework" in page:
    page_header("The Framework", "8 criteria used to score and prioritize countries for partnership investment")

    st.markdown(f"""
<div class="card-gold">
<span class="section-label">HOW TO READ THIS FRAMEWORK</span>
<div style="font-size:0.88rem;color:{DGREY};line-height:1.65;margin-top:4px;">
Each criterion is scored on a <strong>0–10 scale</strong> using real data sources.
<strong>Criteria 1–6</strong> are fully scored and form the quantitative country score.
<strong>Criteria 7–8</strong> require qualitative assessment and are excluded from the numerical score.
The overall country score is the weighted average of Criteria 1–6.
</div></div>""", unsafe_allow_html=True)

    criteria = [
        dict(num="C1", name="Mission Alignment", type="Market", weight_all="15%", weight_16="19%",
             goal="Assess the quality and strength of potential partners in each country ecosystem",
             oneliner="How well do potential partners align with MI's model?",
             metrics=[
                 ("Number of high-fit partners (score 4–5) in ecosystem database", "Ecosystem Database"),
                 ("Number of ideal partners (score 5) in ecosystem database", "Ecosystem Database"),
                 ("Volume-adjusted alignment score weighted by org size", "Ecosystem Database"),
                 ("% of total ecosystem that is high-fit (4 or 5)", "Ecosystem Database"),
             ]),
        dict(num="C2", name="Volume Potential", type="Market", weight_all="23%", weight_16="28%",
             goal="Identify whether a country can realistically get MI to scale",
             oneliner="Can this country deliver 500+ socios per year through partnerships?",
             metrics=[
                 ("Number of organizations with scale rating 4–5 (500+ reach)", "Ecosystem Database"),
                 ("Number of organizations with scale rating 5 (1,000+ reach)", "Ecosystem Database"),
                 ("Volume-weighted alignment score", "Ecosystem Database"),
                 ("% of ecosystem that is large-scale", "Ecosystem Database"),
             ]),
        dict(num="C3", name="Socio Profile Fit & Density", type="Market", weight_all="15%", weight_16="19%",
             goal="Assess the size and serviceability of the urban micro-entrepreneur target population",
             oneliner="Is there sufficient density of urban micro-entrepreneurs matching MI's profile?",
             metrics=[
                 ("Urban population size", "World Bank"),
                 ("Multidimensional Poverty Index — urban population in need", "MPI Index"),
                 ("Informal self-employment rate", "ILO Labor Statistics"),
                 ("% of workforce in urban micro-enterprise", "World Bank"),
             ]),
        dict(num="C4", name="Digital Readiness", type="Market", weight_all="5%", weight_16="9%",
             goal="Determine whether MI can scale virtually in each country",
             oneliner="Is digital infrastructure strong enough for virtual mentoring at scale?",
             metrics=[
                 ("Mobile connectivity rate", "GSMA Mobile Connectivity Index"),
                 ("Internet usage rate", "World Bank Digital Development"),
                 ("Mobile money adoption", "World Bank Findex"),
                 ("4G/LTE coverage %", "GSMA"),
             ]),
        dict(num="C5", name="Political & Operating Risk", type="Market", weight_all="10%", weight_16="14%",
             goal="Assess the level of political and operational risk for NGO activities",
             oneliner="How stable is the political environment for a US-based NGO?",
             metrics=[
                 ("Fragile States Index score", "Fund for Peace"),
                 ("Political freedom score", "Freedom House"),
                 ("NGO operational freedom — legal and regulatory environment", "NGO Law Monitor"),
                 ("Historical US NGO operating risk", "Country research"),
             ]),
        dict(num="C6", name="Legal & Structural Constraints", type="Market", weight_all="7%", weight_16="11%",
             goal="Determine whether MI can operate and generate revenue without complex legal structures",
             oneliner="Can Mentors collect revenue from partners without major legal barriers?",
             metrics=[
                 ("Nonprofit registration requirements", "Country legal research"),
                 ("Ability to receive foreign funding", "Country legal research"),
                 ("Revenue-generating restrictions on NGOs", "NGO Law Monitor"),
                 ("Ease of establishing local legal entity", "World Bank Doing Business"),
             ]),
        dict(num="C7", name="CD Strength & Leadership", type="Operational", weight_all="15%", weight_16="N/A — qualitative",
             goal="Assess whether in-country leadership can execute, build partnerships, and drive scale",
             oneliner="Does the CD have the capability and capacity to build and manage partnerships?",
             metrics=[
                 ("Years of experience as CD", "HQ assessment + CD interviews"),
                 ("Track record of partnership development", "CD interviews"),
                 ("Quality of existing partner relationships", "CD interviews"),
                 ("Full-time vs part-time commitment", "HQ assessment"),
             ]),
        dict(num="C8", name="Program Standardization", type="Operational", weight_all="10%", weight_16="N/A — qualitative",
             goal="Assess whether MI's program can be delivered consistently and scaled across partners",
             oneliner="Is the program standardized enough to be delivered consistently across multiple partners?",
             metrics=[
                 ("Socio Connect adoption and data quality", "Socio Connect platform"),
                 ("Mentor certification rate", "Program records"),
                 ("Curriculum adherence rate", "Program records"),
                 ("Impact data completeness", "Socio Connect platform"),
             ]),
    ]

    col1, col2 = st.columns([2,3])
    with col1:
        wt_df = pd.DataFrame([
            {"Criterion": f"{c['num']}: {c['name']}", "Weight": float(c['weight_16'].replace('%',''))}
            for c in criteria if 'N/A' not in c['weight_16']
        ])
        fig_w = px.bar(wt_df, x="Weight", y="Criterion", orientation="h",
            color_discrete_sequence=[BLUE],
            labels={"Weight":"Weight (%) — C1 to C6 only","Criterion":""},
            title="Criterion Weights (C1–C6 Scoring)", height=320)
        fig_w.update_layout(plot_bgcolor=WHITE, margin=dict(l=0,r=0,t=40,b=0))
        fig_w.update_xaxes(gridcolor="#F0F0F0", ticksuffix="%")
        fig_w.update_yaxes(showgrid=False)
        st.plotly_chart(fig_w, use_container_width=True)

    with col2:
        st.markdown(f'<span class="section-label">All 8 Criteria — expand each for full detail</span>', unsafe_allow_html=True)
        for c in criteria:
            excluded = "N/A" in c['weight_16']
            badge = "🔵 Operational" if c['type'] == "Operational" else "🟢 Market"
            with st.expander(f"**{c['num']}: {c['name']}** — {c['oneliner']}"):
                colA, colB = st.columns(2)
                with colA:
                    st.markdown(f"**Type:** {badge}")
                    st.markdown(f"**Weight (all 8 criteria):** {c['weight_all']}")
                    st.markdown(f"**Weight (C1–C6 score):** {c['weight_16']}")
                    st.markdown(f"**Goal:** {c['goal']}")
                with colB:
                    st.markdown("**Metrics & data sources:**")
                    for metric, source in c['metrics']:
                        st.markdown(f"- {metric} *(source: {source})*")
                if excluded:
                    st.info("C7 and C8 are assessed qualitatively through CD interviews and program data. They are not included in the quantitative country score.")

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 3 — COUNTRY BRIEFS
# ══════════════════════════════════════════════════════════════════════════════
elif "Country Briefs" in page:
    page_header("Country Briefs", "Framework scores and tier assignments for all 12 current operating countries")

    # ── Summary table with criterion column reminders ──────────────────────
    st.markdown(f'<span class="section-label">All Countries — Score Summary (C1–C6)</span>', unsafe_allow_html=True)
    st.caption("C1: Mission Alignment  ·  C2: Volume Potential  ·  C3: Socio Profile Fit  ·  C4: Digital Readiness  ·  C5: Political Risk  ·  C6: Legal Structure  ·  Score = weighted average C1–C6 (out of 10)")

    disp = scores[['country','c1','c2','c3','c4','c5','c6','score','tier']].copy()
    disp.columns = ['Country','C1','C2','C3','C4','C5','C6','Score (C1–C6)','Tier']
    disp = disp.sort_values('Score (C1–C6)', ascending=False)
    st.dataframe(
        disp.style.format({'C1':'{:.2f}','C2':'{:.2f}','C3':'{:.2f}',
                           'C4':'{:.2f}','C5':'{:.2f}','C6':'{:.2f}','Score (C1–C6)':'{:.2f}'}),
        use_container_width=True, hide_index=True,
        height=35 * (len(disp) + 1) + 10
    )

    st.markdown("---")

    # ── Country detail ─────────────────────────────────────────────────────
    sel = st.selectbox("Select a country for detailed view",
                       scores.sort_values('score', ascending=False)['country'].tolist())
    r   = scores[scores['country'] == sel].iloc[0]
    tier = TIER_MAP.get(sel, "Tier 3")
    tc  = TIER_COLOR.get(tier, MGREY)

    st.markdown(f"""
<div style="background:linear-gradient(135deg,{DBLUE} 0%,#005080 100%);border-radius:12px;
            padding:1rem 1.4rem;margin-bottom:1rem;border-bottom:4px solid {GOLD};
            display:flex;justify-content:space-between;align-items:center;">
  <div>
    <div style="font-size:1.4rem;font-weight:800;color:{WHITE};">{sel}</div>
    <div style="font-size:0.8rem;color:#CADCFC;margin-top:3px;">
      {TIER_LABEL.get(tier,tier)}  ·  Cities: {CITIES.get(sel,'—')}
    </div>
  </div>
  <div style="font-size:2.5rem;font-weight:900;color:{GOLD};">{r['score']:.2f}<span style="font-size:1rem;color:#CADCFC;">/10</span></div>
</div>""", unsafe_allow_html=True)

    col1, col2 = st.columns([2,3])
    with col1:
        st.markdown(f'<span class="section-label">Criterion Scores</span>', unsafe_allow_html=True)
        for key, name in CRIT_NAMES.items():
            val = r[key]
            color = GREEN if val >= 7 else AMBER if val >= 5 else RED
            desc  = CRIT_DESC[key]
            st.markdown(f"""
<div style="margin-bottom:8px;">
  <div style="font-size:0.82rem;font-weight:600;color:{DBLUE};">{name}</div>
  <div style="font-size:0.73rem;color:{MGREY};margin-bottom:3px;">{desc}</div>
  {score_bar(val, 10, color)}
</div>""", unsafe_allow_html=True)

    with col2:
        fig_r = go.Figure(go.Scatterpolar(
            r=[r.c1,r.c2,r.c3,r.c4,r.c5,r.c6,r.c1],
            theta=["Mission\nAlignment","Volume\nPotential","Socio\nProfile",
                   "Digital\nReadiness","Political\nRisk","Legal\nStructure","Mission\nAlignment"],
            fill='toself', fillcolor=f"rgba(39,116,174,0.15)",
            line=dict(color=BLUE, width=2), name=sel
        ))
        fig_r.update_layout(
            polar=dict(radialaxis=dict(range=[0,10], tickfont=dict(size=9))),
            showlegend=False, height=340, margin=dict(l=30,r=30,t=30,b=30)
        )
        st.plotly_chart(fig_r, use_container_width=True)

    # Priority partners for this country
    c_pp = pp[pp['Country'] == sel] if 'Country' in pp.columns else pd.DataFrame()
    if len(c_pp):
        st.markdown(f'<span class="section-label">Priority Partners — {sel}</span>', unsafe_allow_html=True)
        st.dataframe(c_pp[['Organization Name','Why Priority','Partnership Type',
                            'Estimated Reach','Cities of Overlap with MI']].rename(
            columns={'Organization Name':'Organization','Why Priority':'Why a Priority',
                     'Partnership Type':'Type','Estimated Reach':'Scale'}),
            use_container_width=True, hide_index=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 4 — FUTURE PARTNERSHIPS
# ══════════════════════════════════════════════════════════════════════════════
elif "Future" in page:
    page_header("Future Partnerships", "Applying the framework to evaluate potential expansion markets")

    st.markdown(f"""
<div class="card-gold">
<span class="section-label">HOW TO USE THIS PAGE</span>
<div style="font-size:0.88rem;color:{DGREY};line-height:1.65;margin-top:4px;">
This page demonstrates how Mentors International can apply the same 8-criterion framework
to evaluate any new country or market beyond the current 12.
Brazil, Ecuador, and South Africa have been scored using the same methodology and data sources.
This is how the framework continues to create value after this project ends.
</div></div>""", unsafe_allow_html=True)

    tier1 = scores[scores['tier']=='Tier 1'].copy()
    tier1['group'] = 'Current Tier 1'
    exp_df = expansion.copy()
    exp_df['group'] = 'Expansion Candidate'
    combined = pd.concat([tier1, exp_df], ignore_index=True)

    fig_c = px.bar(combined.sort_values('score',ascending=False),
        x='country', y='score', color='group',
        color_discrete_map={'Current Tier 1':BLUE, 'Expansion Candidate':GOLD},
        labels={'score':'Framework Score (C1–C6, out of 10)','country':'','group':''},
        height=360)
    fig_c.update_layout(plot_bgcolor=WHITE, margin=dict(l=0,r=0,t=10,b=0),
        legend=dict(orientation="h",y=1.1))
    fig_c.update_yaxes(gridcolor="#F0F0F0", range=[0,13])
    fig_c.update_xaxes(showgrid=False)
    fig_c.add_hline(y=7.0, line_dash="dot", line_color="#999",
                    annotation_text="Tier 1 threshold (7.0)")
    st.plotly_chart(fig_c, use_container_width=True)

    sel_exp = st.selectbox("Explore an expansion country", ["Brazil","Ecuador","South Africa"])
    r = expansion[expansion['country']==sel_exp].iloc[0]

    st.markdown(f"""
<div style="background:linear-gradient(135deg,{DBLUE} 0%,#005080 100%);border-radius:12px;
            padding:1rem 1.4rem;margin:0.5rem 0 1rem;border-bottom:4px solid {GOLD};
            display:flex;justify-content:space-between;align-items:center;">
  <div>
    <div style="font-size:1.3rem;font-weight:800;color:{WHITE};">{sel_exp}</div>
    <div style="font-size:0.78rem;color:#CADCFC;margin-top:3px;">Expansion candidate — framework score (C1–C6)</div>
  </div>
  <div style="font-size:2.2rem;font-weight:900;color:{GOLD};">{r['score']:.2f}<span style="font-size:1rem;color:#CADCFC;">/10</span></div>
</div>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<span class="section-label">Criterion Scores</span>', unsafe_allow_html=True)
        for key, name in CRIT_NAMES.items():
            val  = r[key]
            desc = CRIT_DESC[key]
            color = GREEN if val >= 7 else AMBER if val >= 5 else RED
            st.markdown(f"""
<div style="margin-bottom:8px;">
  <div style="font-size:0.82rem;font-weight:600;color:{DBLUE};">{name}</div>
  <div style="font-size:0.73rem;color:{MGREY};margin-bottom:3px;">{desc}</div>
  {score_bar(val, max(10, val+0.5), color)}
</div>""", unsafe_allow_html=True)

    with col2:
        insights = {
            "Brazil":      "Brazil scores the highest of any country evaluated — including all 12 current markets. Strong ecosystem, massive urban micro-entrepreneur population, and excellent digital infrastructure. The main consideration is the scale of entry investment required and legal complexity.",
            "Ecuador":     "Ecuador scores at Tier 1 level (7.90) — comparable to Peru and Kenya. Strong mission alignment and volume potential. Shares cultural and linguistic similarities with Colombia and Peru, making program adaptation straightforward.",
            "South Africa":"South Africa scores 7.81 — Tier 1 equivalent. Strong ecosystem, high digital readiness, and good legal structure. Operations would focus on township markets in Johannesburg and Cape Town where the micro-entrepreneur density is highest.",
        }
        st.markdown(f"""<div class="card">
<span class="section-label">STRATEGIC ASSESSMENT</span>
<div style="font-size:0.88rem;color:{DGREY};line-height:1.65;margin-top:4px;">{insights[sel_exp]}</div>
</div>""", unsafe_allow_html=True)

        eco_exp = eco[eco['Country']==sel_exp] if sel_exp in eco['Country'].values else pd.DataFrame()
        if len(eco_exp):
            st.markdown(f"**{len(eco_exp)} organizations researched in {sel_exp}**")
            st.dataframe(eco_exp[['Organization Name','Category','align_n','scale_n']].rename(
                columns={'Organization Name':'Organization',
                         'align_n':'Alignment /5','scale_n':'Scale /5'}
            ).sort_values('Alignment /5',ascending=False),
            use_container_width=True, hide_index=True)
        else:
            st.info("Partner research for this country is in progress.")

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 5 — PARTNER PIPELINE
# ══════════════════════════════════════════════════════════════════════════════
elif "Partner Pipeline" in page:
    page_header("Partner Pipeline", "183 potential partnership organizations identified across all 12 countries of operation")

    col1, col2, col3 = st.columns(3)
    all_countries = ["All"] + sorted(eco['Country'].dropna().unique())
    country_f = col1.selectbox("Country", all_countries)
    align_f   = col2.selectbox("Min Alignment Score", [1,2,3,4,5], index=2)
    scale_f   = col3.selectbox("Min Scale Score", [1,2,3,4,5], index=0)

    filtered = eco.copy()
    filtered['align_n'] = pd.to_numeric(filtered['align_n'], errors='coerce').fillna(0)
    filtered['scale_n'] = pd.to_numeric(filtered['scale_n'], errors='coerce').fillna(0)
    filtered['urban_n'] = pd.to_numeric(filtered['urban_n'], errors='coerce').fillna(0)
    if country_f != "All":
        filtered = filtered[filtered['Country']==country_f]
    filtered = filtered[filtered['align_n'] >= align_f]
    filtered = filtered[filtered['scale_n'] >= scale_f]
    filtered = filtered.reset_index(drop=True)

    m1,m2,m3,m4 = st.columns(4)
    m1.metric("Organizations shown", len(filtered))
    m2.metric("Excellent Fit (Score 5)", len(filtered[filtered['align_n']==5]))
    m3.metric("Very Good Fit (Score 4)", len(filtered[filtered['align_n']==4]))
    m4.metric("Countries", filtered['Country'].nunique())

    st.dataframe(
        filtered[['Country','Organization Name','Category',
                  'Alignment with MI (1-5)','Scale Potential (1-5)',
                  'Urban Relevance (1-5)',
                  'Confirmed / Likely Urban & Peri-Urban Areas of Operation',
                  'Website','Notes']].rename(columns={
            'Organization Name':'Organization',
            'Alignment with MI (1-5)':'Alignment',
            'Scale Potential (1-5)':'Scale',
            'Urban Relevance (1-5)':'Urban Relevance',
            'Confirmed / Likely Urban & Peri-Urban Areas of Operation':'Cities of Operation',
        }).sort_values(['Country','Alignment'], ascending=[True,False]),
        use_container_width=True, hide_index=True, height=500
    )
    st.caption("Source: 183 potential partnership organizations identified across all 12 countries of operation · Research by Caleigh Hernandez · Anderson Library databases, NGO registries, MFI directories, Factiva")

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 6 — ECOSYSTEM ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
elif "Ecosystem" in page:
    page_header("Ecosystem Analysis", "Partner landscape across all 12 countries — alignment, scale, and market opportunity")

    tab1, tab2 = st.tabs(["📊 Alignment Overview","🗺️ Country Portfolio"])

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
                color_discrete_sequence=[DBLUE],
                labels={'avg':'Average Alignment Score','Country':''},
                title='Average Alignment Score by Country', height=380)
            fig2.update_layout(plot_bgcolor=WHITE, margin=dict(l=0,r=0,t=40,b=0))
            fig2.update_xaxes(gridcolor="#F0F0F0", range=[0,5.5])
            fig2.update_yaxes(showgrid=False)
            st.plotly_chart(fig2, use_container_width=True)

        avg_s = eco.groupby('Country')['scale_n'].mean().reset_index()
        avg_s.columns = ['Country','avg_scale']
        fig3 = px.bar(avg_s.sort_values('avg_scale'), x='avg_scale', y='Country', orientation='h',
            color_discrete_sequence=[GOLD],
            labels={'avg_scale':'Average Scale Score','Country':''},
            title='Average Scale Potential by Country', height=380)
        fig3.update_layout(plot_bgcolor=WHITE, margin=dict(l=0,r=0,t=40,b=0))
        fig3.update_xaxes(gridcolor="#F0F0F0", range=[0,5.5])
        fig3.update_yaxes(showgrid=False)
        st.plotly_chart(fig3, use_container_width=True)

    with tab2:
        fig4 = px.scatter(scores, x='score', y='c1', color='tier',
            size='score', size_max=50, hover_name='country',
            hover_data={'c1':True,'c2':True,'c3':True,'score':True,'tier':False},
            color_discrete_map={"Tier 1":GREEN,"Tier 2":AMBER,"Tier 3":RED},
            labels={'score':'Overall Score (C1–C6)','c1':'Mission Alignment (C1)','tier':'Tier'},
            title='Market Opportunity vs Mission Alignment', height=420)
        fig4.update_layout(plot_bgcolor=WHITE)
        fig4.update_xaxes(gridcolor="#F0F0F0")
        fig4.update_yaxes(gridcolor="#F0F0F0")
        st.plotly_chart(fig4, use_container_width=True)

        st.markdown(f'<span class="section-label">Country Portfolio — Criterion Profile</span>', unsafe_allow_html=True)
        crit_theta = ["C1: Mission","C2: Volume","C3: Socio Fit",
                      "C4: Digital","C5: Political","C6: Legal","C1: Mission"]
        fig5 = go.Figure()
        tc_map = {"Tier 1":GREEN,"Tier 2":AMBER,"Tier 3":RED}
        for _, row in scores.iterrows():
            vals = [row.c1,row.c2,row.c3,row.c4,row.c5,row.c6,row.c1]
            fig5.add_trace(go.Scatterpolar(
                r=vals, theta=crit_theta, name=row.country,
                line=dict(color=tc_map.get(row.tier,MGREY), width=1.5), opacity=0.7
            ))
        fig5.update_layout(
            polar=dict(radialaxis=dict(range=[0,10])),
            showlegend=True, height=500,
            legend=dict(orientation="v", x=1.05)
        )
        st.plotly_chart(fig5, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 7 — RECOMMENDATIONS
# ══════════════════════════════════════════════════════════════════════════════
elif "Recommendations" in page:
    page_header("Recommendations", "Tier structure, priority partners, and strategic next steps")

    # Project objective at top
    st.markdown(f"""
<div style="background:linear-gradient(135deg,{DBLUE} 0%,#005080 100%);border-radius:12px;
            padding:1.3rem 1.6rem;margin-bottom:1rem;border-bottom:4px solid {GOLD};">
  <div style="font-size:0.65rem;color:{GOLD};letter-spacing:2px;font-weight:700;margin-bottom:4px;">PROJECT OBJECTIVE</div>
  <div style="font-size:1rem;color:{WHITE};line-height:1.7;">
    Develop a structured, data-driven framework to identify, prioritize, and scale high-impact partnerships
    that enable Mentors International to reach their
    <span style="color:{GOLD};font-weight:800;">2030 target of 100,000 socios per year</span>.
  </div>
</div>""", unsafe_allow_html=True)

    # 4-step action plan
    st.markdown(f'<span class="section-label">Recommended Action Plan</span>', unsafe_allow_html=True)
    steps = [
        (BLUE,"1","Finish Scoring — Complete Criteria 7 & 8",
         "As HQ, complete the qualitative assessment of CD Strength (C7) and Program Standardization (C8) for all 12 countries. C7 metrics: CD years of experience, partnership track record, relationship quality, full-time commitment. C8 metrics: Socio Connect data quality, mentor certification rate, curriculum adherence, impact data completeness. This will finalize country tier assignments and surface any tier changes."),
        (GREEN,"2","Prioritize Tier 1 Countries",
         "Direct investment and partnership-building resources to Colombia, Peru, Kenya, and Dominican Republic first. These four countries score 7.0+ on the C1–C6 framework — the strongest combination of partner ecosystem quality, volume potential, and operating conditions. Colombia requires urgent diversification away from Bancolombia. Kenya requires resolving the CD full-time commitment."),
        (AMBER,"3","Equip Tier 1 Country Directors",
         "Build the tools CDs need to convert partnership conversations into signed MOUs. This includes: a 2-page Partner Evidence Brief with Mentors' global impact benchmarks, a country-specific partner target list drawn from the ecosystem database, and a partnership playbook covering outreach, due diligence, and onboarding. The framework has identified the right partners — now CDs need the right content to approach them."),
        (GOLD,"4","Pursue Priority Partners in Tier 1 Countries",
         "Activate the priority partner lists for all Tier 1 countries. Start with the highest-alignment, highest-scale organizations identified in the ecosystem database and priority partners sheet. For multi-country opportunities — Millicom/TIGO (9 countries), Pro Mujer (5 LATAM countries), LDS Humanitarian Program — approach at corporate level rather than country by country."),
    ]
    for color, num, title, body in steps:
        st.markdown(f"""
<div style="display:flex;gap:14px;margin-bottom:12px;align-items:flex-start;">
  <div style="background:{color};color:white;border-radius:50%;width:38px;height:38px;
              display:flex;align-items:center;justify-content:center;font-size:1.1rem;
              font-weight:800;flex-shrink:0;margin-top:2px;">{num}</div>
  <div style="flex:1;">
    <div style="font-weight:700;color:{DBLUE};font-size:0.95rem;">{title}</div>
    <div style="font-size:0.83rem;color:{MGREY};margin-top:4px;line-height:1.6;">{body}</div>
  </div>
</div>""", unsafe_allow_html=True)

    st.markdown("---")

    # Tier structure
    st.markdown(f'<span class="section-label">Country Tier Structure</span>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div style="background:#F0FAF4;border-radius:10px;padding:10px 14px;border-top:4px solid {GREEN};margin-bottom:8px;font-weight:700;color:{GREEN};">🟢 Tier 1 — Invest & Scale</div>', unsafe_allow_html=True)
        for _, r in scores[scores['tier']=='Tier 1'].sort_values('score',ascending=False).iterrows():
            c_pp = pp[pp['Country']==r['country']] if 'Country' in pp.columns else pd.DataFrame()
            with st.expander(f"**{r['country']}** — {r['score']:.2f}/10"):
                if len(c_pp):
                    for _, pr in c_pp.iterrows():
                        st.markdown(f"• **{pr['Organization Name']}** — {pr['Why Priority']}")
                else:
                    st.caption("Priority partner research pending.")
    with col2:
        st.markdown(f'<div style="background:#FFF9EC;border-radius:10px;padding:10px 14px;border-top:4px solid {AMBER};margin-bottom:8px;font-weight:700;color:{AMBER};">🟡 Tier 2 — Targeted Investment</div>', unsafe_allow_html=True)
        for _, r in scores[scores['tier']=='Tier 2'].sort_values('score',ascending=False).iterrows():
            c_pp = pp[pp['Country']==r['country']] if 'Country' in pp.columns else pd.DataFrame()
            with st.expander(f"**{r['country']}** — {r['score']:.2f}/10"):
                if len(c_pp):
                    for _, pr in c_pp.iterrows():
                        st.markdown(f"• **{pr['Organization Name']}** — {pr['Why Priority']}")
                else:
                    st.caption("Priority partner research pending.")
    with col3:
        st.markdown(f'<div style="background:#FFF5F5;border-radius:10px;padding:10px 14px;border-top:4px solid {RED};margin-bottom:8px;font-weight:700;color:{RED};">🔴 Tier 3 — Monitor / Stabilize</div>', unsafe_allow_html=True)
        for _, r in scores[scores['tier']=='Tier 3'].sort_values('score',ascending=False).iterrows():
            with st.expander(f"**{r['country']}** — {r['score']:.2f}/10"):
                st.caption("Monitor existing operations. No new partnership investment at this stage.")

    st.markdown("---")
    st.markdown(f'<span class="section-label">Priority Partners — Full List</span>', unsafe_allow_html=True)
    st.caption("To be updated by Caleigh as additional partner research is completed.")
    if len(pp):
        st.dataframe(pp.rename(columns={
            'Organization Name':'Organization','Why Priority':'Why a Priority',
            'Partnership Type':'Type','Estimated Reach':'Scale',
            'Cities of Overlap with MI':'Cities'
        }), use_container_width=True, hide_index=True)
    else:
        st.info("Priority partner list will be populated as research progresses.")

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 8 — APPENDIX
# ══════════════════════════════════════════════════════════════════════════════
elif "Appendix" in page:
    page_header("Appendix", "Data sources, methodology, and framework limitations")

    tab1, tab2, tab3 = st.tabs(["📚 Data Sources","⚠️ Limitations","🔬 Benchmarks"])

    with tab1:
        sources = [
            ("World Bank","Urban population, poverty headcount ratios, self-employment rates, internet usage","data.worldbank.org"),
            ("GSMA Mobile Connectivity Index","Mobile connectivity, 4G coverage, digital readiness scores","gsma.com/mobileconnectivityindex"),
            ("Fund for Peace — Fragile States Index","Political stability, government effectiveness, security","fragilestatesindex.org"),
            ("Freedom House","Political rights and civil liberties — NGO operating environment","freedomhouse.org"),
            ("Anderson Library Databases","Organization research, MFI directories, NGO databases, Factiva","UCLA Library"),
            ("Country NGO Registries","Local NGO registration databases used by country directors","Country-specific"),
            ("Ecosystem Database","242 organizations scored across 12 countries of operation plus 3 potential expansion countries on alignment, scale, and urban relevance","Internal — Caleigh Hernandez"),
            ("CD Interviews","Ghana (Week 4), Kenya (Week 5), Mexico (Week 5), HQ: Ana Peña + Peter Sturgeon","Primary research"),
        ]
        for name, desc, src in sources:
            st.markdown(f"""<div class="card">
<div style="font-weight:700;color:{DBLUE};">{name}</div>
<div style="font-size:0.82rem;color:{DGREY};margin-top:3px;">{desc}</div>
<div style="font-size:0.75rem;color:{MGREY};margin-top:2px;font-style:italic;">{src}</div>
</div>""", unsafe_allow_html=True)

    with tab2:
        limitations = [
            ("C7 and C8 excluded from quantitative score",
             "CD Strength and Program Standardization require qualitative judgment. They are assessed separately and not included in the numerical score to maintain objectivity across countries."),
            ("Ecosystem research depth varies by country",
             "Countries with more available data (Colombia, Kenya, Dominican Republic) have more organizations in the database. Smaller or less-documented markets may have fewer entries."),
            ("Geography not captured in scoring",
             "The framework does not account for the difficulty of traveling between cities within a country. A single country score does not reflect intra-country operational complexity."),
            ("Self-reported outcome data",
             "Mentors International's impact outcomes (+53% income, +65% savings) are self-reported by participants and have not been independently verified."),
            ("Framework reflects a point in time",
             "Country scores reflect data available as of May 2026. Political environments, partner landscapes, and economic conditions change — the framework should be reviewed annually."),
        ]
        for title, body in limitations:
            with st.expander(f"⚠️ {title}"):
                st.markdown(body)

    with tab3:
        bm = pd.DataFrame({
            "Organization":["Mentors International","BRAC Graduation Approach",
                            "Opportunity International","TechnoServe"],
            "Income Increase":["53% (Year 1)*","38% (over 4 years)","~25% (Year 1)","~20% (Year 1)"],
            "Cost / Year":["$150","$300–500","$400–600","$200–400"],
            "Countries":["12","14","30+","25+"],
            "Data":["Self-reported*","Independently verified","Partner-delivered","Technical assistance"],
        })
        st.dataframe(bm, use_container_width=True, hide_index=True)
        st.caption("* Self-reported FY2025. Independent verification would significantly strengthen the partner evidence brief.")

    st.markdown("---")
    st.caption("UCLA Anderson SICC · Spring 2026 · Mentors International Partnership Growth Strategy · June 10, 2026 · Praveen Gangaraju · Caleigh Hernandez · Morgan Ikemiya · Sydney Kyle · Prof. Gayle Northrop")
