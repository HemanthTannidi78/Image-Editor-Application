import streamlit as st
from PIL import Image
import numpy as np
from filter import *
from convert_util import *


st.set_page_config(page_title="Image Editor", page_icon="", layout="wide")

st.title("Image Editor using OpenCV + Streamlit")

st.sidebar.header("Controls")

blur = st.sidebar.slider("Blur", 1, 51, 1, step=2)
sharp = st.sidebar.slider("Sharpness", 0.0, 3.0, 0.0)
brightness = st.sidebar.slider("Brightness", -100, 100, 0)
contrast = st.sidebar.slider("Contrast", 0.5, 3.0, 1.0)


edge_on = st.sidebar.checkbox("Edge Detection")
gray_on = st.sidebar.checkbox("Grayscale")

if st.sidebar.button("Reset"):
    st.rerun()

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    pil_img = Image.open(uploaded_file)

    image = pil_to_cv2(pil_img)

    processed = image.copy()
    processed = apply_blur(processed, blur)
    processed = apply_sharpness(processed, sharp)
    processed = apply_brightness(processed, brightness)
    processed = apply_contrast(processed, contrast)
    processed = apply_edge_auto_canny(processed, edge_on)
    processed = apply_grayscale(processed, gray_on)

    processed_pil = cv2_to_pil(processed)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original")
        st.image(pil_img, use_container_width=True)

    with col2:
        st.subheader("Processed")
        st.image(processed_pil, use_container_width=True)

    st.download_button(
        "Download Image",
        data=cv2_to_bytes(processed),
        file_name="edited.png",
        mime="image/png"
    )