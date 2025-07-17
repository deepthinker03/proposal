import streamlit as st
import time

st.set_page_config(page_title="My Cutie Pie 💖", layout="centered")

st.markdown("<h1 style='text-align: center; color: deeppink;'>💖 Proposal For My Bndr 💖</h1>", unsafe_allow_html=True)

with st.spinner("Loading love... 💕"):
    time.sleep(2)

# Sweet Messages
messages = [
    "❤️❤️❤️ My Cutie Pie My Bndr ❤️❤️❤️",
    "My Sweet Heart ..Mera Janemann ❤️❤️❤️",
    "❤️❤️ Meraa Gulab Jamun ❤️❤️",
    "You are mine Melaa Motaa Bcchaa 😘",
    "I love you My Cutie Pie ❤️",
    "U are the most liked person... Hamesha tu nai mera saat diya hai.. Awr bharosa kiya hai ❤️",
    "I will never forget our memories...",
    "Your smile is my favorite thing in the world 😊",
    "The way you support me means more than words ❤️",
    "I am missing you every moment Bndrrrr 🙁🙁",
    "I Love you Melaaaa bachaa ❤️... You are MINE..."
]

for msg in messages:
    st.success(msg)
    time.sleep(1.5)

st.markdown("### 💌 Forever Yours")

# Optional image or animation
st.image("https://i.pinimg.com/originals/49/b5/7c/49b57cd2cb57b7e61a2f7d0248b2b76b.gif", caption="Sending love...", use_column_width=True)
