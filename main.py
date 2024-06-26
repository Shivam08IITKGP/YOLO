import cv2
import os
import csv
from datetime import datetime
from config import *
from detector import YOLODetector
from tracker import ObjectTracker
from utils import draw_counting_line, draw_detections, log_data, display_counts
from reader import VideoReader

def main():
    # Create directories if they do not exist
    os.makedirs(INGOING_DIR, exist_ok=True)
    os.makedirs(OUTGOING_DIR, exist_ok=True)

    # Initialize YOLO detector and SORT tracker
    detector = YOLODetector(YOLO_WEIGHTS, MASK_PATH, CLASS_NAMES)
    tracker = ObjectTracker()
    reader = VideoReader(VIDEO_PATH)

    # Initialize counts
    totalCountIn = []
    totalCountOut = []

    # Open the CSV file for writing
    with open(LOG_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time', 'Ingoing Count', 'Outgoing Count', 'Frame Number'])

        frame_number = 0

        while True:
            success, image = reader.read_frame()
            if not success:
                break

            # Detect objects
            detections = detector.detect(image)
            resultsTracker = tracker.update(detections)

            # Draw the counting line
            draw_counting_line(image, LIMITS)

            # Process tracked objects
            for result in resultsTracker:
                process_tracked_object(result, image, totalCountIn, totalCountOut)

            # Log data to CSV
            log_data(writer, len(totalCountIn), len(totalCountOut), frame_number)

            # Display counts
            display_counts(image, len(totalCountIn), len(totalCountOut))

            # Display the image with bounding boxes and counts
            cv2.imshow('Image', image)

            frame_number += 1

            # Keep displaying processed frames until q is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    reader.release()
    cv2.destroyAllWindows()

def process_tracked_object(result, image, totalCountIn, totalCountOut):
    x1, y1, x2, y2, ID = result
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    w = x2 - x1
    h = y2 - y1
    cx = x1 + w // 2
    cy = y1 + h // 2

    draw_detections(image, (x1, y1, w, h), ID)

    if LIMITS[0] < cx < LIMITS[2] and LIMITS[1] - 25 < cy < LIMITS[1] + 25:
        crop_img = image[y1:y2, x1:x2]  # Crop the detected car region
        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        if cx < (LIMITS[2] // 2):
            # Ingoing (left half)
            if totalCountIn.count(ID) == 0:
                totalCountIn.append(ID)
                cv2.imwrite(f'{INGOING_DIR}/{current_time}_{int(ID)}.jpg', crop_img)
        else:
            # Outgoing (right half)
            if totalCountOut.count(ID) == 0:
                totalCountOut.append(ID)
                cv2.imwrite(f'{OUTGOING_DIR}/{current_time}_{int(ID)}.jpg', crop_img)

if __name__ == "__main__":
    main()
