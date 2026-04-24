import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Mentors International — Growth Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.markdown("""
<style>
    [data-testid="stSidebar"] { background-color: #1B2A4A; }
    [data-testid="stSidebar"] * { color: white !important; }
    .block-container { padding-top: 2rem; }
    h1 { color: #1B2A4A; }
    h2 { color: #1B2A4A; }
    .stMetric { background: #f4f6f9; border-radius: 10px; padding: 1rem; }
</style>
""", unsafe_allow_html=True)

# ── DATA ──────────────────────────────────────────────────────────────────────

countries = pd.DataFrame([
    dict(country="Mexico", flag="🇲🇽", region="Latin America", tier=1,
         cd="Zoram Varguez", cd_tenure="10+ yrs", mentors=11,
         fy25=614, fy26=1000,
         m_align=4, socio=4, volume=5, digital=4, mkt=9.0,
         cd_score=5, program=5, legal=4, risk=4, ops=9.0, total=18.0,
         action="Invest + accelerate — highest priority",
         iso="MEX", lat=23.6, lon=-102.5,
         working="DIF govt partnerships active. Heifer International live. CD tech-forward. Virtual hub for all LATAM.",
         not_working="Socio profile drift risk — must stay anchored in Chiapas & Yucatan.",
         ceiling="5,000+ socios/yr possible with 3–4 strong partnerships.",
         key_risk="Socio profile drift into middle-class families.",
         rec="Highest priority. Pursue DIF expansion first, then CEMEX three-party model."),

    dict(country="Colombia", flag="🇨🇴", region="Latin America", tier=1,
         cd="Andrea Arenas", cd_tenure="2 yrs (6+ w/org)", mentors=90,
         fy25=20875, fy26=16000,
         m_align=3, socio=5, volume=5, digital=5, mkt=9.0,
         cd_score=5, program=5, legal=5, risk=4, ops=10.0, total=19.0,
         action="Diversify within Colombia urgently",
         iso="COL", lat=4.6, lon=-74.3,
         working="Best operational team. 100% virtual. Banking regulation enables revenue partnerships.",
         not_working="90%+ volume from Bancolombia alone. Volume declining 20k→16k.",
         ceiling="50,000+ socios/yr if 3–4 banking partnerships secured.",
         key_risk="Bancolombia concentration — single partner drives 50%+ of global volume.",
         rec="Urgent diversification. Research banking compliance obligations. Pursue 3–5 smaller partners now."),

    dict(country="Dominican Republic", flag="🇩🇴", region="Latin America", tier=1,
         cd="Ruth Martes", cd_tenure="6 yrs", mentors=8,
         fy25=169, fy26=836,
         m_align=4, socio=3, volume=3, digital=4, mkt=7.0,
         cd_score=4, program=4, legal=3, risk=4, ops=8.0, total=15.0,
         action="Invest + accelerate",
         iso="DOM", lat=18.7, lon=-70.2,
         working="LDS Church renewing 3x. ECLOF MFI just landed. Virtual mentoring working well.",
         not_working="Small island limits total scale.",
         ceiling="1,500–2,000 socios/yr. Quality over scale.",
         key_risk="Volume ceiling — small country.",
         rec="Use DR as test case for combo model. Deepen ECLOF and LDS relationships."),

    dict(country="Nicaragua", flag="🇳🇮", region="Latin America", tier=1,
         cd="Pio Quintero", cd_tenure="10+ yrs", mentors=10,
         fy25=490, fy26=1000,
         m_align=4, socio=3, volume=3, digital=3, mkt=7.0,
         cd_score=4, program=4, legal=4, risk=2, ops=7.0, total=14.0,
         action="Invest carefully — political risk real",
         iso="NIC", lat=12.9, lon=-85.2,
         working="TIGO flywheel is the template for all partnerships. Pio is exceptional operator.",
         not_working="Cannot convene NGOs publicly. Government restricting US NGO activity.",
         ceiling="1,500–2,000 socios/yr given political constraints.",
         key_risk="Political environment tightening for US-affiliated charities.",
         rec="Maintain and protect. Pursue Millicom at corporate level to replicate across 9 LATAM+Africa countries."),

    dict(country="Kenya", flag="🇰🇪", region="Africa", tier=2,
         cd="Eric Onyango", cd_tenure="4 yrs", mentors=7,
         fy25=592, fy26=600,
         m_align=4, socio=4, volume=3, digital=4, mkt=7.0,
         cd_score=2, program=4, legal=4, risk=3, ops=7.0, total=14.0,
         action="Targeted — CD part-time is binding constraint",
         iso="KEN", lat=-0.0, lon=37.9,
         working="Simplest cleanest model. World Vision partnership in development. Cross-border virtual mentoring proven.",
         not_working="CD has a part-time job — cannot scale without full-time commitment.",
         ceiling="3,000–5,000 socios/yr IF CD issue resolved. Nairobi alone has millions of informal entrepreneurs.",
         key_risk="CD part-time commitment is the single biggest constraint.",
         rec="Ana must resolve Kenya CD situation immediately. Once fixed, Kenya is top priority."),

    dict(country="Peru", flag="🇵🇪", region="Latin America", tier=2,
         cd="Ralph Cabezas", cd_tenure="10+ yrs", mentors=6,
         fy25=297, fy26=800,
         m_align=3, socio=3, volume=3, digital=3, mkt=6.0,
         cd_score=3, program=3, legal=3, risk=3, ops=7.0, total=13.0,
         action="Targeted investment — city decision needed",
         iso="PER", lat=-9.2, lon=-75.0,
         working="CETPRO govt vocational schools as partners. Long-tenured CD.",
         not_working="CD based in wrong city. Trujillo may not be right market.",
         ceiling="Good ceiling if city decision resolved. Lima could 3x addressable partnerships.",
         key_risk="City location — Trujillo limiting partnership opportunity.",
         rec="Make city decision before scaling. Research Lima vs Trujillo vs Cusco."),

    dict(country="Cambodia", flag="🇰🇭", region="Asia", tier=2,
         cd="Kaknika Sovann", cd_tenure="5 yrs", mentors=12,
         fy25=1290, fy26=1650,
         m_align=3, socio=3, volume=3, digital=3, mkt=6.0,
         cd_score=3, program=4, legal=2, risk=3, ops=6.0, total=12.0,
         action="Targeted — legal entity check first",
         iso="KHM", lat=12.6, lon=105.0,
         working="Performing well given accidental merger. Materials in Khmer. Don Bosco starting.",
         not_working="Dispersed across 4 cities. Legal entity may block revenue partnerships.",
         ceiling="3,000+ socios/yr with consolidated ops and 2–3 strong partners.",
         key_risk="Legal entity — may need second entity for revenue collection.",
         rec="Resolve legal structure first. Consolidate to Phnom Penh. Pursue ACLEDA as anchor."),

    dict(country="Honduras", flag="🇭🇳", region="Latin America", tier=3,
         cd="Denis Turcios", cd_tenure="1 yr (20+ w/org)", mentors=5,
         fy25=57, fy26=425,
         m_align=2, socio=2, volume=2, digital=2, mkt=4.0,
         cd_score=2, program=3, legal=2, risk=3, ops=5.0, total=9.0,
         action="Stabilize — too early for partnership push",
         iso="HND", lat=15.2, lon=-86.2,
         working="Peter visited — 2/3 MFIs said yes immediately. LDS Central America Pilot active.",
         not_working="Only 5 mentors — too small to absorb partnerships. Started April 2025.",
         ceiling="Low currently. Needs 12–18 months of building before partnerships.",
         key_risk="Too small to absorb partnerships meaningfully.",
         rec="Stabilize. Build mentor capacity to 10–12 before any major partnership push."),

    dict(country="Guatemala", flag="🇬🇹", region="Latin America", tier=3,
         cd="Dario Lorenzana", cd_tenure="10+ yrs", mentors=3,
         fy25=271, fy26=525,
         m_align=2, socio=2, volume=2, digital=2, mkt=4.0,
         cd_score=2, program=2, legal=2, risk=3, ops=5.0, total=9.0,
         action="Stabilize — CD capability gap blocking growth",
         iso="GTM", lat=15.8, lon=-90.2,
         working="Donor interest is high. International Samaritan recovering. WFP partnership exists.",
         not_working="CD is educator who cannot pitch partnerships. Only 3 mentors.",
         ceiling="Good ceiling IF leadership resolved. Guatemala City has large NGO ecosystem.",
         key_risk="CD capability — educator profile cannot pitch.",
         rec="Address leadership before investing in research. This is a people problem not a market problem."),

    dict(country="Malawi", flag="🇲🇼", region="Africa", tier=3,
         cd="Lameck Chisale", cd_tenure="5 yrs", mentors=7,
         fy25=90, fy26=450,
         m_align=2, socio=2, volume=2, digital=2, mkt=4.0,
         cd_score=3, program=4, legal=2, risk=3, ops=6.0, total=10.0,
         action="Stabilize — market fit uncertain",
         iso="MWI", lat=-13.3, lon=34.3,
         working="Strong CD. Govt approved NGO list is ready-made partner pipeline.",
         not_working="80% of population are subsistence farmers — not Mentors' segment.",
         ceiling="Low given market profile. Urban micro-business ecosystem much smaller than LATAM.",
         key_risk="Market fit — may lack sufficient urban micro-entrepreneur density.",
         rec="Stabilize. Confirm market fit via CD interview before investing."),

    dict(country="Ghana", flag="🇬🇭", region="Africa", tier=3,
         cd="Emmanuella Gyamfi", cd_tenure="1 yr", mentors=11,
         fy25=123, fy26=360,
         m_align=2, socio=2, volume=2, digital=2, mkt=4.0,
         cd_score=2, program=2, legal=2, risk=3, ops=5.0, total=9.0,
         action="Stabilize — too new to business mentoring",
         iso="GHA", lat=7.9, lon=-1.0,
         working="OI and LBH Agritech pilots running. 11 mentors. Accra has growing ecosystem.",
         not_working="Switched from MFI model Jan 2026. CD departing May 30 — no replacement.",
         ceiling="Moderate if stabilized. Accra has good international NGO presence.",
         key_risk="Leadership transition — CD departing with no replacement confirmed.",
         rec="Replacement CD is urgent. OI pilot must continue regardless."),

    dict(country="Cape Verde", flag="🇨🇻", region="Africa", tier=3,
         cd="Monica Cardoso (departing)", cd_tenure="3 yrs", mentors=5,
         fy25=415, fy26=600,
         m_align=1, socio=1, volume=1, digital=2, mkt=3.0,
         cd_score=1, program=1, legal=1, risk=3, ops=3.0, total=6.0,
         action="Exit — deprioritize immediately",
         iso="CPV", lat=16.5, lon=-23.0,
         working="Monica well-networked locally. 76% business survival rate in Giving Machine.",
         not_working="Too small. Too remote. CD departing. No strategic rationale.",
         ceiling="Max 600–800 socios/yr even with perfect execution.",
         key_risk="Everything — scale, location, leadership, strategic fit.",
         rec="Deprioritize immediately. Close if no CD found by end of summer. Redirect resources to Kenya/Cambodia."),
])

