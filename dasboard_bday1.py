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

try:
    import winsound
except ImportError:
    import os

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

try:
    winsound.Beep(264, 250)
    sys.stdout.write('Ha')
    time.sleep(500/2000.0)
    # st.write(' ')
    sys.stdout.write('ppy ')
    winsound.Beep(264, 250)
    time.sleep(250/2000.0)
    # st.write(' ')
    sys.stdout.write('birth')
    winsound.Beep(297, 1000)
    time.sleep(250/2000.0)
    # st.write(' ')
    sys.stdout.write('day ')
    winsound.Beep(264, 1000)
    time.sleep(250/2000.0)
    # st.write(' ')
    sys.stdout.write('to ')
    winsound.Beep(352, 1000)
    time.sleep(250/2000.0)
    # st.write(' ')
    st.write('Happy Birthday to you')
    winsound.Beep(330, 2000)
    time.sleep(500/2000.0)

    sys.stdout.write('Ha')
    winsound.Beep(264, 250)
    time.sleep(500/2000.0)
    # st.write(' ')
    sys.stdout.write('ppy ')
    winsound.Beep(264, 250)
    time.sleep(250/2000.0)
    # st.write(' ')
    sys.stdout.write('birth')
    winsound.Beep(297, 1000)
    time.sleep(250/2000.0)
    # st.write(' ')
    sys.stdout.write('day ')
    winsound.Beep(264, 1000)
    time.sleep(250/2000.0)
    # st.write(' ')
    sys.stdout.write('to ')
    winsound.Beep(396, 1000)
    time.sleep(250/2000.0)
    # st.write(' ')
    st.write('Happy Birthday to you')
    winsound.Beep(352, 2000)
    time.sleep(500/2000.0)
    
    sys.stdout.write('Ha')
    winsound.Beep(264, 250)
    time.sleep(250/2000.0)
    # st.write(' ')
    sys.stdout.write('ppy ')
    winsound.Beep(264, 500)
    time.sleep(250/1000.0)
    # st.write(' ')
    sys.stdout.write('birth')
    winsound.Beep(440, 1000)
    time.sleep(250/2000.0)
    # st.write(' ')
    sys.stdout.write('day ')
    winsound.Beep(352, 1000)
    time.sleep(250/2000.0)
    # st.write(' ')
    sys.stdout.write('dear ')
    winsound.Beep(330, 1000)
    # st.write(' ')
    st.write('Happy Birthday dear ' + name)
    time.sleep(250/2000.0)
    winsound.Beep(297, 1000)
    
    winsound.Beep(440, 1000)
    time.sleep(250/2000.0)
    
    time.sleep(500/2000.0)
    sys.stdout.write('Ha')
    winsound.Beep(466, 250)
    time.sleep(500/2000.0)
    # st.write(' ')
    sys.stdout.write('ppy ')
    winsound.Beep(466, 250)
    time.sleep(250/2000.0)
    # st.write(' ')
    sys.stdout.write('birth')
    winsound.Beep(440, 1000)
    time.sleep(250/2000.0)
    # st.write(' ')
    sys.stdout.write('day ')
    
    winsound.Beep(352, 1000)
    time.sleep(250/2000.0)
    # st.write(' ')
    sys.stdout.write('to ')
    winsound.Beep(396, 1000)
    time.sleep(250/2000.0)
    # st.write(' ')
    st.write('Happy Birthday to you')
    winsound.Beep(352, 2000)
    time.sleep(250/2000.0)
# except:
#     os.system('beep -f 264 -l 250')
#     sys.stdout.write('Ha')
#     sys.stdout.flush()
#     time.sleep(500/2000.0)
#     sys.stdout.write('ppy ')
#     sys.stdout.flush()	
#     os.system('beep -f 264 -l 250')
#     time.sleep(250/2000.0)
#     sys.stdout.write('birth')
    
#     sys.stdout.flush()
#     os.system('beep -f 297 -l 1000')
#     time.sleep(250/2000.0)
#     sys.stdout.write('day ')
#     sys.stdout.flush()
#     os.system('beep -f 264 -l 1000')
#     time.sleep(250/2000.0)
#     sys.stdout.write('to ')
#     sys.stdout.flush()
#     os.system('beep -f 352 -l 1000')
#     time.sleep(250/2000.0)
#     print ('you')
#     os.system('beep -f 330 -l 2000')
#     time.sleep(500/2000.0)
        
