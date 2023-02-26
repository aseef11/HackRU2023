from datetime import datetime
import streamlit as st
from PIL import Image
import math
from pytz import timezone

#Created By: Maanav Choudhary, Nicholas Yim, Aseef Durrani

# Gets rid of menu button in top right of screen
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

#Cache to store the user slider input value for College Ave Gym
@st.cache_resource(ttl=1800)
def get_caData():
    return []

#Cache to store the user slider input value for Busch Gym
@st.cache_resource(ttl=1800)
def get_buschData():
    return []

#Cache to store the user slider input value for Livingston Gym
@st.cache_resource(ttl=1800)
def get_liviData():
    return []

#Cache to store the user slider input value for Cook/Douglass Gym
@st.cache_resource(ttl=1800)
def get_cdData():
    return []

#Cache to store the user slider input value for Easton Ave Gym
@st.cache_resource(ttl=1800)
def get_eaData():
    return []


#Function takes an array of user inputs for a certain gym 
def calculateMeter(vals):
    sum = 0
    #loops through the user entries and sums them
    for i in vals:
        sum += i
    #calculates average by dividng sum by length of array and multiplies by 10 to fit the 0-100 bar
    return math.trunc(round(sum/len(vals),1)*10)

#Makes Site title
ruKnight = Image.open('scarlet_knightLogo.png')
st.image(ruKnight, width=65)
st.title(':red[RU] Gyms Crowd Meter')

st.subheader('Select a gym:')

def mainPage():
    st.set_page_config(page_title="RU Gyms Crowd Meter", page_icon=":tada:", layout="wide")

tz = timezone('EST')
now = datetime.now(tz)
current_time = now.strftime("%I:%M %p")

st.sidebar.title("Other useful links:")
st.sidebar.write("[Rutgers Recreation](http://recreation.rutgers.edu/)")
st.sidebar.subheader("Directions to:")
st.sidebar.markdown(
    """
     - [College Avenue Gym](https://goo.gl/maps/wjMuFWpeGJ24ZWTTA)
     - [Busch Gym](https://goo.gl/maps/g96HRcdu2L6oQNxz6)
     - [Livingston Gym](https://goo.gl/maps/Gx1jhzMx3BkogNUa9)
     - [Cook/Douglas Gym](https://goo.gl/maps/aSWqzzDoD1GGXHd87)
     - [Easton Ave Gym](https://goo.gl/maps/kRCvNeC8o2z4AqBT7)
    """)
st.sidebar.subheader("Hours:")
st.sidebar.markdown(
    """
    :red[**College Ave**]
     - Monday-Thursday **_7am-11pm_**
     - Friday **_7am-9pm_** 
     - Saturday **_11am-7pm_**
     - Sunday **_11am-9pm_**

    :red[**Busch**]
     - Monday-Thursday **_7am-11pm_**
     - Friday **_7am-9pm_** 
     - Saturday **_11am-7pm_**
     - Sunday **_11am-9pm_**

    :red[**Livingston**]
     - Monday-Thursday **_8am-11pm_**
     - Friday **_8am-7pm_** 
     - Saturday **_11am-7pm_**
     - Sunday **_11am-9pm_**

    :red[**Cook/Douglass**]
     - Monday-Thursday **_8am-11pm_**
     - Friday **_8am-9pm_** 
     - Saturday **_11am-7pm_**
     - Sunday **_11am-9pm_**
     
    :red[**Easton Ave**]
     - Monday-Thursday **_12pm-9pm_**
     - Friday **_12pm-7pm_** 
     - Saturday **_Closed_**
     - Sunday **_3pm-9pm_**
    """)



#Check box to select the College Ave gym and show slider and meter
caButton = st.checkbox('College Ave Gym')
#If button is selected, this if shows the meter and slider
if caButton:
    with st.form(key='caForm'):
        #slider for estimate crowd level
        caBusy = st.slider('How busy is the College Ave Gym?', 0, 10)
        #button to submit user input
        caSubmit = st.form_submit_button()
        #Adds the user input to cache for College Ave gym
        if caSubmit:
            get_caData().append(caBusy)  
    #If the college aver gym cache has more than 0 entries, it will calculate and show meter
    if(len(get_caData()) > 0):
        #creates crowd meter, calls on calculateMeter() to return the current crowd average(crowd average is a truncated float)
        caMeter = st.progress(calculateMeter(get_caData()), text='Crowd Meter')
        #estimates capacity as number and writes it
        st.write('**Estimated Gym Capacity at** ', current_time, '**is**', calculateMeter(get_caData()),'%')

        
