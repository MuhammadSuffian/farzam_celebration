import streamlit as st
import random
import time
from datetime import datetime, date
import base64
from PIL import Image
import io
import pytz
import requests
from io import BytesIO
import numpy as np
import math
import hashlib
import os
from cryptography.fernet import Fernet

# Page configuration
st.set_page_config(
    page_title="🎉 Bestie Graduation Bash for FATIMA 🎉",
    page_icon="👯‍♀️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for premium animations and styling
def local_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=Lato:wght@300;400;700&family=Great+Vibes&display=swap');
    
    body {
        overflow-x: hidden;
        background: linear-gradient(135deg, #d8b4fe 0%, #c084fc 50%, #a855f7 100%);
        min-height: 100vh;
    }
    
    .main {
        background: linear-gradient(120deg, rgba(255, 255, 255, 0.9) 0%, rgba(240, 230, 250, 0.8) 100%);
        backdrop-filter: blur(10px);
    }

    .stApp {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(240, 230, 250, 0.85) 50%, rgba(220, 200, 250, 0.9) 100%);
        backdrop-filter: blur(15px);
    }
    
    .floating-element {
        animation: float 6s ease-in-out infinite;
        transform-origin: center;
    }
    
    @keyframes float {
        0% { transform: translateY(0) rotate(0deg) scale(1); }
        25% { transform: translateY(-15px) rotate(3deg) scale(1.02); }
        50% { transform: translateY(0) rotate(0deg) scale(1); }
        75% { transform: translateY(15px) rotate(-3deg) scale(1.02); }
        100% { transform: translateY(0) rotate(0deg) scale(1); }
    }

    @keyframes capToss {
        0% { transform: translateY(0) rotate(0deg); }
        50% { transform: translateY(-150px) rotate(360deg); }
        100% { transform: translateY(0) rotate(720deg); }
    }

    @keyframes diplomaUnroll {
        0% { transform: scale(0.1) rotate(-180deg); opacity: 0; }
        50% { transform: scale(0.5) rotate(-90deg); opacity: 0.5; }
        100% { transform: scale(1) rotate(0deg); opacity: 1; }
    }

    .graduation-cap {
        font-size: 4rem;
        display: inline-block;
        animation: capToss 2s ease-in-out infinite;
        transform-origin: center;
    }

    .diploma {
        font-size: 3.5rem;
        display: inline-block;
        animation: diplomaUnroll 1.5s ease-out;
        transform-origin: center;
    }

    .graduation-emoji {
        font-size: 2.5rem;
        display: inline-block;
        margin: 0 5px;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .premium-container {
        border: 1px solid rgba(255, 255, 255, 0.2);
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(20px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.1),
                    inset 0 0 80px rgba(255, 255, 255, 0.5);
        border-radius: 30px;
        padding: 40px;
        margin: 30px 0;
        transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .premium-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, rgba(100, 149, 237, 0.1), rgba(147, 112, 219, 0.1));
        z-index: -1;
        border-radius: 30px;
    }
    
    .premium-container:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.1), 0 5px 15px rgba(0,0,0,0.05);
    }

    .reflection {
        position: relative;
        overflow: hidden;
    }
    
    .reflection::before {
        content: "";
        position: absolute;
        top: 0;
        left: -100%;
        width: 50%;
        height: 100%;
        background: linear-gradient(
            to right,
            rgba(255, 255, 255, 0) 0%,
            rgba(255, 255, 255, 0.3) 100%
        );
        transform: skewX(-25deg);
        animation: reflection 6s infinite;
    }
    
    @keyframes reflection {
        0% { left: -100%; }
        20%, 100% { left: 100%; }
    }
    
    .shimmer-text {
        background: linear-gradient(-45deg, #d8b4fe, #c084fc, #a855f7, #9333ea);
        background-size: 300% 300%;
        animation: gradient 8s ease infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: 'Cormorant Garamond', serif;
        font-weight: 700;
        font-size: 5rem;
        text-transform: capitalize;
        letter-spacing: 2px;
        line-height: 1.2;
        margin-bottom: 1.5rem;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.1);
    }
    
    .elegant-wish {
        font-family: 'Great Vibes', cursive;
        font-size: 3.5rem;
        background: linear-gradient(45deg, #d8b4fe, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin: 50px 0;
        line-height: 1.4;
        letter-spacing: 1px;
        transform: rotate(-2deg);
    }
    
    .countdown {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.8rem;
        font-weight: 600;
        text-align: center;
        margin: 30px 0;
        color: #333;
    }
    
    .countdown-container {
        display: flex;
        justify-content: center;
        gap: 20px;
    }
    
    .countdown-box {
        background: rgba(255, 255, 255, 0.9);
        box-shadow: 0 10px 30px rgba(168, 85, 247, 0.1);
        color: #333;
        padding: 25px;
        border-radius: 20px;
        min-width: 120px;
        text-align: center;
        border: 1px solid rgba(168, 85, 247, 0.1);
        backdrop-filter: blur(10px);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .countdown-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(168, 85, 247, 0.15);
    }
    
    .countdown-value {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 8px;
        background: linear-gradient(45deg, #d8b4fe, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Cormorant Garamond', serif;
    }
    
    .countdown-label {
        font-size: 1rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #666;
    }
    
    .premium-button {
        background: linear-gradient(45deg, #d8b4fe, #c084fc);
        color: #fff;
        font-family: 'Lato', sans-serif;
        font-weight: 700;
        font-size: 1.1rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 15px 40px;
        border-radius: 50px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1), inset 0 0 20px rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
        backdrop-filter: blur(5px);
        position: relative;
        overflow: hidden;
        cursor: pointer;
    }
    
    .premium-button:before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(120deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: 0.5s;
    }
    
    .premium-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.15), inset 0 0 30px rgba(255, 255, 255, 0.3);
        background: linear-gradient(45deg, #c084fc, #d8b4fe);
    }
    
    .premium-button:hover:before {
        left: 100%;
    }
    
    .premium-button:active {
        transform: translateY(1px);
        box-shadow: 0 5px 10px rgba(0,0,0,0.1), inset 0 0 10px rgba(255, 255, 255, 0.2);
    }
        box-shadow: 0 10px 25px rgba(74, 144, 226, 0.3);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .premium-button::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(45deg, rgba(255,255,255,0.1), rgba(255,255,255,0));
        transform: translateX(-100%);
        transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .premium-button:hover::before {
        transform: translateX(100%);
    }
    
    .premium-button:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(212, 175, 55, 0.4);
    }
    
    .gold-border {
        border: 2px solid #c084fc;
        border-radius: 20px;
        padding: 30px;
        position: relative;
    }
    
    .gold-border::before {
        content: "";
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        border-radius: 20px;
        background: linear-gradient(45deg, #d8b4fe, #c084fc, #a855f7, #9333ea);
        background-size: 400% 400%;
        z-index: -1;
        animation: border-shift 5s linear infinite;
    }
    
    @keyframes border-shift {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }
    
    .message-card {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        padding: 40px;
        margin: 30px 0;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        font-family: 'Lato', sans-serif;
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(168, 85, 247, 0.1);
    }
    
    .message-card::before {
        content: "";
        position: absolute;
        width: 200px;
        height: 200px;
        background: radial-gradient(circle, rgba(168, 85, 247, 0.3) 0%, rgba(255, 255, 255, 0) 70%);
        top: -100px;
        left: -100px;
    }
    
    .message-card::after {
        content: "";
        position: absolute;
        width: 200px;
        height: 200px;
        background: radial-gradient(circle, rgba(168, 85, 247, 0.2) 0%, rgba(255, 255, 255, 0) 70%);
        bottom: -100px;
        right: -100px;
    }
    
    .rose-gold-text {
        background: linear-gradient(to right, #d8b4fe, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
    }
    
    .photo-frame {
        border: 10px solid white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        transform: rotate(2deg);
        transition: all 0.5s ease;
    }
    
    .photo-frame:hover {
        transform: rotate(0deg) scale(1.05);
    }
    
    .shake-animation {
        animation: shake 5s ease-in-out infinite;
        transform-origin: center;
    }
    
    @keyframes shake {
        0%, 100% { transform: rotate(0deg); }
        5%, 15% { transform: rotate(-5deg); }
        10%, 20% { transform: rotate(5deg); }
        25% { transform: rotate(0deg); }
    }
    
    .memory-polaroid {
        background: white;
        padding: 20px 20px 70px 20px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        transform: rotate(random() * 8 - 4 + deg);
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        margin: 25px;
        border-radius: 5px;
        border: 1px solid rgba(168, 85, 247, 0.1);
    }
    
    .memory-polaroid:hover {
        transform: scale(1.05) rotate(0deg);
        z-index: 10;
    }
    
    .memory-polaroid::after {
        content: "Memories";
        position: absolute;
        bottom: 20px;
        left: 0;
        right: 0;
        text-align: center;
        font-family: 'Dancing Script', cursive;
        font-size: 1.5rem;
        color: #333;
    }
    
    .sparkle {
        position: absolute;
        width: 20px;
        height: 20px;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 20 20'%3E%3Cpath d='M10 0L12 7H19L13 12L15 20L10 15L5 20L7 12L1 7H8L10 0Z' fill='%23FFD700'/%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-size: contain;
        opacity: 0;
    }
    
    @keyframes sparkle-fade {
        0% { transform: scale(0) rotate(0deg); opacity: 0; }
        50% { transform: scale(1.2) rotate(180deg); opacity: 1; }
        100% { transform: scale(0) rotate(360deg); opacity: 0; }
    }
    
    .sparkle {
        filter: drop-shadow(0 0 5px rgba(168, 85, 247, 0.5));
        animation: sparkle-fade 2s ease-in-out infinite;
    }
    
    .cake-animation {
        animation: cake-float 3s ease-in-out infinite, cake-glow 2s ease-in-out infinite;
    }
    
    @keyframes cake-float {
        0%, 100% { transform: translateY(0) scale(1); }
        50% { transform: translateY(-25px) scale(1.05); }
    }
    
    @keyframes cake-glow {
        0%, 100% { filter: drop-shadow(0 0 10px rgba(168, 85, 247, 0.7)); }
        50% { filter: drop-shadow(0 0 20px rgba(192, 132, 252, 1)); }
    }
    
    .cake-animation {
        animation: cake-float 4s ease-in-out infinite, cake-glow 3s ease-in-out infinite;
    }
    
    .video-container {
        background: linear-gradient(145deg, rgba(216, 180, 254, 0.1), rgba(192, 132, 252, 0.1));
        border-radius: 20px;
        padding: 20px;
        margin: 20px 0;
        border: 2px solid rgba(168, 85, 247, 0.2);
        box-shadow: 0 10px 30px rgba(168, 85, 247, 0.1);
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
    }
    
    .video-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, rgba(216, 180, 254, 0.05), rgba(192, 132, 252, 0.05));
        z-index: -1;
        border-radius: 20px;
    }
    
    .video-player {
        width: 100%;
        max-width: 100%;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        overflow: hidden;
    }
    
    .video-title {
        font-family: 'Lato', sans-serif;
        font-size: 1.2rem;
        color: #7c3aed;
        font-weight: 600;
        text-align: center;
        margin-bottom: 15px;
        background: linear-gradient(45deg, #d8b4fe, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .video-controls {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: 15px;
    }
    
    .video-btn {
        background: linear-gradient(45deg, #d8b4fe, #c084fc);
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 20px;
        font-family: 'Lato', sans-serif;
        font-weight: 600;
        font-size: 0.9rem;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(168, 85, 247, 0.3);
    }
    
    .video-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(168, 85, 247, 0.4);
    }
    
    </style>
    """, unsafe_allow_html=True)

# Security: password verification
HASHED_PASSWORD = "ae7244fb185a9914fd8758c7a19bde4cc3bb9a524372a9f28d92070494812e74"

def verify_password(plain_text: str) -> bool:
    try:
        return hashlib.sha256(plain_text.encode("utf-8")).hexdigest() == HASHED_PASSWORD
    except Exception:
        return False

# Video encryption/decryption functions
def generate_key_from_password(password: str) -> Fernet:
    """Generate encryption key from password using SHA-256 (matches your encryption method)"""
    try:
        # Hash the password to get a consistent 32-byte key (same as your encryption code)
        key = hashlib.sha256(password.encode("utf-8")).digest()
        # Fernet requires a base64-encoded 32-byte key, so we encode our hash
        key_b64 = base64.urlsafe_b64encode(key)
        return Fernet(key_b64)
    except Exception as e:
        st.error(f"Error generating key: {e}")
        return None

def decrypt_video(encrypted_video_path, password, output_path=None):
    """Decrypt a video file and return video bytes (no disk save)"""
    try:
        # Generate key from password
        fernet = generate_key_from_password(password)
        if fernet is None:
            return None
        
        # Read the encrypted video file
        with open(encrypted_video_path, 'rb') as file:
            encrypted_data = file.read()
        
        # Decrypt the video data
        decrypted_data = fernet.decrypt(encrypted_data)
        
        print(f"Video decrypted successfully in memory!")
        return decrypted_data
        
    except Exception as e:
        print(f"Error decrypting video: {e}")
        return None

def get_video_password():
    """Get the password from session state"""
    # This will be set when user authenticates
    return st.session_state.get('user_password', '')

# Function to auto-play audio from URL
def autoplay_audio_url(url):
    try:
        response = requests.get(url)
        audio_bytes = response.content
        b64 = base64.b64encode(audio_bytes).decode()
        md = f"""
            <audio autoplay loop>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)
    except Exception:
        st.error("Could not load background music. Please ensure you have an internet connection.")

