import boto3
import numpy as np
import cv2
from ultralytics import YOLO
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load your model (replace 'model.pth' with your model file)
model = YOLO("model_checkpoints/yolo11n.pt")

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if any files were uploaded
    if not request.files:
        return jsonify({"error": "No files found in the request"}), 400

    # Process the first file in the request
    file = next(iter(request.files.values()))

    # Check if a file is selected
    if file.filename == '':
        return jsonify({"error": "No file selected for uploading"}), 400

    # Return a success response
    return jsonify({"message": "File successfully uploaded", "file_path": file.filename}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
