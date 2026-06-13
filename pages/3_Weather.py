import streamlit as st
from gemini import generate_weather_report
from translations import translations

language = st.session_state.get("language", "English")
t = translations[language]

st.set_page_config(
    page_title="Weather",
    page_icon="🌤️",
    layout="wide"
)

st.title(
    f"🌤️ {t['weather_title']}"
)

st.caption(
    t["weather_caption"]
)

st.divider()

default_city = st.session_state.get(
    "destination",
    ""
)

city = st.text_input(
    t["destination"],
    value=default_city
)

search = st.button(
    t["check_weather"]
)

if search:

    if city:

        st.session_state["destination"] = city

        with st.spinner(
            t["analyzing_weather"]
        ):

            report = generate_weather_report(
                city,
                language
            )

        st.subheader(
            t["weather_report"]
        )

        st.markdown(report)

    else:

        st.warning(
            t["enter_destination"]
        )