partners = pd.DataFrame([
    dict(country="Mexico", org="DIF Municipal Network", type="Government", priority="HIGH", partner_type="Volume", fit="Already proven — expand to more municipalities in Yucatan & Chiapas"),
    dict(country="Mexico", org="Heifer International", type="NGO", priority="HIGH", partner_type="Volume", fit="Active 200-person project. Strong mission alignment. Renewal every 6 months."),
    dict(country="Mexico", org="CEMEX", type="Corporate CSR", priority="HIGH", partner_type="Combo", fit="Peter's contact. Pilot worked. Needs three-party funding model."),
    dict(country="Mexico", org="Coppel Foundation", type="Corporate CSR", priority="MEDIUM", partner_type="Volume", fit="Major retailer serving low-income families. Active social investment arm."),
    dict(country="Mexico", org="Pro Mujer Mexico", type="MFI", priority="HIGH", partner_type="Volume", fit="Peter named Pro Mujer as ideal LATAM partner."),
    dict(country="Mexico", org="Compartamos Banco", type="MFI/Bank", priority="HIGH", partner_type="Volume + Revenue", fit="Largest microfinance bank in Mexico. 3M+ clients. Financial education mandate."),
    dict(country="Colombia", org="Other Colombian Banks", type="Banking", priority="HIGH", partner_type="Revenue", fit="Banking regulation may require financial education — research compliance obligations."),
    dict(country="Colombia", org="Colombian MFIs", type="MFI", priority="HIGH", partner_type="Volume + Partial Revenue", fit="Dozens of MFIs in Colombia. Cannot pay full cost but could contribute."),
    dict(country="Colombia", org="Coomeva", type="Corporate", priority="MEDIUM", partner_type="Volume", fit="Ana mentioned previous small partnerships. Explore reactivation."),
    dict(country="Dominican Republic", org="ECLOF Dominican Republic", type="MFI", priority="HIGH", partner_type="Volume + Revenue", fit="Just landed. First MFI in DR. Serves micro-entrepreneurs with small loans."),
    dict(country="Dominican Republic", org="LDS Welfare and Self-Reliance", type="Faith-based", priority="HIGH", partner_type="Volume + Revenue", fit="3x renewals. Proven. Pursue expansion."),
    dict(country="Dominican Republic", org="Catholic Charities Centro de Esperanza", type="NGO", priority="MEDIUM", partner_type="Combo", fit="Women exiting exploitation. Perfect mission alignment."),
    dict(country="Nicaragua", org="Millicom (TIGO parent)", type="Telecom — Global", priority="HIGH", partner_type="Volume — Multi-country", fit="TIGO operates across 9 LATAM+Africa countries. Corporate deal unlocks multiple markets."),
    dict(country="Nicaragua", org="Opportunity International", type="MFI", priority="HIGH", partner_type="Volume", fit="Already active. Strong mission alignment."),
    dict(country="Nicaragua", org="World Vision Nicaragua", type="NGO", priority="MEDIUM", partner_type="Volume", fit="Active partner. Pursue referrals into wider network."),
    dict(country="Kenya", org="World Vision Kenya", type="NGO", priority="HIGH", partner_type="Volume", fit="In development. Large and well-resourced. Transformative if landed."),
    dict(country="Kenya", org="Kenya Women Microfinance Bank", type="MFI", priority="HIGH", partner_type="Volume + Revenue", fit="900,000 clients. Largest women-focused MFI in Kenya. Perfect alignment."),
    dict(country="Kenya", org="Equity Bank Foundation", type="Banking/CSR", priority="HIGH", partner_type="Combo", fit="Large social investment arm focused on financial inclusion."),
    dict(country="Peru", org="CETPROs (Govt Vocational Centers)", type="Government", priority="HIGH", partner_type="Volume", fit="Already partners. Graduates have skills and want to start businesses."),
    dict(country="Peru", org="Pro Mujer Peru", type="MFI", priority="HIGH", partner_type="Volume", fit="Peter named Pro Mujer as ideal LATAM partner."),
    dict(country="Cambodia", org="ACLEDA Bank", type="MFI/Bank", priority="HIGH", partner_type="Volume + Revenue", fit="Largest MFI in Cambodia. 400,000+ borrowers. Strong revenue potential."),
    dict(country="Cambodia", org="Don Bosco Cambodia", type="Faith-based NGO", priority="HIGH", partner_type="Volume", fit="Already starting. Don Bosco in 130+ countries globally."),
    dict(country="Honduras", org="MFIs in San Pedro Sula", type="MFI", priority="HIGH", partner_type="Volume", fit="Peter visited — 2/3 said yes immediately. Pursue once capacity exists."),
    dict(country="Honduras", org="Red Cross Choloma", type="NGO", priority="MEDIUM", partner_type="Volume", fit="Developing partnership. Proven entry point."),
    dict(country="Ghana", org="Opportunity International Ghana", type="MFI", priority="HIGH", partner_type="Volume", fit="Already piloting. Large and well-resourced globally."),
    dict(country="Malawi", org="Vision Fund Malawi", type="MFI", priority="MEDIUM", partner_type="Volume", fit="Already a Giving Machine partner. Explore mentoring partnership."),
])

