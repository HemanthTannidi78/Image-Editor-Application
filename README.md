**Image Editing App with Streamlit & OpenCV**

A fully interactive, browser-based image editing application built using Streamlit and OpenCV. This app allows users to upload images, apply multiple filters in real time, preview the results instantly, and download the edited output—all without writing any frontend code.

Project Overview

This project demonstrates core image processing techniques using Python by combining:

A clean and responsive UI powered by Streamlit
Efficient image manipulation using OpenCV and NumPy

Users can interactively adjust filters using sliders and toggles, with all transformations applied dynamically on the image.

The goal is to showcase practical understanding of image processing concepts and building user-friendly ML-based applications.

The application includes the following OpenCV-based filters:

Blur – Smooths noise using Gaussian blur
Sharpness – Enhances edges using sharpening techniques
Brightness – Adjusts pixel intensity
Contrast – Scales pixel values
Edge Detection – Detects contours using Canny algorithm
Grayscale – Converts image to single-channel

All filters are interactive and can be combined for advanced effects.

Tech Stack:
Python
Streamlit (UI framework)
OpenCV (image processing)
NumPy (array manipulation)


How to Run:
Clone the repository:
git clone https://github.com/your-username/image-editor.git
cd image-editor
Install dependencies:
pip install -r requirements.txt
Run the app:
streamlit run app.py


Demo

<img width="1893" height="864" alt="image" src="https://github.com/user-attachments/assets/8b27ea3b-e65a-4611-bcc5-b459944e9ea0" />

<img width="1919" height="816" alt="image" src="https://github.com/user-attachments/assets/cc6544d1-647f-411f-a2c8-96146f7199b1" />

<img width="1911" height="825" alt="image" src="https://github.com/user-attachments/assets/6e0616a5-4647-4f8a-9625-ec0bef44e2fc" />


Check it out here : https://drive.google.com/file/d/1aHaEWhu_E4RG2K2Ajg0qwoP1eMWybuLz/view?usp=sharing

Learning Outcomes:

Understanding image representation using NumPy arrays
Applying core OpenCV transformations
Building interactive apps using Streamlit
Managing image format conversions (PIL ↔ NumPy ↔ Bytes)
Structuring clean and modular Python projects


Future Improvements
Add more filters (Sepia, Cartoon, HDR)
Add cropping and rotation tools
Improve UI styling and themes
Deploy the app online (Streamlit Cloud)
