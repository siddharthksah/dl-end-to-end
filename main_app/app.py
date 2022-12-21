# @author Siddharth
# @website www.siddharthsah.com

# importing the necessary packages
from datetime import datetime
import streamlit as st
from PIL import Image
from utils.utils import save_image, download_image_from_url, check_if_url_is_valid, is_url_image
import requests
import json
import cv2
import os, shutil
from PIL import Image

from image_restoration.restore_inference import inference_image_restoration


from utils.cleanup_ui import cleanup_ui

cleanup_ui()




selectedSidebar = st.radio(
        " ",
        ("Image Enhacement", "Speech2Text", "YT Sentiment"), horizontal=True)

if selectedSidebar == "Image Enhacement":
    #upload button for the input image
    uploaded_file = st.file_uploader("Choose the image", type=['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        
        #getting the file extension of the uploaded file
        file_name = uploaded_file.name
        extension = file_name.split(".")[-1]
        
        # save uploaded image in jpg format in the temp folder and display it

        if extension == "png" or  extension == "PNG" or extension == "jpeg" or extension == "JPEG" or extension == "jpg" or extension == "JPG":
            uploaded_image = Image.open(uploaded_file)
            save_image(uploaded_file)
            col1, col2 = st.columns(2)

            header_placeholder = col1.header("Original")
            image_preview_placeholder = col1.image(uploaded_image, use_column_width=True, caption='Uploaded Image')
            # image_preview_placeholder = st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)
        else:
            st.write("Please upload a valid image file")
            st.stop()
            
    
    
    # create a streamlit button in the center with name Enhance
    if st.button('Enhance'):
        
        try:
            header_placeholder.empty()
            image_preview_placeholder.empty()
        except:
            pass
        
        # if the button is clicked, then call the main function
        
        with st.spinner('Enhancing the image...'):
            
            inference_image_restoration()
                
            enhanced_image = Image.open('./image_restoration/output/restored_imgs/temp.jpg')

        
        
        col1, col2 = st.columns(2)

        col1.header("Original")
        col1.image(uploaded_image, use_column_width=True)
            
        col2.header("Enhanced")
        col2.image(enhanced_image, use_column_width=True)
        

if selectedSidebar == "Speech2Text":
    #upload button for the input image
    uploaded_file = st.file_uploader("Choose the audio", type=['wav'])

    if uploaded_file is not None:
        # save audio file in the temp folder and display it
        
        st.audio(uploaded_file, format="audio/wav")
        
        st.warning("This feature is not available yet")
        
        #speech_to_text("./temp/temp.wav")
        
