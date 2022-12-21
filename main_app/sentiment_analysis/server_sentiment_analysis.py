from flask import Flask, request, Response, render_template
import jsonpickle
import numpy as np
import cv2, os, shutil
from PIL import Image

import warnings
warnings.filterwarnings("ignore")

from restoration import restore_img
from utils import is_valid_image, is_image_sfw

# Initialize the Flask application
app = Flask(__name__)



# route http posts to this method
@app.route('/sentiment/', methods=['POST'])
def restore():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    #print(img)
    img = Image.fromarray(img)
    b, g, r = img.split()
    img = Image.merge("RGB", (r, g, b))
    
    # clean the temp folder if it exists
    if os.path.exists('temp'):
        shutil.rmtree('temp')
        
    # create a temp folder to store the image
    if not os.path.exists('temp'):
        os.makedirs('temp')
        
    temp_image_path = "./temp/temp.jpg"
    
    print(temp_image_path)
        
    img.save(temp_image_path, 'JPEG')
    
    # print("Is a valid image: ", is_valid_image(temp_image_path))
    
    # print("Is SFW: ", is_image_sfw(temp_image_path, threshold=0.3))
    
    if is_valid_image(temp_image_path) and is_image_sfw(temp_image_path, threshold=0.3):
        print("Image is valid and SFW")
        
        # restore the image
        if restore_img() == "OK":
            status = "OK"
        else:
            status = "Error"
    

    response = {'Image Saved': status}
    print(response)

    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")

# start flask app
app.run(host="0.0.0.0", port=8000, debug=True)
