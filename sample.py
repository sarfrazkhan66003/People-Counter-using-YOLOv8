from ultralytics import YOLO
model = YOLO(r"C:\Users\DELL\Desktop\Sarfu\PW Data Science\Project\Project 2 - People Counter\yolov8n.pt")
import cv2
results = model(r"C:\Users\DELL\Desktop\Sarfu\PW Data Science\Project\Project 2 - People Counter\Videos\people.mp4")
results[0].show()