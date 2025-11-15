# 📸 Face Detection App using Viola–Jones Algorithm

This project is a real-time face detection web application built with **Streamlit** and **OpenCV**.  
It uses the classical **Viola–Jones Haar Cascade classifier** to detect faces from your webcam.

---

## 🚀 Features

- Real-time face detection using your webcam  
- Adjustable detection parameters:
  - `scaleFactor`
  - `minNeighbors`
- Custom rectangle color selector  
- Attractive and simple Streamlit UI  
- Keyboard controls:
  - Press **Q** to quit the webcam  
- Cross-platform compatibility (Windows, macOS, Linux)

---

## 📂 Project Structure

```
project/
│
├── app.py
├── detectors/
│   └── haarcascade_frontalface_default.xml
└── requirements.txt
```

---


## ▶️ Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

### 🎥 Inside the app:

- Click **Start Detection** to launch the webcam  
- Press **Q** in the webcam window to stop detection  
- Use the sidebar to:
  - Choose rectangle color  
  - Adjust detection accuracy  
  - Increase or decrease detection strictness  

---

## 🧠 How It Works

This app uses OpenCV’s **Haar Cascade Classifier**, a core component of the Viola–Jones algorithm.

Steps performed in real time:

1. Frame captured from webcam  
2. Converted to grayscale  
3. Face detection using Haar Cascade  
4. Bounding box drawn on detected faces  
5. Process repeats continuously  

You can modify detection behavior through Streamlit sliders.

---


