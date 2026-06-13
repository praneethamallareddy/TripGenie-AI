import streamlit as st
from translations import translations

language = st.session_state.get("language", "English")
t = translations[language]

st.set_page_config(
    page_title="Expenses",
    page_icon="💸",
    layout="wide"
)

st.title(
    f"💸 {t['expenses_title']}"
)

st.caption(
    t["expenses_caption"]
)

st.divider()

expense_name = st.text_input(
    t["expense_name"]
)

amount = st.number_input(
    t["amount"],
    min_value=0,
    value=500
)

category = st.selectbox(
    t["category"],
    [
        t["food"],
        t["travel"],
        t["hotel"],
        t["shopping"],
        t["other"]
    ]
)

if st.button(
    t["add_expense"]
):
    st.success(
        t["expense_added"]
    )

st.divider()

st.subheader(
    t["expense_history"]
)

expenses = [
    (t["food"], 500),
    (t["travel"], 1200),
    (t["hotel"], 2500),
    (t["shopping"], 800)
]

total = 0

for item, cost in expenses:
    total += cost
    st.write(
        f"{item} - ₹{cost}"
    )

st.divider()

st.metric(
    t["total_expenses"],
    f"₹{total}"
)