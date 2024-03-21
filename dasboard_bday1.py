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

name = "Hidayah "

st.header("              Barallah fii umrik Falaqun Nurul Hidayah             ")   
st.subheader("                            Created By Emma                        ")
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
#image_url1 = "https://drive.google.com/uc?id=1VUZbHx4Al9vFcfMJ3APK0tf4BdY_iSg5"
image_url2 = "https://drive.google.com/uc?id=1h63np0iXuyqwQYOA9rIXzcvt5Ic1cbSK"

# Mendapatkan gambar dari URL
#image1 = get_image_from_url(image_url1)
image2 = get_image_from_url(image_url2)

# Tampilkan gambar
#st.image(image1, caption='Gambar dari Google Drive 1', use_column_width=True)
st.image(image2, caption='Kue Digitalnya Hidayah', use_column_width=True)
# ------------------------------------
# Tautan berbagi untuk file audio di Google Drive
audio_url = "https://drive.google.com/file/d/19MqO_8Jk5uZt36NndQIDEIXlNfcFFmpL"

# Menampilkan file audio menggunakan st.audio
# st.audio(audio_url, format='audio/mp3')
st.audio(audio_url)
# -------------------------------------------
# try:
#     winsound.Beep(264, 250)
#     sys.stdout.write('Ha')
#     time.sleep(500/2000.0)
#     # st.write(' ')
#     sys.stdout.write('ppy ')
#     winsound.Beep(264, 250)
#     time.sleep(250/2000.0)
#     # st.write(' ')
#     sys.stdout.write('birth')
#     winsound.Beep(297, 1000)
#     time.sleep(250/2000.0)
#     # st.write(' ')
#     sys.stdout.write('day ')
#     winsound.Beep(264, 1000)
#     time.sleep(250/2000.0)
#     # st.write(' ')
#     sys.stdout.write('to ')
#     winsound.Beep(352, 1000)
#     time.sleep(250/2000.0)
#     # st.write(' ')
#     st.write('Happy Birthday to you')
#     winsound.Beep(330, 2000)
#     time.sleep(500/2000.0)

#     sys.stdout.write('Ha')
#     winsound.Beep(264, 250)
#     time.sleep(500/2000.0)
#     # st.write(' ')
#     sys.stdout.write('ppy ')
#     winsound.Beep(264, 250)
#     time.sleep(250/2000.0)
#     # st.write(' ')
#     sys.stdout.write('birth')
#     winsound.Beep(297, 1000)
#     time.sleep(250/2000.0)
#     # st.write(' ')
#     sys.stdout.write('day ')
#     winsound.Beep(264, 1000)
#     time.sleep(250/2000.0)
#     # st.write(' ')
#     sys.stdout.write('to ')
#     winsound.Beep(396, 1000)
#     time.sleep(250/2000.0)
#     # st.write(' ')
#     st.write('Happy Birthday to you')
#     winsound.Beep(352, 2000)
#     time.sleep(500/2000.0)
    
#     sys.stdout.write('Ha')
#     winsound.Beep(264, 250)
#     time.sleep(250/2000.0)
#     # st.write(' ')
#     sys.stdout.write('ppy ')
#     winsound.Beep(264, 500)
#     time.sleep(250/1000.0)
#     # st.write(' ')
#     sys.stdout.write('birth')
#     winsound.Beep(440, 1000)
#     time.sleep(250/2000.0)
#     # st.write(' ')
#     sys.stdout.write('day ')
#     winsound.Beep(352, 1000)
#     time.sleep(250/2000.0)
#     # st.write(' ')
#     sys.stdout.write('dear ')
#     winsound.Beep(330, 1000)
#     # st.write(' ')
#     st.write('Happy Birthday dear ' + name)
#     time.sleep(250/2000.0)
#     winsound.Beep(297, 1000)
    
#     winsound.Beep(440, 1000)
#     time.sleep(250/2000.0)
    
#     time.sleep(500/2000.0)
#     sys.stdout.write('Ha')
#     winsound.Beep(466, 250)
#     time.sleep(500/2000.0)
#     # st.write(' ')
#     sys.stdout.write('ppy ')
#     winsound.Beep(466, 250)
#     time.sleep(250/2000.0)
#     # st.write(' ')
#     sys.stdout.write('birth')
#     winsound.Beep(440, 1000)
#     time.sleep(250/2000.0)
#     # st.write(' ')
#     sys.stdout.write('day ')
    
#     winsound.Beep(352, 1000)
#     time.sleep(250/2000.0)
#     # st.write(' ')
#     sys.stdout.write('to ')
#     winsound.Beep(396, 1000)
#     time.sleep(250/2000.0)
#     # st.write(' ')
#     st.write('Happy Birthday to you')
#     winsound.Beep(352, 2000)
#     time.sleep(250/2000.0)


def colorful_text(text):
    colored_text = ""
    colors = ['#B5C0D0', '#CCD3CA', '#F5E8DD', '#EED3D9', '#EFBC9B', '#FBF3D5', '#D6DAC8', '#9CAFAA']
    color_index = 0
    for char in text:
        colored_text += f'<span style="color:{colors[color_index]}; font-weight:bold">{char}</span>'
        color_index = (color_index + 1) % len(colors)
    return colored_text

st.markdown(f'<p style="font-size:30px">{colorful_text("HAPPY BIRTHDAY FALAQUN NURUL HIDAYAH <3")}</p>', unsafe_allow_html=True)

# except Exception as e:
#     st.error(f"Error: {e}")


    
