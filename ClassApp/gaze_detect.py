from gaze_tracking import GazeTracking
import cv2

face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')


def detect(gray, frame):
    all_roi_faces=[]
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for i,(x, y, w, h) in enumerate(faces):
        roi_color = frame[y:y+h, x:x+w]
        all_roi_faces.append(roi_color)
    return all_roi_faces


def getGazeAttention(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    all_faces = detect(gray, image)
    gaze = GazeTracking()

    for i,frame in enumerate(all_faces):
        gaze.refresh(frame)
        text=""

        if gaze.is_right():
            text = "Looking right"
        elif gaze.is_left():
            text = "Looking left"
        elif gaze.is_center():
            text = "Looking center"

    return 100
