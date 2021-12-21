import streamlit as st
from py_Files import home
from py_Files import gift_page as gift
from py_Files import connect

st.set_page_config(page_title='White Elephant', page_icon='Images/welephant.png', layout='wide', initial_sidebar_state='auto')
page = st.sidebar.selectbox('Page', ['Home','Gifts Settings'])


st.title('White Elephant')

if page == 'Home':
    home.home()

if page == 'Gifts Settings':
    gift.gift_page()

