import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Mentors International — Growth Strategy",
    page_icon="🌍",
    layout="wide"
)

# ── BRAND ─────────────────────────────────────────────────────────────────────
NAVY  = "#1B2A4A"
GREEN = "#27AE60"
GOLD  = "#D4A843"
TEAL  = "#028090"
RED   = "#E74C3C"
AMBER = "#F39C12"
WHITE = "#FFFFFF"
LGREY = "#F4F6F9"
MGREY = "#64748B"
DGREY = "#2D3748"

LOGO_URI = "data:image/png;base64,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"

st.markdown(f"""
<style>
/* ── Cards ── */
.card {{
    background: #FFFFFF;
    border-radius: 10px;
    padding: 1rem 1.2rem;
    border-left: 4px solid {GREEN};
    box-shadow: 0 2px 10px rgba(0,0,0,0.07);
    margin-bottom: 0.75rem;
}}
.card-dark {{
    background: linear-gradient(135deg, {NAVY} 0%, #243B6E 100%);
    border-radius: 10px;
    padding: 1rem 1.2rem;
    color: #FFFFFF;
    margin-bottom: 0.75rem;
    box-shadow: 0 4px 16px rgba(27,42,74,0.25);
}}
.card-gold {{
    background: linear-gradient(135deg, #FFFBF0 0%, #FEF3D0 100%);
    border-radius: 10px;
    padding: 1rem 1.2rem;
    border-left: 4px solid {GOLD};
    margin-bottom: 0.75rem;
}}
.card-red {{
    background: linear-gradient(135deg, #FEF0F0 0%, #FDDEDE 100%);
    border-radius: 10px;
    padding: 1rem 1.2rem;
    border-left: 4px solid {RED};
    margin-bottom: 0.75rem;
}}
.card-teal {{
    background: linear-gradient(135deg, #EBF8FA 0%, #D4F1F4 100%);
    border-radius: 10px;
    padding: 1rem 1.2rem;
    border-left: 4px solid {TEAL};
    margin-bottom: 0.75rem;
}}
/* ── Stat grid layout ── */
.stat-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 12px;
    margin: 0.8rem 0 1rem 0;
}}
/* ── Stat number boxes ── */
.stat-box {{
    background: #FFFFFF;
    border-radius: 10px;
    padding: 1rem 0.8rem;
    text-align: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.07);
}}
.stat-val {{
    font-size: 1.85rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 4px;
}}
.stat-label {{
    font-size: 0.73rem;
    color: {MGREY};
    line-height: 1.35;
}}
.stat-delta {{
    font-size: 0.67rem;
    color: {GREEN};
    font-weight: 600;
    margin-top: 4px;
}}
/* ── Page banner ── */
.banner {{
    background: linear-gradient(135deg, {NAVY} 0%, #243B6E 100%);
    border-radius: 12px;
    padding: 1.3rem 1.6rem;
    margin-bottom: 1.2rem;
    border-bottom: 3px solid {GREEN};
}}
/* ── Quote ── */
.quote {{
    background: #EEF4FB;
    border-left: 3px solid {NAVY};
    padding: 10px 14px;
    border-radius: 0 8px 8px 0;
    font-style: italic;
    color: {NAVY};
    font-size: 0.88rem;
    margin: 7px 0;
    line-height: 1.5;
}}
/* ── Section label ── */
.section-label {{
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 2px;
    color: {GREEN};
    text-transform: uppercase;
    margin-bottom: 6px;
    display: block;
}}
/* ── Gradient divider ── */
.mi-divider {{
    height: 2px;
    background: linear-gradient(90deg, {GREEN} 0%, {TEAL} 60%, transparent 100%);
    border: none;
    margin: 1rem 0;
    border-radius: 2px;
}}
/* ── Sidebar ── */
[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, #0D1B2E 0%, {NAVY} 60%, #0D1B2E 100%);
    box-shadow: 4px 0 20px rgba(0,0,0,0.25);
}}
[data-testid="stSidebar"] * {{ color: #FFFFFF !important; }}
[data-testid="stSidebar"] .stRadio > label {{ display: none; }}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {{
    color: #CADCFC !important;
    font-size: 0.85rem;
    padding: 5px 0;
}}
/* ── Main layout ── */
.block-container {{
    padding-top: 1rem !important;
    padding-bottom: 2rem;
    max-width: 1200px;
}}
h1 {{ color: {NAVY}; font-size: 1.55rem; margin-bottom: 0.15rem; font-weight: 700; }}
h2 {{ color: {NAVY}; font-size: 1.2rem; }}
h3 {{ color: {NAVY}; font-size: 1rem; }}
[data-testid="stDataFrame"] table {{ font-size: 0.82rem; }}
[data-testid="stExpander"] {{
    border: 1px solid #E2E8F0;
    border-radius: 8px;
    margin-bottom: 6px;
}}
</style>
""", unsafe_allow_html=True)

def page_header(title, subtitle=None, badge=None):
    """Branded page header built with string concatenation — avoids f-string + base64 conflict."""
    badge_html = (
        '<span style="background:' + GREEN + '; color:white; padding:3px 12px;'
        ' border-radius:20px; font-size:0.7rem; font-weight:700; letter-spacing:1px;">'
        + badge + '</span>'
    ) if badge else ""
    sub_html = (
        '<div style="font-size:0.75rem; color:#CADCFC; margin-top:2px;">'
        + subtitle + '</div>'
    ) if subtitle else ""
    html = (
        '<div style="background:linear-gradient(135deg,' + NAVY + ' 0%,#243B6E 100%);'
        ' border-radius:12px; padding:1rem 1.4rem; margin-bottom:1.2rem;'
        ' border-bottom:3px solid ' + GREEN + ';'
        ' display:flex; align-items:center; justify-content:space-between;'
        ' box-shadow:0 4px 16px rgba(27,42,74,0.2);">'
        '<div style="display:flex; align-items:center; gap:14px;">'
        '<img src="' + LOGO_URI + '" height="34"'
        ' style="display:block; filter:brightness(0) invert(1);"'
        ' alt="Mentors International"/>'
        '<div>'
        '<div style="font-size:1.15rem; font-weight:700; color:white;">' + title + '</div>'
        + sub_html +
        '</div>'
        '</div>'
        '<div style="display:flex; align-items:center; gap:10px;">'
        + badge_html +
        '<div style="text-align:right;">'
        '<div style="font-size:0.68rem; color:#CADCFC; font-weight:600;">UCLA Anderson SICC</div>'
        '<div style="font-size:0.65rem; color:#64748B;">Spring 2026</div>'
        '</div></div></div>'
    )
    st.markdown(html, unsafe_allow_html=True)

def stat_card(val, label, delta=None, color=None):
    color = color or GREEN
    delta_html = f'<div class="stat-delta">{delta}</div>' if delta else ""
    return (
        f'<div class="stat-box" style="border-top:3px solid {color};">' +
        f'<div class="stat-val" style="color:{color};">{val}</div>' +
        f'<div class="stat-label">{label}</div>' +
        delta_html +
        '</div>'
    )

def divider():
    st.markdown('<div class="mi-divider">&nbsp;</div>', unsafe_allow_html=True)

