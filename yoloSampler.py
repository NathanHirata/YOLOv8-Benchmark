
import ultralytics
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2
import torch
import sys

model = YOLO("yolov8n.pt")

#results = model.predict(source="tennis.jpg", save=True ) #Photos

#results = model.predict(source="0", save=True ,conf=0.5, save_txt=True, line_thickness = 1,show=True)#,device=cpu)#imgsz = 1080) #Webcam

results = model.predict(source="office.mp4", save=True ,conf=0.5, save_txt=True, vid_stride=True, line_thickness = 1, show =True)#, imgsz = 1920)  #Video



