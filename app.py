import streamlit as st
import os
import google.generativeai as genai
from translations import translations

st.set_page_config(
    page_title="TripGenie AI",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("⚙️ Settings")

language = st.sidebar.selectbox(
    "🌐 Language",
    ["English", "हिन्दी", "తెలుగు"]
)

st.session_state["language"] = language

ai_provider = st.sidebar.selectbox(
    "🤖 AI Provider",
    ["Gemini", "Ollama"]
)

st.session_state["ai_provider"] = ai_provider

if ai_provider == "Gemini":

    user_api_key = st.sidebar.text_input(
        "Gemini API Key (BYOK)",
        type="password"
    )

    if user_api_key:
        os.environ["GEMINI_API_KEY"] = user_api_key
        genai.configure(api_key=user_api_key)

else:

    st.sidebar.success(
        "Using Local Ollama Model"
    )

t = translations[language]

css_path = os.path.join(
    os.path.dirname(__file__),
    "assets",
    "style.css"
)

with open(css_path) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.markdown(
    f"""
<div class='hero'>

<h1>{t["title"]}</h1>

<h3>{t["subtitle"]}</h3>

<p>
{t["description"]}
</p>

</div>
""",
    unsafe_allow_html=True
)

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

st.markdown(
    f"## {t['features']}"
)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        f"""
<div class='card'>
<h2>🤖 {t["ai_planner"]}</h2>
<p>{t["planner_desc"]}</p>
</div>
""",
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        f"""
<div class='card'>
<h2>🌤️ {t["smart_weather"]}</h2>
<p>{t["weather_desc"]}</p>
</div>
""",
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        f"""
<div class='card'>
<h2>💰 {t["budget_tracking"]}</h2>
<p>{t["budget_desc"]}</p>
</div>
""",
        unsafe_allow_html=True
    )

st.divider()

st.info(
    t["info"]
)