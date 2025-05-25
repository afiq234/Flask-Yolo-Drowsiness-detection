from flask import Flask, redirect, url_for, render_template, request, Response
import os
import cv2
from ultralytics import YOLO

MODEL_PATH = "D:/CodingStorage/Python/FlaskFyp2Detection/best.pt"  # Update with your YOLO model path
model = YOLO(MODEL_PATH, task="detect")  # Explicitly specify the task

app = Flask(__name__)
camera = cv2.VideoCapture(0)  # Change the index if necessary


def gen_frames():
    while True:
        success, frame = camera.read()  # Read the camera frame
        if not success:
            print("Failed to capture frame from camera")
            break
        else:
            print("Frame captured successfully")
            # Perform inference
            results = model(frame)
            result = results[0]  # Assuming only one image is processed at a time

            # Use plot() to get the annotated image
            annotated_frame = result.plot()

            # Encode the annotated frame to JPEG
            ret, buffer = cv2.imencode(".jpg", annotated_frame)
            if not ret:
                print("Failed to encode frame")
                continue
            frame = buffer.tobytes()

            # Yield the frame for streaming
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video")
def video():
    return Response(gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 8080)), host="0.0.0.0", debug=True)
