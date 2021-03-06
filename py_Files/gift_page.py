import streamlit as st
from py_Files import connect

global gifts_df
gifts_df = connect.presents()

def gift_page():
    st.title('Gifts Page (Página de Regalos)')
    selection = st.selectbox('Gift Options', ['Add Gift','Delete Gift','Edit Gift'])

    if selection == 'Add Gift':
        add_gift()
    if selection == 'Delete Gift':
        delete_gift()
    if selection == 'Edit Gift':
        edit_gift()

    st.sidebar.image('Images/welephant.png')


def add_gift():
    st.sidebar.header('Gift Number Ranges:')
    st.sidebar.subheader('Remigio-Nova House: 1-7')
    st.sidebar.subheader('Remigio-Gorritz House: 8-11')
    st.sidebar.subheader('Madera-Remigio House: 12-16')
    st.sidebar.subheader('Morales-Nova House: 17 and up')

    largest_number()
    st.header('Add Gift')
    st.subheader('Please fill out the form below. Type in your name, a short 1-3 word description of your gift, and the number assigned to your gift (see left for gift numbers per household). Once you are finished, select add gift.')
    st.subheader("If you make a mistake you can select 'Edit Gift' from the Gift option drop down, find your name, check the box for what ever change you make, and press save.")
    st.subheader('If you get an error and are confused hit Matt up.')
    st.subheader('Do not change anything on the Home Page, I will control it.')
    st.subheader('Gifts Numbers already used:')
    st.subheader(largest)
    name = st.text_input('Your Name')
    gift = st.text_input('Gift')
    gift_number = st.text_input('Gift Number')

    save = st.button('Add Gift')

    if save:
        add_gift_attempt = connect.add_gift(name,gift,gift_number)
        if add_gift_attempt is True:
            st.balloons()
        if add_gift_attempt is False:
            pass

def delete_gift():

    st.header('Delete Entry')
    clear = st.sidebar.button('Clear Database')
    if clear:
        connect.clear_database()

    names_info = connect.names()
    names_info.sort()

    name_selection = st.selectbox('Names', (names_info))

    delete = st.button('Delete Entry')

    if delete:

        try:
            server_delete = connect.delete_entry(name_selection)
            if server_delete is True:
                st.success('Entry successfully deleted')
            if server_delete is False:
                st.error('Entry unsuccessfully deleted')
        except:
            st.error('Something is fucked up')

def edit_gift():
    st.header('Edit Gift Info')
    gift_info = connect.presents()
    gift_infos = gift_info.set_index('Name')
    gift_infos['Number'] = gift_infos['Number'].astype(str)

    names = connect.names()
    names.sort()

    names_selection = st.selectbox('Name', (names))

    for i in names:
        if names_selection == i:
            name_pick = i

    new_name = st.text_input('Current Name is: ' + name_pick)
    change_name = st.checkbox('Update Name')

    show_gift = st.sidebar.checkbox('Show Gift')
    if show_gift:
        current_gift = gift_infos.loc[name_pick]['Gift']
        new_gift = st.text_input(('Current Gift is: ' + current_gift))
        change_gift = st.checkbox('Update Gift')

    else:
        current_gift = gift_infos.loc[name_pick]['Gift']
        new_gift = st.text_input(('Current Gift is: ???'))
        change_gift = st.checkbox('Update Gift')

    current_gift_number = gift_infos.loc[name_pick]['Number']
    new_gift_number = st.text_input(('Current Gift Number is: ' + current_gift_number))
    change_gift_number = st.checkbox('Update Gift Number')


    new_save = st.button('Update Gift')

    if new_save:
        if change_gift:
            connect.update_gift_info(new_gift, 'Gift', name_pick)
        if change_gift_number:
            try:
                connect.update_gift_info(new_gift_number, 'Number', name_pick)
                st.success('Gift Number Updated')
            except:
                st.error('Unsuccessful Updated Gift Number')
        if change_name:
            try:
                connect.update_gift_info(new_name, 'Name', name_pick)
                st.success('Updated Name')
            except:
                st.error('Unsuccessful Updated Name')

def largest_number():
    global largest
    gifts_df = connect.presents()
    largest = gifts_df['Number'].tolist()
    largest.sort()