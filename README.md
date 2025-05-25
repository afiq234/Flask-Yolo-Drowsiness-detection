# Flask-YOLO Drowsiness Detection System

A lightweight Flask-based web application that integrates a YOLOv5, 8, 11 model for real-time or batch drowsiness detection using image-based input and pre-trained models.

## 🚀 Project Overview

This project provides:
- A minimal Flask server (`app.py`) to serve detection via API or local interface.
- A YOLOv5-based model (`best.pt`) and calibration data.
- A training notebook (`train_model.ipynb`) to fine-tune your own drowsiness model.
- Deployment-ready files for platforms like **Render**, **Heroku**, or Docker.

---

## 📁 Directory Structure
.
├── app.py                               # Flask app for drowsiness detection
├── app.yml                              # Render deployment configuration
├── calibration_image_sample_data_20x128x128x3_float32.npy  # Sample input data
├── train_model.ipynb                    # YOLO model training notebook
├── requirements.txt                     # Python dependencies
├── Dockerfile                           # Optional Docker support
├── Procfile                             # Heroku deployment file
├── .env                                 # Environment variables (not committed)
├── .dockerignore                        # Files to ignore in Docker builds
├── test.html                            # (Optional) basic frontend demo
└── README.md                            # Project documentation

---

## 🧰 Technologies

- Python 3.8+
- Flask
- YOLOv5 (PyTorch)
- OpenCV
- Jupyter Notebook

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/afiq234/Flask-Yolo-Drowsiness-detection.git
cd Flask-Yolo-Drowsiness-detection
```

## Install Dependencies
```bash
Copy
Edit
pip install -r requirements.txt
```

### Run the Flask App
```bash
Copy
Edit
python app.py
```

## 🧪 Training a Custom Model
Use train_model.ipynb to train or fine-tune your own YOLO model:

Load labeled data

Train using YOLOv5

Save the trained model as best.pt

Use the trained model in app.py for inference

## ☁️ Deployment
▶️ Render
- Uses app.yml for auto-deploy

- Connect GitHub and deploy in minutes

🔁 Heroku
```bash
heroku create
git push heroku main
```

🐳 Docker
```bash
docker build -t flask-yolo .
docker run -p 5000:5000 flask-yolo
```

---

## 🔐 Notes
.env should not be pushed to GitHub

Add secrets or config keys there, and add it to .gitignore

---

## 📄 License
This project is open-source under the MIT License.

---

## 👨‍💻 Author
Fiq

