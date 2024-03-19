import cv2

face_cascade = cv2.CascadeClassifier('HaarcascadeFrontalFaceDefault.xml')  # Loads a Cascade Coordinates

cap = cv2.VideoCapture(0)  # To Capture from Webcam
# cap = cv2.VideoCapture('filename.mp4')  # To use Video file as Input

if not cap.isOpened():
    print("Input Error: Webcam or video file not found")

while True:
    _, img = cap.read()  # Read Frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to Grayscale
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)  # Detect Faces
    for (x, y, w, h) in faces:  # Draw Rectangle around Each Face
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('img', img)  # Display
    k = cv2.waitKey(30) & 0xff  # Stop if Escape Key (ASCII Value: 27) is Pressed
    if k == 27:
        break

cap.release()  # Release Video Capture Object
cv2.destroyAllWindows()  # Close all OpenCV windows
