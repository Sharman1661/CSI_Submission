import cv2
from ultralytics import YOLO
import random
import time

# 1. Load the pre-trained YOLOv8 model
model = YOLO('best.pt') 

# 2. Open the sample dashcam video
video_path = 'sample_dashcam.mp4'
cap = cv2.VideoCapture(video_path)

print("Starting Edge Device Simulation...")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # 2. Run the YOLO model on the current frame
    # conf=0.5 means it only triggers if it's 50% sure it's a pothole
    results = model(frame, conf=0.5, verbose=False) 

    for result in results:
        boxes = result.boxes
        for box in boxes:
            # If a pothole is detected, simulate grabbing GPS and sending to cloud
            # (In reality, you'd pull this from the phone's GPS module)
            # This will work once we use proper API keys from the phone's GPS
            mock_lat = 17.3850 + random.uniform(-0.001, 0.001)
            mock_lon = 78.4867 + random.uniform(-0.001, 0.001)
            
            print(f"🚨 [URGENT] Pothole Detected! Sending to Cloud -> Lat: {mock_lat:.4f}, Lon: {mock_lon:.4f}")

    # 5. Draw the bounding boxes on the video frame
    annotated_frame = results[0].plot()

    # 6. Display the video on your screen
    cv2.imshow("RoadRadar: Edge Device View", annotated_frame)

    # Press 'q' to quit the simulation
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()