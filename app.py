import streamlit as st
from ultralytics import YOLO
from PIL import Image

st.set_page_config(page_title="Object Detection", layout="centered")
st.title("Object Detection App")

#Load model
model = YOLO("models/weights/best.pt")

#File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    #Open and display original image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    if st.button('Detect Objects'):
        #Predict
        results = model(image)
            
        #Visualize results
        for result in results:
            res_plotted = result.plot()
            res_image = Image.fromarray(res_plotted[..., ::-1])
            st.image(res_image, caption='Predicted Image', use_column_width=True)