# Function to generate premium confetti
def generate_confetti():
    confetti_html = ""
    colors = ["#d8b4fe", "#c084fc", "#a855f7", "#9333ea", "#7c3aed"]
    
    for i in range(50):
        size = random.randint(5, 15)
        delay = random.uniform(0, 5)
        duration = random.uniform(3, 8)
        color = random.choice(colors)
        left_pos = random.randint(0, 100)
        opacity = random.uniform(0.6, 1)
        
        confetti_html += f"""
        <div style="
            position: fixed; 
            left: {left_pos}%; 
            top: -5%; 
            width: {size}px; 
            height: {size * 1.5}px; 
            background-color: {color}; 
            opacity: {opacity};
            animation: confetti-fall {duration}s {delay}s ease-in-out infinite;
            z-index: -1;
            transform: rotate({random.randint(0, 360)}deg);
        "></div>
        """
    
    st.markdown(confetti_html, unsafe_allow_html=True)

# Function to generate sparkles
def generate_sparkles():
    sparkle_html = ""
    
    for i in range(30):
        size = random.randint(10, 20)
        delay = random.uniform(0, 15)
        duration = random.uniform(2, 4)
        left_pos = random.randint(0, 100)
        top_pos = random.randint(0, 100)
        
        sparkle_html += f"""
        <div style="
            position: fixed; 
            left: {left_pos}%; 
            top: {top_pos}%; 
            width: {size}px; 
            height: {size}px;
            background-image: url('data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22%3E%3Cpath fill=%22%23FFD700%22 d=%22M12,1L9,9L1,12L9,15L12,23L15,15L23,12L15,9Z%22/%3E%3C/svg%3E');
            background-size: cover;
            animation: sparkle-fade {duration}s {delay}s ease-in-out infinite;
            z-index: 1;
        "></div>
        """
    
    st.markdown(sparkle_html, unsafe_allow_html=True)

