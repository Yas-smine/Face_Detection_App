import cv2
import streamlit as st


face_cascade = cv2.CascadeClassifier('C:/Users/ABL/Documents/Codes/checkp_python/Face_detection_app/haarcascade_frontalface_default .xml')

# Face detection function
def detect_faces(rgb_color, min_neighbors, scale_factor):
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    
    while True:
        # Read the frames from the webcam
        ret, frame = cap.read()
        if not ret:
            st.error("⚠️ Cannot access webcam.")
            break
       
        # Convert the frames to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect the faces using the face cascade classifier
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        
        
        # Draw rectangles around the detected faces
        r, g, b = rgb_color
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (int(r), int(g), int(b)), 2)
       
        # Display the frames
        cv2.imshow('Face Detection using Viola-Jones Algorithm', frame)
        
        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):   # Quit camera
            break
    
    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Streamlit app
def app():
    st.title(" 📸 Face Detection using Viola-Jones Algorithm")
    
    st.markdown("""
    ### 🔧 How to Use This App
    - Click **Start Detection** to open your webcam.  
    - Press **Q** on your keyboard to quit the webcam.    
    - Use the sidebar to:
        - change the rectangle color  
        - adjust `minNeighbors`  
        - adjust `scaleFactor`
    """)

    # Sidebar Controls
    st.sidebar.header("Settings")

    color = st.sidebar.color_picker("Choose rectangle color", "#00FF00")
    rgb_color = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))

    min_neighbors = st.sidebar.slider(
        "minNeighbors (more = stricter detection)",
        min_value=1,
        max_value=10,
        value=5
    )

    scale_factor = st.sidebar.slider(
        "scaleFactor (higher = faster but less accurate)",
        min_value=1.05,
        max_value=2.0,
        value=1.3,
        step=0.05
    )

    st.write("Press the button below to start detecting faces from your webcam")
    # Add a button to start detecting faces
    if st.button("Detect Faces"):
        # Call the detect_faces function
        detect_faces(rgb_color, min_neighbors, scale_factor)
if __name__ == "__main__":
    app()