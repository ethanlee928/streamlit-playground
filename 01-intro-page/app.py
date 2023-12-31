from pathlib import Path

from PIL import Image

import streamlit as st

st.set_page_config(page_title="Ethan Lee Bio", page_icon="🚀", layout="wide")


@st.cache_data(ttl=3600)  # 1 hour time to live
def load_images():
    img_dir = Path() / "images"
    return {img_path.stem: Image.open(img_path) for img_path in img_dir.glob("*.jpg")}


IMAGES = load_images()
RESPONSE_FILE = Path() / "response.txt"

with st.container():
    st.subheader("Hi I am Ethan 👋")
    st.title("A Computer Vision Engineer")
    st.write("I am passionate about tech! To make the world more efficient.")
    st.write("[Github >](https://github.com/ethanlee928)")

with st.container():
    st.write("---")
    l_col, r_col = st.columns(2)
    with l_col:
        st.header("What I do")
        st.write("##")
        st.write(
            """
                I am interested to the following topics:
                - Theoretical & Computational Physics
                - Machine Learning
                - Financial Engineering
                - High Performance Computing
                """
        )
    with r_col:
        st.video("https://youtu.be/dQw4w9WgXcQ")

with st.container():
    st.write("---")
    st.header("Side Projects for Fun 😆")
    st.write("##")
    simulation_img_col, simulation_txt_col = st.columns((1, 2))
    with simulation_img_col:
        st.image(IMAGES["trajectory"])
    with simulation_txt_col:
        st.subheader("Finance Monte-Carlo Simulation using PyTorch")
        st.write(
            """
                - An easy-to-use python package to do Monte-Carlo Simulation on stock prices
                - GPU accelerated Monte-Carlo simulation, that could allow simulation more random walkers without a large time penalty
                 """
        )
        st.markdown("[Github >](https://github.com/ethanlee928/pyfmc)")

    bot_txt_col, bot_img_col = st.columns((2, 3))
    with bot_txt_col:
        st.subheader("Finance Slackbot")
        st.write(
            """
                    - A simple bot utilizing Polygon API, Slack API to monitor the financial market, including stocks, forex, options, and crypto

                 """
        )
        st.markdown("[Github >](https://github.com/ethanlee928/FinanceBot)")
    with bot_img_col:
        st.image(IMAGES["financebot"])


with st.container():
    st.write("---")
    st.header("Beautiful Places 🛫 🇯🇵")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(IMAGES["tateyama"], caption="Tateyama")
        st.image(IMAGES["snow_corridor"], caption="Snow Corridor")
    with col2:
        st.image(IMAGES["kamikochi"], caption="Kamikochi")
        st.image(IMAGES["monkey"], caption="Wild Monkeys")
    with col3:
        st.image(IMAGES["shirakawa"], caption="Shirakawa")
        st.markdown(
            "<p style='text-align: center; font-style: italic;'>\"a small, traditional village showcasing a building style known as gasshō-zukuri.\" &mdash; Wikipedia</p>",
            unsafe_allow_html=True,
        )
    st.markdown(
        "<h5 style='text-align: center; font-family: Helvetica;'>Shot on iPhone</h5>",
        unsafe_allow_html=True,
    )
