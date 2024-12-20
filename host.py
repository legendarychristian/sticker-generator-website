import boto3
import numpy as np
import cv2
from ultralytics import YOLO
from flask import *

app = Flask(__name__)

# Load your model (replace 'model.pth' with your model file)
model = YOLO("model_checkpoints/yolo11n.pt")

@app.route('/upload', methods=['POST']) 
def upload(): 
    uploaded_files = []
    
    if request.method == 'POST': 
  
        # Get the list of files from webpage 
        files = request.files.getlist("file") 
  
        # Iterate for each file in the files List, and Save them 
        for file in files: 
            uploaded_files.append(file.filename) 

        # Return response
        return jsonify({
            "uploaded_files": uploaded_files,
            "message": f"Uploaded {len(uploaded_files)} files successfully"
        }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)