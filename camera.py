import face_recognition
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)

daniel_image = face_recognition.load_image_file('faces/daniel.jpg')
daniel_face_encoding = face_recognition.face_encodings(daniel_image)[0]

