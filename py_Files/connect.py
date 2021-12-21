import sqlite3
import pandas as pd
import streamlit as st


global database
database = 'secret.db'

def add_gift(name, gift, gift_number):

    db = sqlite3.connect(database)
    df = pd.read_sql_query('SELECT * FROM Gift', db)
    db_gift_numbers = df['Number'].tolist()
    gift_names = df['Gift'].tolist()

    if int(gift_number) in db_gift_numbers:
        st.error('Gift number exist, recheck your number')
    elif gift in gift_names:
        st.error('Please be more specific with your gift')
    else:
        try:
            conn = sqlite3.connect(database)
            c = conn.cursor()
            c.execute('INSERT INTO Gift(Name, Gift, Number) VALUES (?,?,?)',(name,gift,gift_number))
            conn.commit()
            c.close()
            conn.close()
            message = name + "'s gift added!"
            print('Gift information inserted successfully into Gift table')
            st.success(message)
            st.balloons()
            return True
        except:
            print('Failed to insert gift information into Gift table')
            return False

def names():
    try:
        db = sqlite3.connect(database)
        df = pd.read_sql_query('SELECT * FROM Gift', db)
        names = df['Name'].tolist()
        return names
        print('Successfully pulled all names')

    except:
        print('Unsuccessfully pulled all names')

def presents():
    try:
        db = sqlite3.connect(database)
        df = pd.read_sql_query('SELECT * FROM Gift', db)
        return df
        print('Successfully pulled all gift info')
        st.success('Gift Added!!!!')

    except:
        print('Unsuccessfully pulled all gift info')
        st.error('Gift Not Added!!!')

def delete_entry(name):
    try:
        delresult = '"'+name+'"'
        conn = sqlite3.connect(database)
        c = conn.cursor()
        c.execute('DELETE from Gift WHERE Name='+str(delresult))
        conn.commit()
        c.close()
        conn.close()
        return True
    except:
        return False

def update_gift_info(change,location,name):
    db = sqlite3.connect(database)
    df = pd.read_sql_query('SELECT * FROM Gift', db)
    db_gift_numbers = df['Number'].tolist()
    gift_names = df['Gift'].tolist()

    print(change,location,name)

    if location == 'Number':
        print(db_gift_numbers)
        if int(change) in db_gift_numbers:
            st.error('Gift number exist, recheck your number')
        else:
            conn = sqlite3.connect(database)
            c = conn.cursor()
            c.execute('UPDATE Gift SET ' + location + ' = ? WHERE Name = ?', (change, name))
            conn.commit()
            c.close()
            conn.close()

    elif location == 'Gift':
        if change in gift_names:
            st.error('Please be more specific with your gift')
        else:
            conn = sqlite3.connect(database)
            c = conn.cursor()
            c.execute('UPDATE Gift SET ' + location + ' = ? WHERE Name = ?', (change, name))
            conn.commit()
            c.close()
            conn.close()

    elif location == 'Name':
        conn = sqlite3.connect(database)
        c = conn.cursor()
        c.execute('UPDATE Gift SET ' + location + ' = ? WHERE Name = ?', (change, name))
        conn.commit()
        c.close()
        conn.close()

def clear_database():
    try:
        conn = sqlite3.connect(database)
        c = conn.cursor()
        c.execute('DELETE FROM Gift')
        conn.commit()
        c.close()
        conn.close()
        print('Successfully cleared database')
        st.success('Database cleared')

    except:
        print('Unsuccessfully cleared database')
        st.error('Unsuccessfully cleared database')