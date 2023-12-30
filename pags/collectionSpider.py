import streamlit as st
from db_connection import connect_to_db
import pandas as pd

def fetch_data(profile_name):
    db = connect_to_db("DiscoData")
    if db is not None:
        collectionerSpider = db.collectionerSpider
        logs = collectionerSpider.find({'profile_name': profile_name}, {'_id': 0, 'profile_name': 0, 'username_request': 0})
        return logs
    
def filter_data(df, for_sale_threshold):
    filtered_df = df[df['for_sale'] <= for_sale_threshold]
    return filtered_df

def fetch_profile_names():
    db = connect_to_db("DiscoData")
    if db is not None:
        collectionerSpider = db.collectionerSpider
        distinct_profiles = collectionerSpider.distinct('profile_name')
        return distinct_profiles

def app():
    st.header("Collection Spider Search")
    st.subheader('Filter Data Options')
    profile_names = fetch_profile_names()
    selected_profile = st.selectbox('Select Profile Name', profile_names)
    for_sale_threshold = st.slider("Select threshold for 'for sale'", min_value=0, max_value=100, value=2)

    filter_button = st.button('Filter Data')

    if filter_button:
        data = fetch_data(selected_profile)

        if data:
            data_list = list(data)
            df = pd.DataFrame(data_list)

            if not df.empty:
                df['for_sale'] = pd.to_numeric(df['for_sale'], errors='coerce')
                filtered_df = filter_data(df,for_sale_threshold)
                
                if not filtered_df.empty:
                    st.subheader("Filtered Data")
                    if 'url' in filtered_df.columns:
                        st.data_editor(
                            filtered_df,
                            hide_index=True,
                        )
                    else:
                        st.dataframe(filtered_df)
                else:
                    st.write("No rows found based on the selected threshold.")
            else:
                st.write("Empty DataFrame retrieved from the database.")
        else:
            st.write("Failed to retrieve data from the database.")