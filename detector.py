import cv2
import math
import numpy as np
from ultralytics import YOLO

class YOLODetector:
    def __init__(self, weights_path, mask_path, class_names):
        self.model = YOLO(weights_path)
        self.mask = cv2.imread(mask_path)
        self.class_names = class_names

    def detect(self, image):
        image_region = cv2.bitwise_and(image, self.mask)
        results = self.model(image_region, stream=True)
        detections = np.empty((0, 5))

        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0].int().numpy()
                score = math.ceil(box.conf[0] * 100) / 100
                class_index = int(box.cls[0])
                current_class = self.class_names[class_index]
                if current_class in ['car', 'truck', 'bus', 'motorbike']:
                    current_array = np.array([x1, y1, x2, y2, score])
                    detections = np.vstack((detections, current_array))
        return detections
