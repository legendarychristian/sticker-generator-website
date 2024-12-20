import boto3
import numpy as np
import cv2
from ultralytics import YOLO
from fastapi import FastAPI

app = FastAPI()

# Load your model (replace 'model.pth' with your model file)
model = YOLO("model_checkpoints/yolo11n.pt")

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

