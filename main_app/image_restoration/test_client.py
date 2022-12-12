import requests
import json
import cv2
import os, shutil
from PIL import Image


addr = 'http://localhost:8000'
test_url = addr + '/enhance/'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}


img = cv2.imread('input/temp.jpg')

# delete the output folder
if os.path.exists('output'):
    shutil.rmtree('output')


# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)

# send http request with image and receive response
response = requests.post(test_url, data=img_encoded.tobytes(), headers=headers)

if (json.loads(response.text)) == {'Image Saved': 'OK'}:
    print("Restored image saved successfully in the output folder")
    
    # show image with Pillow
    img = Image.open('./output/restored_imgs/temp.jpg')
    img.show()
    
