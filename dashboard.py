import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

# ── EMBEDDED DATA ──
CRITERION_INSIGHTS = {
    "c1": "Criterion 1 — Mission Alignment: Overall Insight\n\nAcross Criterion 1, a clear regional pattern emerged between Latin America and Africa. Latin American ecosystems—particularly stronger markets such as Colombia, Ecuador, Peru, and the Dominican Republic—tended to feature dense institutional ecosystems dominated by MFIs and other large-scale organizations capable of supporting structured partnership models. These ecosystems often combined both strong alignment and operational maturity, creating clearer pathways for rapid institutional scaling.\n\nIn contrast, many African countries demonstrated highly mission-aligned NGO ecosystems, often centered around entrepreneurship development, women’s empowerment, and community-based support models. However, these ecosystems were generally more fragmented, with fewer large-scale anchor institutions and greater reliance on relationship-building across multiple partners. As a result, African markets may offer stronger grassroots alignment with MI’s mentoring philosophy, while Latin American markets may provide more immediate scale through institutional partnerships.\n\nA second pattern emerging across the analysis was the distinction between three partner archetypes:\n\n1. Scale Engines (large MFIs, government-linked institutions, corporates) that provide volume but may have somewhat lower alignment;\n2. Ideal Model Partners (faith-based MFIs, women-focused groups, entrepreneur NGOs) that most closely reflect MI’s relational mentoring model; and\n3. Ecosystem Enablers (INGOs, associations, chambers, networks) that may not directly drive socio growth but can strengthen access, credibility, and ecosystem reach.\n======",
    "c2": "Criterion 2 — Volume Potential: Overall Insight\n\nCriterion 2 revealed that the strongest scale opportunities were generally concentrated in Latin American markets with mature MFI ecosystems and larger institutional infrastructure. Countries such as Brazil, Ecuador, Colombia, and the Dominican Republic consistently demonstrated high estimated socio capacity, multiple scalable high-fit organizations, and relatively diversified scale pathways. These ecosystems appear particularly well-suited for rapid scaling through institutional partnerships capable of reaching large numbers of socios efficiently.\n\nBy contrast, many African markets demonstrated more distributed and fragmented scale ecosystems. Countries like Kenya and Ghana showed strong alignment and meaningful scale potential, but growth was often spread across multiple mid-sized organizations rather than concentrated among dominant anchor institutions. While this may create greater resilience and mission alignment, it may also require more intensive partnership development and ecosystem coordination to achieve comparable scale.\n\nThe analysis also surfaced an important strategic tradeoff between speed of scale and depth of alignment. Larger institutional partners—particularly MFIs and corporate-linked organizations—may accelerate socio growth significantly, but often with somewhat less direct alignment to MI’s mentoring-centered model. Smaller NGO and entrepreneur-support organizations may offer stronger mission alignment and participant engagement, though scaling through these partners may require a more relationship-intensive approach.\n======",
    "c3": "Criterion 3 — Socio Profile Fit & Density: Overall Insight\n\nAcross Criterion 3, many African countries demonstrated exceptionally strong demographic alignment with MI’s target population due to high rates of vulnerability, rapid urbanization, and elevated levels of self-employment. Countries such as Kenya and Ghana, in particular, produced very large estimated urban micro-entrepreneur populations, suggesting strong underlying demand for entrepreneurship-focused support models. These markets often reflected strong grassroots alignment with MI’s mission and target demographic, particularly among urban and semi-urban populations engaged in informal or necessity-driven entrepreneurship.\n\nAt the same time, the analysis also highlighted an important distinction between need and serviceability. While some countries demonstrated extremely high levels of poverty and vulnerability, the framework identified that populations facing severe multidimensional deprivation may require more intensive support systems beyond mentoring alone. This was particularly visible in countries such as Malawi, where strong demographic opportunity was partially offset by higher “friction risk” indicators related to extreme poverty and structural constraints.\n\nIn contrast, many Latin American countries paired strong demographic fit with larger urban populations and more mature institutional ecosystems, potentially creating more scalable operating environments despite somewhat lower vulnerability levels. Countries such as Brazil, Colombia, and Peru combined large urban entrepreneur populations with more moderate poverty conditions, suggesting that participants may be both economically vulnerable enough to benefit from MI’s model while still possessing the stability necessary to engage consistently in entrepreneurship programming.\n\nTogether, these findings reinforce a broader strategic tradeoff emerging throughout the analysis: African markets may offer stronger grassroots alignment and mission fit, while Latin American markets may provide clearer pathways to rapid scale through larger urban populations, stronger institutional infrastructure, and more serviceable operating conditions for virtual and partnership-based delivery models.\n======",
    "c4": "Criterion 4 — Digital Readiness: Overall Insight\n\nCriterion 4 highlighted substantial differences in digital infrastructure and virtual delivery readiness across countries. Larger Latin American markets generally performed very strongly, combining high internet penetration, strong 4G infrastructure, good affordability, and relatively advanced digital engagement behaviors. Countries such as Brazil, Mexico, and the Dominican Republic appear particularly well-positioned for scalable virtual mentoring models with minimal operational friction.\n\nSeveral African countries demonstrated more mixed digital readiness profiles. In countries like Kenya and Ghana, strong mobile infrastructure and growing digital ecosystems created promising conditions for virtual engagement, even where broader internet penetration or affordability remained more constrained. In many cases, populations appeared highly familiar with mobile-based technology and digital finance despite lower overall connectivity levels, suggesting that lightweight, mobile-first delivery models may be especially effective.\n\nThe analysis suggests that digital readiness is not solely determined by infrastructure availability, but also by affordability, digital literacy, and applied digital behaviors. Countries with strong mobile-money ecosystems and practical digital engagement may be more prepared for virtual mentoring than internet penetration rates alone would suggest. Overall, the findings reinforce that virtual scalability will likely require different delivery models by region, ranging from highly scalable digital programming in stronger markets to more hybrid or onboarding-intensive approaches in lower-readiness environments.\n======",
    "c5": "Criterion 5 — Political and Operating Risk: Overall Insight\n\nCriterion 5 revealed substantial variation in the political and operating environments across countries, particularly around institutional stability and civic openness. Countries such as Cape Verde, Ghana, South Africa, and the Dominican Republic demonstrated relatively favorable operating environments characterized by political openness, stable governance structures, and supportive conditions for NGO activity. These environments appear well-suited for long-term partnership development and sustained program implementation.\n\nIn contrast, several countries faced elevated operating risks due to either institutional fragility, restrictive civic environments, or both. Nicaragua and Cambodia stood out as particularly restrictive environments for civil society organizations, while countries such as Kenya, Honduras, and Guatemala demonstrated greater operational uncertainty driven by political instability, governance concerns, or security risks. These conditions do not necessarily prevent implementation, but they increase the importance of strong local partnerships, adaptive operating models, and ongoing risk management.\n\nA broader pattern emerging from the analysis is that strong mission alignment or scale potential does not always correlate with low operational risk. Several highly attractive markets from a demographic or ecosystem perspective also carry elevated political or regulatory complexity. As a result, country prioritization may ultimately require balancing growth opportunity against operational resilience, implementation flexibility, and long-term partnership sustainability.\n======",
    "c6": "Criterion 6 — Legal + Structural Constraints on Revenue-Generating NGOs: Overall Insight\n\nAcross Criterion 6, most countries demonstrated moderate legal feasibility for MI’s revenue-generating nonprofit model. In nearly all markets assessed, nonprofits were legally permitted to engage in earned-income activities under certain restrictions, suggesting that outright legal prohibition is generally not the primary barrier to implementation. Instead, differences across countries were driven more by operational complexity, regulatory predictability, and whether additional legal entities or hybrid structures were required.\n\nCountries such as South Africa and the Dominican Republic emerged as particularly favorable environments due to stronger regulatory quality and lower structural complexity, supporting more flexible and efficient implementation. In contrast, countries such as Mexico and Nicaragua introduced greater administrative and legal complexity through additional entity requirements or weaker regulatory environments.\n\nOverall, the analysis suggests that MI’s model is legally feasible across most target markets, but countries with stronger regulatory environments and simpler operating structures may offer faster and more operationally efficient pathways to scale.\n======",
}