#     sys.stdout.write('Ha')
#     sys.stdout.flush()
#     os.system('beep -f 264 -l 250')
#     time.sleep(500/2000.0)
#     sys.stdout.write('ppy ')
#     sys.stdout.flush()
#     os.system('beep -f 264 -l 250')
#     time.sleep(250/2000.0)
#     sys.stdout.write('birth')
#     sys.stdout.flush()
#     os.system('beep -f 297 -l 1000')
#     time.sleep(250/2000.0)
#     sys.stdout.write('day ')
#     sys.stdout.flush()
#     os.system('beep -f 264 -l 1000')
#     time.sleep(250/2000.0)
#     sys.stdout.write('to ')
#     sys.stdout.flush()
#     os.system('beep -f 396 -l 1000')
#     time.sleep(250/2000.0)
#     print ('you')
#     os.system('beep -f 352 -l 2000')
#     time.sleep(500/2000.0)
        
#     sys.stdout.write('Ha')
#     sys.stdout.flush()
#     os.system('beep -f 264 -l 250')
#     time.sleep(250/2000.0)
#     sys.stdout.write('ppy ')
#     sys.stdout.flush()
#     os.system('beep -f 264 -l 500')
#     time.sleep(250/1000.0)
#     sys.stdout.write('birth')
#     sys.stdout.flush()
#     os.system('beep -f 440 -l 1000')
#     time.sleep(250/2000.0)
#     sys.stdout.write('day ')
#     sys.stdout.flush()
#     os.system('beep -f 352 -l 1000')
#     time.sleep(250/2000.0)
#     sys.stdout.write('dear ')
#     sys.stdout.flush()
#     os.system('beep -f 330 -l 1000')
#     print (name )
#     time.sleep(250/2000.0)
#     os.system('beep -f 297 -l 1000')
        
#     os.system('beep -f 440 -l 1000')
#     time.sleep(250/2000.0)
        
#     time.sleep(500/2000.0)
#     sys.stdout.write('Ha')
#     sys.stdout.flush()
#     os.system('beep -f 466 -l 250')
#     time.sleep(500/2000.0)
#     sys.stdout.write('ppy ')
#     sys.stdout.flush()
#     os.system('beep -f 466 -l 250')
#     time.sleep(250/2000.0)
#     sys.stdout.write('birth')
#     sys.stdout.flush()
#     os.system('beep -f 440 -l 1000')
#     time.sleep(250/2000.0)
#     sys.stdout.write('day ')
#     sys.stdout.flush()
#     os.system('beep -f 352 -l 1000')
#     time.sleep(250/2000.0)
#     sys.stdout.write('to ')
#     sys.stdout.flush()
#     os.system('beep -f 396 -l 1000')
#     time.sleep(250/2000.0)
#     print ('you')
#     os.system('beep -f 352 -l 2000')
#     time.sleep(250/2000.0)


    # st.subheader ('HAPPY BIRTHDAY ' + name + ' <3 !!!')

    # st.markdown (""" ----------------------------------------------
    #              | |  | |    /\    |  __ \ |  __ \ \ \   / / |  _ \|_   _||  __ \|__   __|| |  | ||  __ \    /\ \ \   / /
    #              | |__| |   /  \   | |__) || |__) | \ \_/ /  | |_) | | |  | |__) |  | |   | |__| || |  | |  /  \ \ \_/ /  
    #              |  __  |  / /\ \  |  ___/ |  ___/   \   /   |  _ <  | |  |  _  /   | |   |  __  || |  | | / /\ \ \   /  
    #              | |  | | / ____ \ | |     | |        | |    | |_) |_| |_ | | \ \   | |   | |  | || |__| |/ ____ \ | |   
    #              |_|  |_|/_/    \_\|_|     |_|        |_|    |____/|_____||_|  \_\  |_|   |_|  |_||_____//_/    \_\|_|   
              
    #           """)


    def colorful_text(text):
        colored_text = ""
        colors = ['#B5C0D0', '#CCD3CA', '#F5E8DD', '#EED3D9', '#EFBC9B', '#FBF3D5', '#D6DAC8', '#9CAFAA']
        color_index = 0
        for char in text:
            colored_text += f'<span style="color:{colors[color_index]}; font-weight:bold">{char}</span>'
            color_index = (color_index + 1) % len(colors)
        return colored_text

    st.markdown(f'<p style="font-size:30px">{colorful_text("HAPPY BIRTHDAY FALAQUN NURUL HIDAYAH <3")}</p>', unsafe_allow_html=True)

    # def colorful_text(text):
    #     colored_text = ""
    #     colors = ['#B5C0D0', '#CCD3CA', '#F5E8DD', '#EED3D9', '#EFBC9B', '#FBF3D5', '#D6DAC8', '#9CAFAA']
    #     color_index = 0
    #     for char in text:
    #         colored_text += f'<span style="color:{colors[color_index]}; font-weight:bold">{char}</span>'
    #         color_index = (color_index + 1) % len(colors)
    #     return colored_text

    # # def main():
    # st.title(colorful_text("HAPPY BIRTHDAY FALAQUN NURUL HIDAYAH"))
    #     birthday_message = "HAPPY BIRTHDAY FALAQUN NURUL HIDAYAH"
    #     colored_message = colorful_text(birthday_message)
    #     st.title(f'{colored_message}</p>')

    # if __name__ == "__main__":
    #     main()
