import boto3
import numpy as np
import cv2
from ultralytics import YOLO
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load your model (replace 'model.pth' with your model file)
model = YOLO("model_checkpoints/yolo11n.pt")

@app.route('/upload', methods=['POST'])
def upload_multiple_files():
    # Check if any files were uploaded
    if not request.files:
        return jsonify({"error": "No files found in the request"}), 400

    uploaded_files = []
    invalid_files = []

    # Process all files in the request
    for file_key, file in request.files.items():
        if file.filename == '':
            invalid_files.append({"file_key": file_key, "error": "No file selected for uploading"})
            continue

        # Check the file type (optional)
        if file.content_type not in ['image/jpeg', 'image/png']:
            invalid_files.append({"file_key": file_key, "filename": file.filename, "error": "Invalid file type"})
            continue

        # Add to uploaded files list (you can save files here if needed)
        uploaded_files.append({"file_key": file_key, "filename": file.filename, "content_type": file.content_type})

    # Return response
    return jsonify({
        "uploaded_files": uploaded_files,
        "invalid_files": invalid_files,
        "message": f"Uploaded {len(uploaded_files)} files successfully"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
