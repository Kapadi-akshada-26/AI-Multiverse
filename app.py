import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# ---------------------------
# Load Gemini API
# ---------------------------
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ---------------------------
# Page Setup
# ---------------------------
st.set_page_config(
    page_title="AI Multiverse Chat",
    page_icon="🤖",
    layout="centered"
)

# ---------------------------
# Sidebar (Task 1)
# ---------------------------
st.sidebar.title(" App Settings")

personality = st.sidebar.selectbox(
    "Choose AI Personality",
    [
        "Friendly Assistant",
        "Expert Hacker",
        "Panicked College Student at 3 AM",
        "1920s Mafia Boss",
        "Highly Sarcastic Fitness Coach"
    ]
)

intensity = st.sidebar.slider(
    "Intensity Level",
    1, 10, 5
)

# ---------------------------
# Dynamic Avatar (Task 5)
# ---------------------------
if personality == "Friendly Assistant":
    bot_avatar = "😊"
elif personality == "Expert Hacker":
    bot_avatar = "💻"
elif personality == "Panicked College Student at 3 AM":
    bot_avatar = "😵"
elif personality == "1920s Mafia Boss":
    bot_avatar = "🕴️"
elif personality == "Highly Sarcastic Fitness Coach":
    bot_avatar = "🏋️"
else:
    bot_avatar = "🤖"

# ---------------------------
# Main Screen
# ---------------------------
st.title("🤖 AI Multiverse Chat")
st.caption("Chat with different AI personalities.")

# ---------------------------
# Chat History
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar=msg.get("avatar")):
        st.write(msg["content"])

# ---------------------------
# Chat Input
# ---------------------------
user_input = st.chat_input("Type your message...")

if user_input:

    # Show user message
    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Prompt Engineering (Task 3)
    ai_instructions = f"""
You are {personality}.

Act at an intensity level of {intensity}/10.

The higher the intensity, the more dramatic and immersive your personality should become.
Stay completely in character while answering naturally.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=f"{ai_instructions}\n\nUser: {user_input}"
        )

        reply = response.text

    except Exception as e:
        reply = f"Error: {e}"

    # Assistant Bubble (Task 4)
    with st.chat_message("assistant", avatar=bot_avatar):
        st.write(reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply,
        "avatar": bot_avatar
    })