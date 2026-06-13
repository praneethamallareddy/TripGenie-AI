import streamlit as st
from translations import translations

language = st.session_state.get(
    "language",
    "English"
)

t = translations[language]

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title(
    f"📊 {t['dashboard_title']}"
)

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        t["trips_planned"],
        "15"
    )

with col2:
    st.metric(
        t["countries"],
        "8"
    )

with col3:
    st.metric(
        t["budget_saved"],
        "₹12k"
    )

with col4:
    st.metric(
        t["ai_score"],
        "98%"
    )

st.divider()

st.subheader(
    t["quick_actions"]
)

c1, c2, c3 = st.columns(3)

with c1:
    st.page_link(
        "pages/1_Plan_Trip.py",
        label=f"✈️ {t['plan_trip']}"
    )

with c2:
    st.page_link(
        "pages/3_Weather.py",
        label=f"🌤 {t['weather']}"
    )

with c3:
    st.page_link(
        "pages/2_Packing.py",
        label=f"🎒 {t['packing']}"
    )

st.divider()

st.subheader(
    t["recent_activity"]
)

if language == "English":

    st.success("✈️ Trip created successfully")
    st.success("🌤 Weather report generated")
    st.success("🎒 Packing checklist created")

elif language == "తెలుగు":

    st.success("✈️ ప్రయాణ ప్రణాళిక విజయవంతంగా రూపొందించబడింది")
    st.success("🌤 వాతావరణ నివేదిక రూపొందించబడింది")
    st.success("🎒 ప్యాకింగ్ జాబితా రూపొందించబడింది")

elif language == "हिन्दी":

    st.success("✈️ यात्रा योजना सफलतापूर्वक बनाई गई")
    st.success("🌤 मौसम रिपोर्ट तैयार की गई")
    st.success("🎒 पैकिंग सूची तैयार की गई")