COUNTRY_NOTES = {
    "Colombia": {
        "c1": "Colombia — 9.2 (Exceptional)\n\nColombia performed exceptionally well because it combined both quality and diversity of partners. It had multiple ideal-fit organizations across both MFIs and NGOs, which was relatively rare among countries assessed. The ecosystem included strong organizations such as WWB, Banco W, Interactuar, and Carvajal, creating a highly diversified and scalable partnership environment with broad alignment to MI’s model. Colombia also stood out for its unusually mature institutional ecosystem, where large MFIs and NGOs frequently coexist, supporting both strong alignment and scalable partnership pathways.\n======",
        "c2": "Colombia — 8.3 (Strong)\n\nColombia performed very strongly due to its combination of large, scalable partners and ecosystem diversity. It had 10 scalable high-fit partners, multiple anchor organizations, strong estimated socio capacity, and relatively low concentration risk. The ecosystem appeared both broad and resilient, meaning MI could scale through multiple pathways rather than relying heavily on a small number of institutions.\n======",
        "c3": "Colombia — 8.8 (Exceptional)\n\nColombia performed exceptionally well because it combines a very large urban population with moderate vulnerability and strong levels of self-employment. Importantly, poverty levels appear substantial enough to create demand for MI’s services without reaching levels that would severely constrain business participation. The result is a highly scalable and serviceable urban entrepreneur market.\n======",
        "c4": "Colombia — 7.7 (Strong)\n\nColombia performed strongly across nearly all digital readiness dimensions. The country combines solid internet usage, good 4G coverage, strong affordability, and high levels of digital literacy and consumer readiness. These factors suggest that virtual mentoring delivery would be highly feasible with relatively limited friction, particularly within urban populations already accustomed to engaging digitally.\n======",
        "c5": "Colombia — 5.5 (Moderate)\n\nColombia demonstrated moderate political and operational risk. While the country benefits from a relatively open civic environment and strong institutional infrastructure, lingering fragility and regional security concerns continue to create some operational uncertainty. NGOs can generally operate effectively, though implementation may require active risk management and careful partner selection depending on geography.\n======",
        "c6": "Colombia — 6.8 (Moderate)\n\nColombia showed a moderately strong legal environment for revenue-generating nonprofits. Nonprofits are generally permitted to engage in earned-income activities with appropriate compliance structures, and the country benefits from relatively solid regulatory quality compared to many peer markets. While some structural considerations may still arise depending on implementation design, the environment appears broadly supportive of MI’s model.\n======",
        "overall": "Colombia — 7.94\n\nColombia emerged the strongest overall markets (when considering countries where MI is currently operating) due to its unusually balanced combination of strong mission alignment, high scale potential, large urban entrepreneur population, and solid digital readiness. The country benefits from a mature institutional ecosystem where large MFIs and NGOs coexist, supporting both rapid scaling opportunities and strong partnership quality. Moderate political risk remains the primary constraint but appears manageable within an otherwise highly attractive ecosystem.\n======",
    },
    "Peru": {
        "c1": "Peru — 7.3 (Strong)\n\nPeru received a strong score due to a solid number of high-alignment organizations, including Pro Mujer and Manuela Ramos. However, much of the ecosystem was dominated by MFIs that were considered more “adjacent” than perfectly aligned with MI’s mentoring-driven model. The ecosystem supported strong partnership opportunities overall, though with somewhat less ideal alignment than top-tier countries.\n======",
        "c2": "Peru — 7.0 (Strong)\n\nPeru demonstrated strong scale potential with multiple scalable high-fit organizations and solid estimated socio capacity. The country also benefited from relatively distributed scale capacity across organizations, reducing reliance on any single institution. While Peru lacked the very largest anchor ecosystem seen in Brazil or Ecuador, the country still appeared well-positioned for scalable growth.\n======",
        "c3": "Peru — 8.4 (Strong)\n\nPeru scored strongly because it combines a large urban population with moderate vulnerability and high levels of self-employment. The resulting urban microentrepreneur segment was both substantial and serviceable, with poverty levels remaining meaningful enough to support MI’s relevance without creating excessive operational friction.\n======",
        "c4": "Peru — 7.5 (Strong)\n\nPeru showed strong digital readiness with good internet penetration, reliable infrastructure coverage, and relatively high digital literacy indicators. Applied digital behavior was also moderately strong, suggesting growing comfort with digital tools and online economic activity. Overall, the country appears well-positioned for virtual delivery with only modest adaptation needs.\n======",
        "c5": "Peru — 6.1 (Moderate)\n\nPeru demonstrated moderate operational risk due to recurring political instability despite maintaining a relatively open civic environment. NGOs can generally operate effectively, though changing political dynamics and institutional volatility may create periodic uncertainty that requires active monitoring and flexible partnership strategies.\n======",
        "c6": "Peru — 6.9 (Moderate)\n\nPeru demonstrated a relatively favorable legal environment for MI’s model. Nonprofits are generally able to engage in revenue-generating activities with manageable compliance considerations, and the country benefits from comparatively strong regulatory quality indicators. While some structural planning may still be necessary, the overall environment appears supportive of implementation and scaling.\n======",
        "overall": "Peru — 7.23\n\nPeru emerged as a strong overall market due to its balanced performance across nearly all criteria. The country combines strong demographic fit, scalable institutional partnerships, solid digital readiness, and manageable legal complexity. While some political instability remains, Peru appears well-positioned for partnership-based expansion with relatively moderate operational friction.\n======",
    },
    "Kenya": {
        "c1": "Kenya — 8.0 (Strong)\n\nKenya emerged as one of the strongest ecosystems in Africa due to its combination of highly aligned NGOs and scalable implementation potential. Organizations like Hand in Hand and SHOFCO demonstrated strong mission alignment with MI’s relational entrepreneurship model, while the broader ecosystem offered scalable urban entrepreneurship solutions. Although Kenya only had one “ideal fit” organization under the strict scoring framework, the broader ecosystem demonstrated unusually strong alignment across NGOs and entrepreneur-support organizations, creating a highly compatible partnership environment even if scale is somewhat more fragmented than in Latin America.\n======",
        "c2": "Kenya — 8.2 (Strong)\n\nKenya emerged as one of the strongest African markets for scale potential. It combined multiple scalable high-fit organizations with several anchor partners and strong estimated annual socio capacity. Importantly, Kenya’s scale potential was distributed across a broad set of aligned organizations rather than concentrated among only one or two dominant institutional players, creating both strong growth potential and ecosystem resilience. This differs somewhat from many Latin American markets, where scale is often driven through larger institutional partnerships.\n======",
        "c3": "Kenya — 9.6 (Exceptional)\n\nKenya ranked among the strongest countries because it combined rapid urban growth, high vulnerability, and extremely high self-employment rates. These factors produced one of the largest estimated urban microentrepreneur populations in the analysis. Although multidimensional poverty remains significant, conditions were still viewed as sufficiently serviceable for entrepreneurship-focused programming, creating very strong alignment with MI’s model.\n======",
        "c4": "Kenya — 6.4 (Moderate)\n\nKenya presented an interesting digital profile characterized by strong infrastructure coverage but comparatively lower internet penetration and digital readiness among the broader population. Despite these constraints, applied digital behavior was relatively strong, reflecting Kenya’s broader mobile-money ecosystem and familiarity with mobile technology. Virtual delivery appears viable but may require more participant support and adaptation than top-performing digital markets.\n======",
        "c5": "Kenya — 2.6 (Very Weak)\n\nKenya received one of the weaker scores due primarily to high fragility indicators despite a somewhat more open operating environment than several peer countries. Political tensions, periodic instability, and governance concerns may create meaningful operational risks for NGOs, particularly when scaling nationally or relying on long-term continuity across regions.\n======",
        "c6": "Kenya — 6.0 (Moderate)\n\nKenya demonstrated moderate legal feasibility for MI’s operating model. Revenue-generating nonprofit activity is generally permitted with restrictions, and implementation may require careful structuring depending on the nature of earned-income activities. While the broader legal framework appears workable, somewhat weaker regulatory predictability may increase operational complexity over time.\n======",
        "overall": "Kenya — 7.22\n\nKenya emerged as one of the strongest African markets overall due to its exceptional demographic alignment, strong mission fit, and meaningful scale potential. The country benefits from a highly aligned NGO ecosystem and one of the largest estimated urban microentrepreneur populations in the analysis. While political risk and moderate digital readiness create some operational complexity, Kenya remains one of the clearest opportunities for mission-aligned expansion in Africa.\n======",
    },
    "Dominican Republic": {
        "c1": "Dominican Republic — 7.7 (Strong)\n\nThe Dominican Republic scored strongly due to a dense and highly aligned MFI ecosystem, including organizations like ADOPEM, BANFONDESA, and Esperanza. The country also benefited from complementary NGO partners, creating strong partnership availability and consistency. While the ecosystem leaned heavily toward MFIs rather than a broader mix of partner types, the country benefits from the type of dense institutional infrastructure that may support relatively rapid scaling through partnership-based delivery models.\n======",
        "c2": "Dominican Republic — 8.1 (Strong)\n\nThe Dominican Republic showed strong volume potential because of its dense MFI ecosystem and several highly scalable anchor organizations. The country had high estimated socio capacity and a strong average scale score among aligned organizations. Scale potential was concentrated in a relatively small number of large institutions, but overall diversification remained strong enough to support resilient growth.\n======",
        "c3": "Dominican Republic — 3.5 (Weak)\n\nThe Dominican Republic’s score was significantly reduced by a “Low Need Risk” penalty. Although the country has a moderate urban population and reasonable self-employment levels, vulnerability and multidimensional poverty indicators were relatively low, suggesting the target population may be comparatively less aligned with MI’s poverty-focused model. This reduced the perceived relevance and urgency of MI’s intervention.\n======",
        "c4": "Dominican Republic — 8.9 (Exceptional)\n\nThe Dominican Republic emerged as one of the strongest countries for digital readiness due to exceptionally high internet usage, near-universal 4G coverage, and strong digital literacy indicators. Applied digital behavior was also relatively advanced, suggesting that socios are already comfortable using technology for practical and economic activities. Together, these factors indicate that virtual delivery could scale very efficiently with minimal adaptation.\n======",
        "c5": "Dominican Republic — 8.3 (Strong)\n\nThe Dominican Republic scored strongly due to its relatively stable political environment and generally open operating conditions for NGOs. While not entirely risk-free, the country appears conducive to sustained program delivery and partnership-building with limited likelihood of major operational disruption.\n======",
        "c6": "Dominican Republic — 7.2 (Strong)\n\nThe Dominican Republic emerged as one of the stronger legal environments in the analysis due to relatively favorable regulatory quality and manageable structural complexity. Revenue generation by nonprofits is generally feasible with limited additional structuring requirements, creating a comparatively enabling environment for implementation and long-term operational planning.\n======",
        "overall": "Dominican Republic — 7.15\n\nThe Dominican Republic scored strongly due to its dense and scalable institutional ecosystem, excellent digital readiness, and favorable operating environment. Large MFI partners create clear pathways for rapid scale through institutional partnerships. While the country’s lower poverty and vulnerability indicators slightly reduced demographic alignment with MI’s target population, the overall environment remains highly conducive to efficient implementation and growth.\n======",
    },
    "Cambodia": {
        "c1": "Cambodia — 8.7 (Strong)\n\nCambodia scored highly because it had a relatively large number of high-fit organizations (14) and several ideal-fit partners (4), including standout organizations like SHE Investments and Friends International. The ecosystem showed good overall alignment quality, but the comments suggest that many organizations still fell into the “moderate fit” range (2–3 alignment), making the ecosystem somewhat less consistently aligned than top-tier countries like Ecuador or Brazil. Strong anchor organizations boosted the score substantially.\n======",
        "c2": "Cambodia — 6.7 (Moderate)\n\nCambodia demonstrated moderate-to-strong scale potential driven by several scalable, high-fit organizations and an estimated annual socio capacity of roughly 9,000. The country benefited from a relatively distributed ecosystem with 10 organizations capable of supporting meaningful throughput. However, average scale scores remained moderate and the ecosystem lacked the depth of large anchor institutions seen in top-performing countries, limiting its ability to scale rapidly without significant coordination across partners.\n======",
        "c3": "Cambodia — 7.2 (Strong)\n\nCambodia scored strongly because it has a sizable and growing urban vulnerable population with high levels of self-employment, creating a meaningful pool of urban microentrepreneurs aligned with MI’s target demographic. While poverty levels remain significant, they were not deemed severe enough to create major engagement barriers, allowing Cambodia to maintain a strong balance between need and serviceability.\n======",
        "c4": "Cambodia — 7.0 (Strong)\n\nCambodia demonstrated strong digital readiness relative to many peer countries due to near-universal 4G coverage, reasonable affordability, and growing levels of digital engagement. While internet usage and digital purchasing behavior remain moderate, the country appears sufficiently connected to support virtual mentoring with relatively limited adaptation. Continued onboarding and lightweight technical support may still be beneficial for some participant segments.\n======",
        "c5": "Cambodia — 2.8 (Very Weak)\n\nCambodia scored poorly on political and operating risk due to a combination of high state fragility and a highly restrictive political environment. Freedom House indicators suggest significant constraints on civil liberties and civic participation, creating elevated risk for NGOs operating independently or engaging in community-based programming. Although organizations can still operate in-country, the environment may require careful navigation, strong local partnerships, and ongoing risk monitoring.\n======",
        "c6": "Cambodia — 5.3 (Weak)\n\nCambodia demonstrated moderate-to-elevated legal and structural complexity for revenue-generating nonprofits. While nonprofits are generally permitted to generate revenue under certain conditions, implementation may require careful structuring, compliance oversight, and ongoing regulatory navigation. Combined with relatively weak regulatory quality indicators, the environment may create additional administrative friction for scaling MI’s model.\n======",
        "overall": "Cambodia — 6.50\n\nCambodia emerged as a moderate opportunity driven by strong mission alignment, solid demographic fit, and growing digital readiness. The country benefits from several highly aligned entrepreneur-support organizations and a meaningful urban microentrepreneur population. However, weaker political openness, regulatory complexity, and a more fragmented ecosystem reduce operational confidence and long-term scalability relative to stronger-performing markets.\n======",
    },
    "Ghana": {
        "c1": "Ghana — 4.1 (Weak)\n\nGhana received a weaker score because the ecosystem lacked depth despite having one standout partner (Sinapi Aba). Most organizations were rated as moderate-fit (3–4 alignment) rather than ideal-fit organizations, limiting the overall weighted alignment score. While several organizations demonstrated meaningful alignment, the ecosystem lacked the density and institutional scale seen in stronger Latin American markets, resulting in a more fragmented partnership landscape overall.\n======",
        "c2": "Ghana — 4.6 (Weak)\n\nGhana’s scale potential was limited by the small number of scalable, high-fit organizations despite the presence of a few large anchor institutions. Much of the country’s potential scale was concentrated among only a handful of organizations, creating elevated dependency risk. While some organizations were individually strong, the broader ecosystem lacked sufficient depth for broad-based scaling.\n======",
        "c3": "Ghana — 9.4 (Exceptional)\n\nGhana emerged as one of the strongest countries under this criterion due to its combination of rapid urban growth, high vulnerability, and very high self-employment rates. Together, these factors created a very large estimated urban microentrepreneur segment. While poverty levels remain high, they were still viewed as compatible with entrepreneurial engagement rather than prohibitive, making Ghana an especially attractive market from a socio-demographic perspective.\n======",
        "c4": "Ghana — 7.1 (Strong)\n\nGhana demonstrated strong digital readiness driven by excellent 4G infrastructure and growing internet penetration. Although affordability remains somewhat weaker than in leading Latin American markets, digital access and usability indicators suggest that virtual mentoring is increasingly viable. Some onboarding or lower-bandwidth adaptations may still be needed for more vulnerable participant populations.\n======",
        "c5": "Ghana — 8.8 (Exceptional)\n\nGhana ranked among the strongest countries on political and operating risk due to its relatively stable governance environment and high levels of political openness. The country is widely viewed as one of the more stable democracies in the region, creating favorable conditions for NGO activity, partnership development, and long-term program continuity.\n======",
        "c6": "Ghana — 6.5 (Moderate)\n\nGhana demonstrated a moderately favorable environment for nonprofit revenue generation. While nonprofits may engage in earned-income activities under certain restrictions, implementation would likely require ongoing compliance management and careful structuring. Regulatory quality was relatively solid overall, supporting a generally workable—though not frictionless—operating environment.\n======",
        "overall": "Ghana — 6.44\n\nGhana demonstrated strong demographic alignment, political stability, and growing digital readiness, making it one of the more attractive African markets in the analysis. The country benefits from a large vulnerable urban entrepreneur population and strong mission fit among several organizations. However, a more fragmented ecosystem and lower institutional scale capacity may require a more relationship-intensive approach to scaling compared to stronger Latin American markets.\n======",
    },
    "Mexico": {
        "c1": "Mexico — 6.7 (Moderate)\n\nMexico performed moderately well because it combined several highly aligned NGO-type organizations (such as CREA and ProEmpleo) with substantial scale potential. The country had multiple ideal-fit organizations, but the overall ecosystem concentration of high-fit organizations was lower than stronger-performing countries. The ecosystem appears promising but would require more targeted partner prioritization.\n======",
        "c2": "Mexico — 5.8 (Moderate)\n\nMexico demonstrated moderate scale potential supported by several high-quality organizations operating at relatively large scale. However, the ecosystem was somewhat dependent on a smaller number of organizations, creating moderate concentration risk. The country appears capable of supporting meaningful growth, though likely through careful partner prioritization rather than broad ecosystem expansion.\n======",
        "c3": "Mexico — 7.5 (Strong)\n\nMexico scored strongly because of its enormous urban population, which generated a very large estimated urban microentrepreneur segment even with relatively lower vulnerability and self-employment rates. However, the country received a “Low Need Risk” penalty because poverty indicators were comparatively low, suggesting that some urban populations may be less aligned with MI’s target demographic despite the country’s sheer scale potential.\n======",
        "c4": "Mexico — 9.2 (Exceptional)\n\nMexico ranked among the strongest countries for digital readiness due to high internet penetration, strong infrastructure coverage, excellent affordability, and high levels of consumer digital readiness. Applied digital behavior was also relatively advanced, suggesting that participants are already comfortable engaging online for economic activities. These conditions create a highly favorable environment for scalable virtual mentoring delivery.\n======",
        "c5": "Mexico — 6.3 (Moderate)\n\nMexico demonstrated a moderate operating environment characterized by relatively stable institutions but meaningful regional security and governance challenges. NGOs generally operate freely, particularly within urban areas, though operational risk may vary substantially by geography. Overall, the country appears manageable from a risk perspective with appropriate partner selection and localized risk mitigation.\n======",
        "c6": "Mexico — 4.8 (Weak)\n\nMexico demonstrated greater structural complexity than many peer countries because revenue-generating activities may require the use of additional legal entities depending on organizational design and tax structure. While the broader regulatory environment is reasonably functional, the need for separate or hybrid structures may increase administrative burden, legal complexity, and implementation timelines.\n======",
        "overall": "Mexico — 6.21\n\nMexico demonstrated strong digital readiness, a massive urban population, and meaningful institutional scale potential. However, lower mission alignment scores and increased legal complexity surrounding revenue-generating nonprofit structures reduced its overall ranking relative to stronger Latin American peers. The country appears operationally viable but may require more structured implementation planning and institutional alignment.\n======",
    },
    "Honduras": {
        "c1": "Honduras — 8.3 (Strong)\n\nHonduras scored highly because of its strong concentration of highly aligned organizations relative to ecosystem size. Organizations such as CDE MIPYME, Pro Mujer, and VisionFund contributed to a very high percentage of high-fit partners (nearly 79%). Although the overall ecosystem was smaller and thinner than countries like Colombia or Brazil, the organizations that did exist were strongly aligned with MI’s model.\n======",
        "c2": "Honduras — 5.2 (Moderate)\n\nHonduras showed moderate scale potential. While the ecosystem lacked large anchor organizations, it benefited from a broad distribution of mid-sized organizations capable of serving socios. The relatively low concentration risk strengthened the country’s resilience, but the absence of very large-scale institutions reduced the ability to scale rapidly.\n======",
        "c3": "Honduras — 6.6 (Moderate)\n\nHonduras scored moderately well because of its growing urban population and relatively high vulnerability levels, which produced a meaningful urban microentrepreneur segment. However, the overall market size remained smaller than stronger-performing countries, limiting long-term scale potential despite reasonable demographic alignment.\n======",
        "c4": "Honduras — 5.3 (Weak)\n\nHonduras demonstrated weaker digital readiness primarily due to affordability constraints and relatively low levels of applied digital behavior. Although network infrastructure coverage was fairly strong, practical engagement with digital tools remained limited among the target population. As a result, virtual mentoring may require significant simplification, onboarding, or hybrid delivery models to ensure consistent participation.\n======",
        "c5": "Honduras — 4.1 (Weak)\n\nHonduras scored poorly because of both elevated fragility and a relatively constrained civic environment. Political instability, governance concerns, and security risks may complicate long-term program implementation and partnership development. Although meaningful NGO work remains possible, operations would likely require careful oversight and strong local relationship management.\n======",
        "c6": "Honduras — 5.3 (Weak)\n\nHonduras demonstrated relatively weak legal and structural conditions for revenue-generating nonprofit activities. Although earned-income models are generally possible, the combination of lower regulatory quality and potential structural ambiguity may create administrative and compliance burdens that complicate implementation and scaling efforts.\n======",
        "overall": "Honduras — 5.92\n\nHonduras scored moderately due to strong mission alignment and a concentrated ecosystem of highly aligned organizations. However, weaker digital readiness, elevated political risk, and lower institutional scale capacity reduced overall attractiveness. The country may support targeted partnership opportunities but would likely require careful operational management and more gradual scaling strategies.\n======",
    },
    "Guatemala": {
        "c1": "Guatemala — 4.3 (Weak)\n\nGuatemala showed some promising MFI partners, including Génesis and FINCA, but the ecosystem lacked broader NGO-type organizations that closely aligned with MI’s relational mentoring model. Many of the strongest organizations were also more rural-focused, reducing alignment with MI’s urban and semi-urban target population. As a result, the ecosystem was narrower and less balanced despite a few strong institutions.\n======",
        "c2": "Guatemala — 4.7 (Weak)\n\nGuatemala demonstrated moderate organizational scale quality, with aligned organizations tending to operate at relatively large scale. However, the ecosystem itself was small and heavily concentrated among a few organizations, increasing partnership dependency risk. The country would likely require significant reliance on a limited set of partners to achieve meaningful scale.\n======",
        "c3": "Guatemala — 6.9 (Moderate)\n\nGuatemala demonstrated moderate-to-strong potential with a meaningful urban vulnerable population and solid urban growth dynamics. However, lower self-employment rates and a somewhat smaller estimated target segment reduced its overall scale attractiveness relative to top-performing countries.\n======",
        "c4": "Guatemala — 5.8 (Moderate)\n\nGuatemala showed moderate digital readiness. While infrastructure coverage and affordability were reasonably solid, lower levels of internet usage and applied digital engagement suggest that virtual participation may be uneven across target populations. Virtual delivery appears feasible, though likely with more hybrid support and participant onboarding than stronger-performing countries.\n======",
        "c5": "Guatemala — 4.7 (Weak)\n\nGuatemala demonstrated elevated operational risk due to weaker political openness and ongoing institutional instability. While NGOs remain active in-country, governance challenges and regulatory uncertainty may create operational friction and increase the importance of strong local partnerships and adaptive risk management.\n======",
        "c6": "Guatemala — 6.0 (Moderate)\n\nGuatemala showed moderate legal feasibility for MI’s model. Revenue generation appears legally permissible but may require structural considerations and active compliance management depending on the organization’s operating model. Combined with somewhat weaker regulatory quality indicators, the environment may create moderate operational complexity for scaling activities.\n======",
        "overall": "Guatemala — 5.29\n\nGuatemala demonstrated moderate demographic potential and reasonable legal feasibility but was constrained by weaker institutional scale, moderate digital readiness, and elevated political and operational risk. The ecosystem includes several promising organizations, particularly within the MFI sector, but scaling may require more selective partnership development and operational support.\n======",
    },
    "Nicaragua": {
        "c1": "Nicaragua — 4.9 (Weak)\n\nNicaragua demonstrated strong mission alignment on paper, with several ideal-fit organizations, but the ecosystem was heavily concentrated in MFIs and lacked broader diversity among partner types. Political and operating environment concerns also reduced confidence in long-term scalability, particularly given that some organizations (Caritas, a potential partner) had reportedly been forced to close due to government pressures. This weakened the overall ecosystem strength despite some highly aligned partners.\n======",
        "c2": "Nicaragua — 4.6 (Weak)\n\nNicaragua’s scale potential was constrained by ecosystem concentration and limited organizational diversity. Although a few organizations demonstrated strong alignment and scale capacity, the country relied heavily on a narrow set of institutions. Political instability and organizational closures further increased the perceived risk of scaling through a concentrated ecosystem.\n======",
        "c3": "Nicaragua — 5.9 (Moderate)\n\nNicaragua demonstrated moderate potential due to a reasonably aligned vulnerable and self-employed urban population. However, the country’s relatively small urban market limited overall scale opportunity compared to larger regional peers. Structural poverty indicators were elevated but not severe enough to trigger a high-friction penalty.\n======",
        "c4": "Nicaragua — 4.4 (Weak)\n\nNicaragua demonstrated relatively weak digital readiness due to lower infrastructure quality, affordability constraints, and limited practical digital engagement among the population. While basic digital access exists, overall usability indicators suggest that virtual mentoring would face meaningful barriers and likely require substantial adaptation or supplemental support mechanisms.\n======",
        "c5": "Nicaragua — 2.8 (Very Weak)\n\nNicaragua emerged as one of the highest-risk operating environments in the analysis due to extremely low political openness and increasing restrictions on civil society organizations. Government actions toward NGOs and civic institutions create substantial uncertainty around long-term program viability, partnership continuity, and organizational independence. This environment presents significant barriers to sustained scaling and operational resilience.\n======",
        "c6": "Nicaragua — 3.0 (Very Weak)\n\nNicaragua emerged as one of the weakest legal environments in the analysis due to low regulatory quality and significant structural complexity surrounding nonprofit operations. Revenue generation may require additional legal entities and substantial compliance management, while the broader political environment creates additional uncertainty for long-term implementation. Together, these conditions create meaningful barriers to operational flexibility and scaling.\n======",
        "overall": "Nicaragua — 4.46\n\nNicaragua scored poorly due primarily to its highly restrictive political environment, weaker legal feasibility, and elevated operational risk for NGOs. Although the country demonstrated moderate demographic alignment and several promising organizations, institutional instability and regulatory uncertainty create significant barriers to sustainable scaling and partnership development.\n======",
    },
    "Malawi": {
        "c1": "Malawi — 4.0 (Weak)\n\nMalawi scored poorly primarily because the country’s population and organizational landscape are heavily rural, limiting alignment with MI’s urban and semi-urban focus. While a few strong organizations existed (such as FINCA and VisionFund), the ecosystem lacked sufficient density of urban microentrepreneur-focused organizations. Overall alignment skewed toward moderate rather than strong fit.\n======",
        "c2": "Malawi — 3.2 (Very Weak)\n\nMalawi scored poorly because of limited overall ecosystem scale capacity and extremely high concentration risk. The country had only a few scalable organizations and relied heavily on a small number of partners for potential growth. Combined with the country’s largely rural ecosystem, this substantially constrained MI’s ability to scale efficiently.\n======",
        "c3": "Malawi — 6.2 (Moderate)\n\nMalawi’s underlying demographic opportunity was actually quite strong due to extraordinarily high vulnerability and self-employment rates combined with rapid urban growth. However, the country received a substantial “High Friction Risk” penalty because multidimensional poverty indicators were exceptionally severe. This suggested that many potential participants may face constraints too significant for mentoring alone to address consistently, reducing overall feasibility despite strong need.\n======",
        "c4": "Malawi — 1.5 (Very Weak)\n\nMalawi scored extremely low on digital readiness due to very limited internet usage, weak affordability, low consumer readiness, and minimal applied digital engagement. Although basic network coverage exists, substantial structural barriers remain to consistent virtual participation. Virtual mentoring would likely require significant infrastructure support, simplified delivery methods, or alternative non-digital engagement models.\n======",
        "c5": "Malawi — 4.6 (Weak)\n\nMalawi demonstrated moderate-to-elevated operating risk. While the country maintains a relatively open civic environment, broader fragility indicators suggest institutional and economic instability that could affect long-term program consistency and operational reliability. NGOs can generally operate effectively, though resilience planning and flexible implementation models may be important.\n======",
        "c6": "Malawi — 5.4 (Weak)\n\nMalawi demonstrated moderate-to-weak legal feasibility due primarily to lower regulatory quality and institutional predictability. While nonprofits can generally engage in revenue-generating activities under certain conditions, the broader operating environment may create administrative friction and increase the need for strong local legal and compliance support.\n======",
        "overall": "Malawi — 4.22\n\nMalawi demonstrated strong underlying demographic need but faced significant structural constraints across multiple criteria. Extremely low digital readiness, elevated poverty-related friction risk, weaker scale potential, and moderate operational instability substantially reduced implementation feasibility. While the country reflects strong mission relevance, scaling MI’s model would likely require significant adaptation and support infrastructure.\n======",
    },
    "Cape Verde": {
        "c1": "Cape Verde — 1.0 (Very Weak)\n\nCape Verde received the lowest score due to an extremely limited partner ecosystem. Only one organization emerged as a strong fit (Pro Empresa), resulting in very low partner depth, weak weighted alignment, and minimal ecosystem diversity. While the one standout organization was promising, the country lacked enough viable partners to support scalable implementation.\n======",
        "c2": "Cape Verde — 1.0 (Very Weak)\n\nCape Verde scored extremely low because it lacked scalable, high-fit organizations and had virtually no estimated socio capacity. The ecosystem depended almost entirely on one smaller organization and showed minimal diversification or scale infrastructure. As a result, the country was not viewed as a viable scaling market under MI’s framework.\n======",
        "c3": "Cape Verde — 1.2 (Very Weak)\n\nCape Verde received a very low score due primarily to its extremely small urban population and correspondingly tiny estimated urban microentrepreneur segment. Although the country does not face major structural poverty constraints, the overall market size is simply too limited to support meaningful scale for MI’s model.\n======",
        "c4": "Cape Verde — 6.4 (Moderate)\n\nCape Verde demonstrated moderate digital readiness supported by relatively strong internet penetration and good consumer digital readiness. However, weaker infrastructure scale and limited available data on applied digital behaviors reduced confidence in the consistency of virtual engagement at scale. The country appears digitally viable, though its small overall ecosystem limits broader scalability.\n======",
        "c5": "Cape Verde — 10.0 (Exceptional)\n\nCape Verde emerged as the strongest operating environment in the analysis due to its combination of low fragility and exceptionally high political openness. The country demonstrated strong institutional stability, rule of law, and civil liberties protections, creating an enabling environment for NGOs and long-term partnership development. Operational risk appears minimal relative to peer countries.\n======",
        "c6": "Cape Verde — 6.8 (Moderate)\n\nCape Verde demonstrated a relatively favorable legal environment for nonprofit revenue generation. Although earned-income activities may still require compliance considerations depending on organizational structure, the country benefits from comparatively strong regulatory quality and institutional predictability. Overall, the environment appears manageable for implementation with limited structural complexity.\n======",
        "overall": "Cape Verde — 3.42\n\nCape Verde scored lowest overall primarily due to its very limited ecosystem scale and small target population. Although the country performs exceptionally well on political stability and regulatory openness, the market lacks sufficient partner depth and demographic scale to support meaningful expansion under MI’s model.\n======",
    },
    "Brazil": {
        "c1": "Brazil — 15.2 (Outlier / Exceptional)\n\nBrazil significantly outperformed every other country across nearly every metric. It had the highest number of high-fit organizations (19), ideal-fit organizations (13), weighted alignment score (33), and percentage of high-fit organizations (over 90%). The ecosystem appears exceptionally dense, diverse, and consistently aligned with MI’s model, creating unusually strong conditions for rapid scaling and low-friction partnership development.\n\nOne thing to flag analytically is that Brazil’s final score exceeds the intended 1–10 scale, which suggests the normalization and weighting framework is benchmarking against MI’s current countries of operation rather than potential expansion markets. Conceptually, however, the result clearly signals that Brazil emerged as the strongest ecosystem in the analysis.\n======",
        "c2": "Brazil — 13.4 (Outlier / Exceptional)\n\nBrazil substantially outperformed all other countries on scale potential. It had the highest number of scalable high-fit organizations, the highest number of anchor partners, the greatest estimated annual socio capacity, and the lowest concentration risk. The ecosystem demonstrated both exceptional depth and diversification, meaning MI could scale rapidly through many different pathways simultaneously.\n\nAs with Criterion 1, one thing to flag analytically is that Brazil’s final score exceeds the intended 1–10 scale, which suggests the normalization and weighting framework is benchmarking against MI’s current countries of operation rather than potential expansion markets. Conceptually, however, the result clearly signals that Brazil represents an unusually strong ecosystem across alignment, scale, and demographic opportunity relative to the broader country set analyzed. Brazil’s results also reinforce a broader pattern emerging across the analysis: Latin American ecosystems—particularly MFI-heavy markets—may offer the clearest pathway to rapid scale through institutional partnerships.\n======",
        "c3": "Brazil — 9.9 (Exceptional)\n\nBrazil achieved the highest score under this criterion because of its enormous urban population and massive estimated urban microentrepreneur segment. Although vulnerability and self-employment rates were more moderate than some African countries, the country’s sheer population scale created unmatched market potential. Importantly, poverty indicators suggested that the population remained highly serviceable for entrepreneurship-focused interventions without excessive structural barriers.\n======",
        "c4": "Brazil — 10.0 (Exceptional)\n\nBrazil achieved the highest digital readiness score in the analysis due to its combination of high internet usage, strong infrastructure coverage, advanced digital literacy, and exceptionally high levels of applied digital behavior. The country’s mature digital ecosystem suggests that virtual mentoring could scale efficiently and at large volume with minimal operational friction. Brazil also reinforces a broader pattern emerging throughout the framework: larger Latin American markets may offer not only strong institutional scale potential, but also the digital infrastructure necessary to support highly scalable virtual delivery models.\n======",
        "c5": "Brazil — 6.7 (Moderate)\n\nBrazil demonstrated a moderately favorable operating environment characterized by relatively open civic institutions and a well-developed NGO sector, balanced against moderate political and institutional volatility. NGOs generally maintain strong operational freedom, particularly within large urban centers, though political polarization and governance fluctuations may introduce some uncertainty over time. Overall, Brazil appears capable of supporting large-scale partnership development with manageable operational risk.\n======",
        "c6": "Brazil — 6.1 (Moderate)\n\nBrazil demonstrated a moderately favorable legal environment for revenue-generating nonprofits. While nonprofits can generally engage in earned-income activities under certain restrictions, implementation may still require careful legal structuring and compliance management depending on the model used. The country’s relatively large and mature nonprofit sector suggests that these complexities are manageable, though operational navigation may still require specialized local expertise.\n======",
        "overall": "Brazil — 11.04\n\nBrazil substantially outperformed all other countries across the combined framework due to its exceptional partner ecosystem, unmatched scale potential, enormous urban entrepreneur population, and highly advanced digital infrastructure. The country consistently demonstrated the strongest combination of institutional scale, demographic opportunity, and operational readiness in the analysis.\n\nImportantly, Brazil’s score exceeding the intended 1–10 scale reflects that the framework is benchmarking primarily against MI’s current countries of operation rather than larger potential expansion markets. Conceptually, however, the results clearly signal that Brazil represents an unusually strong ecosystem for rapid, partnership-driven scaling relative to the broader country set analyzed.\n======",
    },
    "Ecuador": {
        "c1": "Ecuador — 9.9 (Exceptional)\n\nEcuador scored near the top because it combined very strong partner quality, high ecosystem concentration, and multiple ideal-fit organizations. It had one of the highest weighted alignment scores and one of the highest percentages of high-fit organizations (70%). The ecosystem demonstrated both strong diversity and depth, making it one of the clearest fits for low-friction scaling and partnership development.\n======",
        "c2": "Ecuador — 9.0 (Exceptional)\n\nEcuador ranked among the strongest countries for volume potential due to its exceptionally high estimated socio capacity, large number of scalable organizations, and relatively low concentration risk. The ecosystem combined both strong scale and diversification, allowing for rapid expansion without overreliance on any one institution. Ecuador’s ecosystem appears particularly attractive because it combines strong alignment with the type of institutional density that may allow MI to scale relatively quickly through fewer, larger partnerships.\n======",
        "c3": "Ecuador — 6.8 (Moderate)\n\nEcuador demonstrated moderate-to-strong demographic potential with a reasonably large urban microentrepreneur segment and good levels of self-employment. However, the country’s smaller overall urban population and lower vulnerability indicators reduced its scale attractiveness relative to top-performing countries like Colombia, Kenya, or Brazil.\n======",
        "c4": "Ecuador — 7.5 (Strong)\n\nEcuador demonstrated strong digital readiness supported by good internet access, reliable infrastructure, and solid consumer digital readiness. The country’s digital profile suggests that virtual mentoring delivery would be broadly feasible across urban populations, particularly when paired with institutional partners already operating digitally enabled programming.\n======",
        "c5": "Ecuador — 6.7 (Moderate)\n\nEcuador showed a moderately favorable operating environment with manageable levels of fragility and a relatively open civic space. While some political and institutional volatility remains, the overall environment appears conducive to NGO activity and partnership development, particularly when paired with strong local implementation partners.\n======",
        "c6": "Ecuador — 5.3 (Weak)\n\nEcuador demonstrated moderate legal feasibility but somewhat weaker regulatory quality than several regional peers. Although nonprofits can generally engage in earned-income activities under certain restrictions, implementation may require careful compliance management and structural planning to navigate operational complexity effectively.\n======",
        "overall": "Ecuador — 7.90\n\nEcuador emerged as a strong overall expansion opportunity due to its exceptional partner ecosystem, high scale potential, strong digital readiness, and favorable demographic profile. The country combines strong alignment with relatively mature institutional infrastructure, creating a highly attractive environment for rapid partnership-driven scaling. Moderate political and regulatory complexity remain manageable relative to the country’s broader strengths.\n======",
    },
    "South Africa": {
        "c1": "South Africa — 8.8 (Exceptional)\n\nSouth Africa scored exceptionally well because of its strong combination of ideal-fit organizations, broad ecosystem depth, and consistently high alignment across organizations. The ecosystem demonstrated both quality and scalability, with a relatively high percentage of high-fit partners and strong organizational diversity that supports urban entrepreneurship programming.\n======",
        "c2": "South Africa — 7.0 (Strong)\n\nSouth Africa demonstrated strong scale potential primarily because aligned organizations tended to operate at very large scale, producing high estimated socio capacity despite relatively few scalable high-fit partners overall. The ecosystem appeared efficient and capable of supporting significant growth, though somewhat dependent on a limited number of larger institutions.\n======",
        "c3": "South Africa — 8.2 (Strong)\n\nSouth Africa scored strongly because its very large urban population and high vulnerability levels produced a sizable estimated urban microentrepreneur segment. While self-employment rates were lower than many peer countries, the sheer scale of the urban population compensated substantially. The country appeared to offer strong demographic opportunity without triggering major poverty-related friction concerns.\n======",
        "c4": "South Africa — 8.5 (Exceptional)\n\nSouth Africa scored exceptionally well because of its high internet penetration, excellent infrastructure coverage, and strong consumer digital readiness. The population also demonstrated relatively advanced applied digital behavior, indicating familiarity with using technology for economic activities. Together, these conditions create a highly scalable environment for virtual programming and digitally enabled mentoring models.\n======",
        "c5": "South Africa — 7.2 (Strong)\n\nSouth Africa scored strongly because of its relatively open political environment, strong constitutional protections, and established civil society sector. Although the country faces meaningful social and economic challenges, NGOs generally operate freely and at scale. Overall, the environment appears supportive of long-term partnership development and sustained program delivery.\n======",
        "c6": "South Africa — 7.8 (Strong)\n\nSouth Africa ranked among the strongest countries under this criterion because nonprofits are generally able to engage in revenue-generating activities without requiring additional legal entities. Combined with relatively solid regulatory quality and institutional predictability, the environment appears highly supportive of flexible implementation, operational efficiency, and long-term scaling.\n======",
        "overall": "South Africa — 7.81\n\nSouth Africa performed strongly across multiple dimensions, particularly digital readiness, political openness, legal feasibility, and demographic scale. The country benefits from a relatively mature civil society and enabling operating environment, supporting efficient implementation and virtual delivery models. While institutional scale was somewhat lower than top Latin American markets, South Africa appears highly attractive as a stable and scalable African expansion opportunity.\n======",
    },
}

