import logging

import av
import cv2
from streamlit_webrtc import webrtc_streamer

import streamlit as st

logger = logging.getLogger(__name__)


@st.cache_resource
def load_face_cascade():
    face_cascade = cv2.CascadeClassifier()
    face_cascade.load("haarcascade_frontalcatface.xml")
    return face_cascade


@st.cache_resource
def load_eyes_cascade():
    eyes_cascade = cv2.CascadeClassifier()
    eyes_cascade.load("haarcascade_eye_tree_eyeglasses.xml")
    return eyes_cascade


FACE_CASCADE = load_face_cascade()
EYES_CASCADE = load_eyes_cascade()


st.title("OpenCV Haarcascade Face & Eyes Detection 👀")
st.write("[Tutorial](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)")

st.code(
    """
FACE_CASCADE = cv2.CascadeClassifier()
EYES_CASCADE = cv2.CascadeClassifier()

FACE_CASCADE.load("haarcascade_frontalcatface.xml")
EYES_CASCADE.load("haarcascade_eye_tree_eyeglasses.xml")
    
def detect(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.equalizeHist(gray_img)

    # -- Detect faces
    faces = FACE_CASCADE.detectMultiScale(gray_img)
    for x, y, w, h in faces:
        center = (x + w // 2, y + h // 2)
        img = cv2.ellipse(img, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)

        faceROI = gray_img[y : y + h, x : x + w]
        # -- In each face, detect eyes
        eyes = EYES_CASCADE.detectMultiScale(faceROI)
        for x2, y2, w2, h2 in eyes:
            eye_center = (x + x2 + w2 // 2, y + y2 + h2 // 2)
            radius = int(round((w2 + h2) * 0.25))
            img = cv2.circle(img, eye_center, radius, (255, 0, 0), 4)
    return img
        """
)


def detect(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.equalizeHist(gray_img)

    # -- Detect faces
    faces = FACE_CASCADE.detectMultiScale(gray_img)
    for x, y, w, h in faces:
        center = (x + w // 2, y + h // 2)
        img = cv2.ellipse(img, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)

        faceROI = gray_img[y : y + h, x : x + w]
        # -- In each face, detect eyes
        eyes = EYES_CASCADE.detectMultiScale(faceROI)
        for x2, y2, w2, h2 in eyes:
            eye_center = (x + x2 + w2 // 2, y + y2 + h2 // 2)
            radius = int(round((w2 + h2) * 0.25))
            img = cv2.circle(img, eye_center, radius, (255, 0, 0), 4)
    return img


def callback(frame):
    img = frame.to_ndarray(format="bgr24")
    img = detect(img)
    return av.VideoFrame.from_ndarray(img, format="bgr24")


webrtc_streamer(
    key="example",
    video_frame_callback=callback,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
)
