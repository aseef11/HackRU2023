import streamlit as st
import pandas as pd
import numpy as np
import math
from PIL import Image
from statistics import mean
import sched, time

@st.cache_resource(ttl=1800)
def get_caData():
    return []

@st.cache_resource(ttl=1800)
def get_buschData():
    return []

@st.cache_resource(ttl=1800)
def get_cdData():
    return []

@st.cache_resource(ttl=1800)
def get_liviData():
    return []

def iterate(entries):
    sum = 0
    for i in entries:
        sum += i
    return sum
def calculateMeter(num, vals):
    return math.trunc(round(num/len(vals),1)*10)

ruKnight = Image.open('scarlet_knightLogo.png')
st.image(ruKnight, width=65)

st.title(':red[RU] Gyms Crowd Meter')

st.subheader('Select a gym:')
def mainPage():
    st.set_page_config(page_title="RU Gyms Crowd Meter", page_icon=":tada:", layout="wide")
st.sidebar.markdown("Other useful links:")
caButton = st.checkbox('College Ave Gym')
startTime = None
endTime = None
if caButton:
    with st.form(key='caForm'):
        caBusy = st.slider('How busy is the College Ave Gym?', 0, 10)
        caSubmit = st.form_submit_button()
        if caSubmit:
                get_caData().append(caBusy)
        caNum = iterate(get_caData())
    if len(get_caData())>0:
        caMeter = st.progress(calculateMeter(caNum, get_caData()), text='Crowd Meter')

buschButton = st.checkbox('Busch Gym')
if buschButton:
    with st.form(key='buschForm'):
        buschBusy = st.slider('How busy is the Busch Gym?', 0, 10)
        buschSubmit = st.form_submit_button()
        if buschSubmit:
            get_buschData().append(buschBusy)  
        buschNum = iterate(get_buschData())
      
    if(len(get_buschData()) > 0):
        buschMeter = st.progress(calculateMeter(buschNum, get_buschData()), text='Crowd Meter')


cdButton = st.checkbox('Cook/Douglass Gym')
if cdButton:
    with st.form(key='cdForm'):
        cdBusy = st.slider('How busy is the Cook/Douglas Gym?', 0, 10)
        cdSubmit = st.form_submit_button()
        if cdSubmit:
            get_cdData().append(cdBusy)  
        cdNum = iterate(get_cdData())
          
    if(len(get_cdData()) > 0):
        cdMeter = st.progress(calculateMeter(cdNum,get_cdData()), text='Crowd Meter')
                

liviButton = st.checkbox('Livingston Gym')
if liviButton:
    with st.form(key='liviForm'):
        liviBusy = st.slider('How busy is the Livingston Gym?', 0, 10)
        liviSubmit = st.form_submit_button()
        if liviSubmit:
            get_liviData().append(liviBusy)  
        liviNum = iterate(get_liviData())
              
    if(len(get_liviData()) > 0):
        liviMeter = st.progress(calculateMeter(liviNum, get_liviData()), text='Crowd Meter')


        
