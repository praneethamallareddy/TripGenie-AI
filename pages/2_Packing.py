import streamlit as st
from translations import translations

language = st.session_state.get("language", "English")
t = translations[language]

st.set_page_config(
    page_title="Packing",
    page_icon="🎒",
    layout="wide"
)

st.title(f"🎒 {t['packing_title']}")

st.caption(
    t["packing_caption"]
)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    destination = st.text_input(
        t["destination"]
    )

with col2:
    trip_type = st.selectbox(
        t["trip_type"],
        [
            t["beach"],
            t["adventure"],
            t["business"],
            t["family"]
        ]
    )

with col3:
    days = st.number_input(
        t["days"],
        min_value=1,
        max_value=30,
        value=5
    )

generate = st.button(
    t["generate_list"]
)

if generate:

    st.subheader(
        t["packing_checklist"]
    )

    items = [
        t["clothes"],
        t["pants"],
        t["socks"],
        t["shoes"],
        t["toothbrush"],
        t["toiletries"],
        t["phone_charger"],
        t["wallet"],
        t["id_card"],
        t["medicines"]
    ]

    for item in items:
        st.checkbox(item)