ECO_RUBRICS = {
    "Tier": "Updated to Suggested Country Tiering System\n======",
    "Status": "If there was any crossover from MI's April Partnerships Reports, the status of the partnership was taken from the Reports\n======",
    "Alignment with MI (1-5)": "Alignment with Mentors International (1–5 Scoring Rubric)\n\n5 – Excellent Fit (Ideal Partner)\nDefinition: Fully aligned across all criteria with strong, direct synergy.\n\nMission is explicitly social / poverty alleviation focused\nCore work directly serves micro-entrepreneurs (not adjacent populations)\nStrong, active presence in urban or semi-urban areas\nClear and direct pipeline access to beneficiaries (large, reachable population)\nBeneficiaries would clearly and immediately benefit from MI’s mentoring (high complementarity)\nProgramming is highly complementary (mentorship would enhance—not duplicate—their work)\n\n\n4 – Very Good Fit\n\nDefinition: Meets most criteria well, with minor gaps or indirect elements.\n\nMission is social / poverty-focused, though may be broader than microenterprise\nWorks with micro-entrepreneurs OR closely adjacent groups (e.g., small business owners, informal workers)\nSolid presence in urban/semi-urban areas (but not exclusive)\nPipeline access is good but may require coordination\nMentoring would provide clear value-add, though not as immediately embedded as a “5”\n\n\n3 – Good Fit\n\nDefinition: Partial alignment; could be useful but with notable gaps.\n\nMission is may not focus primarily on economic empowerment and poverty alleviation\nEngagement with micro-entrepreneurs is indirect, occasional, or a subset\nUrban presence exists but may be limited, fragmented, or secondary\nPipeline access is uncertain, indirect, or relationship-dependent\nMentoring could add value, but fit is not obvious or central\n\n2 – Fair Fit\nDefinition: Meets minimum requirement (urban exposure with microentrepreneurs) but limited alignment otherwise.\n\nMission may be economic, institutional, or general development (not clearly poverty-focused)\nMinimal or unclear engagement with micro-entrepreneurs\nUrban presence exists, but not targeted or meaningful\nPipeline access is weak or difficult to access\nMentoring value is uncertain or marginal\n\n\n1 – Poor Fit\nDefinition: Does not meet core criteria.\n\nMission is not social / not poverty-focused\nNo meaningful work with micro-entrepreneurs\nNo relevant urban/semi-urban presence\nNo viable pipeline access\nMentoring would not be relevant or additive\n\n\n======",
    "Urban Relevance (1-5)": "% of work in urban / peri-urban microenterprise contexts \n\nThis is for context. Urban relevance was considered heavily in Alignment with MI\n\nScoring Rubric:\n5 - Highly Urban-Focused\n4 - Strong Urban Presence\n3 - Mixed (Urban & Rural)\n2 - Limited Urban Relevance\n1 - Not Urban-Relevant\n======",
    "Scale Potential (1-5)": "Estimated number of socios this organization can provide to MI\n\nScoring Rubric:\n5 - Excellent - 1000+ socios\n4 - Very Good - 500-999 socios\n3 - Good - 200-499 socios\n2- Fair - 500-199 socios\n1 - Poor - 0-49 socios\n\n======",
    "Geographic Reach": "Not necessarily important for quality of a partnership, but may support MI in determining who takes the lead in contacting (CD or HQ)\n\nScoring Rubric:\n4 - International\n3 - National\n2 - Regional\n1 - Local\n======",
    "Confirmed / Likely Urban & Peri-Urban Areas of Operation": "This column identifies the cities, metropolitan areas, townships, informal settlements, or peri-urban communities where each organization is confirmed or strongly believed to operate entrepreneurship, livelihoods, microfinance, or small business programming relevant to Mentors International’s target socio population. Locations were compiled using publicly available organizational information, program descriptions, branch networks, partnership announcements, and ecosystem research.\n======",
    "Confidence Level": "High = explicitly documented urban entrepreneur operations\nMedium = strong evidence but partly inferred\nLow = indirect or partner-driven footprint\n======",
}