except Exception as e:
    st.error(f"Error: {e}")

# -----------------------------------------------
# import time
# import streamlit as st

# # Define the message and the duration of each frame in seconds
# message = "Happy Birthday"
# duration = 0.5

# # Create a loop to display each character of the message for the specified duration
# for i in range(len(message)):
#     st.write(message[:i+1])
#     time.sleep(duration)
    
# import streamlit as st
# import time
# from random import randint

# def happy_birthday_animation():
#     space = ''
#     for i in range(1, 1000):
#         count = randint(1, 100)
#         while(count > 0):
#             space += ' '
#             count -= 1
#         if(i % 10 == 0):
#             st.write(space + '🎂Happy Birthday!')
#         elif(i % 9 == 0):
#             st.write(space + "🎂")
#         elif(i % 5 == 0):
#             st.write(space + "💛")
#         elif(i % 8 == 0):
#             st.write(space + "🎉")
#         elif(i % 7 == 0):
#             st.write(space + "🍫")
#         elif(i % 6 == 0):
#             st.write(space + "Happy Birthday!💖")
#         else:
#             st.write(space + "🔸")
#         space = ''
#         time.sleep(0.2)

# if __name__ == "__main__":
#     start_animation = st.sidebar.button("Start Animation")
#     if start_animation:
#         happy_birthday_animation()














# import streamlit as st
# from __future__ import print_function
# import time
# import sys

# try:
#     import winsound
# except ImportError:
#     import os

# st.title('🎂 Barakallah Fii Umrik 🎂')

# name = st.text_input("What is your name? ")

# st.markdown(""" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
#             Barallah fii umrik Falaqun Nurul Hidayah     
#             ==========================================
#             Created By Emma
#             Semoga segala wish dan goals dalam hidupmu bisa tercapai. Aamiinnnn
#             >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>""")

# try:
# 	winsound.Beep(264, 250)
# 	st.sys.stdout.write('Ha')	
# 	time.sleep(500/2000.0)
# 	st.sys.stdout.write('ppy ')
# 	winsound.Beep(264, 250)
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('birth')
# 	winsound.Beep(297, 1000)
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('day ')
# 	winsound.Beep(264, 1000)
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('to ')
# 	winsound.Beep(352, 1000)
# 	time.sleep(250/2000.0)
# 	print('you')
# 	winsound.Beep(330, 2000)
# 	time.sleep(500/2000.0)

# 	st.sys.stdout.write('Ha')
# 	winsound.Beep(264, 250)
# 	time.sleep(500/2000.0)
# 	st.sys.stdout.write('ppy ')
# 	winsound.Beep(264, 250)
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('birth')
# 	winsound.Beep(297, 1000)
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('day ')
# 	winsound.Beep(264, 1000)
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('to ')
# 	winsound.Beep(396, 1000)
# 	time.sleep(250/2000.0)
# 	st.write('you')
# 	winsound.Beep(352, 2000)
# 	time.sleep(500/2000.0)

# 	st.sys.stdout.write('Ha')
# 	winsound.Beep(264, 250)
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('ppy ')
# 	winsound.Beep(264, 500)
# 	time.sleep(250/1000.0)
# 	st.sys.stdout.write('birth')
# 	winsound.Beep(440, 1000)
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('day ')
# 	winsound.Beep(352, 1000)
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('dear ')
# 	winsound.Beep(330, 1000)
# 	st.write(name)
# 	time.sleep(250/2000.0)
# 	winsound.Beep(297, 1000)

# 	winsound.Beep(440, 1000)
# 	time.sleep(250/2000.0)

