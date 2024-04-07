import streamlit as st

# from __future__ import print_function
import time
import sys

st.markdown(
    """
    <style>
    body {
        background-color: #000000;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# try:
#     import winsound
# except ImportError:
#     import os

st.title('🎂 Barakallah Fii Umrik 🎂')

name = "Viola "

st.header("              Barallah fii umrik Zuvia Laviola             ")   
st.markdown("                    Created By Emma                        ")
st.write("it's your brithday 🎉! Selamat ulang tahun BESTIEE! Semoga tahun ini membawa kamu lebih dekat pada impianmu dan membahagiakanmu sebanyak yang kamu bahagiakan orang lain. Dan semoga segala keinginan dan goals dalam hidupmu bisa tercapai di tahun ini. Aamiinnnn")


from PIL import Image
import requests
from io import BytesIO
import streamlit as st

# Fungsi untuk mendapatkan gambar dari URL
def get_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

# URL gambar di Google Drive
# image_url1 = "https://drive.google.com/uc?id=1VUZbHx4Al9vFcfMJ3APK0tf4BdY_iSg5"
image_url2 = "https://drive.google.com/uc?id=1TO6QURYgGGZE_8YLzrs0tfD7uFHnJzKh" 

# Mendapatkan gambar dari URL
# image1 = get_image_from_url(image_url1)
image2 = get_image_from_url(image_url2)

# Tampilkan gambar
# st.image(image1, caption='Gambar dari Google Drive 1', use_column_width=True)
st.image(image2, caption='Kue Digitalnya COMEL KANNN', use_column_width=True)
# ------------------------------------
# URL raw file audio di GitHub
audio_url = "https://github.com/Emmaru2/Birthday_cie/raw/main/Good_Morning_to_All(chosic.com).mp3"

# Menampilkan file audio menggunakan st.audio
st.audio(audio_url, format='audio/mp3')



def colorful_text(text):
    colored_text = ""
    colors = ['#222831', '#31363F', '#76ABAE', '#35374B', '#344955', '#50727B', '#78A083', '#070F2B', '#1B1A55', '#535C91', '#9290C3']
    color_index = 0
    for char in text:
        colored_text += f'<span style="color:{colors[color_index]}; font-weight:bold">{char}</span>'
        color_index = (color_index + 1) % len(colors)
    return colored_text

st.markdown(f'<p style="font-size:30px">{colorful_text("HAPPY BIRTHDAY ZUVIA LAVIOLA <3")}</p>', unsafe_allow_html=True)

# except Exception as e:
#     st.error(f"Error: {e}")
