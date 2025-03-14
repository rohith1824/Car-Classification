from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os
import time

app = FastAPI()

# Mount the "static" directory so FastAPI can serve images
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Load the TensorFlow model
model = tf.keras.models.load_model("model.h5")

# Define class labels
LABELS = ['Convertible', 'Coupe', 'Hatchback', 'Minivan', 'SUV', 'Sedan', 'Truck', 'Van', 'Wagon']

# Create a temporary uploads folder
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def preprocess_image(image: Image.Image):
    """Preprocess image for model inference."""
    image = image.resize((224, 224))  # Resize to match model input size
    image = np.array(image) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image


def delete_file(path: str):
    """Wait a bit and then delete the file."""
    time.sleep(10)  # Optionally wait before deletion
    if os.path.exists(path):
        os.remove(path)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the HTML file for the web interface."""
    return templates.TemplateResponse("index.html", {"request": request, "image_url": None, "prediction": None})


@app.post("/predict/")
async def predict(request: Request, file: UploadFile = File(...), background_tasks: BackgroundTasks = None):
    """Handle image upload, classify it, and schedule file deletion."""
    # Save the uploaded image temporarily
    image_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(image_path, "wb") as buffer:
        buffer.write(await file.read())

    # Open and preprocess the image
    image = Image.open(image_path)
    processed_image = preprocess_image(image)

    # Get model prediction
    prediction = model.predict(processed_image)
    confidence = float(np.max(prediction)) * 100  # Convert to percentage
    predicted_class = LABELS[np.argmax(prediction)]

    # Get the image URL
    image_url = f"/static/uploads/{file.filename}"

    # Schedule the deletion of the file as a background task
    if background_tasks:
        background_tasks.add_task(delete_file, image_path)

    # Return the response with the image URL and prediction results
    return templates.TemplateResponse("index.html", {
        "request": request,
        "image_url": image_url,
        "prediction": predicted_class,
        "confidence": round(confidence, 2)
    })
