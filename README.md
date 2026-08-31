# 🤖 AI Multiverse Chat

A simple interactive AI chatbot built with **Streamlit** and the **Google Gemini API** as part of the **MirAI School of Technology Virtual Summer Internship 2026 – AI Builder Track**.

The application allows users to chat with Gemini using different creative AI personalities and control how intensely the selected personality behaves.

## 🚀 Try it Now

**🌐 Live Demo:** 
https://kapadi-akshada-26-ai-multiverse-app-jqcvvs.streamlit.app/

## ✨ Features

* 🎭 Multiple AI personalities
* 🎚️ Personality intensity control from 1–10
* 💬 Streamlit chat interface
* 🤖 Gemini-powered AI responses
* 😀 Dynamic emoji avatars
* 💾 Chat history using Streamlit session state
* ⚙️ Sidebar settings

## 🎭 Available Personalities

The application currently includes:

* 😊 Friendly Assistant
* 💻 Expert Hacker
* 😵 Panicked College Student at 3 AM
* 🕴️ 1920s Mafia Boss
* 🏋️ Highly Sarcastic Fitness Coach

The selected personality determines how the AI responds.

## 🎚️ Intensity Level

The sidebar includes an **Intensity Level** slider ranging from **1 to 10**.

The selected value is passed to Gemini through the prompt:

```python
Act at an intensity level of {intensity}/10.
```

A higher intensity instructs the AI to act more dramatically and immersively.

## 😀 Dynamic Avatars

The assistant's avatar changes according to the selected personality.

| Personality                      | Avatar |
| -------------------------------- | ------ |
| Friendly Assistant               | 😊     |
| Expert Hacker                    | 💻     |
| Panicked College Student at 3 AM | 😵     |
| 1920s Mafia Boss                 | 🕴️    |
| Highly Sarcastic Fitness Coach   | 🏋️    |

This is implemented using Python `if/elif` control flow.

## 💬 Chat Interface

The application uses Streamlit's native chat components:

```python
st.chat_message()
```

User messages and AI responses are displayed as chat bubbles.

Chat history is maintained using:

```python
st.session_state
```

## 🧠 Prompt Engineering

The AI instructions are dynamically generated using the selected personality and intensity level:

```python
ai_instructions = f"""
You are {personality}.

Act at an intensity level of {intensity}/10.

The higher the intensity, the more dramatic and immersive your personality should become.
Stay completely in character while answering naturally.
"""
```

This allows the same Gemini model to respond differently depending on the user's selected personality.

## 🛠️ Technologies Used

* Python
* Streamlit
* Google Gemini API
* Google GenAI Python SDK
* python-dotenv

## 📁 Project Structure

```text
AI-Multiverse-Chat/
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

The `.env` file is used locally for the Gemini API key and is excluded from GitHub using `.gitignore`.

## 🚀 Setup

### 1. Install the required packages

```bash
pip install -r requirements.txt
```

### 2. Add your Gemini API key

Create a `.env` file in the project folder:

```text
GEMINI_API_KEY=your_api_key_here
```

### 3. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🎯 Assignment Requirements Completed

### Task 1 — UI Cleanup

The personality selector was moved into the sidebar using `st.sidebar.selectbox()`.

### Task 2 — Persona Expansion

Five creative personalities are available in the application.

### Task 3 — Parameter Tuning

An Intensity Level slider from 1–10 was added using `st.sidebar.slider()`, and its value is included in the Gemini prompt.

### Task 4 — Visual Upgrade

The application uses `st.chat_message()` to display user and assistant messages as chat bubbles.

### Task 5 — Dynamic Avatars

An `if/elif` block assigns a different emoji to `bot_avatar` based on the selected personality.

## 👩‍💻 Author

**Akshada Kapadi**

B.Tech Computer Engineering
MirAI School of Technology – AI Builder Track
Virtual Summer Internship 2026

## 📌 Project Context

This project was developed for **Assignment 2 – Upgrading the AI Multiverse** of the MirAI School of Technology Virtual Summer Internship 2026.