# 	time.sleep(500/2000.0)
# 	st.sys.stdout.write('Ha')
# 	winsound.Beep(466, 250)
# 	time.sleep(500/2000.0)
# 	st.sys.stdout.write('ppy ')
# 	winsound.Beep(466, 250)
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('birth')
# 	winsound.Beep(440, 1000)
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('day ')
# 	winsound.Beep(352, 1000)
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('to ')
# 	winsound.Beep(396, 1000)
# 	time.sleep(250/2000.0)
# 	st.write('you')
# 	winsound.Beep(352, 2000)
# 	time.sleep(250/2000.0)
# except:
# 	os.system('beep -f 264 -l 250')
# 	st.sys.stdout.write('Ha')
# 	sys.stdout.flush()
# 	time.sleep(500/2000.0)
# 	st.sys.stdout.write('ppy ')
# 	sys.stdout.flush()	
# 	os.system('beep -f 264 -l 250')
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('birth')
# 	sys.stdout.flush()
# 	os.system('beep -f 297 -l 1000')
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('day ')
# 	sys.stdout.flush()
# 	os.system('beep -f 264 -l 1000')
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('to ')
# 	sys.stdout.flush()
# 	os.system('beep -f 352 -l 1000')
# 	time.sleep(250/2000.0)
# 	st.write ('you')
# 	os.system('beep -f 330 -l 2000')
# 	time.sleep(500/2000.0)
	
# 	st.sys.stdout.write('Ha')
# 	sys.stdout.flush()
# 	os.system('beep -f 264 -l 250')
# 	time.sleep(500/2000.0)
# 	st.sys.stdout.write('ppy ')
# 	sys.stdout.flush()
# 	os.system('beep -f 264 -l 250')
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('birth')
# 	sys.stdout.flush()
# 	os.system('beep -f 297 -l 1000')
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('day ')
# 	sys.stdout.flush()
# 	os.system('beep -f 264 -l 1000')
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('to ')
# 	sys.stdout.flush()
# 	os.system('beep -f 396 -l 1000')
# 	time.sleep(250/2000.0)
# 	st.write ('you')
# 	os.system('beep -f 352 -l 2000')
# 	time.sleep(500/2000.0)
	
# 	st.sys.stdout.write('Ha')
# 	sys.stdout.flush()
# 	os.system('beep -f 264 -l 250')
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('ppy ')
# 	sys.stdout.flush()
# 	os.system('beep -f 264 -l 500')
# 	time.sleep(250/1000.0)
# 	st.sys.stdout.write('birth')
# 	sys.stdout.flush()
# 	os.system('beep -f 440 -l 1000')
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('day ')
# 	sys.stdout.flush()
# 	os.system('beep -f 352 -l 1000')
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('dear ')
# 	sys.stdout.flush()
# 	os.system('beep -f 330 -l 1000')
# 	st.write (name )
# 	time.sleep(250/2000.0)
# 	os.system('beep -f 297 -l 1000')
	
# 	os.system('beep -f 440 -l 1000')
# 	time.sleep(250/2000.0)
	
# 	time.sleep(500/2000.0)
# 	st.sys.stdout.write('Ha')
# 	sys.stdout.flush()
# 	os.system('beep -f 466 -l 250')
# 	time.sleep(500/2000.0)
# 	st.sys.stdout.write('ppy ')
# 	sys.stdout.flush()
# 	os.system('beep -f 466 -l 250')
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('birth')
# 	sys.stdout.flush()
# 	os.system('beep -f 440 -l 1000')
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('day ')
# 	sys.stdout.flush()
# 	os.system('beep -f 352 -l 1000')
# 	time.sleep(250/2000.0)
# 	st.sys.stdout.write('to ')
# 	sys.stdout.flush()
# 	os.system('beep -f 396 -l 1000')
# 	time.sleep(250/2000.0)
# 	st.write ('you')
# 	os.system('beep -f 352 -l 2000')
# 	time.sleep(250/2000.0)

# st.write ('HAPPY BIRTHDAY ' + name + ' <3 !!!')

# st.write ("  --------------------------------------------------------------------------------------------------------")
# st.write ("  | |  | |    /\    |  __ \ |  __ \ \ \   / / |  _ \|_   _||  __ \|__   __|| |  | ||  __ \    /\ \ \   / /")
# st.write ("  | |__| |   /  \   | |__) || |__) | \ \_/ /  | |_) | | |  | |__) |  | |   | |__| || |  | |  /  \ \ \_/ /  ")
# st.write ("  |  __  |  / /\ \  |  ___/ |  ___/   \   /   |  _ <  | |  |  _  /   | |   |  __  || |  | | / /\ \ \   /  ")
# st.write ("  | |  | | / ____ \ | |     | |        | |    | |_) |_| |_ | | \ \   | |   | |  | || |__| |/ ____ \ | |   ")
# st.write ("  |_|  |_|/_/    \_\|_|     |_|        |_|    |____/|_____||_|  \_\  |_|   |_|  |_||_____//_/    \_\|_|   ")
    