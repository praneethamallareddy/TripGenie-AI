import streamlit as st
from translations import translations

language = st.session_state.get("language", "English")
t = translations[language]

st.set_page_config(
    page_title="Budget",
    page_icon="💰",
    layout="wide"
)

st.title(
    f"💰 {t['budget_title']}"
)

st.caption(
    t["budget_caption"]
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    total_budget = st.number_input(
        t["total_budget"],
        min_value=1000,
        value=50000,
        step=1000
    )

with col2:
    current_spending = st.number_input(
        t["current_spending"],
        min_value=0,
        value=10000,
        step=500
    )

remaining = total_budget - current_spending

st.divider()

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        t["total_budget"],
        f"₹{total_budget:,}"
    )

with c2:
    st.metric(
        t["spent"],
        f"₹{current_spending:,}"
    )

with c3:
    st.metric(
        t["remaining"],
        f"₹{remaining:,}"
    )

st.divider()

usage = (current_spending / total_budget) * 100

st.subheader(
    t["budget_usage"]
)

st.progress(
    min(int(usage), 100)
)

st.write(
    f"{usage:.0f}% {t['used']}"
)

st.divider()

st.subheader(
    t["expense_allocation"]
)

food = current_spending * 0.30
travel = current_spending * 0.40
hotel = current_spending * 0.20
other = current_spending * 0.10

st.write(
    f"🍽️ {t['food']} : ₹{food:,.0f}"
)

st.write(
    f"✈️ {t['travel']} : ₹{travel:,.0f}"
)

st.write(
    f"🏨 {t['hotel']} : ₹{hotel:,.0f}"
)

st.write(
    f"🛍️ {t['other']} : ₹{other:,.0f}"
)