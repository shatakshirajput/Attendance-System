import streamlit as st

def header_home():
    logo_url = "https://i.ibb.co/dZdWtR2/app-logo.png"
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
        <img src='{logo_url}' style='height:100px;' />
        <h1 style='text-align:center; color:#1F2937; white-space:nowrap; display:inline-block; margin-top:10px;'>WELCOME TO FACEMARK</h1>
        <h3>Login as :</h3>
        </div>   
    """, unsafe_allow_html=True)

def header_dashboard():
    logo_url = "https://i.ibb.co/dZdWtR2/app-logo.png"  
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
        <img src='{logo_url}' style='height:85px;' />
        <h2 style='text-align:left; color:#5865F2'>FACE<br/>MARK</h1>
        </div>               
    """, unsafe_allow_html=True)