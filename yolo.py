import streamlit

# Import Streamlit
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from ultralytics import YOLO

TRAINED_YOLO_MODEL_PATH = '/home/ec2-user/yolo/best.pt'

#function to invoke Yolo model and perform prediction
def predict_lung_cancer(image):
    # Load the Yolo model
    model = YOLO(TRAINED_YOLO_MODEL_PATH)

    # Perform prediction
    results = model(image)

    for result in results:
        boxes = result.boxes
        labels = result.names
        result.show()
        result.save(filename='result.jpg')
        box_count = len(boxes);
        if box_count > 0:
            st.write('Possible lung cancer nodules were detected in the image.')
            st.write('The following nodules were detected:')
            for box in boxes:
                #st.write(f'Label: {labels[box.cls]}')
                #get box coordinates
                box_coords = box.xyxy[0]
                #st.write(f'Label: {labels[box.cls]}')
                st.write(f'Coordinates: {box_coords}')
            st.image('result.jpg')
        else:
            st.write('No lung cancer nodules were detected in the image.')

def detectapp():
    
    # Title of the web app
    st.title('Lung cancer CT Analyzer')

    # Display a welcome message
    #st.write('Welcome to this simple Streamlit app!')

    # Display a user action in a big font
    st.markdown('### Upload your image file for analysis')

    # Create a file uploader and display the uploaded image
    uploaded_file = st.file_uploader('Choose an image file', type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        predict_lung_cancer(image)

detectapp()
