import streamlit as st
from streamlit_option_menu import option_menu
import pags.logs, pags.requests

st.set_page_config(
    page_title="Home"
)

class MultiApp:
    def __init__(self) -> None:
        self.apps = []
    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        with st.sidebar:
            app = option_menu(
                menu_title="Datass",
                options=['Logs', "Requests"],
                default_index=1,
                styles={
                "container": {"padding": "5!important","background-color":'black'},
                "icon": {"color": "white", "font-size": "23px"}, 
                "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"},
                }
            )
        if app == "Logs":
            pags.logs.app()
        if app == "Requests":
            pags.requests.app()    

    run()      