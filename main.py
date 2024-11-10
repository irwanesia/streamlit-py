import streamlit as st
import pandas as pd
import time as ts
from datetime import time
import matplotlib.pyplot as plt
import numpy as np

tabel=pd.DataFrame({"Column 1": [1,2,3,4,5,6,7], "Column 2": [10,20,30,40,50,60,70]})

# 4. removing hamburger/menyembunyikan button hamburger
# st.markdown("""
#             <style>
#                 .stAppToolbar.st-emotion-cache-15ecox0.ezrtsby0{
#                     visibility: hidden;
#                 }
#             </style>
#             """, unsafe_allow_html=True)

st.markdown("---")
# some more text element
st.write("## 1. some more text element")
st.title("Ini Judul Menggunakan Streamlit")
st.header('Dan ini merupakan Header')
st.subheader('Hi! ini merupkan Subheader')
st.text('Selanjutnya! text menggunakan st.text() digunakna untuk membuat paragraf atau kalimat')
st.markdown(">**text bold** text biasa, *text miring*")
st.markdown("## Hello World")
st.markdown("#### Hello World")
st.markdown("[Link Google](https://www.google.com)")
st.markdown("---")
st.caption("Hi i'am caption")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

json={"a":"1,2,3", "b":"4,5,6"}
st.json(json)

code="""
print("Hello World)
def funct():
    return 0
"""
st.code(code, language="python")

st.markdown("---")
# display element of streamlit
st.write("## 2. display element of streamlit")
st.metric(label="Wind Speed", value="120ms⁻¹", delta="-1.4ms\^-1")

st.table(tabel)
st.dataframe(tabel)

st.markdown("---")
# media widget of streamlit
st.write("## 3. media widget of streamlit")
st.image("image.png", caption="ini caption image", width=240)
st.audio("audio.mp3")  # file harus berada di folder yang sama dengan script streamlit
st.video("try-catch.mp4")

st.markdown("---")
# basic interactive widgets
st.write("## 5. basic interactive widgets")

def change():
    # print("Changed")
    print(st.session_state.checker)
    
state = st.checkbox("Checkbox", value=True, on_change=change, key="checker")

if state:
    st.write("Checkbox checked")
else:
    st.write("Checkbox unchecked")

radio_btn = st.radio("In which Vilage in West Java do you live?", options=("Losari", "Ciledug", "Pabuaran", "Pabedilan"))
print(radio_btn)

def btn_click():
    print("Button clicked")
    
btn = st.button("Click Me!", on_click=btn_click)

carselect = st.selectbox("What is your favourite car?", options=("Audi","BMW","Ferari","Tesla","Esemka"))
print(carselect)

multi_select = st.multiselect("What is your favourite Tech", options=("Microsoft","Apple","Amazon","Oracle","IdCamp","WPU"))
st.write(multi_select)

# file uploader widget
st.markdown("---")
st.title("Uploading Files")
st.write("## 6. file uploader widget")
image = st.file_uploader("Please upload an image", type=["jpg","png","jpeg"])
if image is not None:
    st.image(image)

images = st.file_uploader("Multiple upload an image", type=["jpg","png","jpeg"], accept_multiple_files=True)
if images is not None:
    for img in images:
        st.image(img)
    
vd = st.file_uploader("Please upload an video", type="mp4")
if vd is not None:
    st.video(vd)
    

st.markdown("---")
# Some more interactive
st.write("## 7. Some more interactive")
# val = st.text_input("Enter your Course Title")
val_text = st.text_input("Enter your Course Title", max_chars=60)
val_area = st.text_area("Course Description", max_chars=360)
val_date = st.date_input("Enter Your Brithday")
val_time = st.time_input("Set Timer")
# val_slider = st.slider("This is a slider")
val_slider = st.slider("This is a slider", min_value=20, max_value=100, value=77)
print(val_date)

st.markdown("---")
# Timer App With Progress Bar
st.write("## 8. Timer App With Progress Bar")

def converter(value):
    m,s,mm = value.split(":")
    t_s = int(m)*60+int(s)+int(mm)/1000
    return t_s

val_times = st.time_input("Set Timer", value=time(0,0,0))
# print(type(val_times))
if str(val_times) == "00:00:00":
    st.write("Please sent timer")
else:
    # print("Performing other function")
    sec=converter(str(val_times))
    bar = st.progress(0)
    per=sec/100
    progress_status = st.empty()
    for i in range(100):
        # Update progress bar
        bar.progress(i + 1)
        # bar.progress((i+1)*10)
        progress_status.write(str(i+1)+"%")
        ts.sleep(per)
        
        
st.markdown("---")
# Streamlit Forms
st.write("## 9. Streamlit Forms")
st.markdown("<h1 style='text-align: center;'>User Registrasi</h1>", unsafe_allow_html=True)
# form = st.form("Form 1")
# form.text_input("First Name", value="Enter first name")
# st.form_submit_button("Submit")
with st.form("Form 2", clear_on_submit=True):

    col1,col2 = st.columns(2)
    f_name = col1.text_input("First Name")
    l_name = col2.text_input("Last Name")
    f_name = col1.text_input("Email")
    col2.selectbox("Gender", options=("Male","Female"))
    col1.text_input("Password")
    col2.text_input("Confirm Password")
    st.text_input("No. Telp")
    st.text_input("Address")
    
    d,m,y = st.columns(3)
    d.text_input("Day")
    m.text_input("Month")
    y.text_input("Year")
    
    s_state = st.form_submit_button("Submit")
    
    if s_state:
        if f_name == "" and l_name == "":
            st.warning("Please fill above fields")
        else:
            st.success("Registration Success")
            

st.markdown("---")
# Sidebar & Graphs
st.write("## 10. Sidebar & Graphs")
x = np.linspace(0,10,100)
bar_x=np.array([1,2,3,4,5])
# st.sidebar.write("Hello this is my sidebar")
opt = st.sidebar.radio("Select any graph", options=("line", "bar", "H-Bar"))
if opt == "line":
    st.markdown("<h1 style='text-align: center'>Line Chart</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x), '--')
    st.write(fig)
elif opt == "bar":
    st.markdown("<h1 style='text-align: center'>Bar Chart</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    
    plt.bar(bar_x, bar_x*10)
    st.write(fig)
else:
    st.markdown("<h1 style='text-align: center'>H-Bar Chart</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    
    plt.barh(bar_x*10, bar_x)
    st.write(fig)