# Premium graduation wishes templates
def get_premium_eid_wishes():
    return [
        "Bestie FATIMA (Famu), you did it! So proud of you and all our crazy adventures together. Happy Graduation!",
        "To my favorite partner-in-crime, Famu: Congrats on graduating! You're so cute, humorous, and loyal - the world better be ready for us! 🤣",
        "Fatima, my best friend, you've worked so hard and I've loved every moment by your side. Your child-like spirit brings so much joy!",
        "We survived all-nighters, coffee runs, and endless laughter. Happy Graduation, Famu! You're so good and loyal, my bestie! 😂",
        "Fatima (Famu), you're not just a graduate, you're my forever best friend. You're so cute and full of humor - let's celebrate like only we can!",
        "From silly selfies to serious study sessions, we did it all. Congrats, Famu! I love the child in you - you're so good and loyal! 🤪",
        "Cheers to you, Fatima! Couldn't have asked for a better best friend to share this journey with. You're so cute and humorous!",
        "Besties forever! So proud of you, Famu. Happy Graduation! You're so good, loyal, and that child-like quality you have is amazing! 😂"
    ]

# Function to create fancy text with sparkle animation
def fancy_header(text, element_class="shimmer-text", tag="h1"):
    return f'<{tag} class="{element_class}">{text}</{tag}>'