#Check box to select the Busch gym and show slider and meter
buschButton = st.checkbox('Busch Gym')
#If button is selected, this if shows the meter and slider
if buschButton:
    with st.form(key='buschForm'):
        #slider for estimate crowd level
        buschBusy = st.slider('How busy is the Busch Gym?', 0, 10)
        #button to submit user input
        buschSubmit = st.form_submit_button()
        #Adds the user input to cache for Busch gym
        if buschSubmit:
            get_buschData().append(buschBusy)  
    #If the Busch gym cache has more than 0 entries, it will calculate and show meter
    if(len(get_buschData()) > 0):
        #creates crowd meter, calls on calculateMeter() to return the current crowd average(crowd average is a truncated float)
        buschMeter = st.progress(calculateMeter(get_buschData()), text='Crowd Meter')
        #estimates capacity as number and writes it
        st.write('**Estimated Gym Capacity at** ', current_time, '**is**', calculateMeter(get_buschData()),'%')


#Check box to select the Livingston gym and show slider and meter
liviButton = st.checkbox('Livingston Gym')
#If button is selected, this if shows the meter and slider
if liviButton:
    with st.form(key='liviForm'):
        #slider for estimate crowd level
        liviBusy = st.slider('How busy is the Livingston Gym?', 0, 10)
        #button to submit user input
        liviSubmit = st.form_submit_button()
        #Adds the user input to cache for Livingston gym
        if liviSubmit:
            get_liviData().append(liviBusy)  
    #If the Livingston gym cache has more than 0 entries, it will calculate and show meter
    if(len(get_liviData()) > 0):
        #creates crowd meter, calls on calculateMeter() to return the current crowd average(crowd average is a truncated float)
        liviMeter = st.progress(calculateMeter(get_liviData()), text='Crowd Meter')
        #estimates capacity as number and writes it
        st.write('**Estimated Gym Capacity at** ', current_time, '**is**', calculateMeter(get_liviData()),'%')

        
#Check box to select the Cook/Douglass gym and show slider and meter
cdButton = st.checkbox('Cook/Douglass Gym')
#If button is selected, this if shows the meter and slider
if cdButton:
    with st.form(key='cdForm'):
        #slider for estimate crowd level
        cdBusy = st.slider('How busy is the Cook/Douglas Gym?', 0, 10)
        #button to submit user input
        cdSubmit = st.form_submit_button()
        #Adds the user input to cache for Cook Douglass gym
        if cdSubmit:
            get_cdData().append(cdBusy)  
    #If the Cook Douglass gym cache has more than 0 entries, it will calculate and show meter
    if(len(get_cdData()) > 0):
        #creates crowd meter, calls on calculateMeter() to return the current crowd average(crowd average is a truncated float)
        cdMeter = st.progress(calculateMeter(get_cdData()), text='Crowd Meter')
        #estimates capacity as number and writes it
        st.write('**Estimated Gym Capacity at** ', current_time, '**is**', calculateMeter(get_cdData()),'%')
                

#Check box to select the Easton Ave gym and show slider and meter
eaButton = st.checkbox('Easton Ave Gym')
#If button is selected, this if shows the meter and slider
if eaButton:
    with st.form(key='eaForm'):
        #slider for estimate crowd level
        eaBusy = st.slider('How busy is the Easton Ave Gym?', 0, 10)
        #button to submit user input
        eaSubmit = st.form_submit_button()
        #Adds the user input to cache for Easton Ave gym
        if eaSubmit:
            get_eaData().append(eaBusy)  
    #If the Easton Ave gym cache has more than 0 entries, it will calculate and show meter
    if(len(get_eaData()) > 0):
        #creates crowd meter, calls on calculateMeter() to return the current crowd average(crowd average is a truncated float)
        eaMeter = st.progress(calculateMeter(get_eaData()), text='Crowd Meter')
        #estimates capacity as number and writes it
        st.write('**Estimated Gym Capacity at** ', current_time, '**is**', calculateMeter(get_eaData()),'%')
        
