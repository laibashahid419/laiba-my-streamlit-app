import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="Login | Emotion Sensor", layout="centered")

# Custom CSS styling
def inject_css():
    st.markdown("""
    <style>
    .stApp {
        background: url("background.jpg") no-repeat center center fixed;
        background-size: cover;
        opacity: 0.95;
    }
    .overlay {
        background-color: rgba(0, 0, 0, 0.6);
        height: 100%;
        width: 100%;
        padding: 30px;
        border-radius: 15px;
        color: white;
        text-align: center;
    }
    .header {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 20px;
        margin-bottom: 30px;
    }
    .logo {
        width: 80px;
        height: 80px;
        border-radius: 10px;
        cursor: pointer;
    }
    h1 {
        font-size: 2.5rem;
        color: white;
        margin: 0;
    }
    h2 {
        font-size: 1.8rem;
        margin-bottom: 20px;
    }
    .login-form input, .login-form button {
        width: 100%;
        padding: 12px 15px;
        border: none;
        border-radius: 8px;
        font-size: 1rem;
        margin-bottom: 10px;
    }
    .login-form button {
        background-color: #6C5CE7;
        color: white;
        border-radius: 10px;
        transition: background-color 0.3s ease;
    }
    .login-form button:hover {
        background-color: navy;
    }
    .note {
        font-size: 0.9rem;
        margin-top: 10px;
    }
    .note a {
        color: #6C5CE7;
        text-decoration: none;
    }
    .note a:hover {
        text-decoration: underline;
    }
    .footer {
        color: #ccc;
        font-size: 0.9rem;
        margin-top: 40px;
    }
    </style>
    """, unsafe_allow_html=True)

# Inject CSS
inject_css()

# Layout
st.markdown('<div class="overlay">', unsafe_allow_html=True)

# Header
col1, col2 = st.columns([1, 5])
with col1:
    st.image("eso.png", width=80)
with col2:
    st.markdown("<h1>Emotion Sensor</h1>", unsafe_allow_html=True)

st.markdown("<h2>Login to your account</h2>", unsafe_allow_html=True)

# Login form
with st.form(key="login-form"):
    username = st.text_input("Username or Email")
    password = st.text_input("Password", type="password")
    login = st.form_submit_button("Login")

# Logic for redirect (mocked)
if login:
    if username and password:
        st.success("Login successful! Redirecting to emotion analysis...")
        # You can use session state or multipage routing here
    else:
        st.error("Please enter both username and password.")

# Note
st.markdown('<p class="note">Don\'t have an account? <a href="#">Sign up</a></p>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">&copy; 2025 Emotion Sensor AI. All rights reserved.</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)




