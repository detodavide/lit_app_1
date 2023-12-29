from pymongo import MongoClient
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

def connect_to_db(database):
    try:
        mongodb_uri = st.secrets["MONGODB_URI"]
        client = MongoClient(mongodb_uri)
        db = client[database]
        return db
    except Exception as e:
        print(f"An error occurred while connecting to the database: {str(e)}")
        return None
    
import socket
import streamlit as st

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

if __name__ == '__main__':

    ip = get_ip_address()
    st.write(f"The current IP address of the Streamlit app is: {ip}")
    db = connect_to_db("DiscoData")
    if db is not None:
        bigdata1 = db.botDiscoLogs
        print(bigdata1.find_one())
