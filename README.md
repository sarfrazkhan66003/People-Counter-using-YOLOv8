# 🧠 People Counter using YOLOv8 and SORT Tracking

## 📘 Overview :-
  - This project detects and counts people in real-time video streams using the YOLOv8 object detection model and the SORT (Simple Online and Realtime Tracking) algorithm.
  - It can be used for crowd analytics, retail footfall monitoring, or security surveillance.

## 🚀 Features
  - Real-time person detection using YOLOv8
  - Multi-object tracking using SORT (Kalman Filter + Hungarian Algorithm)
  - Counts people entering or exiting defined zones
  - Smooth visualization using cvzone overlays
  - Lightweight and runs efficiently on CPU or GPU

🧩 Algorithm Explanation
- 1. YOLOv8 – Object Detection
    - YOLO (You Only Look Once) is a deep learning model for real-time object detection.
    - The model divides the image into grids and predicts bounding boxes and class probabilities.
    - Here, we use yolov8n.pt (Nano version) from the Ultralytics library.
    - We filter detections by class "person" (class ID = 0).
    - Output from YOLO:
      - Bounding boxes [x1, y1, x2, y2]
      - Confidence score
      - Class ID

- 2. SORT – Object Tracking
  - SORT (Simple Online and Realtime Tracking) maintains identities of detected objects across frames.
  - It uses:
    - Kalman Filter → predicts next object position
    - Hungarian Algorithm (LAP) → matches detections to existing tracks
    - IOU (Intersection Over Union) → measures overlap between predicted and detected boxes
  Each detected person gets a unique ID, and their path is updated frame-by-frame.
  - Modules used in SORT:
    - filterpy → Kalman filtering
    - lap → solves assignment problem (Hungarian matching)
    - numpy, scikit-image → for matrix and image operations

- 3. Counting Logic
  - Two virtual lines are drawn: Line In (Up) and Line Out (Down).
  - When a person’s centroid crosses one of these lines, the counter updates.
  - cvzone.putTextRect() displays current counts on screen.
 
## 🗂️ Project Structure

  People-Counter/
  │
  ├── People-Counter.py         # Main Python file
  ├── sort.py                   # SORT tracking module
  ├── yolov8n.pt                # YOLOv8 model weights
  ├── mask.png                  # Region mask (optional)
  ├── graphics.png              # UI graphics (optional)
  ├── Videos/
  │   └── people.mp4            # Test video file
  └── README.md                 # Documentation

## 🧮 How It Works
| Step | Process                      | Module             |
| ---- | ---------------------------- | ------------------ |
| 1    | Load YOLOv8 model            | `ultralytics.YOLO` |
| 2    | Capture video frame          | `cv2.VideoCapture` |
| 3    | Detect people in frame       | `YOLO.predict()`   |
| 4    | Track objects using SORT     | `sort.py`          |
| 5    | Count line crossings         | `cvzone` overlay   |
| 6    | Display results in real-time | `cv2.imshow()`     |

## 📊 Output
  - Live video with bounding boxes, unique IDs, and count overlays.
  - Two counters displayed:
  - Count Up → people entering
  - Count Down → people exiting

## 🧰 Technologies Used
- Python 3.10
- OpenCV
- Ultralytics YOLOv8
- SORT Tracker (Kalman + Hungarian)
- cvzone for visuals
- NumPy & scikit-image
    
