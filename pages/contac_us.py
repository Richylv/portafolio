import streamlit as st
from send_email import send_mail
import pandas

st.header("Contact me")
df = pandas.read_csv('topics.csv')

with st.form(key='my_form'):
     user_email = st.text_input('Your email address')
     topic = st.selectbox('Select a topic',df)
     raw_message = st.text_area('Your message')
     message = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic: {topic}
{raw_message}
"""

     btn = st.form_submit_button()
     if btn:
         send_mail(message)
         st.info('Your mail was send successfully')



