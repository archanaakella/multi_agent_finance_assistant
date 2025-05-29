import streamlit as st
import requests

st.set_page_config(page_title="Multi-Agent Finance Assistant", layout="centered")
st.title("📊 Multi-Agent Finance Assistant")

# Text Query Section
st.subheader("💬 Text-Based Financial Query")
query = st.text_input("Ask a financial question (e.g., 'Samsung earnings'):")

if query:
    try:
        response = requests.get(f"http://127.0.0.1:8001/retrieve/?query={query}")
        if response.status_code == 200:
            result = response.json()
            insight = result.get("retrieved_insight", "No insight available.")
            st.success(f"📈 Market Insight: {insight}")
        else:
            st.error(f"Error from API: {response.status_code}")
    except Exception as e:
        st.error(f"❌ Failed to fetch insight: {e}")

# Voice Query Section
st.subheader("🎙️ Voice-Based Query (Simulated)")
uploaded_file = st.file_uploader("Upload a voice query (.wav format):", type=["wav"])

if uploaded_file:
    try:
        # Simulate speech-to-text conversion (or assume text for now)
        simulated_text = "Samsung earnings"  # You can integrate Whisper STT here
        response = requests.post(
            "http://127.0.0.1:8001/process_voice/",
            json={"audio_text": simulated_text}
        )
        if response.status_code == 200:
            result = response.json()
            spoken_response = result.get("spoken_response", "No voice insight.")
            st.success(f"🔊 Voice Response: {spoken_response}")
        else:
            st.error(f"Voice query failed with status {response.status_code}")
    except Exception as e:
        st.error(f"❌ Error processing voice query: {e}")