# ── SIDEBAR ───────────────────────────────────────────────────────────────────

st.sidebar.markdown("## 🌍 Mentors International")
st.sidebar.markdown("**Country Growth Dashboard**")
st.sidebar.markdown("UCLA Anderson SICC | April 2026")
st.sidebar.markdown("---")
page = st.sidebar.radio("Navigate", [
    "Overview",
    "Country Map",
    "Scoring Table",
    "Country Briefs",
    "Partner Pipeline",
    "Recommendations"
])
st.sidebar.markdown("---")
st.sidebar.caption("Working Document — Update as research progresses")

TIER_COLOR = {1: "#27AE60", 2: "#F39C12", 3: "#E74C3C"}
TIER_LABEL = {1: "Tier 1 — Invest", 2: "Tier 2 — Targeted", 3: "Tier 3 — Stabilize/Exit"}

# ── PAGE 1: OVERVIEW ──────────────────────────────────────────────────────────

if page == "Overview":
    st.title("Mentors International — Organization Overview")
    st.caption("US-based 501(c)(3) nonprofit | Founded 1990 | Economic Development & Employment")
    st.markdown("---")

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Countries", "12")
    col2.metric("Families Served (FY25)", "24,074")
    col3.metric("Field Mentors", "250+")
    col4.metric("Annual Budget", "$4.77M")
    col5.metric("2030 Goal", "100,000")

    st.markdown("---")
    col_l, col_r = st.columns(2)

    with col_l:
        st.subheader("What Mentors Does")
        st.markdown("""
Mentors International trains and mentors micro-entrepreneurs — small business owners in developing markets —
to help them grow stable, sustainable livelihoods.

Programs are delivered through local field teams and implementation partners across **12 countries**.

**Three Programs:**
- **Entrepreneur Training** (core) — 17,144 trained in FY25
- **Catalyst Program** — established businesses in LATAM
- **Vocational Training** — 7,000 graduates in FY25

**Key Outcomes:** 29% average income increase | 54% savings increase
        """)

    with col_r:
        st.subheader("The Core Problem")
        st.markdown("""
Mentors wants to grow from **24,000 → 100,000 families by 2030**.

The challenge: approximately **60–80% of current volume** comes from a single partner relationship.
This is a critical concentration risk.

**This project answers:**
> *Which of the 12 countries offer the best opportunities to diversify and grow — and what should Mentors do first?*
        """)

    st.markdown("---")
    st.subheader("Country Portfolio at a Glance")
    tier_counts = countries.groupby("tier").size().reset_index(name="count")
    tier_counts["label"] = tier_counts["tier"].map(TIER_LABEL)
    tier_counts["color"] = tier_counts["tier"].map(TIER_COLOR)

    col1, col2, col3 = st.columns(3)
    t1 = countries[countries.tier == 1]
    t2 = countries[countries.tier == 2]
    t3 = countries[countries.tier == 3]

    with col1:
        st.markdown("### 🟢 Tier 1 — Invest & Accelerate")
        for _, r in t1.iterrows():
            st.markdown(f"**{r.flag} {r.country}** — Score: {r.total}/20")
    with col2:
        st.markdown("### 🟡 Tier 2 — Targeted Investment")
        for _, r in t2.iterrows():
            st.markdown(f"**{r.flag} {r.country}** — Score: {r.total}/20")
    with col3:
        st.markdown("### 🔴 Tier 3 — Stabilize / Exit")
        for _, r in t3.iterrows():
            st.markdown(f"**{r.flag} {r.country}** — Score: {r.total}/20")

