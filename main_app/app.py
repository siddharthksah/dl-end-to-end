# @author Siddharth
# @website www.siddharthsah.com

# importing the necessary packages
from datetime import datetime
import streamlit as st
from PIL import Image
from utils import save_image
import requests
import json
import cv2
import os, shutil
from PIL import Image

from image_restoration.restore_inference import inference_image_restoration




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


selectedSidebar = st.radio(
        " ",
        ("Image Enhacement", "Speech2Text", "YT Sentiment"), horizontal=True)


if selectedSidebar == "Image Enhacement":
    #upload button for the input image
    uploaded_file = st.file_uploader("Choose the image", type=['jpg', 'png', 'jpeg'])
    #print(uploaded_file)
    url = ""
    #if uploaded_file is None:
    url = st.text_input("Or paste the URL below", key="text")

    if uploaded_file is not None:
        
        #getting the file extension of the uploaded file
        file_name = uploaded_file.name
        extension = file_name.split(".")[-1]
        
        # save uploaded image in jpg format in the temp folder and display it

        if extension == "png" or  extension == "PNG" or extension == "jpeg" or extension == "JPEG" or extension == "jpg" or extension == "JPG":
            uploaded_image = Image.open(uploaded_file)
            save_image(uploaded_file)
            image_preview_placeholder = st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)
        else:
            st.write("Please upload a valid image file")
            st.stop()
    
    # create a streamlit button in the center with name Enhance
    if st.button('Enhance'):
        # if the button is clicked, then call the main function
        image_preview_placeholder.empty()
        
        col1, col2 = st.columns(2)

        col1.header("Original")
        col1.image(uploaded_image, use_column_width=True)
        
        with st.spinner('Enhancing the image...'):
            
            inference_image_restoration()
                
            enhanced_image = Image.open('../image_restoration/output/restored_imgs/temp.jpg')

            
        col2.header("Enhanced")
        col2.image(enhanced_image, use_column_width=True)


    
