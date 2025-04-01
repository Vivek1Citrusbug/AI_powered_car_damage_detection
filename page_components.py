import streamlit as st

def configure_ui():
    """
    Set up the UI components
    """

    st.set_page_config(page_title="AI-Powered Car Damage Detection", layout="wide")

    st.markdown("""
        <style>
        .stApp { background-color: #f8f9fa; }
        .title { text-align: center; color: #4CAF50; font-size: 28px; font-weight: bold; }
        .sidebar .sidebar-content { background-color: #ffffff; }
        </style>
        """, unsafe_allow_html=True)

    st.markdown("<p class='title'>AI-Powered car dent and damage Detection</p>", unsafe_allow_html=True)
    st.write("🚀 Upload multiple **images**, and the app will detect **dent and damages**.")

def get_sidebar_options():
    """
    Render sidebar options
    """
    
    st.sidebar.title("🔍 Select YOLOv8 Model")
    model_choice = st.sidebar.selectbox("Choose a model", ["YOLOv8-medium", "YOLOv8-small"])

    st.sidebar.title("📤 Upload Images or Videos")
    uploaded_files = st.sidebar.file_uploader("Upload multiple images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    
    # use_webcam = st.sidebar.checkbox("📷 Enable Webcam for Live Detection")
    # for using webcam we can also return it as use_webcam

    return model_choice, uploaded_files

