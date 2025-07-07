# ♻️ Garbage Classification App

A deep learning web application for real-time garbage classification built with **TensorFlow** and **Streamlit**.

🔗 **Live App:** [classification-garbage.streamlit.app](https://classification-garbage.streamlit.app/)

---

## 📌 Overview

This project classifies garbage images into one of six categories:

- Cardboard
- Glass
- Metal
- Paper
- Plastic
- Trash

It uses a trained Keras model and provides an easy-to-use interface via Streamlit where users can either:

- Capture an image from their **webcam**
- Upload an image from their **device**

---

## 🚀 Features

- 📷 Real-time camera and file upload support  
- ⚡ Fast and accurate predictions using a custom-trained CNN model  
- 🧠 Clean UI built with Streamlit  
- 💾 Model loaded in `.keras` format  
- 🌐 Hosted on Streamlit Cloud  

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **Backend Model:** TensorFlow / Keras  
- **Language:** Python  
- **Libraries:** NumPy, PIL, Streamlit  

---

## 🧪 Model Details

- **Input Shape:** 124x124 RGB images  
- **Model Type:** Custom CNN (trained in `Garbage_Classification_Improved.ipynb`)  
- **Output Classes:** 6 garbage types  
- **Saved Format:** `saved_model.keras`  

---

## 📁 File Structure

```plaintext
.
├── app.py                             # Streamlit web app
├── saved_model.keras                 # Trained model file
├── Garbage_Classification_Improved.ipynb  # Model training code
├── requirements.txt                  # Python dependencies
└── README.md                         # Project documentation
