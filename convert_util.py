import numpy as np
from PIL import Image
import cv2
import io

def pil_to_cv2(pil_image):
    return cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

def cv2_to_pil(cv2_image):
    return Image.fromarray(cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB))

def cv2_to_bytes(cv2_image):
    pil_img = cv2_to_pil(cv2_image)
    buf = io.BytesIO()
    pil_img.save(buf, format="PNG")
    return buf.getvalue()