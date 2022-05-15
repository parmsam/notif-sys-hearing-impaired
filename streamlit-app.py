#load libraries ----
import streamlit as st
import time
import os
import predict_from_microphone_dog
import predict_from_microphone_baby

#define UI ----

if 'disabled_status_baby' not in st.session_state:
    st.session_state.disabled_status_baby = False
if 'disabled_status_dog' not in st.session_state:
    st.session_state.disabled_status_dog = False

def disable_all():
    st.session_state.disabled_status_baby = True
    st.session_state.disabled_status_dog = True

st.title("Notification System for the Hearing Impaired")
start_baby = st.button("Start baby crying predictions")
start_dog = st.button("Start dog barking predictions")
stop = st.button("Stop")

#define server logic ----
if start_baby:
    st.success("Started baby crying prediction program")
    st.warning("Click stop button before clicking other button")
    predict_from_microphone_baby
if start_dog:
    st.success("Started dog barking prediction program")
    st.warning("Click stop button before clicking other button")
    predict_from_microphone_dog
if stop:
    st.stop()
