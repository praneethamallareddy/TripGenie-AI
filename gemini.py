import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from ollama import ask_ollama

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def get_ai_response(prompt):

    provider = st.session_state.get(
        "ai_provider",
        "Gemini"
    )

    try:

        is_streamlit_cloud = (
            os.getenv("STREAMLIT_SERVER_PORT") is not None
        )

        if provider == "Ollama" and not is_streamlit_cloud:
            return ask_ollama(prompt)

    except Exception:
        pass

    response = model.generate_content(prompt)
    return response.text


def generate_itinerary(
    destination,
    budget,
    days,
    interests,
    language="English"
):

    prompt = f"""
You are an expert travel planner.

Generate the entire response in {language}.

Destination: {destination}
Budget: ₹{budget}
Duration: {days} days
Interests: {", ".join(interests)}

Include:

1. Day-by-day itinerary
2. Morning activities
3. Afternoon activities
4. Evening activities
5. Tourist attractions
6. Local food recommendations
7. Estimated daily expenses
8. Hidden gems
9. Travel tips

Use only {language}.

Format using Markdown.
"""

    return get_ai_response(prompt)


def generate_weather_report(
    destination,
    language="English"
):

    prompt = f"""
You are a travel weather assistant.

Generate the entire response in {language}.

Destination: {destination}

Provide:

1. Weather Overview
2. Packing Suggestions
3. Travel Advice
4. Recommended Activities
5. Safety Tips

Use only {language}.

Format using Markdown.
"""

    return get_ai_response(prompt)


def generate_packing_list(
    destination,
    days,
    language="English"
):

    prompt = f"""
Generate the entire response in {language}.

Create a travel packing checklist.

Destination: {destination}
Trip Duration: {days} days

Include:

1. Clothing
2. Electronics
3. Toiletries
4. Documents
5. Medicines
6. Travel Essentials

Use only {language}.

Format as a checklist.
"""

    return get_ai_response(prompt)


def generate_budget_plan(
    destination,
    budget,
    days,
    language="English"
):

    prompt = f"""
Generate the entire response in {language}.

Create a travel budget breakdown.

Destination: {destination}
Budget: ₹{budget}
Duration: {days} days

Break down:

1. Accommodation
2. Food
3. Transport
4. Activities
5. Shopping
6. Emergency Reserve

Use only {language}.

Format using Markdown.
"""

    return get_ai_response(prompt)


def ask_travel_assistant(
    question,
    language="English"
):

    prompt = f"""
You are TripGenie AI.

Answer entirely in {language}.

Question:

{question}

Provide a practical and helpful answer.

Use only {language}.
"""

    return get_ai_response(prompt)