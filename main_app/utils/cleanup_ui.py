import streamlit as st

def cleanup_ui():

    #####################################################################
    #####################################################################
    # favicon and page configs
    favicon = './assets/icon.png'
    st.set_page_config(page_title='Demo App', page_icon = favicon)
    # favicon being an object of the same kind as the one you should provide st.image() with (ie. a PIL array for example) or a string (url or local file path)
    st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    #####################################################################
    #####################################################################
    
    return True