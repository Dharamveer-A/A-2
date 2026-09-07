import streamlit as st
import base64
import os

_ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")
_LOGO_PATH = os.path.join(_ASSETS_DIR, "logo.png")


@st.cache_data
def get_logo_data_uri():
    with open(_LOGO_PATH, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    return f"data:image/png;base64,{encoded}"


def header_home():

    logo_url = get_logo_data_uri()
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='{logo_url}' style='height:100px; border-radius:22px; border:3px solid #F5EFDD; box-shadow: 0 6px 16px rgba(0,0,0,0.25); margin-bottom:14px;' />
            <h1 style='text-align:center; color:#F5EFDD'>ATTENDANCE AI</h1>
        </div>   
                
                """, unsafe_allow_html=True)


def header_dashboard():

    logo_url = get_logo_data_uri()
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:14px">
            <img src='{logo_url}' style='height:85px; border-radius:19px; border:3px solid #2F6B4E; box-shadow: 0 4px 12px rgba(0,0,0,0.15);' />
            <h2 style='text-align:left; color:#2F6B4E'>ATTENDANCE AI</h2>
        </div>   
                
                """, unsafe_allow_html=True)