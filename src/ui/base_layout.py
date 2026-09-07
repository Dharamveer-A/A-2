import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: #2F6B4E !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#F5EFDD !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: #F5EFDD !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
# asdasd
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
                
                /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }

                
         
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Outfit', sans-serif !important;
                font-weight: 800 !important;
                font-size: 2.5rem !important;
                letter-spacing: 0.02em !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
                white-space: nowrap !important;
            }
                

            h2 {
                font-family: 'Outfit', sans-serif !important;
                font-weight: 800 !important;
                font-size: 1.6rem !important;
                letter-spacing: 0.02em !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
                white-space: nowrap !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }
                

            button{
                border-radius: 1.5rem !important;
                background-color: #2F6B4E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #C9962E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: #24312A !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button:hover{
                transform :scale(1.05)}
        </style>  

                """
            ,unsafe_allow_html=True)