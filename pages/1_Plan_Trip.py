import streamlit as st
from translations import translations
from gemini import generate_itinerary

language = st.session_state.get("language", "English")
t = translations[language]

st.set_page_config(
    page_title="AI Trip Planner",
    page_icon="✈️",
    layout="wide"
)

st.title(f"✈️ {t['plan_trip']}")
st.caption(t["plan_trip_caption"])

st.divider()

col1, col2 = st.columns(2)

with col1:

    destination = st.text_input(
        t["destination"],
        placeholder=t["destination_placeholder"]
    )

    start_date = st.date_input(
        t["start_date"]
    )

    budget = st.number_input(
        t["budget"],
        min_value=1000,
        value=50000,
        step=1000
    )

with col2:

    days = st.slider(
        t["trip_duration"],
        1,
        14,
        5
    )

    travelers = st.selectbox(
        t["travelers"],
        [
            t["solo"],
            t["couple"],
            t["family"],
            t["friends"]
        ]
    )

    style = st.selectbox(
        t["travel_style"],
        [
            t["adventure"],
            t["luxury"],
            t["budget_travel"],
            t["relaxation"],
            t["nature"],
            t["food_culture"]
        ]
    )

st.write("")

generate = st.button(
    t["generate_itinerary"]
)

st.divider()

if generate:

    if not destination:

        st.warning(
            t["enter_destination"]
        )

    else:

        st.success(
            t["generating_itinerary"]
        )

        interests = [style]

        itinerary = generate_itinerary(
            destination=destination,
            budget=budget,
            days=days,
            interests=interests,
            language=language
        )

        st.markdown(itinerary)

        st.session_state["destination"] = destination