st.set_page_config(
    page_title="Mentors International — Partnership Growth Framework",
    page_icon="🌍", layout="wide"
)

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
TIER_COLOR = {"Tier 1":GREEN,"Tier 2":AMBER,"Tier 3":RED,"Expansion":BLUE}
TIER_LABEL = {
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
    df['align_n'] = pd.to_numeric(df['align_n'], errors='coerce').fillna(0)
    df['scale_n'] = pd.to_numeric(df['scale_n'], errors='coerce').fillna(0)
    df['urban_n'] = pd.to_numeric(df['urban_n'], errors='coerce').fillna(0)
    return df

@st.cache_data
def load_eco_exp():
    df = pd.read_csv('eco_exp.csv')
    df['align_n'] = pd.to_numeric(df['align_n'], errors='coerce').fillna(0)
    df['scale_n'] = pd.to_numeric(df['scale_n'], errors='coerce').fillna(0)
    df['urban_n'] = pd.to_numeric(df['urban_n'], errors='coerce').fillna(0)
    return df

@st.cache_data
def load_pp():
    return pd.read_csv('priority_partners.csv')

scores   = load_scores()
expansion = load_expansion()
eco      = load_eco()
eco_exp  = load_eco_exp()
pp       = load_pp()

st.markdown(f"""
<style>
#MainMenu {{visibility:hidden;}}
footer {{visibility:hidden;}}
header[data-testid="stHeader"] {{display:none;}}
[data-testid="stSidebar"] {{display:none;}}
.block-container {{padding-top:0 !important; padding-bottom:2rem; max-width:1280px;}}
h1,h2,h3 {{color:{DBLUE};}}
.card {{background:{WHITE};border-radius:10px;padding:1rem 1.2rem;
        box-shadow:0 2px 8px rgba(0,0,0,0.07);margin-bottom:0.75rem;
        border-left:4px solid {BLUE};}}
.card-gold {{background:#FFFDF0;border-left:4px solid {GOLD};
             border-radius:10px;padding:1rem 1.2rem;margin-bottom:0.75rem;}}
.card-green {{background:#F0FAF4;border-left:4px solid {GREEN};
              border-radius:10px;padding:1rem 1.2rem;margin-bottom:0.75rem;}}
.card-blue {{background:#EEF5FC;border-left:4px solid {BLUE};
             border-radius:10px;padding:1rem 1.2rem;margin-bottom:0.75rem;}}
.kpi-card {{background:{WHITE};border-radius:10px;padding:1rem 0.8rem;
            text-align:center;box-shadow:0 2px 8px rgba(0,0,0,0.08);
            border-top:4px solid {BLUE};}}
.kpi-val {{font-size:1.9rem;font-weight:800;color:{BLUE};line-height:1.1;}}
.kpi-lab {{font-size:0.75rem;color:{MGREY};margin-top:4px;line-height:1.3;}}
.section-label {{font-size:0.65rem;font-weight:700;letter-spacing:2px;
                 color:{BLUE};text-transform:uppercase;margin-bottom:6px;display:block;}}
</style>""", unsafe_allow_html=True)

# ── TOP HEADER ────────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="background:linear-gradient(135deg,{DBLUE} 0%,#005080 100%);
            padding:0.8rem 1.4rem;border-bottom:3px solid {GOLD};">
  <span style="font-size:1.1rem;font-weight:900;color:{WHITE};">Mentors</span>
  <span style="font-size:1.1rem;font-weight:900;color:{GOLD};"> International</span>
  <span style="font-size:0.7rem;color:#CADCFC;margin-left:10px;">
    Partnership Growth Framework &nbsp;·&nbsp; Social Impact Consulting Corps (SICC) &nbsp;·&nbsp; UCLA Anderson &nbsp;·&nbsp; Spring 2026
  </span>
</div>""", unsafe_allow_html=True)

# ── HORIZONTAL NAV ────────────────────────────────────────────────────────────
page = option_menu(
    menu_title=None,
    options=["Overview","Framework","Country Briefs","Future Partnerships",
             "Partner Pipeline","Ecosystem Analysis","Recommendations","Appendix"],
    icons=["house","grid","globe","binoculars","people","bar-chart","lightbulb","paperclip"],
    default_index=0, orientation="horizontal",
    styles={
        "container":{"padding":"0","background-color":DBLUE},
        "icon":{"color":GOLD,"font-size":"0.8rem"},
        "nav-link":{"font-size":"0.78rem","color":"#CADCFC","padding":"8px 10px",
                    "text-align":"center"},
        "nav-link-selected":{"background-color":BLUE,"color":WHITE,"font-weight":"700"},
    }
)

def page_header(title, sub=None):
    sub_html = f'<div style="font-size:0.8rem;color:{MGREY};margin-top:3px;">{sub}</div>' if sub else ""
    st.markdown(f"""
<div style="padding:1rem 0 0.5rem;">
  <div style="font-size:1.4rem;font-weight:800;color:{DBLUE};">{title}</div>
  {sub_html}
  <div style="height:3px;background:linear-gradient(90deg,{BLUE},{GOLD},transparent);
              margin-top:6px;border-radius:2px;"></div>
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

def eco_table(df_in):
    """Display ecosystem database table with key columns."""
    col_map = {
        'Organization Name':'Organization',
        'Alignment with MI (1-5)':'Alignment',
        'Scale Potential (1-5)':'Scale',
        'Urban Relevance (1-5)':'Urban Relevance',
        'Confirmed / Likely Urban & Peri-Urban Areas of Operation':'Cities',
        'align_n':'Alignment Score',
        'scale_n':'Scale Score',
        'urban_n':'Urban Score',
    }
    desired = ['Country','Organization Name','Category','Status',
               'Alignment with MI (1-5)','Scale Potential (1-5)',
               'Urban Relevance (1-5)',
               'Confirmed / Likely Urban & Peri-Urban Areas of Operation',
               'Website','Notes']
    avail = [c for c in desired if c in df_in.columns]
    display = df_in[avail].rename(columns=col_map)
    sort_col = 'Alignment' if 'Alignment' in display.columns else display.columns[0]
    st.dataframe(display.sort_values(['Country', sort_col], ascending=[True,False]),
                 use_container_width=True, hide_index=True, height=480)

# ══════════════════════════════════════════════════════════════════════════════
# OVERVIEW
# ══════════════════════════════════════════════════════════════════════════════
if page == "Overview":
    page_header("Overview", "Mentors International · Partnership Growth Strategy · Spring 2026")

    st.markdown(f"""
<div style="background:linear-gradient(135deg,{DBLUE} 0%,#005080 100%);border-radius:12px;
            padding:1.4rem 1.8rem;margin-bottom:1rem;border-left:5px solid {GOLD};">
  <div style="font-size:0.65rem;color:{GOLD};letter-spacing:2px;font-weight:700;margin-bottom:6px;">MISSION</div>
  <div style="font-size:1.3rem;font-weight:700;color:{WHITE};line-height:1.5;">
    Lifting families around the world from poverty to prosperity through entrepreneurship and one-on-one mentoring.
  </div>
</div>""", unsafe_allow_html=True)

    st.markdown("---")
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
# FRAMEWORK
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Framework":
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
        dict(num="C1", name="Mission Alignment", weight_all="15%", weight_16="19%",
             goal="Assess the quality and strength of potential partners in each country ecosystem",
             oneliner="How well do potential partners align with MI's model?",
             metrics=[("# high-fit partners (score 4–5) in ecosystem DB","Ecosystem Database"),
                      ("# ideal partners (score 5) in ecosystem DB","Ecosystem Database"),
                      ("Volume-adjusted alignment score","Ecosystem Database"),
                      ("% of ecosystem that is high-fit (4 or 5)","Ecosystem Database")]),
        dict(num="C2", name="Volume Potential", weight_all="23%", weight_16="28%",
             goal="Identify whether a country can realistically get MI to scale",
             oneliner="Can this country deliver 500+ socios per year through partnerships?",
             metrics=[("# orgs with scale rating 4–5 (500+ reach)","Ecosystem Database"),
                      ("# orgs with scale rating 5 (1,000+ reach)","Ecosystem Database"),
                      ("Volume-weighted alignment score","Ecosystem Database"),
                      ("% of ecosystem that is large-scale","Ecosystem Database")]),
        dict(num="C3", name="Socio Profile Fit & Density", weight_all="15%", weight_16="19%",
             goal="Assess the size and serviceability of the urban micro-entrepreneur target population",
             oneliner="Is there sufficient density of urban micro-entrepreneurs matching MI's profile?",
             metrics=[("Urban population size","World Bank"),
                      ("Multidimensional Poverty Index — urban population","MPI Index"),
                      ("Informal self-employment rate","ILO Labor Statistics"),
                      ("% of workforce in urban micro-enterprise","World Bank")]),
        dict(num="C4", name="Digital Readiness", weight_all="5%", weight_16="9%",
             goal="Determine whether MI can scale virtually in each country",
             oneliner="Is digital infrastructure strong enough for virtual mentoring at scale?",
             metrics=[("Mobile connectivity rate","GSMA Mobile Connectivity Index"),
                      ("Internet usage rate","World Bank"),
                      ("Mobile money adoption","World Bank Findex"),
                      ("4G/LTE coverage %","GSMA")]),
        dict(num="C5", name="Political & Operating Risk", weight_all="10%", weight_16="14%",
             goal="Assess the level of political and operational risk for NGO activities",
             oneliner="How stable is the political environment for a US-based NGO?",
             metrics=[("Fragile States Index score","Fund for Peace"),
                      ("Political freedom score","Freedom House"),
                      ("NGO operational freedom","NGO Law Monitor"),
                      ("Historical US NGO operating risk","Country research")]),
        dict(num="C6", name="Legal & Structural Constraints", weight_all="7%", weight_16="11%",
             goal="Determine whether MI can operate and generate revenue without complex legal structures",
             oneliner="Can Mentors collect revenue from partners without major legal barriers?",
             metrics=[("Nonprofit registration requirements","Country legal research"),
                      ("Ability to receive foreign funding","Country legal research"),
                      ("Revenue restrictions on NGOs","NGO Law Monitor"),
                      ("Ease of establishing local legal entity","World Bank")]),
        dict(num="C7", name="CD Strength & Leadership", weight_all="15%", weight_16="N/A — qualitative",
             goal="Assess whether in-country leadership can execute and build partnerships",
             oneliner="Does the CD have capability and capacity to build partnerships?",
             metrics=[("Years of experience as CD","HQ + CD interviews"),
                      ("Partnership track record","CD interviews"),
                      ("Quality of existing partner relationships","CD interviews"),
                      ("Full-time vs part-time commitment","HQ assessment")]),
        dict(num="C8", name="Program Standardization", weight_all="10%", weight_16="N/A — qualitative",
             goal="Assess whether MI's program can be delivered consistently across partners",
             oneliner="Is the program standardized enough to scale across multiple partners?",
             metrics=[("Socio Connect adoption and data quality","Socio Connect"),
                      ("Mentor certification rate","Program records"),
                      ("Curriculum adherence rate","Program records"),
                      ("Impact data completeness","Socio Connect")]),
    ]

    col1, col2 = st.columns([2,3])
    with col1:
        wt_df = pd.DataFrame([
            {"Criterion": f"{c['num']}: {c['name']}", "Weight": float(c['weight_16'].replace('%',''))}
            for c in criteria if 'N/A' not in c['weight_16']
        ])
        fig_w = px.bar(wt_df, x="Weight", y="Criterion", orientation="h",
            color_discrete_sequence=[BLUE],
            labels={"Weight":"Weight (%) — C1–C6 scoring","Criterion":""},
            title="Criterion Weights (C1–C6)", height=320)
        fig_w.update_layout(plot_bgcolor=WHITE, margin=dict(l=0,r=0,t=40,b=0))
        fig_w.update_xaxes(gridcolor="#F0F0F0", ticksuffix="%")
        fig_w.update_yaxes(showgrid=False)
        st.plotly_chart(fig_w, use_container_width=True)

    with col2:
        st.markdown(f'<span class="section-label">All 8 criteria — expand each for full detail</span>', unsafe_allow_html=True)
        for c in criteria:
            excluded = "N/A" in c['weight_16']
            with st.expander(f"**{c['num']}: {c['name']}** — {c['oneliner']}"):
                colA, colB = st.columns(2)
                with colA:
                    st.markdown(f"**Weight (all 8):** {c['weight_all']}")
                    st.markdown(f"**Weight (C1–C6 score):** {c['weight_16']}")
                    st.markdown(f"**Goal:** {c['goal']}")
                with colB:
                    st.markdown(f'<div style="font-size:0.82rem;font-weight:600;color:{DBLUE};margin-bottom:4px;">Metrics & data sources:</div>', unsafe_allow_html=True)
                    for metric, source in c["metrics"]:
                        st.markdown(f'<div style="font-size:0.82rem;color:{DGREY};padding:2px 0;">• {metric} <span style="color:{MGREY};font-style:italic;">({source})</span></div>', unsafe_allow_html=True)

                if excluded:
                    st.info("Assessed qualitatively through CD interviews. Not included in the quantitative country score.")

