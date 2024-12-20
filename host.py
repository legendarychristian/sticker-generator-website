import boto3
import numpy as np
import cv2
from ultralytics import YOLO
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

# Load your model (replace 'model.pth' with your model file)
model = YOLO("model_checkpoints/yolo11n.pt")

@app.post("/upload-images/")
async def upload_images(files: list[UploadFile] = File(...)):
    uploaded_files = []
    
    for file in files:
        # Validate file type
        if file.content_type not in ["image/jpeg", "image/png"]:
            return {"error": f"File {file.filename} is not a valid image."}
        
        uploaded_files.append({"filename": file.filename, "content_type": file.content_type})

    return {"uploaded_files": uploaded_files}
