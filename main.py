import os
import streamlit as st
from streamlit_option_menu import option_menu
from apps.face import face_page
from apps.audio import audio_page

# Allow KMP duplication for Mac/Intel chip conflict
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

# --- Page Configuration ---
st.set_page_config(
    page_title="Emotion Detector",
    page_icon="🧠",
    layout="centered"
)

# --- Modern dark UI (Hero Section) ---
st.markdown("""
<style>
body {
    background-color: #000;
    color: #fff;
    font-family: 'Segoe UI', sans-serif;
}
.navbar {
    display: flex;
    justify-content: space-between;
    padding: 1rem 2rem;
    position: relative;
    width: 100%;
    z-index: 10;
}
.navbar .logo {
    font-size: 1.5rem;
    font-weight: bold;
    color: white;
}
.nav-links {
    list-style: none;
    display: flex;
    gap: 1.5rem;
    margin: 0;
    padding: 0;
}
.nav-links li a {
    text-decoration: none;
    color: white;
    font-weight: 500;
}
.hero {
    height: 80vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}
.hero h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    background: radial-gradient(circle, #ff00ff, #00ffff, #0099ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero p {
    font-size: 1.2rem;
    margin-bottom: 2rem;
}
.button-group {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    justify-content: center;
}
.btn {
    border: none;
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    border-radius: 999px;
    cursor: pointer;
    transition: all 0.3s ease-in-out;
    color: white;
    box-shadow: 0 0 10px rgba(255,255,255,0.2);
}
.btn:hover {
    transform: scale(1.05);
}
.btn.blue { background-color: #007bff; }
.btn.purple { background-color: #9b59b6; }
.btn.orange { background-color: #f39c12; }
.btn.green { background-color: #27ae60; }
</style>


""", unsafe_allow_html=True)

# --- Sidebar Layout ---
with st.sidebar:
    st.title("Emotion AI")
    st.caption("😑 😁 😭 Real-time Emotion Detection")
    st.markdown("---")

    selected_page = option_menu(
        menu_title=None,
        options=["Face Emotion Detection", "Audio Emotion Detection"],
        icons=["camera", "mic"],
        default_index=0,
    )

    st.markdown("---")
    st.markdown("👨🏾‍💻 Made by [Aaron](https://github.com/thebugged)")

# --- Page Router ---
pages = {
    "Face Emotion Detection": face_page,
    "Audio Emotion Detection": audio_page
}

if selected_page in pages:
    pages[selected_page]()
else:
    st.error("Invalid Page Selected.")