# ── PAGE 2: COUNTRY MAP ───────────────────────────────────────────────────────

elif page == "Country Map":
    st.title("Country Map — 12 Countries")
    st.caption("Color = Tier | Size = FY25 volume | Click a country for details")
    st.markdown("---")

    countries["tier_label"] = countries["tier"].map(TIER_LABEL)
    countries["color"] = countries["tier"].map(TIER_COLOR)
    countries["label"] = countries.apply(lambda r: f"{r.flag} {r.country}<br>Score: {r.total}/20<br>FY25: {r.fy25:,}", axis=1)

    fig = px.scatter_geo(
        countries,
        lat="lat", lon="lon",
        color="tier_label",
        size="fy25",
        size_max=40,
        hover_name="country",
        hover_data={"fy25": True, "total": True, "action": True, "lat": False, "lon": False, "tier_label": False},
        color_discrete_map={
            "Tier 1 — Invest": "#27AE60",
            "Tier 2 — Targeted": "#F39C12",
            "Tier 3 — Stabilize/Exit": "#E74C3C"
        },
        text="flag",
        projection="natural earth",
    )
    fig.update_traces(textposition="top center", textfont=dict(size=16))
    fig.update_layout(
        height=550,
        margin=dict(l=0, r=0, t=0, b=0),
        legend=dict(title="Tier", orientation="h", y=-0.05),
        geo=dict(showframe=False, showcoastlines=True, coastlinecolor="#ccc",
                 landcolor="#f5f5f0", showocean=True, oceancolor="#d6eaf8")
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total FY25 Families", f"{countries.fy25.sum():,}")
    col2.metric("Total FY26 Target", f"{countries.fy26.sum():,}")
    growth = ((countries.fy26.sum() - countries.fy25.sum()) / countries.fy25.sum() * 100)
    col3.metric("Target Growth", f"+{growth:.0f}%")

# ── PAGE 3: SCORING TABLE ─────────────────────────────────────────────────────

elif page == "Scoring Table":
    st.title("Master Scoring Table — All 12 Countries")
    st.caption("Market Opportunity (out of 10) + Operational Readiness (out of 10) = Total out of 20")
    st.markdown("---")

    sort_by = st.selectbox("Sort by", ["Total Score", "Market Score", "Ops Score", "FY25 Volume", "Country"])
    sort_map = {"Total Score": "total", "Market Score": "mkt", "Ops Score": "ops",
                "FY25 Volume": "fy25", "Country": "country"}

    display = countries.sort_values(sort_map[sort_by], ascending=(sort_by == "Country")).copy()

    def tier_badge(t):
        colors = {1: "🟢", 2: "🟡", 3: "🔴"}
        return colors.get(t, "")

    display["Tier"] = display["tier"].apply(lambda t: f"{tier_badge(t)} {t}")
    display["Country"] = display.apply(lambda r: f"{r.flag} {r.country}", axis=1)
    display["Market Score"] = display["mkt"].apply(lambda x: f"{x}/10")
    display["Ops Score"] = display["ops"].apply(lambda x: f"{x}/10")
    display["Total"] = display["total"].apply(lambda x: f"{x}/20")
    display["FY25"] = display["fy25"].apply(lambda x: f"{x:,}")
    display["FY26 Target"] = display["fy26"].apply(lambda x: f"{x:,}")

    st.dataframe(
        display[["Country", "Tier", "Market Score", "Ops Score", "Total",
                 "FY25", "FY26 Target", "action"]].rename(columns={"action": "Priority Action"}),
        use_container_width=True, hide_index=True
    )

    st.markdown("---")
    st.subheader("Score Breakdown — All Criteria")

    fig = go.Figure()
    criteria = ["m_align", "socio", "volume", "digital", "cd_score", "program", "legal", "risk"]
    labels = ["Mission Align", "Socio Density", "Volume Potential", "Digital Readiness",
              "CD Strength", "Program Std.", "Legal Entity", "Political Risk"]

    for _, row in countries.sort_values("total", ascending=False).iterrows():
        fig.add_trace(go.Bar(
            name=f"{row.flag} {row.country}",
            x=labels,
            y=[row[c] for c in criteria],
            text=[row[c] for c in criteria],
            textposition="auto"
        ))

    fig.update_layout(
        barmode="group", height=450,
        xaxis_title="Criterion", yaxis_title="Score (1–5)",
        yaxis=dict(range=[0, 5.5]),
        legend=dict(orientation="h", y=-0.3)
    )
    st.plotly_chart(fig, use_container_width=True)

# ── PAGE 4: COUNTRY BRIEFS ────────────────────────────────────────────────────

elif page == "Country Briefs":
    st.title("Country Briefs")
    st.caption("Select a country to view the full brief")
    st.markdown("---")

    options = [f"{r.flag} {r.country}" for _, r in countries.sort_values("total", ascending=False).iterrows()]
    selected = st.selectbox("Select Country", options)
    country_name = selected.split(" ", 1)[1]
    r = countries[countries.country == country_name].iloc[0]

    tier_color = TIER_COLOR[r.tier]
    st.markdown(f"## {r.flag} {r.country} &nbsp;&nbsp; <span style='background:{tier_color};color:white;padding:4px 12px;border-radius:6px;font-size:0.9rem'>{TIER_LABEL[r.tier]}</span>", unsafe_allow_html=True)
    st.markdown(f"*{r.action}*")
    st.markdown("---")

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Market Score", f"{r.mkt}/10")
    col2.metric("Ops Score", f"{r.ops}/10")
    col3.metric("Total Score", f"{r.total}/20")
    col4.metric("FY25 Families", f"{r.fy25:,}")
    col5.metric("FY26 Target", f"{r.fy26:,}")

    st.markdown("---")
    col_l, col_r = st.columns(2)

    with col_l:
        st.subheader("📊 Market Opportunity")
        st.markdown(f"- **Mission Alignment:** {r.m_align}/5")
        st.markdown(f"- **Socio Profile Fit & Density:** {r.socio}/5")
        st.markdown(f"- **Volume & Renewal Potential:** {r.volume}/5")
        st.markdown(f"- **Digital Readiness:** {r.digital}/5")

        st.subheader("⚙️ Operational Readiness")
        st.markdown(f"- **CD Strength:** {r.cd_score}/5  ({r.cd}, {r.cd_tenure})")
        st.markdown(f"- **Program Standardization:** {r.program}/5")
        st.markdown(f"- **Legal Entity Structure:** {r.legal}/5")
        st.markdown(f"- **Political Risk:** {r.risk}/5")

    with col_r:
        st.subheader("✅ What Is Working")
        st.info(r.working)

        st.subheader("⚠️ What Is Not Working")
        st.warning(r.not_working)

        st.subheader("📈 Growth Ceiling")
        st.success(r.ceiling)

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🚨 Key Risk")
        st.error(r.key_risk)
    with col2:
        st.subheader("💡 Recommendation")
        st.markdown(f"> {r.rec}")

    st.markdown("---")
    st.subheader("Named Partner Opportunities")
    country_partners = partners[partners.country == country_name]
    if len(country_partners) > 0:
        st.dataframe(
            country_partners[["org", "type", "priority", "partner_type", "fit"]].rename(columns={
                "org": "Organization", "type": "Type", "priority": "Priority",
                "partner_type": "Partnership Type", "fit": "Why a Fit"
            }),
            use_container_width=True, hide_index=True
        )
    else:
        st.caption("Research in progress — partners to be added.")

# ── PAGE 5: PARTNER PIPELINE ──────────────────────────────────────────────────

elif page == "Partner Pipeline":
    st.title("Partner Pipeline — All Named Opportunities")
    st.caption("All partner opportunities across 12 countries")
    st.markdown("---")

    col1, col2 = st.columns(2)
    country_filter = col1.multiselect("Filter by Country", sorted(partners.country.unique()), default=sorted(partners.country.unique()))
    priority_filter = col2.multiselect("Filter by Priority", ["HIGH", "MEDIUM", "LOW"], default=["HIGH", "MEDIUM"])

    filtered = partners[partners.country.isin(country_filter) & partners.priority.isin(priority_filter)]

    st.markdown(f"**{len(filtered)} opportunities** matching filters")
    st.dataframe(
        filtered[["country", "org", "type", "priority", "partner_type", "fit"]].rename(columns={
            "country": "Country", "org": "Organization", "type": "Type",
            "priority": "Priority", "partner_type": "Partnership Type", "fit": "Why a Fit"
        }).sort_values(["Country", "Priority"]),
        use_container_width=True, hide_index=True
    )

    st.markdown("---")
    st.subheader("Partners by Country")
    partner_counts = partners.groupby("country").size().reset_index(name="count")
    fig = px.bar(partner_counts.sort_values("count", ascending=True),
                 x="count", y="country", orientation="h",
                 color="count", color_continuous_scale="Blues",
                 labels={"count": "Named Partners", "country": ""})
    fig.update_layout(height=400, showlegend=False, coloraxis_showscale=False)
    st.plotly_chart(fig, use_container_width=True)

# ── PAGE 6: RECOMMENDATIONS ───────────────────────────────────────────────────

elif page == "Recommendations":
    st.title("Strategic Recommendations")
    st.caption("Summary for Mentors International Board | April 2026")
    st.markdown("---")

    st.subheader("Portfolio Summary")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Tier 1 Countries", "4", "Invest & Accelerate")
    col2.metric("Tier 2 Countries", "3", "Targeted Investment")
    col3.metric("Tier 3 Countries", "5", "Stabilize / Exit")
    col4.metric("Exit Candidate", "1", "Cape Verde")

    st.markdown("---")

    fig = px.scatter(
        countries,
        x="mkt", y="ops",
        color="tier",
        size="fy25",
        size_max=50,
        text="flag",
        hover_name="country",
        hover_data={"total": True, "action": True, "tier": False, "mkt": True, "ops": True},
        color_discrete_map={1: "#27AE60", 2: "#F39C12", 3: "#E74C3C"},
        labels={"mkt": "Market Opportunity Score (out of 10)", "ops": "Operational Readiness Score (out of 10)", "tier": "Tier"}
    )
    fig.update_traces(textposition="top center", textfont=dict(size=18))
    fig.add_hline(y=7, line_dash="dot", line_color="gray", annotation_text="Ops threshold")
    fig.add_vline(x=7, line_dash="dot", line_color="gray", annotation_text="Market threshold")
    fig.update_layout(height=500, title="Country Positioning — Market vs Operational Readiness")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    st.subheader("🟢 Tier 1 — Invest & Accelerate Now")
    for _, r in countries[countries.tier == 1].sort_values("total", ascending=False).iterrows():
        with st.expander(f"{r.flag} {r.country} — Score: {r.total}/20"):
            st.markdown(f"**Action:** {r.action}")
            st.markdown(f"**Recommendation:** {r.rec}")

    st.subheader("🟡 Tier 2 — Targeted Investment (Resolve Blockers First)")
    for _, r in countries[countries.tier == 2].sort_values("total", ascending=False).iterrows():
        with st.expander(f"{r.flag} {r.country} — Score: {r.total}/20"):
            st.markdown(f"**Action:** {r.action}")
            st.markdown(f"**Key Blocker:** {r.key_risk}")
            st.markdown(f"**Recommendation:** {r.rec}")

    st.subheader("🔴 Tier 3 — Stabilize or Exit")
    for _, r in countries[countries.tier == 3].sort_values("total", ascending=False).iterrows():
        with st.expander(f"{r.flag} {r.country} — Score: {r.total}/20"):
            st.markdown(f"**Action:** {r.action}")
            st.markdown(f"**Recommendation:** {r.rec}")

    st.markdown("---")
    st.subheader("Top 3 Immediate Actions for Mentors")
    st.markdown("""
1. **Diversify Colombia urgently** — 90% concentration in Bancolombia is an existential risk. Research banking compliance obligations and pursue 3–5 smaller partners now.
2. **Resolve Kenya CD situation** — Kenya has the highest market potential per dollar of investment. A full-time CD unlocks 3,000–5,000 socios/yr in Nairobi alone.
3. **Pursue Millicom at the corporate level** — TIGO Nicaragua is the best partnership model in the network. Millicom operates across 9 countries. One corporate deal could replicate the flywheel across multiple markets simultaneously.
    """)