# Personal memories and quotes for Fatima (Famu)
def get_personal_memories():
    return [
        "Our legendary late-night study sessions (and snack attacks) - you're so cute, Famu!",
        "Laughing until we cried over the silliest things - your humor is the best, Fatima!",
        "Taking goofy graduation cap selfies together - I love the child in you, bestie!",
        "Cheering each other on through every exam and meltdown - you're so good and loyal!",
        "Our secret bestie handshake before big presentations - you're my best friend forever!",
        "Dancing in the dorm room after good news - you're so cute and full of humor!",
        "All the inside jokes only we understand, Bestie! You're so good and loyal, Famu!",
        "Dreaming about our future adventures together - I love your child-like spirit, Fatima!"
    ]

# Check if today is Eid
def is_eid():
    # Graduation is a one-time event, so always show the full content
    return True

# Calculate time until Eid
def time_until_eid():
    # Graduation is a one-time event, so no countdown needed
    return 0, 0, 0, 0

# Display premium countdown
def show_premium_countdown():
    # Graduation is a one-time event, so skip countdown
    return True

# Create floating images with parallax effect
def create_floating_image(image_url, size=200, rotation=5, delay=0):
    return f"""
    <img src="{image_url}" width="{size}" style="
        border-radius: 10px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        transform: rotate({rotation}deg);
        animation: float 6s {delay}s ease-in-out infinite;
    ">
    """

