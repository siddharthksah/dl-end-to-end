import os
from PIL import Image
import numpy as np
import cv2
import streamlit as st
import shutil


@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img


def save_image(image_file):
    try:
        shutil.rmtree('./temp')
    except:
        pass
    if not os.path.exists('temp'):
        os.makedirs('temp')
    if image_file is not None:
        img = load_image(image_file)
        img = img.convert('RGB')
        path = 'temp/'
        img.save(os.path.join(path , 'temp.jpg'))

    else:
        st.write("Corrupted file!")