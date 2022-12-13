import os
from PIL import Image
import numpy as np
import cv2
import streamlit as st
import shutil
from tabnanny import check
import requests,os
import streamlit as st
import urllib
import urllib.request
import validators


@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img


def save_image(image_file):
	try:
		shutil.rmtree('../temp')
	except:
		pass
	if not os.path.exists('../temp'):
		os.makedirs('../temp')
	if image_file is not None:
		img = load_image(image_file)
		img = img.convert('RGB')
		path = '../temp/'
		img.save(os.path.join(path , 'temp.jpg'))

	else:
		st.write("Corrupted file!")
		


def check_if_url_is_valid(url):
	return validators.url(url)

def is_url_image(image_url):
	image_formats = ("image/png", "image/jpeg", "image/jpg")
	r = requests.head(image_url)
	if r.headers["content-type"] in image_formats:
		return True
	return False



def download_image_from_url(url):
	if check_if_url_is_valid(url):
		#st.write("URL OK")
		if is_url_image(url) == True:
			img_data = requests.get(url).content
			with open('../temp/temp.jpg', 'wb') as handler:
				handler.write(img_data)

	else:
		st.error("Not a valid URL!")

	return str(os.path.exists("../temp/temp.jpg")) # Or folder, will return true or false