## Deployed Version  
🚀 **Live API Endpoint:** http://18.218.123.164/ 

Car Classification API 🚗🔍
A FastAPI-based machine learning model to classify car types, containerized with Docker, and deployed on AWS EC2.

📌 Project Overview
This project predicts the type of car using an ML model trained on Google Colab. The backend is built with FastAPI, containerized using Docker, and deployed on AWS EC2.

📂 Project Structure
carApp/
│── app.py                   # FastAPI application
│── Car_Classification.ipynb  # Jupyter Notebook for model training (Google Colab)
│── model.h5                  # Trained ML model (Excluded from GitHub)
│── Dockerfile                # Docker containerization
│── requirements.txt          # Dependencies
│── static/                   # Static files (if any)
│── templates/                # HTML templates for the web UI
│── .gitignore                # Ignored files
│── README.md                 # Project documentation (this file)

⚙️ Installation & Setup
🔹 1. Clone the Repository
git clone https://github.com/rohith1824/Car-Classification.git
cd Car-Classification

🔹 2. Set Up Virtual Environment (Optional but Recommended)
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

🔹 3. Install Dependencies
pip install -r requirements.txt

🔹 4. Run the FastAPI Server
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
Open http://127.0.0.1:8000/docs to test API endpoints.

🚀 Docker Deployment
🔹 1. Build Docker Image
docker build -t car-classifier .

🔹 2. Run Docker Container
docker run -d -p 80:8000 car-classifier
Access the API at http://localhost/docs

🌍 AWS EC2 Deployment
🔹 1. SSH into Your EC2 Instance
ssh -i "your-key.pem" ubuntu@your-ec2-public-ip

🔹 2. Install Docker on EC2
sudo apt update
sudo apt install docker.io -y

🔹 3. Run Docker Container on EC2
sudo docker run -d -p 80:8000 car-classifier

📌 Credits
ML Model: Trained on Google Colab using TensorFlow/Keras.
Backend: FastAPI.
Containerization: Docker.
Deployment: AWS EC2.
