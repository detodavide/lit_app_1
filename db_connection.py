from pymongo import MongoClient
from dotenv import load_dotenv
import streamlit as st
import os
import socket
import re

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

def get_client_ip():
    query_params = st.experimental_get_query_params()
    remote_address = query_params.get("client_ip", [""])[0]

    # Validate the retrieved IP address
    ip_pattern = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
    if ip_pattern.match(remote_address):
        return remote_address
    else:
        return "IP address not found or invalid."

if __name__ == '__main__':

    ip = get_client_ip()
    st.write(f"The current IP address of the Streamlit app is: {ip}")
    db = connect_to_db("DiscoData")
    if db is not None:
        bigdata1 = db.botDiscoLogs
        print(bigdata1.find_one())