# ══════════════════════════════════════════════════════════════════════════════
# COUNTRY BRIEFS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Country Briefs":
    page_header("Country Briefs", "Framework scores and tier assignments for all 12 current operating countries")

    # ── Country portfolio radar — moved from Ecosystem Analysis ───────────────
    st.markdown(f'<span class="section-label">Country Portfolio — Criterion Profile</span>', unsafe_allow_html=True)
    st.caption("Note: Click on country names in the legend to add or exclude from the visual")

    crit_theta = ["C1: Mission","C2: Volume","C3: Socio Fit",
                  "C4: Digital","C5: Political","C6: Legal","C1: Mission"]
    fig_radar = go.Figure()
    tc_map = {"Tier 1":GREEN,"Tier 2":AMBER,"Tier 3":RED}
    for _, row in scores.iterrows():
        vals = [row.c1,row.c2,row.c3,row.c4,row.c5,row.c6,row.c1]
        fig_radar.add_trace(go.Scatterpolar(
            r=vals, theta=crit_theta, name=row.country,
            line=dict(color=tc_map.get(row.tier,MGREY), width=1.5), opacity=0.75
        ))
    fig_radar.update_layout(
        polar=dict(radialaxis=dict(range=[0,10])),
        showlegend=True, height=480,
        legend=dict(orientation="v", x=1.02),
        margin=dict(l=30,r=120,t=20,b=20)
    )
    st.plotly_chart(fig_radar, use_container_width=True)

    st.markdown("---")

    # ── Overall criterion insights ────────────────────────────────────────────
    st.markdown(f'<span class="section-label">Overall Insights by Criterion — Across All Countries</span>', unsafe_allow_html=True)
    crit_insight_labels = {
        "c1":"C1: Mission Alignment","c2":"C2: Volume Potential",
        "c3":"C3: Socio Profile Fit","c4":"C4: Digital Readiness",
        "c5":"C5: Political Risk","c6":"C6: Legal Structure",
    }
    ci_cols = st.columns(3)
    for idx, (key, label) in enumerate(crit_insight_labels.items()):
        insight = CRITERION_INSIGHTS.get(key, "")
        if insight:
            with ci_cols[idx % 3].expander(f"📊 {label}"):
                st.markdown(f'<div style="font-size:0.82rem;color:{DGREY};line-height:1.65;">{insight.replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)

    st.markdown("---")

    # ── Summary table ─────────────────────────────────────────────────────────
    st.markdown(f'<span class="section-label">All Countries — Score Summary (C1–C6)</span>', unsafe_allow_html=True)
    st.caption("C1: Mission Alignment  ·  C2: Volume Potential  ·  C3: Socio Profile Fit  ·  C4: Digital Readiness  ·  C5: Political Risk  ·  C6: Legal Structure  ·  Score = weighted average out of 10")

    disp = scores[['country','c1','c2','c3','c4','c5','c6','score','tier']].copy()
    disp.columns = ['Country','C1','C2','C3','C4','C5','C6','Score','Tier']
    disp = disp.sort_values('Score', ascending=False)
    st.dataframe(
        disp.style.format({'C1':'{:.2f}','C2':'{:.2f}','C3':'{:.2f}',
                           'C4':'{:.2f}','C5':'{:.2f}','C6':'{:.2f}','Score':'{:.2f}'}),
        use_container_width=True, hide_index=True,
        height=35*(len(disp)+1)+10
    )

    st.markdown("---")

    # ── Country detail ─────────────────────────────────────────────────────────
    sel  = st.selectbox("Select a country for detailed view",
                        scores.sort_values('score', ascending=False)['country'].tolist())
    r    = scores[scores['country']==sel].iloc[0]
    tier = TIER_MAP.get(sel,"Tier 3")
    tc   = TIER_COLOR.get(tier,MGREY)

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
  <div style="font-size:2.5rem;font-weight:900;color:{GOLD};">{r['score']:.2f}
    <span style="font-size:1rem;color:#CADCFC;">/10</span>
  </div>
</div>""", unsafe_allow_html=True)

    col1, col2 = st.columns([2,3])
    with col1:
        st.markdown(f'<span class="section-label">Criterion Scores</span>', unsafe_allow_html=True)
        country_data = COUNTRY_NOTES.get(sel, {})
        for key, name in CRIT_NAMES.items():
            val   = r[key]
            desc  = CRIT_DESC[key]
            color = GREEN if val >= 7 else AMBER if val >= 5 else RED
            note  = country_data.get(key, "")
            st.markdown(f"""
<div style="margin-bottom:6px;">
  <div style="font-size:0.82rem;font-weight:600;color:{DBLUE};">{name}</div>
  <div style="font-size:0.73rem;color:{MGREY};margin-bottom:3px;">{desc}</div>
  {score_bar(val,10,color)}
</div>""", unsafe_allow_html=True)
            if note:
                with st.expander(f"Why {val:.1f}? — {name}"):
                    st.markdown(f'<div style="font-size:0.82rem;color:{DGREY};line-height:1.65;">{note.replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)
        # Overall country note
        overall_note = country_data.get("overall", "")
        if overall_note:
            st.markdown(f'<span class="section-label" style="margin-top:8px;">Overall Assessment</span>', unsafe_allow_html=True)
            st.markdown(f'<div style="font-size:0.85rem;color:{DGREY};line-height:1.65;background:{OFFWH};padding:10px 12px;border-radius:8px;border-left:3px solid {BLUE};">{overall_note.replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)

    with col2:
        fig_r = go.Figure(go.Scatterpolar(
            r=[r.c1,r.c2,r.c3,r.c4,r.c5,r.c6,r.c1],
            theta=["Mission\nAlignment","Volume\nPotential","Socio\nProfile",
                   "Digital\nReadiness","Political\nRisk","Legal\nStructure","Mission\nAlignment"],
            fill='toself', fillcolor="rgba(39,116,174,0.15)",
            line=dict(color=BLUE, width=2), name=sel
        ))
        fig_r.update_layout(
            polar=dict(radialaxis=dict(range=[0,10], tickfont=dict(size=9))),
            showlegend=False, height=340, margin=dict(l=30,r=30,t=30,b=30)
        )
        st.plotly_chart(fig_r, use_container_width=True)

    c_pp = pp[pp['Country']==sel] if 'Country' in pp.columns else pd.DataFrame()
    if len(c_pp):
        st.markdown(f'<span class="section-label">Priority Partners — {sel}</span>', unsafe_allow_html=True)
        st.dataframe(c_pp[['Organization Name','Why Priority','Partnership Type',
                            'Estimated Reach','Cities of Overlap with MI']].rename(
            columns={'Organization Name':'Organization','Why Priority':'Why a Priority',
                     'Partnership Type':'Type','Estimated Reach':'Scale'}),
            use_container_width=True, hide_index=True)

# ══════════════════════════════════════════════════════════════════════════════
# FUTURE PARTNERSHIPS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Future Partnerships":
    page_header("Future Partnerships", "Evaluating potential expansion markets using the Growth Criteria Framework")

    st.markdown(f"""
<div class="card-gold">
<span class="section-label">HOW TO USE THIS PAGE</span>
<div style="font-size:0.88rem;color:{DGREY};line-height:1.65;margin-top:4px;">
We evaluated 3 potential countries for future Mentors International expansion: Brazil, Ecuador, and South Africa
using the Growth Criteria Framework. You can compare these results against current countries of operation
to gauge potential expansion feasibility.
</div></div>""", unsafe_allow_html=True)

    tier1 = scores[scores['tier']=='Tier 1'].copy(); tier1['group'] = 'Current Tier 1'
    exp_df = expansion.copy(); exp_df['group'] = 'Expansion Candidate'
    combined = pd.concat([tier1, exp_df], ignore_index=True)

    fig_c = px.bar(combined.sort_values('score',ascending=False),
        x='country', y='score', color='group',
        color_discrete_map={'Current Tier 1':BLUE,'Expansion Candidate':GOLD},
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
  <div style="font-size:2.2rem;font-weight:900;color:{GOLD};">{r['score']:.2f}
    <span style="font-size:1rem;color:#CADCFC;">/10</span>
  </div>
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
        st.markdown(f'<span class="section-label">Criterion Notes</span>', unsafe_allow_html=True)
        exp_country_data = COUNTRY_NOTES.get(sel_exp, {})
        for key, name in CRIT_NAMES.items():
            note = exp_country_data.get(key, "")
            if note:
                with st.expander(f"Why this score? — {name}"):
                    st.markdown(f'<div style="font-size:0.82rem;color:{DGREY};line-height:1.65;">{note.replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)
        overall_note = exp_country_data.get("overall", "")
        if overall_note:
            st.markdown(f'<div style="font-size:0.85rem;color:{DGREY};line-height:1.65;background:{OFFWH};padding:10px 12px;border-radius:8px;border-left:3px solid {BLUE};margin-top:8px;">{overall_note.replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f'<span class="section-label">Ecosystem Database — {sel_exp}</span>', unsafe_allow_html=True)
    with st.expander("📖 How to read the scores"):
        col_r1, col_r2, col_r3 = st.columns(3)
        with col_r1:
            st.markdown("**Alignment with MI (1–5)**")
            st.markdown(f'<div style="font-size:0.8rem;color:{DGREY};line-height:1.6;">{ECO_RUBRICS.get("Alignment with MI (1-5)","").replace(chr(10),"<br>")}</div>', unsafe_allow_html=True)
        with col_r2:
            st.markdown("**Scale Potential (1–5)**")
            st.markdown(f'<div style="font-size:0.8rem;color:{DGREY};line-height:1.6;">{ECO_RUBRICS.get("Scale Potential (1-5)","").replace(chr(10),"<br>")}</div>', unsafe_allow_html=True)
        with col_r3:
            st.markdown("**Urban Relevance (1–5)**")
            st.markdown(f'<div style="font-size:0.8rem;color:{DGREY};line-height:1.6;">{ECO_RUBRICS.get("Urban Relevance (1-5)","").replace(chr(10),"<br>")}</div>', unsafe_allow_html=True)
    exp_orgs = eco_exp[eco_exp['Country']==sel_exp].copy()
    exp_orgs['align_n'] = pd.to_numeric(exp_orgs['align_n'], errors='coerce').fillna(0)
    exp_orgs['scale_n'] = pd.to_numeric(exp_orgs['scale_n'], errors='coerce').fillna(0)
    eco_table(exp_orgs)

# ══════════════════════════════════════════════════════════════════════════════
# PARTNER PIPELINE — Ecosystem Database (Existing)
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Partner Pipeline":
    page_header("Ecosystem Database — Existing Countries",
                "183 potential partnership organizations identified across all 12 countries of operation")

    col1, col2, col3 = st.columns(3)
    all_countries = ["All"] + sorted(eco['Country'].dropna().unique())
    country_f = col1.selectbox("Country", all_countries)
    align_f   = col2.selectbox("Min Alignment Score", [1,2,3,4,5], index=2)
    scale_f   = col3.selectbox("Min Scale Score",     [1,2,3,4,5], index=0)

    filtered = eco.copy()
    filtered['align_n'] = pd.to_numeric(filtered['align_n'], errors='coerce').fillna(0)
    filtered['scale_n'] = pd.to_numeric(filtered['scale_n'], errors='coerce').fillna(0)
    if country_f != "All":
        filtered = filtered[filtered['Country']==country_f]
    filtered = filtered[filtered['align_n'] >= align_f]
    filtered = filtered[filtered['scale_n'] >= scale_f]
    filtered = filtered.reset_index(drop=True)

    with st.expander("📖 How to read the scores — Scoring Rubric"):
        col_r1, col_r2, col_r3 = st.columns(3)
        align_rub = ECO_RUBRICS.get("Alignment with MI (1-5)", "")
        scale_rub = ECO_RUBRICS.get("Scale Potential (1-5)", "")
        urban_rub = ECO_RUBRICS.get("Urban Relevance (1-5)", "")
        with col_r1:
            st.markdown(f'**Alignment with MI (1–5)**')
            st.markdown(f'<div style="font-size:0.8rem;color:{DGREY};line-height:1.6;">{align_rub.replace(chr(10),"<br>")}</div>', unsafe_allow_html=True)
        with col_r2:
            st.markdown(f'**Scale Potential (1–5)**')
            st.markdown(f'<div style="font-size:0.8rem;color:{DGREY};line-height:1.6;">{scale_rub.replace(chr(10),"<br>")}</div>', unsafe_allow_html=True)
        with col_r3:
            st.markdown(f'**Urban Relevance (1–5)**')
            st.markdown(f'<div style="font-size:0.8rem;color:{DGREY};line-height:1.6;">{urban_rub.replace(chr(10),"<br>")}</div>', unsafe_allow_html=True)

    m1,m2,m3,m4 = st.columns(4)
    m1.metric("Organizations shown", len(filtered))
    m2.metric("Excellent Fit (Score 5)", int((filtered['align_n']==5).sum()))
    m3.metric("Very Good Fit (Score 4)", int((filtered['align_n']==4).sum()))
    m4.metric("Countries", int(filtered['Country'].nunique()))

    eco_table(filtered)
    st.caption("Source: 183 potential partnership organizations identified across all 12 countries of operation · Research by Caleigh Hernandez · Anderson Library databases, NGO registries, MFI directories, Factiva")

# ══════════════════════════════════════════════════════════════════════════════
# ECOSYSTEM ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Ecosystem Analysis":
    page_header("Ecosystem Analysis", "Partner landscape across all 12 countries of operation")

    # C1 vs C2 scatter (Mission Alignment vs Volume Potential)
    st.markdown(f'<span class="section-label">Mission Alignment vs Volume Potential — by Country</span>', unsafe_allow_html=True)
    fig_mv = px.scatter(scores, x='c1', y='c2', color='tier',
        size='score', size_max=55, hover_name='country',
        hover_data={'c1':True,'c2':True,'score':True,'tier':False},
        color_discrete_map={"Tier 1":GREEN,"Tier 2":AMBER,"Tier 3":RED},
        labels={'c1':'C1: Mission Alignment (0–10)',
                'c2':'C2: Volume Potential (0–10)','tier':'Tier'},
        height=420)
    fig_mv.update_layout(plot_bgcolor=WHITE)
    fig_mv.update_xaxes(gridcolor="#F0F0F0", range=[0,11])
    fig_mv.update_yaxes(gridcolor="#F0F0F0", range=[0,11])
    st.plotly_chart(fig_mv, use_container_width=True)
    st.caption("Countries naturally cluster into three tiers. Tier 1 (green) perform strongly across both dimensions — clearest near-term expansion opportunities. Tier 2 (orange) show moderate-to-strong potential with slightly lower alignment or scale. Tier 3 (red) score lower across one or both criteria, suggesting greater limitations. Hover over each dot to see the specific country. The graph helps visually distinguish where MI is best positioned to scale efficiently while remaining aligned with its mission.")

    st.markdown("---")

    # 4 graphs — all existing countries only
    col1, col2 = st.columns(2)

    with col1:
        # Graph 1: Potential Mission Aligned Partners by Country
        a5 = eco[eco['align_n']==5].groupby('Country').size().reset_index(name='n')
        fig1 = px.bar(a5.sort_values('n'), x='n', y='Country', orientation='h',
            color_discrete_sequence=[BLUE],
            labels={'n':'# of Partners with a 5 Alignment Score','Country':''},
            title='Mission Aligned Partners by Country', height=380)
        fig1.update_layout(plot_bgcolor=WHITE, margin=dict(l=0,r=0,t=40,b=0))
        fig1.update_xaxes(gridcolor="#F0F0F0", dtick=1)
        fig1.update_yaxes(showgrid=False)
        st.plotly_chart(fig1, use_container_width=True)
        st.caption("Interpret as ecosystem breadth — the number of organizations that could realistically partner with MI. Colombia stands out combining high quantity and quality, suggesting a mature diversified ecosystem. Honduras and Guatemala score well on alignment quality despite fewer total organizations — strong focused partnerships but less diversification. Cape Verde and Malawi show limited ecosystem breadth with fewer immediately viable partnership opportunities.")

        # Graph 3: Scalability by Country (# of scale 4–5 orgs)
        scalable = eco[eco['scale_n']>=4].groupby('Country').size().reset_index(name='n')
        fig3 = px.bar(scalable.sort_values('n'), x='n', y='Country', orientation='h',
            color_discrete_sequence=[DBLUE],
            labels={'n':'# of Partners Capable of Producing 500+ Socios','Country':''},
            title='Scalability by Country', height=380)
        fig3.update_layout(plot_bgcolor=WHITE, margin=dict(l=0,r=0,t=40,b=0))
        fig3.update_xaxes(gridcolor="#F0F0F0", dtick=1)
        fig3.update_yaxes(showgrid=False)
        st.plotly_chart(fig3, use_container_width=True)
        st.caption("Measures depth of scale-ready partnerships — organizations capable of supporting large-scale socio growth. Colombia and Kenya stand out combining multiple scalable partners, strong diversity, and substantial socio capacity. Kenya is notable for exceptional scale potential despite somewhat lower average alignment quality. Brazil, Ecuador, and South Africa dramatically outperform current countries — particularly Brazil, which appears structurally different in ecosystem size and institutional scale capacity.")

    with col2:
        # Graph 2: Average Alignment Score by Country
        avg_a = eco.groupby('Country')['align_n'].mean().reset_index()
        avg_a.columns = ['Country','avg']
        fig2 = px.bar(avg_a.sort_values('avg'), x='avg', y='Country', orientation='h',
            color_discrete_sequence=[GOLD],
            labels={'avg':'Average Alignment Score (0–5)','Country':''},
            title='Average Alignment Score by Country', height=380)
        fig2.update_layout(plot_bgcolor=WHITE, margin=dict(l=0,r=0,t=40,b=0))
        fig2.update_xaxes(gridcolor="#F0F0F0", range=[0,5.5])
        fig2.update_yaxes(showgrid=False)
        st.plotly_chart(fig2, use_container_width=True)
        st.caption("Reflects average quality of fit between organizations and MI's model. Interpret carefully alongside ecosystem size — Honduras and Guatemala score highly partly because their ecosystems are small and concentrated. Colombia and Peru are particularly compelling: strong alignment scores with broader ecosystems and larger scale infrastructure, suggesting stronger long-term scalability. Lower-scoring countries may still contain strong individual partners but alignment is less consistent.")

        # Graph 4: Average Scale Potential by Country
        avg_s = eco.groupby('Country')['scale_n'].mean().reset_index()
        avg_s.columns = ['Country','avg']
        fig4 = px.bar(avg_s.sort_values('avg'), x='avg', y='Country', orientation='h',
            color_discrete_sequence=[AMBER],
            labels={'avg':'Average Scale Score (0–5)','Country':''},
            title='Average Scale Potential by Country', height=380)
        fig4.update_layout(plot_bgcolor=WHITE, margin=dict(l=0,r=0,t=40,b=0))
        fig4.update_xaxes(gridcolor="#F0F0F0", range=[0,5.5])
        fig4.update_yaxes(showgrid=False)
        st.plotly_chart(fig4, use_container_width=True)
        st.caption("Reflects the average organizational size and scale capability among aligned partners. Guatemala ranking highly is an important nuance — fewer overall scalable organizations but those that do align tend to be relatively large. This 'smaller but stronger' structure differs from countries with many small-to-mid-sized aligned organizations. Mexico and Dominican Republic also perform well. Distinguishes ecosystems anchored by a few large institutional partners versus those requiring aggregation of multiple smaller partnerships.")

# ══════════════════════════════════════════════════════════════════════════════
# RECOMMENDATIONS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Recommendations":
    page_header("Recommendations", "Tier structure and priority partners")

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
    st.caption("To be updated as additional partner research is completed.")
    if len(pp):
        st.dataframe(pp.rename(columns={
            'Organization Name':'Organization','Why Priority':'Why a Priority',
            'Partnership Type':'Type','Estimated Reach':'Scale',
            'Cities of Overlap with MI':'Cities'}),
            use_container_width=True, hide_index=True)
    else:
        st.info("Priority partner list will be populated as research progresses.")

# ══════════════════════════════════════════════════════════════════════════════
# APPENDIX
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Appendix":
    page_header("Appendix", "Data sources, methodology, and framework limitations")

    tab1, tab2, tab3 = st.tabs(["📚 Data Sources","⚠️ Limitations","🔬 Benchmarks"])

    with tab1:
        sources = [
            ("World Bank","Urban population, poverty ratios, self-employment rates, internet usage","data.worldbank.org"),
            ("GSMA Mobile Connectivity Index","Mobile connectivity, 4G coverage, digital readiness","gsma.com/mobileconnectivityindex"),
            ("Fund for Peace — Fragile States Index","Political stability, government effectiveness","fragilestatesindex.org"),
            ("Freedom House","Political rights and civil liberties — NGO operating environment","freedomhouse.org"),
            ("Anderson Library Databases","Organization research, MFI directories, NGO databases, Factiva","UCLA Library"),
            ("Country NGO Registries","Local NGO registration databases","Country-specific"),
            ("Ecosystem Database","242 organizations scored across 12 countries of operation plus 3 potential expansion countries on alignment, scale, and urban relevance","Internal — Caleigh Hernandez"),
            ("HQ Interviews","Ana Peña (Director of Operations) · Peter Sturgeon (CEO) · April 20–21, 2026","Primary research"),
            ("CD Interviews — Colombia","Andrea Arenas Cardenas · Country Director · April 21, 2026","Primary research"),
            ("CD Interviews — Ghana","Emmanuella Gyamfi · Country Director · April 23, 2026","Primary research"),
            ("CD Interviews — Guatemala","R. Dario Lorenzana & Ana Lorena Cordon · CD & Program Lead · April 24, 2026","Primary research"),
            ("CD Interviews — Mexico","Zoram Emmanuel Varguez Bacab · Country Director · April 24, 2026","Primary research"),
            ("CD Interviews — Nicaragua","Pio Quintero & Silvia Elena Leyton Lopez · CD & Program Lead · April 24, 2026","Primary research"),
            ("CD Interviews — Kenya","Eric Onyango · Country Director · April 28, 2026","Primary research"),
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
             "CD Strength and Program Standardization require qualitative judgment. Assessed separately and not included in the numerical score."),
            ("Ecosystem research depth varies by country",
             "Countries with more available data have more organizations in the database. Smaller markets may have fewer entries."),
            ("Geography not captured in scoring",
             "The framework does not account for difficulty of traveling between cities within a country."),
            ("Self-reported outcome data",
             "MI's impact outcomes (+53% income, +65% savings) are self-reported and not independently verified."),
            ("Framework reflects a point in time",
             "Scores reflect data available as of May 2026. The framework should be reviewed annually."),
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
            "Data":["Self-reported*","Independently verified","Partner-delivered","Technical assistance"],
        })
        st.dataframe(bm, use_container_width=True, hide_index=True)
        st.caption("* Self-reported FY2025.")

    st.markdown("---")
    st.caption("UCLA Anderson SICC · Spring 2026 · Praveen Gangaraju · Caleigh Hernandez · Morgan Ikemiya · Sydney Kyle · Prof. Gayle Northrop · June 10, 2026")
