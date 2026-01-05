from sqlalchemy import create_engine
import streamlit as st

def get_engine():
    db_url = st.secrets["database"]["url"]
    return create_engine(db_url)
