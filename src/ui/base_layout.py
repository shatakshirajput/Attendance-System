import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background: #F3F5F9 !important;
            }

            .stApp div[data-testid="stColumn"]{
                background-color:#E5E7EB !important;
                padding:2.5rem !important;
                border-radius: 5rem !important;
           }
        </style>  
        """,unsafe_allow_html=True)
    

def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #F3F5F9 !important;
            }
        </style>  
        """,unsafe_allow_html=True)

def style_base_layout():
    st.markdown("""
        <style>
        /* Hide Top Bar of streamlit */
        #MainMenu, footer, header {
            visibility: hidden;
        }
                
        .block-container {
            padding-top:1.5rem !important;    
        }

        h1 {
            font-family: 'Playfair Display', serif !important;
            font-size: 3.5rem !important;
            line-height:1.1 1important;
            margin-bottom:0rem !important;
            color: #1F2937 !important;
        }
        h2 {
            font-family: 'Playfair Display', serif !important;
            font-size: 2rem !important;
            line-height:0.9 !important;
            margin-bottom:0rem !important;
            color: #1F2937 !important;
        }
                
        h3, h4, p {
            font-family: 'Inter', sans-serif;
            color: #6B7280 !important;    
        }

        button{
            border-radius: 1.5rem !important;
            background-color: #5B6EFF !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button[kind="secondary"]{
            border-radius: 1.5rem !important;
            background-color: #E5E7EB !important;
            color: #5B6EFF !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button[kind="tertiary"]{
            border-radius: 1.5rem !important;
            background-color: #000000 !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button:hover{
            transform :scale(1.05)
        }
                
        </style>  
        """,unsafe_allow_html=True)