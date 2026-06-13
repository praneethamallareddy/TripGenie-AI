import streamlit as st
from gemini import ask_travel_assistant
from translations import translations

language = st.session_state.get("language", "English")
t = translations[language]

st.set_page_config(
    page_title="Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title(
    f"🤖 {t['assistant_title']}"
)

st.caption(
    t["assistant_caption"]
)

st.divider()

question = st.text_area(
    t["ask_question"],
    placeholder=t["question_placeholder"]
)

if st.button(
    t["send"]
):

    if question:

        with st.spinner(
            t["thinking"]
        ):

            answer = ask_travel_assistant(
                question,
                language
            )

        st.markdown(answer)

st.divider()

st.subheader(
    t["example_questions"]
)

st.info(
    t["example1"]
)

st.info(
    t["example2"]
)

st.info(
    t["example3"]
)

st.info(
    t["example4"]
)