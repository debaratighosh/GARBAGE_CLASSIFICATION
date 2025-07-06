# Garbage Classification - Streamlit App with Live Camera

import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the model (ensure saved_model.keras is in the same directory)
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("saved_model.keras")

model = load_model()

# Class labels for prediction
class_names = ['Cardboard', 'Glass', 'Metal', 'Paper', 'Plastic', 'Trash']

# Image preprocessing function
def preprocess(image):
    image = image.resize((124, 124))
    img_array = tf.keras.utils.img_to_array(image)
    img_array = tf.expand_dims(img_array, 0)
    return img_array

# Streamlit UI
st.set_page_config(page_title="Garbage Classifier", layout="centered")
st.title("♻️ Garbage Classification App")
st.write("Take a photo or upload an image to classify garbage type.")

option = st.radio("Choose Input Method", ("📷 Camera", "📁 Upload"))

image = None
if option == "📷 Camera":
    camera_image = st.camera_input("Take a picture")
    if camera_image:
        image = Image.open(camera_image)
elif option == "📁 Upload":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file)

if image:
    st.image(image, caption="Input Image", use_column_width=True)
    img_tensor = preprocess(image)
    prediction = model.predict(img_tensor)
    predicted_class = class_names[np.argmax(prediction[0])]
    confidence = np.max(prediction[0]) * 100

    st.success(f"🗑️ Predicted: **{predicted_class}** ({confidence:.2f}% confidence)")