# Main function
def main():
    # Password gate
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.markdown("""
            <div class="premium-container" style="max-width: 500px; margin: 60px auto; text-align: center;">
                <h2 style="font-family: 'Cormorant Garamond', serif; margin-bottom: 10px; color: #333;">🔒 Access Required</h2>
                <p style="font-family: 'Lato', sans-serif; color: #666;">Enter the password to access Fatima's Graduation Celebration</p>
            </div>
        """, unsafe_allow_html=True)

        with st.form("password_form", clear_on_submit=False):
            password_input = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Unlock Celebration")
            if submitted:
                if verify_password(password_input):
                    st.session_state.authenticated = True
                    st.session_state.user_password = password_input  # Store password for video decryption
                    st.rerun()
                else:
                    st.error("Incorrect password")

        if not st.session_state.authenticated:
            st.stop()

    st.sidebar.markdown("### Bestie Graduation Bash!")
    st.sidebar.markdown("**Honoring:** FATIMA (a.k.a. Famu 😂)")
    st.sidebar.markdown("**From:** Your Best Friend 💖")
    timezone = pytz.timezone('Asia/Karachi')
    current_time = datetime.now(timezone)
    st.sidebar.markdown(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    local_css()
    generate_confetti()
    generate_sparkles()
    
    # Play background music (a celebratory graduation tune)
    try:
        audio_url = "https://github.com/AkashGutha/birthday-greetings/raw/master/song.mp3"  # Replace with a fun, upbeat song if you want
        autoplay_audio_url(audio_url)
    except:
        pass
    # Always show full content for graduation
    show_full_content = True
    
    # If it's not Eid, show countdown instead
    if not show_full_content:
        access_granted = show_premium_countdown()
        
        # Add a backdoor for testing (remove in production)
        if st.sidebar.checkbox("Preview Eid Content", value=False):
            access_granted = True
            st.sidebar.warning("Preview mode enabled")
        
        if not access_granted:
            # Add footer
            st.markdown("""
            <div style="text-align: center; margin-top: 50px; padding-top: 30px; border-top: 1px solid #eee;">
                <p style="font-family: 'Montserrat', sans-serif; font-size: 0.9rem; color: #666;">
                    Crafted with 💖 by your Bestie | 2025
                </p>
            </div>
            """, unsafe_allow_html=True)
            return
    
    # Full Eid content
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Header
        # Header
            st.markdown(f"""
<div class="premium-container reflection" style="text-align: center; background: linear-gradient(135deg, rgba(74, 144, 226, 0.1) 0%, rgba(155, 89, 182, 0.1) 100%);">
    <span class="graduation-cap">🎓</span>
    {fancy_header("Celebrating FATIMA's Graduation!", "shimmer-text")}
    <div style="margin: 20px 0;">
        <span class="graduation-emoji">📚</span>
        <span class="diploma">📜</span>
        <span class="graduation-emoji">🎊</span>
    </div>
    <p class="elegant-wish">A Journey of Excellence, A Future of Promise for Famu 🎓✨</p>
</div>
""", unsafe_allow_html=True)
    
    # Premium Eid layout
    st.markdown("""
    <div class="premium-container gold-border" style="background: linear-gradient(135deg, rgba(74, 144, 226, 0.05) 0%, rgba(155, 89, 182, 0.05) 100%);">
        <div style="display: flex; flex-direction: column; align-items: center; text-align: center;">
            <div class="shake-animation" style="margin-bottom: 40px;">
                <span class="graduation-cap" style="font-size: 80px;">🎓</span>
                <span style="font-size: 80px; background: linear-gradient(45deg, #4a90e2, #9b59b6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">✨</span>
                <span class="graduation-emoji" style="font-size: 80px;">👩‍🎓</span>
            </div>
    """, unsafe_allow_html=True)
    
    # Display premium personalized message
    eid_message = random.choice(get_premium_eid_wishes())
    
    st.markdown(f"""
        <div class="message-card">
            <h2 style="font-family: 'Montserrat', sans-serif; font-weight: 600; margin-bottom: 20px; color: #9333ea;">
                Dear Bestie FATIMA (Famu),
            </h2>
            <p style="font-family: 'Playfair Display', serif; font-size: 1.3rem; line-height: 1.8; color: #7c3aed; margin-bottom: 20px;">
                {eid_message}
            </p>
            <p style="font-family: 'Montserrat', sans-serif; font-size: 1.1rem; color: #666; margin-top: 30px;">
                I'm so grateful for every moment we've shared as best friends. You're so cute, full of humor, and incredibly loyal. I love the child in you, Fatima (Famu) - it brings so much joy to our friendship. You're not just my friend, you're my best friend, and you're so good and loyal. Here's to more adventures, laughter, and bestie memories. Who would have thought you'd make it this far? Just kidding! 😂
            </p>
            <p class="rose-gold-text" style="text-align: right; font-size: 1.5rem; margin-top: 30px;">
                Besties Forever! 💖
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Birthday memories and quotes
    st.markdown("""
        <h3 style="font-family: 'Cormorant Garamond', serif; text-align: center; margin: 60px 0 30px; background: linear-gradient(45deg, #d8b4fe, #c084fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.5rem; font-weight: 700;">
            ✨ Cherished Memories Together ✨
        </h3>
    """, unsafe_allow_html=True)
    
    # Special memories and quotes in 4 columns
    memories = get_personal_memories()
    
    # Create 4 columns for memories
    col1, col2, col3, col4 = st.columns(4)
    memory_cols = [col1, col2, col3, col4]
    
    # Distribute memories across columns
    for i, memory in enumerate(memories):
        col_index = i % 4  # Determine which column to place the memory
        with memory_cols[col_index]:
            st.markdown(f"""
                <div style="background: linear-gradient(145deg, rgba(216, 180, 254, 0.1), rgba(192, 132, 252, 0.1)); border-radius: 25px; padding: 30px; box-shadow: 0 15px 35px rgba(168, 85, 247, 0.15), inset 0 0 25px rgba(255, 255, 255, 0.5); transform: rotate({random.uniform(-3, 3)}deg); margin: 20px 10px; min-height: 180px; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(255, 255, 255, 0.3); backdrop-filter: blur(10px); transition: all 0.4s ease; cursor: pointer;" onmouseover="this.style.transform='scale(1.05) rotate({random.uniform(-2, 2)}deg)'; this.style.boxShadow='0 20px 40px rgba(168, 85, 247, 0.2), inset 0 0 35px rgba(255, 255, 255, 0.6)';" onmouseout="this.style.transform='scale(1) rotate({random.uniform(-3, 3)}deg)'; this.style.boxShadow='0 15px 35px rgba(168, 85, 247, 0.15), inset 0 0 25px rgba(255, 255, 255, 0.5)';">
                    <p style="font-family: 'Lato', sans-serif; font-size: 1.2rem; background: linear-gradient(45deg, #d8b4fe, #c084fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; font-weight: 600; text-shadow: 2px 2px 4px rgba(0,0,0,0.05);">
                        "{memory}"
                    </p>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("""
        </div>
    """, unsafe_allow_html=True)
    
    # Video section
    st.markdown("""
        <h3 style="font-family: 'Cormorant Garamond', serif; text-align: center; margin: 60px 0 30px; background: linear-gradient(45deg, #d8b4fe, #c084fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.5rem; font-weight: 700;">
            🎬 Featuring Cute Famu in Cute Videos 🎬
        </h3>
    """, unsafe_allow_html=True)
    
    # Video container with 2 rows of 3 videos each
    video_files = [
        "famu1.mp4", "famu2.mp4", "famu3.mp4",
        "famu4.mp4", "famu5.mp4", "famu6.mp4"
    ]
    
    # Create two rows of videos
    for row in range(2):
        cols = st.columns(3)
        for col_idx in range(3):
            video_idx = row * 3 + col_idx
            if video_idx < len(video_files):
                with cols[col_idx]:
                    video_file = video_files[video_idx]
                    video_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), video_file)
                    
                    if os.path.exists(video_path):
                        # Create a unique key for each video
                        video_key = f"video_{video_idx}"
                        
                        # Check if video is already decrypted in session state
                        if f"decrypted_{video_key}" not in st.session_state:
                            st.session_state[f"decrypted_{video_key}"] = None
                        
                        # Decrypt button
                        if st.button(f"🔓 Decrypt Video {video_idx + 1}", key=f"decrypt_{video_key}"):
                            password = st.session_state.get('user_password', '')
                            if password:
                                with st.spinner(f"Decrypting video {video_idx + 1}..."):
                                    decrypted_bytes = decrypt_video(video_path, password)
                                    if decrypted_bytes:
                                        st.session_state[f"decrypted_{video_key}"] = decrypted_bytes
                                        st.success(f"Video {video_idx + 1} decrypted successfully!")
                                    else:
                                        st.error(f"Failed to decrypt video {video_idx + 1}")
                            else:
                                st.error("No password available")
                        
                        # Display video if decrypted
                        if st.session_state[f"decrypted_{video_key}"]:
                            decrypted_video_bytes = st.session_state[f"decrypted_{video_key}"]
                            try:
                                # Display video in fixed container
                                st.markdown(f"""
                                    <div class="video-container">
                                        <div class="video-title">Video {video_idx + 1} - Cute Famu Moments! 💜</div>
                                        <div class="video-player">
                                """, unsafe_allow_html=True)
                                
                                st.video(decrypted_video_bytes)
                                
                                st.markdown("""
                                        </div>
                                    </div>
                                """, unsafe_allow_html=True)
                            except Exception as e:
                                st.error(f"Error loading video {video_idx + 1}: {e}")
                        else:
                            # Placeholder for encrypted video
                            st.markdown(f"""
                                <div class="video-container">
                                    <div style="font-size: 3rem; margin-bottom: 15px; text-align: center;">🔒</div>
                                    <div class="video-title">Encrypted Video {video_idx + 1}</div>
                                    <p style="font-family: 'Montserrat', sans-serif; font-size: 0.9rem; color: #666; text-align: center;">
                                        Click decrypt to unlock Famu's cute moments!
                                    </p>
                                </div>
                            """, unsafe_allow_html=True)
                    else:
                        # Placeholder for missing video file
                        st.markdown(f"""
                            <div class="video-container">
                                <div style="font-size: 3rem; margin-bottom: 15px; text-align: center;">📹</div>
                                <div class="video-title">Video {video_idx + 1} - Coming Soon!</div>
                                <p style="font-family: 'Montserrat', sans-serif; font-size: 0.9rem; color: #666; text-align: center;">
                                    More cute Famu moments to be added!
                                </p>
                            </div>
                        """, unsafe_allow_html=True)
    
    # Interactive "gift" - digital birthday cake
    st.markdown("""
        <h3 style="font-family: 'Playfair Display', serif; text-align: center; margin: 40px 0 20px; color: #7c3aed;">
            Bestie Vibes Only
        </h3>
        
        <div style="text-align: center; margin: 40px 0;">
            <div style="font-size: 120px; margin: 20px 0 40px 0; display: inline-block;">
                <span class="graduation-emoji">👩‍🎓</span>
                <span class="graduation-cap">🎓</span>
                <span class="diploma">📜</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Make a wish section
    st.markdown("""
       <style>
        <div class="premium-container" style="text-align: center; max-width: 600px; margin: 30px auto; background: linear-gradient(135deg, rgba(251, 194, 235, 0.8) 0%, rgba(249, 213, 236, 0.8) 100%); border: 1px solid rgba(255, 255, 255, 0.3); box-shadow: 0 20px 40px rgba(0,0,0,0.1), inset 0 0 60px rgba(255, 255, 255, 0.5);">
            <h3 style="font-family: 'Dancing Script', cursive; font-size: 3rem; color: #9333ea; margin: 20px 0;">
                Bestie Graduation Bash for FATIMA!
            </h3>
            
             <p style="font-family: 'Montserrat', sans-serif; font-size: 1.2rem; color: #7c3aed; margin-bottom: 40px;">
                 Love you forever, Famu! You're so cute, humorous, and loyal - my best friend! I love the child in you, Fatima. Here's to your big day and all our future adventures! 👯‍♀️💖 You're so good and loyal - who would have thought our study buddy would become a graduate? 😂
             </p>
    </div>
                </style>
    """, unsafe_allow_html=True)
    
    # Blessings button with animation - centered using columns
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("👯‍♀️ Send Bestie Wishes! 💖", key="blessings_button", use_container_width=True):
            st.balloons()
            st.markdown("""
            <div style="text-align: center; margin: 30px 0;">
                <h3 style="font-family: 'Dancing Script', cursive; font-size: 2rem; color: #9333ea;">
                    Bestie, you're a star!
                </h3>
                <p style="font-family: 'Montserrat', sans-serif; font-size: 1.1rem; color: #7c3aed;">
                    Here's to us, to you, and to all the memories we'll make. Love you, Fatima!
                </p>
                <div style="font-size: 50px; margin: 20px 0;">
                    <span class="graduation-emoji">👯‍♀️</span>
                    <span class="graduation-cap">🎓</span>
                    <span class="graduation-emoji">💖</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("""
        </div>
    """, unsafe_allow_html=True)
    
    # Birthday quotes carousel
    st.markdown("""
        <div style="text-align: center; margin: 40px 0;">
            <h3 style="font-family: 'Playfair Display', serif; color: #7c3aed; margin-bottom: 20px;">
                Bestie Graduation Wishes
            </h3>
            <div class="premium-container" style="background: linear-gradient(to right, #e9d5ff, #ddd6fe); text-align: center; padding: 30px;">
                 <p style="font-family: 'Dancing Script', cursive; font-size: 1.8rem; color: #7c3aed;">
                     "Fatima (Famu), you're not just a graduate, you're my best friend for life! You're so cute, humorous, and loyal. I love the child in you - you're so good and loyal! Congrats and let's celebrate! Remember when you thought a FYP Report was a type of dessert? 🤣"
                 </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Final Eid wish
    st.markdown("""
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding-top: 30px; border-top: 1px solid #eee;">
        <p style="font-family: 'Montserrat', sans-serif; font-size: 0.9rem; color: #7c3aed;">
            Crafted with 💖 by your Bestie | 2025
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()