def section(label):
    st.markdown(f'<div class="section-label">{label}</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# DATA
# ══════════════════════════════════════════════════════════════════════════════
countries = pd.DataFrame([
  dict(country="Colombia",flag="🇨🇴",region="Latin America",tier=1,
       cd="Andrea Arenas",cd_tenure="2 yrs (6+ w/org)",mentors=90,
       fy25=20875,fy26=16000,mkt=9.0,ops=10.0,total=19.0,
       m_align=4,socio=5,volume=5,digital=5,cd_score=5,program=5,legal=5,risk=4,
       lat=4.6,lon=-74.3,
       action="Diversify within Colombia — urgently",
       working="Best ops team. 100% virtual. 90+ mentors. Banking regulation enables revenue partnerships.",
       not_working="~50% of global volume from Bancolombia alone. Declining 20k→16k.",
       ceiling="50,000+ socios/yr with 3–4 banking partnerships.",
       risk_note="Bancolombia concentration — single partner = existential risk.",
       rec="Research Colombian banking compliance law. Pursue Bancamía, Banco Mundo Mujer, Interactuar this quarter.",
       cd_interview=False,
       ecosystem="Multiple 5-alignment orgs across MFIs + NGOs. Rare combo."),
  dict(country="Mexico",flag="🇲🇽",region="Latin America",tier=1,
       cd="Zoram Varguez",cd_tenure="10+ yrs",mentors=11,
       fy25=614,fy26=1000,mkt=9.0,ops=9.0,total=18.0,
       m_align=4,socio=4,volume=5,digital=4,cd_score=5,program=5,legal=4,risk=4,
       lat=23.6,lon=-102.5,
       action="Invest + accelerate — highest ceiling in the network",
       working="DIF govt partnerships active. Heifer International live. ICATEY vocational pipeline. CD tech-forward.",
       not_working="Socio profile drift risk — must stay anchored in Chiapas & Yucatan south.",
       ceiling="5,000+ socios/yr with 3–4 strong partnerships.",
       risk_note="Socio profile drift into middle-class families.",
       rec="ICATEY + Heifer are the model. Pursue DIF expansion, CEMEX combo, Pro Mujer Mexico.",
       cd_interview=True,
       ecosystem="Strong 5-alignment NGOs (CREA, ProEmpleo) paired with massive scale players."),
  dict(country="Dominican Republic",flag="🇩🇴",region="Latin America",tier=1,
       cd="Ruth Martes",cd_tenure="6 yrs",mentors=8,
       fy25=169,fy26=836,mkt=8.0,ops=8.0,total=15.0,
       m_align=4,socio=3,volume=4,digital=4,cd_score=4,program=4,legal=3,risk=4,
       lat=18.7,lon=-70.2,
       action="Invest + accelerate — combo model pilot candidate",
       working="LDS Church renewing 3x. ECLOF MFI active. Densest 5-alignment MFI ecosystem globally.",
       not_working="Small island — scale ceiling is real.",
       ceiling="1,500–2,000 socios/yr. Quality over scale.",
       risk_note="Volume ceiling — small country.",
       rec="Use DR as combo model test. ADOPEM, Esperanza International, BANFONDESA are top targets.",
       cd_interview=False,
       ecosystem="Extremely dense 5-alignment MFI ecosystem. ADOPEM, BANFONDESA, Esperanza."),
  dict(country="Nicaragua",flag="🇳🇮",region="Latin America",tier=1,
       cd="Pio Quintero",cd_tenure="10+ yrs",mentors=10,
       fy25=490,fy26=1000,mkt=6.0,ops=7.0,total=13.0,
       m_align=3,socio=3,volume=3,digital=3,cd_score=5,program=4,legal=4,risk=2,
       lat=12.9,lon=-85.2,
       action="Protect & leverage — political risk real but Pio is exceptional",
       working="TIGO flywheel is the network template. Pio is the strongest CD in LATAM.",
       not_working="Govt forcing NGOs to close. Cannot convene NGOs publicly.",
       ceiling="1,500–2,000 socios/yr given political constraints.",
       risk_note="US NGO activity increasingly restricted by Nicaraguan government.",
       rec="Pursue Millicom (TIGO parent) at corporate level — 9 LATAM+Africa countries. Protect existing.",
       cd_interview=False,
       ecosystem="High alignment on paper but many orgs forced to close by government."),
  dict(country="Kenya",flag="🇰🇪",region="Africa",tier=2,
       cd="Eric Onyango",cd_tenure="4 yrs",mentors=7,
       fy25=592,fy26=600,mkt=7.0,ops=6.0,total=13.0,
       m_align=4,socio=4,volume=4,digital=3,cd_score=3,program=4,legal=4,risk=3,
       lat=-0.0,lon=37.9,
       action="High potential — resolve CD full-time commitment first",
       working="Best NGO ecosystem in Africa. World Vision MOU imminent. 82% socio graduation rate.",
       not_working="CD has a part-time job. Cold outreach fails — people expect money from NGOs.",
       ceiling="3,000–5,000 socios/yr if CD goes full-time.",
       risk_note="CD part-time commitment — single biggest constraint on all Kenya growth.",
       rec="Ana must resolve CD situation immediately. Hand in Hand EA, SHOFCO, IRC Re:BUILD are top targets.",
       cd_interview=True,
       ecosystem="Best mix in Africa: high-alignment NGOs (Hand in Hand, SHOFCO) + scalable MFIs."),
  dict(country="Peru",flag="🇵🇪",region="Latin America",tier=2,
       cd="Ralph Cabezas",cd_tenure="10+ yrs",mentors=6,
       fy25=297,fy26=800,mkt=6.0,ops=6.0,total=12.0,
       m_align=3,socio=3,volume=3,digital=3,cd_score=3,program=3,legal=3,risk=3,
       lat=-9.2,lon=-75.0,
       action="City decision needed before further investment",
       working="CETPRO govt vocational schools active. Long-tenured CD.",
       not_working="CD in wrong city. Trujillo ecosystem smaller than Lima.",
       ceiling="Strong ceiling if Lima decision resolved.",
       risk_note="City location — Trujillo vs Lima vs Cusco unresolved.",
       rec="Make city decision first. Pro Mujer Peru + Financiera Confianza as priority partners.",
       cd_interview=False,
       ecosystem="Good 4–5 alignment orgs (Pro Mujer, Manuela Ramos). MFIs dominate."),
  dict(country="Cambodia",flag="🇰🇭",region="Asia",tier=2,
       cd="Kaknika Sovann",cd_tenure="5 yrs",mentors=12,
       fy25=1290,fy26=1650,mkt=6.0,ops=6.0,total=12.0,
       m_align=3,socio=3,volume=3,digital=3,cd_score=3,program=4,legal=2,risk=3,
       lat=12.6,lon=105.0,
       action="Legal entity check first — then ACLEDA as anchor",
       working="Performing well. Materials in Khmer. SHE Investments + Friends International are strong.",
       not_working="Dispersed across 4 cities. Legal entity may block revenue partnerships.",
       ceiling="3,000+ socios/yr with consolidated ops and 2–3 partners.",
       risk_note="Legal entity — may need separate entity to collect revenue in Cambodia.",
       rec="Resolve legal structure. Consolidate to Phnom Penh. ACLEDA Bank is the Bancolombia equivalent.",
       cd_interview=False,
       ecosystem="Less consistent. But ACLEDA, Friends International, SHE are strong anchors."),
  dict(country="Honduras",flag="🇭🇳",region="Latin America",tier=3,
       cd="Denis Turcios",cd_tenure="1 yr",mentors=5,
       fy25=57,fy26=425,mkt=4.0,ops=5.0,total=9.0,
       m_align=2,socio=2,volume=2,digital=2,cd_score=2,program=3,legal=2,risk=3,
       lat=15.2,lon=-86.2,
       action="Stabilize — build mentor capacity before partnerships",
       working="Peter visited — 2/3 MFIs said yes in one afternoon. Strong ecosystem anchors exist.",
       not_working="Only 5 mentors. Too small to absorb partnerships. Started April 2025.",
       ceiling="Low currently. 12–18 months needed.",
       risk_note="Scale — program too small to absorb partner volume.",
       rec="Build to 10–12 mentors first. ProMujer Honduras + VisionFund as future targets.",
       cd_interview=False,
       ecosystem="Thin but CDE MIPYME, Pro Mujer, VisionFund are strong 5-alignment anchors."),
  dict(country="Guatemala",flag="🇬🇹",region="Latin America",tier=3,
       cd="Dario Lorenzana",cd_tenure="10+ yrs",mentors=3,
       fy25=271,fy26=525,mkt=4.0,ops=5.0,total=9.0,
       m_align=2,socio=2,volume=2,digital=2,cd_score=2,program=2,legal=2,risk=3,
       lat=15.8,lon=-90.2,
       action="Leadership change before ecosystem investment",
       working="Strong MFIs exist (Génesis, FINCA). High donor interest.",
       not_working="CD is educator — cannot pitch. Only 3 mentors. Rural-first ecosystem.",
       ceiling="Good ceiling if leadership resolved.",
       risk_note="CD capability — educator cannot pitch. This is a people problem.",
       rec="Address CD first. Pro Mujer Guatemala + Génesis Empresarial as future anchors.",
       cd_interview=False,
       ecosystem="Strong MFIs (Génesis, FINCA). Fewer high-alignment NGOs. Many orgs are rural-first."),
  dict(country="Malawi",flag="🇲🇼",region="Africa",tier=3,
       cd="Lameck Chisale",cd_tenure="5 yrs",mentors=7,
       fy25=90,fy26=450,mkt=4.0,ops=6.0,total=10.0,
       m_align=2,socio=2,volume=2,digital=2,cd_score=3,program=4,legal=2,risk=3,
       lat=-13.3,lon=34.3,
       action="Stabilize — market fit needs confirmation",
       working="Strong CD. Govt NGO list is a ready-made pipeline. FINCA + VisionFund active.",
       not_working="80% of population agricultural — not Mentors' urban segment.",
       ceiling="Low. Urban micro-business density too thin.",
       risk_note="Market fit — may lack sufficient urban micro-entrepreneur density.",
       rec="Stabilize. FINCA Malawi and CARE Malawi are best bets via Giving Machine relationships.",
       cd_interview=False,
       ecosystem="Great need but mostly rural. A few 5-alignment orgs (FINCA, VisionFund)."),
  dict(country="Ghana",flag="🇬🇭",region="Africa",tier=3,
       cd="Emmanuella Gyamfi",cd_tenure="1 yr",mentors=11,
       fy25=123,fy26=360,mkt=4.0,ops=5.0,total=9.0,
       m_align=2,socio=2,volume=2,digital=2,cd_score=2,program=2,legal=2,risk=3,
       lat=7.9,lon=-1.0,
       action="Stabilize — new CD urgently needed",
       working="OI + LBH Agritech pilots running. 11 mentors. Sinapi Aba Trust is top ecosystem partner.",
       not_working="Switched from MFI model Jan 2026. CD departing May 30. No replacement confirmed.",
       ceiling="Moderate if stabilized. Accra has a developing ecosystem.",
       risk_note="Leadership transition — CD departing with no replacement.",
       rec="New CD is the only priority. OI pilot must continue. Data gap is core constraint.",
       cd_interview=True,
       ecosystem="One standout 5-alignment (Sinapi Aba). Most others 3–4. Fidelity Bank in conversation."),
  dict(country="Cape Verde",flag="🇨🇻",region="Africa",tier=3,
       cd="Monica Cardoso (dep.)",cd_tenure="3 yrs",mentors=5,
       fy25=415,fy26=600,mkt=3.0,ops=3.0,total=6.0,
       m_align=1,socio=1,volume=1,digital=2,cd_score=1,program=1,legal=1,risk=3,
       lat=16.5,lon=-23.0,
       action="Exit — deprioritize immediately",
       working="Monica well-networked locally. Pro Empresa is a strong anchor.",
       not_working="Too small. Too remote. CD departing. No strategic rationale.",
       ceiling="600–800 socios maximum. Not a scale market.",
       risk_note="Everything — scale, location, leadership, strategic rationale.",
       rec="Deprioritize. Close if no strong CD found by end of summer 2026.",
       cd_interview=False,
       ecosystem="Very limited. Only one true standout (Pro Empresa)."),
])

partners = pd.DataFrame([
  dict(country="Colombia",org="Bancamía",type="MFI",priority="HIGH",ptype="Volume + Revenue",fit="Large urban microentrepreneur base. Strong social mission. Research compliance obligations."),
  dict(country="Colombia",org="Banco Mundo Mujer",type="MFI",priority="HIGH",ptype="Volume + Revenue",fit="Women-focused. Excellent scale and direct pipeline."),
  dict(country="Colombia",org="Interactuar",type="NGO",priority="HIGH",ptype="Volume",fit="Best NGO fit — training, finance, mentorship combined. Longstanding urban focus."),
  dict(country="Colombia",org="Banking compliance research",type="Research",priority="HIGH",ptype="Revenue",fit="Which Colombian banks have same financial education obligation as Bancolombia? Research now."),
  dict(country="Mexico",org="Pro Mujer Mexico",type="MFI/INGO",priority="HIGH",ptype="Volume",fit="Peter named Pro Mujer as ideal LATAM partner. Approach at corporate level."),
  dict(country="Mexico",org="DIF Municipal Network",type="Government",priority="HIGH",ptype="Volume",fit="Already proven. Expand to more municipalities in Yucatan & Chiapas."),
  dict(country="Mexico",org="CEMEX",type="Corporate CSR",priority="HIGH",ptype="Combo",fit="Pilot worked. Three-party model: CEMEX + MasterCard Foundation + Mentors."),
  dict(country="Mexico",org="Fundación ProEmpleo",type="NGO",priority="HIGH",ptype="Volume",fit="Leading NGO with training + incubation. Highly aligned. National reach."),
  dict(country="Dominican Republic",org="ADOPEM",type="MFI/Women",priority="HIGH",ptype="Volume + Revenue",fit="Strongest DR partner. Women-focused. Large direct urban entrepreneur base."),
  dict(country="Dominican Republic",org="Esperanza International",type="MFI/Faith",priority="HIGH",ptype="Volume + Revenue",fit="Closest MI analogue globally. Combines lending, training, mentorship."),
  dict(country="Dominican Republic",org="BANFONDESA",type="MFI",priority="HIGH",ptype="Volume + Revenue",fit="Strong focus on underserved populations. Excellent mission alignment."),
  dict(country="Dominican Republic",org="LDS Humanitarian Program",type="Faith-based",priority="HIGH",ptype="Volume + Revenue",fit="90% of LDS budget. Serves anyone regardless of faith. NEVER approached."),
  dict(country="Nicaragua",org="Millicom / TIGO (corporate)",type="Telecom",priority="HIGH",ptype="Multi-country Volume",fit="TIGO parent. 9 LATAM+Africa countries. Replicates Nicaragua flywheel at scale."),
  dict(country="Nicaragua",org="Pro Mujer Nicaragua",type="INGO/Women",priority="HIGH",ptype="Volume",fit="Strongest MI-aligned partner globally. Credit + training + health for women."),
  dict(country="Kenya",org="Hand in Hand Eastern Africa",type="NGO",priority="HIGH",ptype="Volume",fit="Largest job-creation NGO in Kenya. Women-focused. 1,000+ socios potential."),
  dict(country="Kenya",org="SHOFCO",type="NGO",priority="HIGH",ptype="Volume",fit="Massive Kibera/Mathare footprint. Trusted community pipeline."),
  dict(country="Kenya",org="IRC Re:BUILD Program",type="INGO",priority="HIGH",ptype="Volume",fit="Large-scale. Pre-screened urban entrepreneurs. High readiness."),
  dict(country="Kenya",org="World Vision Kenya",type="INGO",priority="HIGH",ptype="Volume",fit="MOU IMMINENT after 9 months of Eric's persistence."),
  dict(country="Kenya",org="Kenya Women Microfinance Bank",type="MFI/Women",priority="HIGH",ptype="Volume + Revenue",fit="900,000 clients. Largest women-focused MFI in Kenya."),
  dict(country="Peru",org="Pro Mujer Peru",type="INGO/Women",priority="HIGH",ptype="Volume",fit="Peter named directly. One of the strongest MI-aligned partners anywhere."),
  dict(country="Peru",org="Financiera Confianza",type="MFI",priority="HIGH",ptype="Volume + Revenue",fit="Financial inclusion focus. Strong urban outreach."),
  dict(country="Cambodia",org="ACLEDA Bank",type="MFI",priority="HIGH",ptype="Volume + Revenue",fit="Dominant SME bank in urban Cambodia. The Bancolombia equivalent."),
  dict(country="Cambodia",org="Friends International",type="NGO",priority="HIGH",ptype="Volume",fit="Works with marginalized urban youth. Livelihoods + small business pathways."),
  dict(country="Ghana",org="Sinapi Aba Trust",type="MFI/Faith",priority="HIGH",ptype="Volume",fit="Best partner in Ghana. Group lending + urban pipeline. Approach after new CD hired."),
  dict(country="Honduras",org="CDE MIPYME Honduras",type="NGO",priority="MEDIUM",ptype="Volume",fit="Network of business development centers. Pre-screened pipeline."),
  dict(country="Global",org="LDS Humanitarian Program",type="Faith — Global",priority="HIGH",ptype="Multi-country",fit="90% of LDS budget. Serves anyone regardless of faith. Mentors only uses 10% Welfare arm."),
  dict(country="Global",org="MasterCard Foundation",type="Foundation",priority="HIGH",ptype="Combo funder",fit="Peter's named third-party funder for combo model. Active in Kenya, Colombia, LATAM."),
  dict(country="Global",org="Pro Mujer (LATAM corporate)",type="INGO Regional",priority="HIGH",ptype="Multi-country Volume",fit="Peter: 'A total home run.' Nicaragua, Mexico, Peru, Colombia, Bolivia. Approach centrally."),
])

ecosystem = pd.DataFrame([
  dict(country="Colombia",org="Bancamía",cat="MFI",align=5,scale=5,status="Idea"),
  dict(country="Colombia",org="Banco Mundo Mujer",cat="MFI",align=5,scale=5,status="Idea"),
  dict(country="Colombia",org="Interactuar",cat="NGO",align=5,scale=4,status="Idea"),
  dict(country="Colombia",org="Fundación WWB Colombia",cat="NGO/Women",align=5,scale=4,status="Idea"),
  dict(country="Colombia",org="Fundación Carvajal",cat="NGO",align=5,scale=4,status="Idea"),
  dict(country="Colombia",org="Banco W",cat="MFI",align=5,scale=5,status="Idea"),
  dict(country="Colombia",org="World Vision Colombia",cat="INGO",align=3,scale=4,status="In Conversation"),
  dict(country="Colombia",org="Coomeva",cat="Co-op",align=3,scale=5,status="In Conversation"),
  dict(country="Mexico",org="Pro Mujer Mexico",cat="INGO/Women",align=5,scale=4,status="Idea"),
  dict(country="Mexico",org="CREA",cat="NGO/Women",align=5,scale=3,status="Idea"),
  dict(country="Mexico",org="Fundación ProEmpleo",cat="NGO",align=5,scale=4,status="Idea"),
  dict(country="Mexico",org="VisionFund Mexico",cat="MFI/Faith",align=5,scale=4,status="Idea"),
  dict(country="Mexico",org="Financiera Independencia",cat="MFI",align=4,scale=5,status="Idea"),
  dict(country="Dominican Republic",org="ADOPEM",cat="MFI/Women",align=5,scale=5,status="Idea"),
  dict(country="Dominican Republic",org="Esperanza International",cat="MFI/Faith",align=5,scale=5,status="Idea"),
  dict(country="Dominican Republic",org="BANFONDESA",cat="MFI",align=5,scale=5,status="Idea"),
  dict(country="Dominican Republic",org="ECLOF DR",cat="MFI/Faith",align=5,scale=4,status="Active"),
  dict(country="Dominican Republic",org="Mujeres en Desarrollo",cat="NGO/Women",align=5,scale=3,status="Idea"),
  dict(country="Nicaragua",org="Banco FAMA",cat="MFI",align=5,scale=5,status="Idea"),
  dict(country="Nicaragua",org="FINCA Nicaragua",cat="MFI/INGO",align=5,scale=5,status="Idea"),
  dict(country="Nicaragua",org="Pro Mujer Nicaragua",cat="INGO/Women",align=5,scale=5,status="Idea"),
  dict(country="Kenya",org="Hand in Hand Eastern Africa",cat="NGO",align=5,scale=5,status="Idea"),
  dict(country="Kenya",org="Imagine Leaders",cat="NGO",align=4,scale=3,status="Active"),
  dict(country="Kenya",org="Pendekizoletu Organisation",cat="NGO",align=4,scale=3,status="Active"),
  dict(country="Kenya",org="World Vision Kenya",cat="INGO",align=3,scale=4,status="In Conversation"),
  dict(country="Kenya",org="SHOFCO",cat="NGO",align=4,scale=5,status="Idea"),
  dict(country="Kenya",org="IRC Re:BUILD",cat="INGO",align=4,scale=5,status="Idea"),
  dict(country="Kenya",org="Kenya Women MFB",cat="MFI/Women",align=4,scale=5,status="Idea"),
  dict(country="Kenya",org="Inkomoko",cat="NGO",align=4,scale=5,status="Idea"),
  dict(country="Peru",org="Pro Mujer Peru",cat="INGO/Women",align=5,scale=4,status="Idea"),
  dict(country="Peru",org="Movimiento Manuela Ramos",cat="NGO/Women",align=5,scale=3,status="Idea"),
  dict(country="Peru",org="FINCA Peru",cat="INGO/MFI",align=5,scale=4,status="Idea"),
  dict(country="Peru",org="Financiera Confianza",cat="MFI",align=4,scale=5,status="Idea"),
  dict(country="Cambodia",org="SHE Investments",cat="NGO/Women",align=5,scale=3,status="Idea"),
  dict(country="Cambodia",org="Friends International",cat="NGO",align=5,scale=4,status="Idea"),
  dict(country="Cambodia",org="ACLEDA Bank",cat="MFI",align=4,scale=5,status="Idea"),
  dict(country="Ghana",org="Sinapi Aba Trust",cat="MFI/Faith",align=5,scale=5,status="Idea"),
  dict(country="Ghana",org="Advans Ghana",cat="MFI",align=4,scale=5,status="Idea"),
  dict(country="Ghana",org="Fidelity Bank Ghana",cat="MFI/Corp",align=3,scale=5,status="In Conversation"),
  dict(country="Honduras",org="CDE MIPYME Honduras",cat="NGO",align=5,scale=4,status="Idea"),
  dict(country="Honduras",org="ProMujer Honduras",cat="INGO/Women",align=5,scale=4,status="Idea"),
  dict(country="Honduras",org="ODEF Financiera",cat="MFI",align=5,scale=4,status="Idea"),
  dict(country="Guatemala",org="Pro Mujer Guatemala",cat="INGO/Women",align=5,scale=4,status="Idea"),
  dict(country="Guatemala",org="Génesis Empresarial",cat="NGO/MFI",align=5,scale=5,status="Idea"),
  dict(country="Malawi",org="FINCA Malawi",cat="MFI/INGO",align=5,scale=4,status="Idea"),
  dict(country="Malawi",org="Vision Fund Malawi",cat="MFI/Faith",align=5,scale=4,status="In Conversation"),
  dict(country="Cape Verde",org="Pro Empresa Cabo Verde",cat="Government",align=5,scale=3,status="In Conversation"),
])

TC = {1:"#27AE60",2:"#F39C12",3:"#E74C3C"}
TL = {1:"Tier 1 — Invest",2:"Tier 2 — Targeted",3:"Tier 3 — Stabilize/Exit"}

# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
st.sidebar.markdown(
    '<div style="padding:1.1rem 0.6rem 0.6rem; text-align:center;">'
    '<img src="' + LOGO_URI + '" width="150"'
    ' style="filter:brightness(0) invert(1); display:inline-block;"'
    ' alt="Mentors International"/>'
    '<div style="font-size:0.62rem; color:#CADCFC; letter-spacing:1px; margin-top:8px;">'
    'GROWTH STRATEGY DASHBOARD</div>'
    '<div style="font-size:0.58rem; color:#445566; margin-top:2px;">'
    'UCLA Anderson SICC · May 2026</div>'
    '</div>'
    '<div style="height:2px; background:linear-gradient(90deg,#27AE60,#028090,transparent);'
    ' margin:0.3rem 0 0.5rem;"></div>',
    unsafe_allow_html=True
)

page = st.sidebar.radio("", [
    "🎯  Theory of Change",
    "📊  Overview",
    "🗺️  Country Map",
    "📋  Country Briefs",
    "🤝  Partner Pipeline",
    "🔬  Ecosystem Analysis",
    "💬  Field Interviews",
    "💡  Recommendations",
])

st.sidebar.markdown(f"""
<hr style='border-color:#2C3E6B; margin:0.4rem 0;'>
<div style='font-size:0.72rem; padding:0 0.3rem; line-height:1.8;'>
  <div style='color:{GREEN}; font-weight:700; margin-bottom:3px;'>Research Status</div>
  ✅ HQ: Ana Peña + Peter Sturgeon<br>
  ✅ CD Interview — Ghana (Wk 4)<br>
  ✅ CD Interview — Kenya (Wk 5)<br>
  ✅ CD Interview — Mexico (Wk 5)<br>
  ⚠️ Nicaragua — recording failed<br>
  ⏳ 8 CD interviews pending<br>
  ✅ Ecosystem DB — 185+ orgs<br>
  ✅ Framework scoring — 12 countries<br>
  ⏳ Partner Evidence Brief<br>
  <div style='color:{GOLD}; margin-top:6px; font-style:italic;'>Final presentation June 10</div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — THEORY OF CHANGE
# ══════════════════════════════════════════════════════════════════════════════
if "Theory" in page:
    page_header("Mission & Theory of Change",
                "The foundation of every recommendation in this project",
                "FOUNDED 1990")

    col1, col2 = st.columns([3,2])
    with col1:
        st.markdown(f"""
<div class='card-dark' style='border-bottom:3px solid {GREEN};'>
  <div style='font-size:0.65rem; color:{GREEN}; letter-spacing:2px; margin-bottom:8px;'>MISSION</div>
  <div style='font-size:1.55rem; font-weight:800; color:white; line-height:1.25;'>
    Lifting families around the world<br>from poverty to prosperity
  </div>
  <div style='font-size:1rem; color:{GOLD}; margin-top:8px; font-style:italic;'>
    through entrepreneurship and one-on-one mentoring.
  </div>
</div>""", unsafe_allow_html=True)

        st.markdown(f"""
<div class='card-gold'>
  <div style='font-size:0.65rem; color:{NAVY}; letter-spacing:2px; margin-bottom:8px; font-weight:700;'>THEORY OF CHANGE</div>
  <div style='font-size:1.05rem; color:{NAVY}; line-height:1.75;'>
    Because <strong>poverty traps families not from lack of effort but lack of knowledge</strong>,
    Mentors International works across <strong>12 countries</strong> to help
    micro-entrepreneurs grow stable businesses through one-on-one mentoring,
    in order to reach <strong>100,000 families out of poverty by 2030</strong>.
  </div>
</div>""", unsafe_allow_html=True)

    with col2:
        st.markdown(f"<div style='font-weight:700; color:{NAVY}; margin-bottom:10px;'>How the Model Works</div>", unsafe_allow_html=True)
        steps = [
            (GREEN,"🤝","Partner","NGO, MFI, or govt program sources pre-screened entrepreneurs"),
            (TEAL, "👤","Mentor","Trained local field coach assigned to each socio"),
            (NAVY, "📅","Visit","Twice a month at their place of business"),
            (AMBER,"📚","Skill","One lesson per visit from 28 certified modules"),
            (GREEN,"📈","Outcome","Income ↑  Savings ↑  Debt ↓"),
        ]
        for i,(color,icon,label,desc) in enumerate(steps):
            st.markdown(f"""
<div style='display:flex; align-items:center; gap:10px; margin-bottom:9px;'>
  <div style='background:{color}; color:white; border-radius:50%; width:36px; height:36px;
              display:flex; align-items:center; justify-content:center; font-size:1rem; flex-shrink:0;'>{icon}</div>
  {"<div style='color:#CCC; font-size:0.9rem; flex-shrink:0;'>↓</div>" if i<4 else ""}
  <div>
    <div style='font-weight:700; color:{NAVY}; font-size:0.88rem;'>{label}</div>
    <div style='font-size:0.78rem; color:{MGREY};'>{desc}</div>
  </div>
</div>""", unsafe_allow_html=True)

        st.markdown(f"""
<div style='background:{LGREY}; border-radius:8px; padding:9px 12px; margin-top:4px;
            border-left:3px solid {GREEN}; font-size:0.8rem; color:{NAVY};'>
  <strong>Key rule:</strong> Partners source. Mentors delivers.<br>
  The partner never touches program delivery.
</div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"<div style='font-weight:700; color:{NAVY}; margin-bottom:12px;'>Why This Model Is Distinctive</div>", unsafe_allow_html=True)
    st.markdown(f"""
<div class="stat-grid">
  {stat_card("+53%", "Income increase in Year 1*", "Self-reported FY2025", GREEN)}
  {stat_card("$150", "Cost per family per year", "Most cost-effective at scale", NAVY)}
  {stat_card("+65%", "Savings increase Year 1*", "Self-reported FY2025", TEAL)}
  {stat_card("$5", "Economic return per $1 donated", "2025 Annual Report", GOLD)}
  {stat_card("-22%", "Reduction in debt Year 1*", "Self-reported FY2025", AMBER)}
</div>
""", unsafe_allow_html=True)

    st.markdown(f"<div style='font-size:0.75rem; color:{MGREY}; margin-top:6px;'>* Self-reported by Mentors International for FY2025. Not independently verified.</div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — OVERVIEW
# ══════════════════════════════════════════════════════════════════════════════
elif "Overview" in page:
    page_header("Organization Overview", "FY2025 · 12 Countries · $6.4M Revenue · 43,160 Entrepreneurs Served")

    st.markdown(f"""
<div class="stat-grid">
  {stat_card("43,160", "Entrepreneurs served", "+79% vs FY24", GREEN)}
  {stat_card("12", "Countries operating", "3 regions", TEAL)}
  {stat_card("300+", "Field mentors", "+20% vs FY24", NAVY)}
  {stat_card("$150", "Cost per family / year", "Most cost-effective model", GOLD)}
  {stat_card("100,000", "2030 goal", "Entrepreneurs per year", AMBER)}
</div>
""", unsafe_allow_html=True)

    st.markdown("---")
    col1, col2 = st.columns([3,2])

    with col1:
        st.markdown(f"<div style='font-weight:700; color:{NAVY}; margin-bottom:10px;'>The Core Problem</div>", unsafe_allow_html=True)
        st.markdown(f"""
<div class='card-red'>
  <div style='font-size:1rem; font-weight:700; color:{RED}; margin-bottom:8px;'>⚠️ ~50% of global volume from ONE partner</div>
  <div style='font-size:0.88rem; color:{DGREY}; line-height:1.65;'>
    Bancolombia: 20,875 socios (FY25) → ~16,000 (FY26). <strong>Already declining.</strong><br>
    Outside Colombia: 97% of funding comes from individual donors — mostly Utah-based LDS community.<br>
    No systematic framework. No partnership playbook. No partner evidence brief.<br><br>
    <strong>This project answers:</strong> Which countries offer the best opportunities to diversify and grow — and what should Mentors do first?
  </div>
</div>""", unsafe_allow_html=True)

        st.markdown(f"<div style='font-weight:700; color:{NAVY}; margin:12px 0 8px;'>2025 Strategic Shifts</div>", unsafe_allow_html=True)
        for before, after, why in [
            ("Direct microlending","Refers to local financial partners","Removes capital burden. Makes Mentors a natural MFI partner."),
            ("3 programs","1 program — mentoring only","One job for CDs. Comparable data across 12 countries."),
            ("Manual tracking","Socio Connect — all 12 offices","Audit-ready data. Unlocks institutional funding conversations."),
        ]:
            st.markdown(f"""
<div style='display:flex; gap:8px; margin-bottom:7px; align-items:center;'>
  <div style='background:#FCE4D6; border-radius:6px; padding:5px 9px; font-size:0.78rem; color:{RED}; flex:1; text-align:center;'>{before}</div>
  <div style='color:{MGREY}; font-size:0.9rem;'>→</div>
  <div style='background:#C6EFCE; border-radius:6px; padding:5px 9px; font-size:0.78rem; color:{GREEN}; flex:1; text-align:center;'>{after}</div>
  <div style='font-size:0.75rem; color:{MGREY}; flex:2; padding-left:6px;'>{why}</div>
</div>""", unsafe_allow_html=True)

    with col2:
        st.markdown(f"<div style='font-weight:700; color:{NAVY}; margin-bottom:10px;'>FY25 → FY26 Volume by Tier</div>", unsafe_allow_html=True)
        tier_vol = countries.groupby("tier")[["fy25","fy26"]].sum().reset_index()
        tier_vol["label"] = tier_vol.tier.map({1:"🟢 Tier 1",2:"🟡 Tier 2",3:"🔴 Tier 3"})
        fig_tier = go.Figure()
        fig_tier.add_trace(go.Bar(x=tier_vol.label, y=tier_vol.fy25, name="FY25", marker_color=NAVY))
        fig_tier.add_trace(go.Bar(x=tier_vol.label, y=tier_vol.fy26, name="FY26 Target", marker_color=GREEN, opacity=0.75))
        fig_tier.update_layout(barmode="group",height=240,plot_bgcolor=WHITE,
            margin=dict(l=0,r=0,t=10,b=0),legend=dict(orientation="h",y=1.1))
        fig_tier.update_yaxes(gridcolor="#F0F0F0")
        fig_tier.update_xaxes(showgrid=False)
        st.plotly_chart(fig_tier, use_container_width=True)

        st.markdown(f"<div style='font-weight:700; color:{NAVY}; margin:8px 0 6px;'>Volume by Country</div>", unsafe_allow_html=True)
        vol = countries[["country","flag","fy25","fy26","tier"]].copy()
        vol["label"] = vol.apply(lambda r: f"{r.flag} {r.country}",axis=1)
        fig_vol = go.Figure()
        fig_vol.add_trace(go.Bar(x=vol.label,y=vol.fy25,name="FY25",marker_color=NAVY))
        fig_vol.add_trace(go.Bar(x=vol.label,y=vol.fy26,name="FY26 Target",marker_color=GREEN,opacity=0.7))
        fig_vol.update_layout(barmode="group",height=260,plot_bgcolor=WHITE,
            xaxis_tickangle=-35,margin=dict(l=0,r=0,t=10,b=0),
            legend=dict(orientation="h",y=1.1),showlegend=False)
        fig_vol.update_yaxes(gridcolor="#F0F0F0",title="Entrepreneurs")
        fig_vol.update_xaxes(showgrid=False)
        st.plotly_chart(fig_vol, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 3 — COUNTRY MAP
# ══════════════════════════════════════════════════════════════════════════════
elif "Map" in page:
    page_header("Country Map & Strategic Positioning", "Market opportunity vs operational readiness across 12 countries")

    tab1, tab2 = st.tabs(["🗺️ World Map","📍 Market vs Readiness"])

    with tab1:
        countries["tier_label"] = countries.tier.map(TL)
        fig_map = px.scatter_geo(countries, lat="lat", lon="lon",
            color="tier_label", size="fy25", size_max=55,
            hover_name="country",
            hover_data={"fy25":True,"total":True,"action":True,"lat":False,"lon":False,"tier_label":False},
            color_discrete_map={TL[1]:GREEN,TL[2]:AMBER,TL[3]:RED},
            text="flag", projection="natural earth")
        fig_map.update_traces(textposition="top center", textfont=dict(size=18))
        fig_map.update_layout(height=500, margin=dict(l=0,r=0,t=0,b=0),
            legend=dict(title="Tier",orientation="h",y=-0.05),
            geo=dict(showframe=False,showcoastlines=True,coastlinecolor="#CCC",
                     landcolor="#F5F5F0",showocean=True,oceancolor="#D6EAF8"))
        st.plotly_chart(fig_map, use_container_width=True)
        st.markdown(f"""
<div class="stat-grid" style="grid-template-columns:repeat(3,1fr);">
  {stat_card(f"{countries.fy25.sum():,}", "FY25 Total Entrepreneurs", None, GREEN)}
  {stat_card(f"{countries.fy26.sum():,}", "FY26 Target", None, NAVY)}
  {stat_card(f"+{((countries.fy26.sum()-countries.fy25.sum())/countries.fy25.sum()*100):.0f}%", "Growth Required", "By end FY26", AMBER)}
</div>
""", unsafe_allow_html=True)

    with tab2:
        fig_pos = px.scatter(countries, x="mkt", y="ops", color="tier",
            size="fy25", size_max=65, text="flag", hover_name="country",
            hover_data={"total":True,"action":True,"tier":False},
            color_discrete_map={1:GREEN,2:AMBER,3:RED},
            labels={"mkt":"Market Opportunity /10","ops":"Operational Readiness /10","tier":"Tier"})
        fig_pos.update_traces(textposition="top center", textfont=dict(size=18))
        fig_pos.add_hline(y=7, line_dash="dot", line_color="#BBB", annotation_text="Ops threshold")
        fig_pos.add_vline(x=7, line_dash="dot", line_color="#BBB", annotation_text="Market threshold")
        # Quadrant labels
        for tx,ty,txt in [(5,9,"High Ops\nWeak Market\n→ Protect"),(9,9,"High Both\n→ Invest Now"),(5,4,"Low Both\n→ Exit"),(9,4,"Strong Market\nWeak Ops\n→ Unblock")]:
            fig_pos.add_annotation(x=tx,y=ty,text=txt,showarrow=False,
                font=dict(size=9,color=MGREY),align="center")
        fig_pos.update_layout(height=520, plot_bgcolor=WHITE,
            title="Where to Invest vs Where to Protect")
        fig_pos.update_xaxes(gridcolor="#F0F0F0",range=[2,11])
        fig_pos.update_yaxes(gridcolor="#F0F0F0",range=[2,11])
        st.plotly_chart(fig_pos, use_container_width=True)
        st.caption("Bubble size = FY25 entrepreneur volume. Nicaragua is Tier 1 operationally (Pio's strength) but Tier 3 on market opportunity (govt restrictions).")

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 4 — COUNTRY BRIEFS
# ══════════════════════════════════════════════════════════════════════════════
elif "Country Briefs" in page:
    page_header("Country Briefs", "Deep-dive on each country — scoring, CD interview findings, named partners")

    options = [f"{r.flag} {r.country}" for _,r in countries.sort_values("total",ascending=False).iterrows()]
    sel = st.selectbox("Select country", options)
    cname = sel.split(" ",1)[1]
    r = countries[countries.country==cname].iloc[0]
    tc = TC[r.tier]

    st.markdown(f"""
<div style='background:linear-gradient(135deg,{NAVY} 0%,#243B6E 100%); border-radius:12px;
            padding:1.1rem 1.5rem; color:white; border-bottom:3px solid {tc}; margin-bottom:1rem;'>
  <div style='display:flex; justify-content:space-between; align-items:center;'>
    <div>
      <div style='font-size:1.6rem; font-weight:800;'>{r.flag} {r.country}</div>
      <div style='font-size:0.82rem; color:#CADCFC; margin-top:3px;'>{r.action}</div>
    </div>
    <div style='background:{tc}; border-radius:8px; padding:7px 16px; font-size:0.82rem; font-weight:700;'>
      {TL[r.tier]}
    </div>
  </div>
</div>""", unsafe_allow_html=True)

    st.markdown(f"""
<div class="stat-grid" style="grid-template-columns:repeat(6,1fr);">
  {stat_card(int(r.mkt) if r.mkt == int(r.mkt) else r.mkt, "Market Score /10", None, TEAL)}
  {stat_card(int(r.ops) if r.ops == int(r.ops) else r.ops, "Ops Score /10", None, NAVY)}
  {stat_card(int(r.total) if r.total == int(r.total) else r.total, "Total Score /20", None, GREEN)}
  {stat_card(f"{r.fy25:,}", "FY25 Socios", None, MGREY)}
  {stat_card(f"{r.fy26:,}", "FY26 Target", None, AMBER)}
  {stat_card(r.mentors, "Field Mentors", None, TEAL)}
</div>
""", unsafe_allow_html=True)

    st.markdown("---")
    col_l, col_r = st.columns([2,3])

    with col_l:
        st.markdown(f"<div style='font-weight:700; color:{NAVY}; margin-bottom:8px;'>Scoring Breakdown</div>", unsafe_allow_html=True)
        crit = pd.DataFrame({
            "Criterion":["Mission Align","Socio Density","Volume Potential","Digital Ready",
                         "CD Strength","Program Std","Legal Entity","Political Risk"],
            "Score":[r.m_align,r.socio,r.volume,r.digital,r.cd_score,r.program,r.legal,r.risk],
            "Type":["Market"]*4+["Ops"]*4
        })
        fig_br = px.bar(crit, x="Score", y="Criterion", orientation="h",
            color="Type", color_discrete_map={"Market":TEAL,"Ops":GREEN},
            range_x=[0,5.5], height=270)
        fig_br.update_layout(plot_bgcolor=WHITE,margin=dict(l=0,r=0,t=5,b=0),
            legend=dict(orientation="h",y=1.1))
        fig_br.update_xaxes(gridcolor="#F0F0F0",dtick=1)
        fig_br.update_yaxes(showgrid=False)
        st.plotly_chart(fig_br, use_container_width=True)
        st.markdown(f"**CD:** {r.cd} ({r.cd_tenure})")
        st.markdown(f"<div style='font-size:0.82rem; color:{MGREY};'>{r.ecosystem}</div>", unsafe_allow_html=True)

    with col_r:
        st.success(f"✅ **Working:** {r.working}")
        st.warning(f"⚠️ **Not Working:** {r.not_working}")
        st.info(f"📈 **Growth Ceiling:** {r.ceiling}")
        st.error(f"🚨 **Key Risk:** {r.risk_note}")
        st.markdown(f"""<div class='card-gold'>
<strong>💡 Recommendation:</strong><br>
<span style='font-size:0.88rem;'>{r.rec}</span>
</div>""", unsafe_allow_html=True)

    if r.cd_interview:
        st.markdown("---")
        st.markdown(f"<div style='font-weight:700; color:{NAVY}; margin-bottom:6px;'>🎙️ CD Interview Findings</div>", unsafe_allow_html=True)
        if cname == "Kenya":
            bullets = [
                "Uses Kenya govt NGO registry systematically — studies mission and compliance before any outreach",
                "World Vision MOU imminent after 9 months of persistence — emails, calls, personal office visits",
                "50% partnership conversion rate on actively pursued organizations",
                "82% socio graduation rate — strongest program quality metric in Africa",
                "Handover model: partners work with entrepreneurs 1–2 months first, then Mentors takes over 1-on-1 — dramatically improves commitment",
                "Kibera: 56 NGOs claim to solve clean water — problem persists. Focus on larger, credible, traceable orgs only",
                "Hidden motives test: 'What happens to your org if the problem is solved?' Good orgs say 'we close'",
                "USAID freeze = challenge (orgs closing) + opportunity (surviving orgs more open to new partners)",
                "Active partners: Imagine Leaders + Pendekizoletu Organisation — both confirmed top performers",
            ]
        elif cname == "Mexico":
            bullets = [
                "Two socio tiers confirmed: (1) homemakers selling basics from home — primary education, (2) semi-formal with degrees, entrepreneurs by circumstance",
                "90% are necessity entrepreneurs — not successful business owners",
                "ICATEY model: govt teaches trades, Mentors helps graduates build businesses — win-win because ICATEY gets business start-up statistics as their KPI",
                "Heifer International: provides machinery + training, Mentors adds pricing/marketing — perfect complementary model",
                "Commitment problem: partners promise 400 people but deliver people who don't want training",
                "Hidden motives flagged: political agendas behind stated missions in some partner organizations",
            ]
        elif cname == "Ghana":
            bullets = [
                "Cold outreach always fails in Ghana — people hear 'NGO' and expect money, not training",
                "Data gap is the binding constraint — only 4 months of clean Socio Connect data since Jan 2026 switch",
                "Already uses Bancolombia -40% loan default story in meetings — shows global proof points work even without local data",
                "Partnership style: past network + spontaneous networking (met trust fund contact on a flight) + HQ recommendations",
                "2-month close time when alignment is right — fast when you find the right org",
                "Needs: a structured target partner list + Partner Evidence Brief with global benchmarks",
                "This is a data maturity problem, not a market problem",
            ]
        for b in bullets:
            st.markdown(f"<div style='font-size:0.87rem; color:{DGREY}; padding:4px 0 4px 8px; border-left:2px solid {GREEN}; margin-bottom:5px;'>• {b}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"<div style='font-weight:700; color:{NAVY}; margin-bottom:8px;'>Named Partner Opportunities</div>", unsafe_allow_html=True)
    cp = partners[partners.country==cname]
    if len(cp):
        st.dataframe(cp[["org","type","priority","ptype","fit"]].rename(
            columns={"org":"Organization","type":"Type","priority":"Priority","ptype":"Partnership Type","fit":"Why a Fit"}),
            use_container_width=True, hide_index=True)
    else:
        st.caption("Research in progress.")

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 5 — PARTNER PIPELINE
# ══════════════════════════════════════════════════════════════════════════════
elif "Partner Pipeline" in page:
    page_header("Partner Pipeline", "Named opportunities across 12 countries · HQ interviews · CD interviews · Anderson Library research")

    c1,c2,c3 = st.columns(3)
    all_c = sorted(partners.country.unique())
    cf = c1.multiselect("Country", all_c, default=all_c)
    pf = c2.multiselect("Priority", ["HIGH","MEDIUM"], default=["HIGH","MEDIUM"])
    tf = c3.multiselect("Partnership Type", sorted(partners.ptype.unique()), default=list(partners.ptype.unique()))
    filt = partners[partners.country.isin(cf)&partners.priority.isin(pf)&partners.ptype.isin(tf)]

    st.markdown(f"""
<div class="stat-grid" style="grid-template-columns:repeat(3,1fr);">
  {stat_card(len(filt), "Total Opportunities", None, NAVY)}
  {stat_card(len(filt[filt.priority=="HIGH"]), "HIGH Priority", None, GREEN)}
  {stat_card(filt.country.nunique(), "Countries", None, TEAL)}
</div>
""", unsafe_allow_html=True)

    st.dataframe(filt[["country","org","type","priority","ptype","fit"]].rename(
        columns={"country":"Country","org":"Organization","type":"Type",
                 "priority":"Priority","ptype":"Partnership Type","fit":"Why a Fit"}
        ).sort_values(["Country","Priority"]),
        use_container_width=True, hide_index=True)

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<div style='font-weight:700; color:{NAVY}; margin-bottom:8px;'>Partners per Country</div>", unsafe_allow_html=True)
        pc = partners[partners.country!="Global"].groupby("country").size().reset_index(name="n")
        fig_pc = px.bar(pc.sort_values("n"), x="n", y="country", orientation="h",
            color="n", color_continuous_scale=[[0,LGREY],[0.5,TEAL],[1,NAVY]],
            labels={"n":"Named Partners","country":""}, height=380)
        fig_pc.update_layout(plot_bgcolor=WHITE, coloraxis_showscale=False, margin=dict(l=0,r=0,t=5,b=0))
        fig_pc.update_xaxes(gridcolor="#F0F0F0")
        fig_pc.update_yaxes(showgrid=False)
        st.plotly_chart(fig_pc, use_container_width=True)

    with col2:
        st.markdown(f"<div style='font-weight:700; color:{NAVY}; margin-bottom:8px;'>🌐 Global / Multi-Country Opportunities</div>", unsafe_allow_html=True)
        for _,gp in partners[partners.country=="Global"].iterrows():
            st.markdown(f"""<div class='card'>
<div style='font-weight:700; color:{NAVY}; font-size:0.9rem;'>{gp.org}</div>
<div style='font-size:0.75rem; color:{MGREY};'>{gp.type} · {gp.ptype}</div>
<div style='font-size:0.82rem; color:{DGREY}; margin-top:5px;'>{gp.fit}</div>
</div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 6 — ECOSYSTEM ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
elif "Ecosystem" in page:
    page_header("Ecosystem Analysis", "185+ organizations researched · Anderson Library · NGO registries · MFI directories · Factiva")

    # Three archetypes at top
    st.markdown(f"<div style='font-weight:700; color:{NAVY}; margin-bottom:10px;'>Three Partner Archetypes — Caleigh's Framework</div>", unsafe_allow_html=True)
    a1,a2,a3 = st.columns(3)
    with a1:
        st.markdown(f"""<div class='card-teal'>
<div style='font-weight:700; color:{TEAL}; font-size:0.95rem;'>⚙️ Scale Engines</div>
<div style='font-size:0.78rem; color:{MGREY}; margin-top:6px;'><strong>Who:</strong> Large MFIs, Government programs, Corporate CSR</div>
<div style='font-size:0.78rem; color:{MGREY}; margin-top:4px;'><strong>Profile:</strong> High scale, lower alignment</div>
<div style='font-size:0.78rem; color:{MGREY}; margin-top:4px;'><strong>Examples:</strong> Bancolombia, Compartamos, SENA</div>
<div style='font-size:0.78rem; color:{MGREY}; margin-top:4px;'><strong>Pitch:</strong> Loan default data. Frame Mentors as performance tool.</div>
<div style='font-size:0.78rem; color:#E74C3C; margin-top:4px;'><strong>Risk:</strong> Will push for weaker program delivery.</div>
</div>""", unsafe_allow_html=True)
    with a2:
        st.markdown(f"""<div class='card' style='border-left-color:{GREEN};'>
<div style='font-weight:700; color:{GREEN}; font-size:0.95rem;'>⭐ Ideal Model Partners</div>
<div style='font-size:0.78rem; color:{MGREY}; margin-top:6px;'><strong>Who:</strong> Faith-based MFIs, Women-focused groups, Entrepreneur NGOs</div>
<div style='font-size:0.78rem; color:{MGREY}; margin-top:4px;'><strong>Profile:</strong> High alignment, mid-scale</div>
<div style='font-size:0.78rem; color:{MGREY}; margin-top:4px;'><strong>Examples:</strong> Pro Mujer, ADOPEM, Sinapi Aba, Hand in Hand</div>
<div style='font-size:0.78rem; color:{MGREY}; margin-top:4px;'><strong>Pitch:</strong> Shared mission. Position Mentors as their business skills arm.</div>
<div style='font-size:0.78rem; color:#F39C12; margin-top:4px;'><strong>Risk:</strong> Lower volume per partner — need 3–5 for scale.</div>
</div>""", unsafe_allow_html=True)
    with a3:
        st.markdown(f"""<div class='card-gold'>
<div style='font-weight:700; color:{GOLD}; font-size:0.95rem;'>🌐 Ecosystem Enablers</div>
<div style='font-size:0.78rem; color:{MGREY}; margin-top:6px;'><strong>Who:</strong> INGOs, Chambers, Government umbrella bodies</div>
<div style='font-size:0.78rem; color:{MGREY}; margin-top:4px;'><strong>Profile:</strong> Network reach, indirect impact</div>
<div style='font-size:0.78rem; color:{MGREY}; margin-top:4px;'><strong>Examples:</strong> KCB Foundation, Youth Enterprise Fund, KUSCCO</div>
<div style='font-size:0.78rem; color:{MGREY}; margin-top:4px;'><strong>Pitch:</strong> Ask for referrals, not socios. Use as door-openers.</div>
<div style='font-size:0.78rem; color:#E74C3C; margin-top:4px;'><strong>Risk:</strong> Pipeline too indirect — socios uncommitted.</div>
</div>""", unsafe_allow_html=True)

    st.markdown("---")
    tab1, tab2, tab3 = st.tabs(["🏆 Country Rankings","📊 Ecosystem Overview","🔍 Organization Database"])

    with tab1:
        # ── Caleigh's actual framework scores from Framework Analysis sheet ──
        # Source: Mentors_International_Framework_Research.xlsx
        # 8 criteria — C1-C5 scored from real data sources, C6-C8 pending
        framework_scores = pd.DataFrame([
            dict(country="Colombia",          c1=9.17, c2=8.26, c3=8.82, c4=7.66, c5=5.55),
            dict(country="Dominican Republic",c1=7.71, c2=8.12, c3=3.45, c4=8.93, c5=8.29),
            dict(country="Mexico",            c1=6.68, c2=5.79, c3=7.52, c4=9.24, c5=6.26),
            dict(country="Peru",              c1=7.25, c2=7.04, c3=8.36, c4=7.50, c5=6.07),
            dict(country="Kenya",             c1=7.95, c2=8.17, c3=9.60, c4=6.37, c5=2.62),
            dict(country="Cambodia",          c1=8.68, c2=6.67, c3=7.18, c4=7.04, c5=2.83),
            dict(country="Ghana",             c1=4.09, c2=4.61, c3=9.39, c4=7.06, c5=8.78),
            dict(country="Honduras",          c1=8.29, c2=5.20, c3=6.61, c4=5.33, c5=4.07),
            dict(country="Guatemala",         c1=4.31, c2=4.71, c3=6.87, c4=5.84, c5=4.71),
            dict(country="Nicaragua",         c1=4.93, c2=4.61, c3=5.87, c4=4.38, c5=2.81),
            dict(country="Malawi",            c1=4.03, c2=3.21, c3=6.18, c4=1.54, c5=4.60),
            dict(country="Cape Verde",        c1=1.00, c2=1.00, c3=1.19, c4=6.40, c5=10.0),
        ])

        framework_scores["C1–C5 Average"] = framework_scores[["c1","c2","c3","c4","c5"]].mean(axis=1).round(2)
        framework_scores = framework_scores.sort_values("C1–C5 Average", ascending=False).reset_index(drop=True)
        framework_scores.insert(0, "Rank", range(1, len(framework_scores)+1))

        # ── Explanation banner ────────────────────────────────────────────────
        st.markdown(f"""<div class='card-gold'>
<strong>Source: Caleigh's Framework Analysis — Mentors_International_Framework_Research.xlsx</strong><br>
<span style='font-size:0.82rem; color:{MGREY};'>
8 criteria scored using real data (World Bank, GSMA, Fund for Peace, Freedom House, Ecosystem Database).
Criteria 1–5 are complete. Criteria 6 (Legal Structure), 7 (CD Strength), 8 (Program Standardization) are still being scored — shown as ⏳ pending.
</span>
</div>""", unsafe_allow_html=True)

        # ── Criteria legend ───────────────────────────────────────────────────
        c1,c2 = st.columns(2)
        with c1:
            st.markdown(f"""
<div style='font-size:0.8rem; color:{NAVY}; line-height:2;'>
<strong>Criteria 1–5 (scored from real data):</strong><br>
<span style='color:{TEAL};'>C1</span> Mission Alignment — ecosystem database alignment scores<br>
<span style='color:{TEAL};'>C2</span> Volume Potential — scalable + anchor partners, socio capacity<br>
<span style='color:{TEAL};'>C3</span> Socio Profile Fit — World Bank urban population & poverty data<br>
<span style='color:{TEAL};'>C4</span> Digital Readiness — GSMA Mobile Index, World Bank internet usage<br>
<span style='color:{TEAL};'>C5</span> Political Risk — Fund for Peace Fragile States + Freedom House
</div>""", unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
<div style='font-size:0.8rem; color:{NAVY}; line-height:2;'>
<strong>Criteria 6–8 (in progress — pending CD interviews):</strong><br>
<span style='color:{AMBER};'>C6</span> Legal & Structural Constraints — revenue-generating nonprofit rules<br>
<span style='color:{AMBER};'>C7</span> CD Strength & Leadership — rubric scored from interviews<br>
<span style='color:{AMBER};'>C8</span> Program Standardization — rubric scored from program data<br><br>
<span style='font-size:0.75rem; color:{MGREY}; font-style:italic;'>All scores out of 10. Final composite will use Caleigh's weighted formula once C6–C8 complete.</span>
</div>""", unsafe_allow_html=True)

        st.markdown("---")

        # ── Radar / bar chart of C1-C5 scores ────────────────────────────────
        st.markdown(f"<div style='font-weight:700; color:{NAVY}; margin-bottom:8px;'>Criterion Scores by Country — C1 to C5 (out of 10)</div>", unsafe_allow_html=True)

        selected_countries = st.multiselect(
            "Compare countries",
            options=framework_scores["country"].tolist(),
            default=["Colombia","Kenya","Mexico","Dominican Republic","Peru"]
        )

        if selected_countries:
            plot_df = framework_scores[framework_scores["country"].isin(selected_countries)].copy()
            plot_melt = plot_df.melt(
                id_vars=["country"],
                value_vars=["c1","c2","c3","c4","c5"],
                var_name="Criterion", value_name="Score"
            )
            crit_labels = {
                "c1":"C1: Mission\nAlignment",
                "c2":"C2: Volume\nPotential",
                "c3":"C3: Socio\nProfile Fit",
                "c4":"C4: Digital\nReadiness",
                "c5":"C5: Political\nRisk",
            }
            plot_melt["Criterion"] = plot_melt["Criterion"].map(crit_labels)
            fig_crit = px.bar(
                plot_melt, x="Criterion", y="Score", color="country",
                barmode="group", height=360,
                color_discrete_sequence=px.colors.qualitative.Set2,
                labels={"Score":"Score /10","country":"Country"},
            )
            fig_crit.update_layout(plot_bgcolor=WHITE, margin=dict(l=0,r=0,t=10,b=0),
                legend=dict(orientation="h", y=1.1))
            fig_crit.update_yaxes(gridcolor="#F0F0F0", range=[0,11])
            fig_crit.update_xaxes(showgrid=False)
            st.plotly_chart(fig_crit, use_container_width=True)

        # ── Ranking table ─────────────────────────────────────────────────────
        st.markdown(f"<div style='font-weight:700; color:{NAVY}; margin-bottom:8px;'>Full Country Rankings — C1 to C5 Average</div>", unsafe_allow_html=True)

        display_df = framework_scores[["Rank","country","C1–C5 Average","c1","c2","c3","c4","c5"]].copy()
        display_df.columns = ["Rank","Country","C1–C5 Avg /10",
                               "C1: Mission\nAlignment","C2: Volume\nPotential",
                               "C3: Socio\nProfile Fit","C4: Digital\nReadiness",
                               "C5: Political\nRisk"]
        display_df["C6: Legal"] = "⏳"
        display_df["C7: CD Strength"] = "⏳"
        display_df["C8: Program Std"] = "⏳"

        st.dataframe(display_df, use_container_width=True, hide_index=True)

        st.caption(
            "Rankings based on Caleigh's 5 completed criteria only. "
            "C6 (Legal Structure), C7 (CD Strength), C8 (Program Standardization) are pending — "
            "final rankings will shift once these are scored. "
            "Note: Cape Verde scores C5=10.0 (most stable political environment) but is still an exit "
            "candidate due to scale and leadership constraints captured in C6–C8."
        )


    with tab2:
        col1,col2 = st.columns(2)
        with col1:
            a5 = ecosystem[ecosystem["align"]==5].groupby("country").size().reset_index(name="n")
            fig_a5 = px.bar(a5.sort_values("n",ascending=True), x="n", y="country",
                orientation="h", color_discrete_sequence=[GREEN],
                labels={"n":"# of 5-Alignment Orgs","country":""},
                title="Top Mission-Aligned Partners (Score 5) per Country", height=360)
            fig_a5.update_layout(plot_bgcolor=WHITE,margin=dict(l=0,r=0,t=40,b=0))
            fig_a5.update_xaxes(gridcolor="#F0F0F0",dtick=1)
            fig_a5.update_yaxes(showgrid=False)
            st.plotly_chart(fig_a5, use_container_width=True)

        with col2:
            avg = ecosystem.groupby("country")["align"].mean().reset_index()
            avg.columns = ["country","avg_align"]
            fig_avg = px.bar(avg.sort_values("avg_align",ascending=True), x="avg_align", y="country",
                orientation="h",
                color="avg_align", color_continuous_scale=[[0,"#FCE4D6"],[0.5,TEAL],[1,GREEN]],
                labels={"avg_align":"Average Alignment Score","country":""},
                title="Average Alignment Score by Country", height=360)
            fig_avg.update_layout(plot_bgcolor=WHITE, coloraxis_showscale=False, margin=dict(l=0,r=0,t=40,b=0))
            fig_avg.update_xaxes(gridcolor="#F0F0F0",range=[0,5.5])
            fig_avg.update_yaxes(showgrid=False)
            st.plotly_chart(fig_avg, use_container_width=True)

        st.markdown(f"""<div class='card-gold'>
<strong>Caleigh's Key Insight:</strong>
Latin America is best for rapid scale via institutional MFI partnerships (Colombia + DR have the densest 5-alignment ecosystems globally).
Africa is more fragmented but NGO alignment is higher — Kenya is the standout.
Three distinct archetypes emerge across all 185+ orgs: Scale Engines, Ideal Model Partners, Ecosystem Enablers.
</div>""", unsafe_allow_html=True)

    with tab3:
        c1,c2,c3 = st.columns(3)
        cf2 = c1.selectbox("Country",["All"]+sorted(ecosystem.country.unique()))
        af2 = c2.selectbox("Min Alignment",[1,3,4,5],index=2)
        sf2 = c3.selectbox("Status",["All"]+sorted(ecosystem.status.unique()))
        eco_f = ecosystem.copy()
        if cf2!="All": eco_f = eco_f[eco_f.country==cf2]
        eco_f = eco_f[eco_f["align"]>=af2]
        if sf2!="All": eco_f = eco_f[eco_f.status==sf2]
        st.markdown(f'<div class="section-label">Organizations shown: {len(eco_f)}</div>', unsafe_allow_html=True)
        st.dataframe(eco_f[["country","org","cat","align","scale","status"]].rename(
            columns={"country":"Country","org":"Organization","cat":"Category",
                     "align":"Alignment /5","scale":"Scale /5","status":"Status"}
        ).sort_values(["Alignment /5","Scale /5"],ascending=False),
        use_container_width=True, hide_index=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 7 — FIELD INTERVIEWS
# ══════════════════════════════════════════════════════════════════════════════
elif "Interviews" in page:
    page_header("Field Interviews", "HQ: Ana Peña · Peter Sturgeon · CD Interviews: Ghana · Kenya · Mexico")

    tab1, tab2, tab3 = st.tabs(["🏢 HQ Interviews","🌍 CD Interviews","🔁 Cross-Cutting Insights"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"<div style='font-weight:700; color:{NAVY}; margin-bottom:8px;'>Ana Peña — Director of Operations</div>", unsafe_allow_html=True)
            for q in [
                "\"You guys have everything I have. There is not a manual beyond that.\"",
                "\"Most of my country directors are terrified of pitching new partners.\"",
                "\"Where do the TIGOs of the world live?\"",
            ]:
                st.markdown(f"<div class='quote'>{q}</div>", unsafe_allow_html=True)

            st.markdown(f"""<div class='card-teal' style='margin-top:10px;'>
<div style='font-weight:700; color:{TEAL};'>The TIGO Flywheel — The Network Template</div>
<div style='font-size:0.82rem; color:{DGREY}; margin-top:6px; line-height:1.6;'>
TIGO Nicaragua → 1 good 6-month report + 1 referral ask → OI → Banco de Alimentos → Global Food Bank Alliance<br>
<strong>= 5 new partners from one anchor relationship.</strong><br><br>
Send a strong mid-program report. Then ask directly for referrals. That sequence is the flywheel.
</div></div>""", unsafe_allow_html=True)

            st.markdown(f"""<div class='card' style='margin-top:8px;'>
<div style='font-weight:700; color:{NAVY};'>Partners source. Mentors delivers.</div>
<div style='font-size:0.82rem; color:{MGREY}; margin-top:5px;'>
Partners identify and refer socios only. Mentors teams always deliver the program. This means ANY org with trusted relationships with micro-entrepreneurs qualifies as a partner.
</div></div>""", unsafe_allow_html=True)

        with col2:
            st.markdown(f"<div style='font-weight:700; color:{NAVY}; margin-bottom:8px;'>Peter Sturgeon — CEO</div>", unsafe_allow_html=True)
            for q in [
                "\"Volume partnerships — our lack is due to training, not opportunity.\"",
                "\"I went to Honduras, met 3 MFIs. 2 out of 3 said yes. In one afternoon.\"",
                "\"A country rises or falls based on the strength of the country director.\"",
            ]:
                st.markdown(f"<div class='quote'>{q}</div>", unsafe_allow_html=True)

            st.markdown(f"""<div class='card-gold' style='margin-top:10px;'>
<div style='font-weight:700; color:{NAVY};'>Three Partnership Types</div>
<div style='font-size:0.82rem; margin-top:8px; line-height:1.8;'>
<span style='color:{RED};'>⬤</span> <strong>Volume Only</strong> — partner sources socios free. Easy but donor-dependent.<br>
<span style='color:{GOLD};'>⬤</span> <strong>Revenue Only</strong> — partner pays full cost. Very rare.<br>
<span style='color:{GREEN};'>⬤</span> <strong>Combo Model ⭐</strong> — partner + foundation covers gap. <strong>Never built yet.</strong>
</div></div>""", unsafe_allow_html=True)

            st.markdown(f"""<div class='card' style='margin-top:8px; border-left-color:{RED};'>
<div style='font-weight:700; color:{NAVY};'>LDS Humanitarian — Biggest Untapped Opportunity</div>
<div style='font-size:0.82rem; color:{MGREY}; margin-top:5px;'>
Mentors uses LDS Welfare (10% of budget, members only). The Humanitarian arm = 90% of budget, serves ANYONE. Has never been approached.
</div></div>""", unsafe_allow_html=True)

    with tab2:
        subtab1, subtab2, subtab3 = st.tabs(["🇰🇪 Kenya — Eric Onyango","🇲🇽 Mexico CD Team","🇬🇭 Ghana — Emmanuel Gyamfi"])

        with subtab1:
            st.caption("Week 5 · Nairobi · 4 yrs as CD · 50% partnership conversion · 82% socio graduation rate")
            col1,col2 = st.columns([3,2])
            with col1:
                st.markdown(f"<div class='quote'>\"I've never seen somebody so consistent.\" — World Vision Kenya, after 9 months of Eric's persistence. MOU now imminent.</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='quote'>\"In Kibera there are 56 NGOs claiming to work on clean water. And yet clean water continues to be a problem. Many organisations are not trying to solve the problem — they're ensuring their own continuity.\"</div>", unsafe_allow_html=True)
            with col2:
                st.markdown(
                    '<div class="stat-grid" style="grid-template-columns:1fr;">'
                    + stat_card("50%", "Partnership conversion rate", "Of pursued orgs", GREEN)
                    + stat_card("82%", "Socio graduation rate", "Program completion", TEAL)
                    + '</div>',
                    unsafe_allow_html=True
                )

            st.markdown(f"<div style='font-weight:700; color:{NAVY}; margin:10px 0 6px;'>Key Insights from Eric</div>", unsafe_allow_html=True)
            insights = [
                (GREEN,"Kenya Handover Model (Best Practice)","Partners work with entrepreneurs 1–2 months first. Then Mentors takes over one-on-one. Pre-screening dramatically improves commitment. Recommend as the standard in the playbook."),
                (TEAL,"NGO Registry as Primary Research Tool","Uses Kenya's govt NGO registration website systematically — studies mission and compliance before outreach. Every CD should do this with their country's equivalent registry."),
                (AMBER,"USAID Freeze — Double-Edged","Many USAID-dependent NGOs have closed (bad). But surviving orgs are more open to new partnerships because they need to demonstrate relevance (opportunity)."),
                (RED,"Hidden Motives Filter","Test: 'What happens to your org if the problem you're solving is solved?' Good orgs say 'we close'. Avoid orgs with vague answers. Focus on larger, credible, traceable organizations only."),
            ]
            for color,title,body in insights:
                st.markdown(f"""<div class='card' style='border-left-color:{color};'>
<div style='font-weight:700; color:{NAVY}; font-size:0.88rem;'>{title}</div>
<div style='font-size:0.82rem; color:{MGREY}; margin-top:4px;'>{body}</div>
</div>""", unsafe_allow_html=True)

        with subtab2:
            st.caption("Week 5 · Mérida, Chiapas, Oaxaca · Zoram Varguez (10+ yrs) + Carla + Olivia")
            st.markdown(f"""<div class='card'>
<div style='font-weight:700; color:{NAVY}; margin-bottom:8px;'>Two Socio Tiers Confirmed</div>
<div style='display:flex; gap:12px;'>
  <div style='background:{LGREY}; border-radius:8px; padding:10px; flex:1;'>
    <div style='font-weight:700; color:{NAVY}; font-size:0.85rem;'>Tier 1 — Basic Community</div>
    <div style='font-size:0.8rem; color:{MGREY}; margin-top:4px;'>Homemakers selling chicken, fruit, sewing from home. Primary school education. Supplemental income. Mostly women.</div>
  </div>
  <div style='background:{LGREY}; border-radius:8px; padding:10px; flex:1;'>
    <div style='font-weight:700; color:{NAVY}; font-size:0.85rem;'>Tier 2 — Semi-Formal</div>
    <div style='font-size:0.8rem; color:{MGREY}; margin-top:4px;'>Printing, consulting, English classes, food delivery. Some with degrees. Entrepreneurs by circumstance. Higher education but still need financial management.</div>
  </div>
</div>
<div style='font-size:0.8rem; color:{MGREY}; margin-top:8px;'><strong>Key:</strong> 90% are necessity entrepreneurs. Not successful business owners.</div>
</div>""", unsafe_allow_html=True)

            c1,c2 = st.columns(2)
            with c1:
                st.markdown(f"""<div class='card-teal'>
<div style='font-weight:700; color:{TEAL};'>The ICATEY Model — Govt Partnership Done Right</div>
<div style='font-size:0.82rem; color:{DGREY}; margin-top:6px; line-height:1.6;'>
ICATEY (govt vocational training) teaches trades. Mentors follows up to help graduates build businesses from those trades.<br><br>
<strong>Win-win:</strong> ICATEY gets business start-up statistics (their KPI). Mentors gets socios with skills and commitment.<br><br>
<strong>Replicate with:</strong> DIF municipal network, SENA (Colombia), CETPROs (Peru), and other govt vocational systems.
</div></div>""", unsafe_allow_html=True)
            with c2:
                st.markdown(f"""<div class='card-gold'>
<div style='font-weight:700; color:{NAVY};'>The Commitment Problem</div>
<div style='font-size:0.82rem; color:{DGREY}; margin-top:6px; line-height:1.6;'>
Partners promise 400 people but deliver people who don't want to be trained.<br><br>
<strong>Root cause:</strong> Partner mission aligns but their actual reach includes uncommitted people.<br><br>
<strong>Fix:</strong> Partners must have <em>retained, committed</em> beneficiaries before partnership — not just an occasional audience. Use Kenya Handover Model.
</div></div>""", unsafe_allow_html=True)

        with subtab3:
            st.caption("Week 4 · Accra · 1 yr as CD (departing May 30) · Switched from MFI model Jan 2026")
            st.markdown(f"<div class='quote'>\"I keep getting the opinion that I don't have a better story to tell, and that is why I'm probably not able to convince a partner.\"</div>", unsafe_allow_html=True)
            c1,c2 = st.columns(2)
            with c1:
                st.markdown(f"""<div class='card-red'>
<div style='font-weight:700; color:{RED};'>The Data Gap — Core Constraint</div>
<div style='font-size:0.82rem; color:{DGREY}; margin-top:6px; line-height:1.6;'>
Only 4 months of clean Socio Connect data since Jan 2026 switch. Emmanuel already uses the Bancolombia -40% loan default story in meetings — global proof works even without local data.<br><br>
<strong>This is a data maturity problem, not a market problem.</strong>
</div></div>""", unsafe_allow_html=True)
            with c2:
                st.markdown(f"""<div class='card-teal'>
<div style='font-weight:700; color:{TEAL};'>Cold Outreach Always Fails in Ghana</div>
<div style='font-size:0.82rem; color:{DGREY}; margin-top:6px; line-height:1.6;'>
When mentors approach entrepreneurs cold, dropout rates are very high. In Ghana, people hear "NGO" and expect money.<br><br>
<strong>This confirms</strong> partner sourcing is essential everywhere — partners with community trust eliminate this problem.
</div></div>""", unsafe_allow_html=True)
            st.markdown(f"""<div class='card'>
<div style='font-weight:700; color:{NAVY};'>Emmanuel's Partnership Style — More Creative Than Expected</div>
<div style='font-size:0.82rem; color:{MGREY}; margin-top:6px; line-height:1.6;'>
He uses three channels simultaneously: (1) HQ recommendations — check if global partners have Ghana branches. (2) Past work network — has a target list but needs stronger data to approach them. (3) Spontaneous networking — met a trust fund contact on a flight; attended an office opening and met an MP; spoke to a program director through a direct referral.<br><br>
<strong>He is entrepreneurial. What he needs is content + a structured target list — not training on how to network.</strong>
</div></div>""", unsafe_allow_html=True)

    with tab3:
        st.markdown(f"""<div class='card-dark' style='margin-bottom:1rem; border-bottom:3px solid {GREEN};'>
<div style='color:{GREEN}; font-weight:700; margin-bottom:8px;'>The Universal Finding — All Three CD Interviews</div>
<div style='color:white; font-size:0.9rem; line-height:1.7;'>
Cold outreach to entrepreneurs always fails. Partners who already have committed, pre-screened beneficiaries are the only reliable source of quality socios. True in Ghana, Kenya, and Mexico independently.
</div></div>""", unsafe_allow_html=True)

        c1,c2 = st.columns(2)
        with c1:
            st.markdown(f"<div style='font-weight:700; color:{NAVY}; margin-bottom:8px;'>The Data Story Gap — Four Voices, Same Problem</div>", unsafe_allow_html=True)
            data_gap = pd.DataFrame({
                "Source":["Ana Peña","Peter Sturgeon","Emmanuel (Ghana)","Eric (Kenya)"],
                "What they said":[
                    "We don't have a strong framework for what a good partner looks like",
                    "If I were a better promoter we'd be presenting at international conferences",
                    "I don't have a better story to tell — that's why I can't convince partners",
                    "I use the Bancolombia loan default story but I need Kenya-specific evidence",
                ]
            })
            st.dataframe(data_gap, use_container_width=True, hide_index=True)
            st.markdown(f"""<div class='card' style='border-left-color:{GREEN};'>
<strong>The Fix:</strong> A single 2-page Partner Evidence Brief every CD walks into every meeting with. Global benchmarks + local data slot. Mentors has better 1-year outcomes than BRAC's 4-year program. That story is not being told.
</div>""", unsafe_allow_html=True)

        with c2:
            st.markdown(f"<div style='font-weight:700; color:{NAVY}; margin-bottom:8px;'>Market vs People Constraint</div>", unsafe_allow_html=True)
            col_a,col_b = st.columns(2)
            with col_a:
                st.markdown(f"<div style='font-size:0.82rem; font-weight:700; color:{RED}; margin-bottom:4px;'>Market constraint:</div>", unsafe_allow_html=True)
                for x in ["Cape Verde — too small","Malawi — 80% agricultural","Nicaragua — political restrictions"]:
                    st.markdown(f"<div style='font-size:0.82rem; color:{DGREY}; padding:2px 0;'>🔴 {x}</div>", unsafe_allow_html=True)
            with col_b:
                st.markdown(f"<div style='font-size:0.82rem; font-weight:700; color:{AMBER}; margin-bottom:4px;'>People constraint:</div>", unsafe_allow_html=True)
                for x in ["Guatemala — educator can't pitch","Kenya — CD part-time","Ghana — data gap, CD departing","Honduras — too new"]:
                    st.markdown(f"<div style='font-size:0.82rem; color:{DGREY}; padding:2px 0;'>🟡 {x}</div>", unsafe_allow_html=True)

            st.markdown(f"""<div class='card-gold' style='margin-top:10px;'>
<strong>The hidden motives filter</strong> (Kenya + Mexico both flagged this independently):<br>
<div style='font-size:0.82rem; color:{MGREY}; margin-top:5px;'>"What happens to your org if the poverty problem is solved?" Good orgs say "we close". If the answer is unclear — that org sustains itself on the problem. Avoid them.</div>
</div>""", unsafe_allow_html=True)

            st.markdown(f"""<div class='card-teal' style='margin-top:8px;'>
<strong>The Kenya Handover Model — Recommend for Playbook</strong><br>
<div style='font-size:0.82rem; color:{MGREY}; margin-top:5px;'>Partners work with entrepreneurs 1–2 months first. Then Mentors takes over. Pre-screening dramatically improves commitment. Should be the standard partnership structure in the playbook.</div>
</div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 8 — RECOMMENDATIONS
# ══════════════════════════════════════════════════════════════════════════════
elif "Recommendations" in page:
    page_header("Strategic Recommendations",
                "Based on HQ interviews · CD interviews · Ecosystem research (185+ orgs) · Framework scoring · May 2026",
                "FINAL JUNE 10")

    st.markdown(f"""
<div class='banner'>
  <div style='font-size:0.65rem; color:{GREEN}; letter-spacing:2px; margin-bottom:4px;'>THE GOAL</div>
  <div style='font-size:1.05rem; color:white; line-height:1.7;'>
    Because poverty traps families not from lack of effort but lack of knowledge,
    Mentors International works across 12 countries to help micro-entrepreneurs grow stable businesses
    through one-on-one mentoring, in order to reach
    <span style='color:{GREEN}; font-weight:800;'>100,000 families out of poverty by 2030</span>.
  </div>
</div>""", unsafe_allow_html=True)

    st.markdown(f"""
<div class="stat-grid">
  {stat_card("4", "Tier 1 — Invest Now", "Colombia · Mexico · DR · Nicaragua", GREEN)}
  {stat_card("3", "Tier 2 — Targeted", "Kenya · Peru · Cambodia", AMBER)}
  {stat_card("4", "Tier 3 — Stabilize", "Honduras · Guatemala · Malawi · Ghana", RED)}
  {stat_card("1", "Exit Candidate", "Cape Verde", MGREY)}
  {stat_card(len(partners), "Named Partners", "Across 12 countries", TEAL)}
</div>
""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"<div style='font-weight:700; color:{NAVY}; font-size:1.1rem; margin-bottom:12px;'>Top 5 Immediate Recommendations</div>", unsafe_allow_html=True)

    recs = [
        (RED,"🚨","1. Diversify Colombia — Now",
         "90% concentration in Bancolombia is an existential risk. Volume already declining 20k→16k. Research which Colombian banks have same financial education compliance obligations as Bancolombia. Pursue Bancamía, Banco Mundo Mujer, Interactuar this quarter. Jackie should lead."),
        (AMBER,"👤","2. Resolve Kenya CD — One Decision Unlocks Everything",
         "Kenya has the best NGO ecosystem in Africa and 82% socio graduation rate. But the CD has a part-time job. Full-time commitment or replacement — this single decision unlocks 3,000–5,000 socios/yr in Nairobi. Ana must act."),
        (NAVY,"🌐","3. Pursue Millicom at Corporate Level",
         "TIGO Nicaragua is the best partnership model in the network. Millicom (TIGO parent) operates in 9 LATAM+Africa countries. One corporate conversation could replicate the Nicaragua flywheel across multiple markets simultaneously."),
        (TEAL,"⛪","4. Approach LDS Humanitarian Program",
         "Mentors uses only 10% of LDS budget (Welfare arm, members only). LDS Humanitarian = 90% of budget, serves ANYONE regardless of faith. Has never been approached. Single largest untapped funding + volume opportunity."),
        (GREEN,"📄","5. Build the Partner Evidence Brief",
         "Emmanuel, Ana, Peter, and Eric all described the same gap. CDs walk into meetings without evidence. A 2-page brief — Bancolombia -40% default, +53% income, $5 return per $1, one human story — changes every CD conversation immediately."),
    ]
    for color,icon,title,body in recs:
        st.markdown(f"""<div class='card' style='border-left-color:{color};'>
<div style='font-size:0.95rem; font-weight:700; color:{NAVY};'>{icon} {title}</div>
<div style='font-size:0.83rem; color:{MGREY}; margin-top:5px; line-height:1.6;'>{body}</div>
</div>""", unsafe_allow_html=True)

    st.markdown("---")

    # Positioning chart
    fig_rec = px.scatter(countries, x="mkt", y="ops", color="tier",
        size="fy25", size_max=65, text="flag", hover_name="country",
        hover_data={"total":True,"action":True,"tier":False},
        color_discrete_map={1:GREEN,2:AMBER,3:RED},
        labels={"mkt":"Market Opportunity /10","ops":"Operational Readiness /10","tier":"Tier"},
        title="Country Portfolio — Market Opportunity vs Operational Readiness")
    fig_rec.update_traces(textposition="top center", textfont=dict(size=18))
    fig_rec.add_hline(y=7, line_dash="dot", line_color="#BBB")
    fig_rec.add_vline(x=7, line_dash="dot", line_color="#BBB")
    fig_rec.update_layout(height=460, plot_bgcolor=WHITE)
    fig_rec.update_xaxes(gridcolor="#F0F0F0",range=[2,11])
    fig_rec.update_yaxes(gridcolor="#F0F0F0",range=[2,11])
    st.plotly_chart(fig_rec, use_container_width=True)

    st.markdown("---")
    c1,c2,c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='card' style='background:#E8F5E9; border-left-color:{GREEN};'><strong>🟢 Tier 1 — Invest Now</strong></div>", unsafe_allow_html=True)
        for _,r in countries[countries.tier==1].sort_values("total",ascending=False).iterrows():
            with st.expander(f"{r.flag} {r.country} — {r.total}/20"):
                st.markdown(f"**Action:** {r.action}")
                st.markdown(f"**Rec:** {r.rec}")
    with c2:
        st.markdown(f"<div class='card' style='background:#FEF9E7; border-left-color:{AMBER};'><strong>🟡 Tier 2 — Resolve Blockers</strong></div>", unsafe_allow_html=True)
        for _,r in countries[countries.tier==2].sort_values("total",ascending=False).iterrows():
            with st.expander(f"{r.flag} {r.country} — {r.total}/20"):
                st.markdown(f"**Blocker:** {r.risk_note}")
                st.markdown(f"**Rec:** {r.rec}")
    with c3:
        st.markdown(f"<div class='card' style='background:#FDEDEC; border-left-color:{RED};'><strong>🔴 Tier 3 — Stabilize/Exit</strong></div>", unsafe_allow_html=True)
        for _,r in countries[countries.tier==3].sort_values("total",ascending=False).iterrows():
            with st.expander(f"{r.flag} {r.country} — {r.total}/20"):
                st.markdown(f"**Action:** {r.action}")
                st.markdown(f"**Rec:** {r.rec}")

    st.markdown("---")
    st.markdown(f"<div style='font-weight:700; color:{NAVY}; margin-bottom:8px;'>Sector Benchmarks</div>", unsafe_allow_html=True)
    bm = pd.DataFrame({
        "Organization":["Mentors International","BRAC Graduation Approach","Opportunity International","TechnoServe"],
        "Income Increase":["53% (Year 1)*","38% (over 4 yrs)","~25% (Year 1)","~20% (Year 1)"],
        "Cost/yr":["$150","$300–500","$400–600","$200–400"],
        "Countries":["12","14","30+","25+"],
        "Data":["Self-reported","Independently verified","Partner-delivered","Technical assistance"],
    })
    st.dataframe(bm, use_container_width=True, hide_index=True)
    st.caption("* Mentors outcomes are self-reported for FY2025. Independent verification would significantly strengthen institutional partner conversations.")
    st.markdown("---")
    st.caption(f"UCLA Anderson SICC · Spring 2026 · {len(ecosystem)} organizations in ecosystem DB · {len(partners)} named partners · 3 CD interviews completed · Final presentation June 10")
