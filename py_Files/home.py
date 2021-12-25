import streamlit as st
from py_Files import connect
import random

global names
names = connect.names()
number = 0
global presents_df
presents_df = connect.presents()

def home():
    nname = st.sidebar.button('Next Name')
    if nname:
        next_name()
        #refresh()

    restart = st.sidebar.button('Restart')
    if restart:
        global number
        number = 0
        refresh()

    refesh = st.sidebar.button('Refresh')
    if refesh:
        refresh()

    shuffle = st.sidebar.button('Shuffle Names')
    if shuffle:
        shuffle_names()

    st.sidebar.image('Images/welephant.png')

    hname, hgift, hselection= st.columns([1, 1, 1])
    name, gift, selection = st.columns([1, 1, 1])

    hname.header('Names (Nombres)')
    for x in names:
        if x == names[number]:
            name.markdown(f'<p style="background-color:#c0c0c0;color:#000000;font-size:24px;border-radius:50%;text-align: center;">{x}</p>',
                          unsafe_allow_html=True)
        else:
            name.markdown(f'<p style="background-color:#146B3A;color:#000000;font-size:24px;border-radius:2%;text-align: center;">{x}</p>',
                          unsafe_allow_html=True)
    hgift.header('Gifts (Regalos)')
    hselection.header('Changes Left (Cambios Restante)')
    for index, row in presents_df.iterrows():
        gifter = row[0]
        gift_name = row[1]
        list_number = row[2]
        list_numberstr = str(list_number)
        gift_selection = selection.selectbox(list_numberstr,['Three', 'Two', 'One', 'None'], key = gifter)
        if gift_selection == 'Three':
            line = list_numberstr
            gift.markdown(f'<p style="background-color:#c0c0c0;color:#000000;font-size:24px;border-radius:2%;text-align: center;">{line}</p>',
                          unsafe_allow_html=True)
        elif gift_selection == 'Two':
            line = str(list_number) + ' ' + gift_name
            gift.markdown(f'<p style="background-color:#165B33;color:#000000;font-size:24px;border-radius:2%;text-align: center;">{line}</p>',
                          unsafe_allow_html=True)
        elif gift_selection == 'One':
            line = str(list_number) + ' ' + gift_name
            gift.markdown(f'<p style="background-color:#FFD700;color:#000000;font-size:24px;border-radius:2%;text-align: center;">{line}</p>',
                          unsafe_allow_html=True)
        elif gift_selection == 'None':
            line = str(list_number) + ' ' + gift_name
            gift.markdown(f'<p style="background-color:#BB2528;color:#000000;font-size:24px;border-radius:2%;text-align: center;">{line}</p>',
                          unsafe_allow_html=True)

def shuffle_names():
    random.shuffle(names)

def next_name():
    global number
    number += 1

def refresh():
    global presents_df
    presents_df = connect.presents()
    update_names()

def delete_value(value):
    new_value = int(value) - 1
    print(new_value)
    connect.change_value(new_value,value)
    presents_df = connect.presents()
    home()

def add_value(gift_value):
    #print(gift_name, gift_value)
    change = int(gift_value) + 1
    print(change)
    connect.change_value(new_value,value)
    #home()

def update_names():
    global names
    names = connect.names()