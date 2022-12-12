from PIL import Image
from nsfw_detector import predict
import os
import warnings
warnings.filterwarnings("ignore")


# write a function to check if an image is valid with path
def is_valid_image(img_path):
    img = Image.open(img_path)
    try:
        img.verify()
        return True
    except Exception:
        return False

    
    
# check if an image path is sfw
def is_image_sfw(img_path, threshold):
    # merge current path to /nsfw_detection/nsfw_mobilenet_model.h5 to get the model path
    nsfw_model_path = os.path.abspath("nsfw_detection/nsfw_mobilenet_model.h5")
    model = predict.load_model(nsfw_model_path)
    result = predict.classify(model, img_path)
    # get value from dictionary
    for key, value in result.items():
        for key, value in value.items():
            if key == "porn" and key > threshold:
                return False
            else:
                return True
    return False


