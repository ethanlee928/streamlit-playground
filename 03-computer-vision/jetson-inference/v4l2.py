import cv2
from jetson_inference import detectNet
from jetson_utils import cudaToNumpy, videoSource

import streamlit as st


@st.cache_resource
def load_model():
    return detectNet("ssd-mobilenet-v2", threshold=0.5)


@st.cache_resource
def load_videoSource():
    return videoSource("v4l2:///dev/video0")


SOURCE = load_videoSource()
DETECTOR = load_model()


st.title("Object Detection with SSD MobilenetV2 👀")
st.write(
    "The default model SSD-Mobilenet-v2 is trained on the MS COCO dataset, with [91 classes](https://github.com/dusty-nv/jetson-inference/blob/master/data/networks/ssd_coco_labels.txt)"
)

with st.empty():
    while True:
        img = SOURCE.Capture(timeout=1000)
        if img is None:
            continue
        detections = DETECTOR.Detect(img, overlay="box,labels,conf")
        np_img = cudaToNumpy(img, cv2.COLOR_RGBA2BGR)
        st.image(np_img, caption="Detection Results")
