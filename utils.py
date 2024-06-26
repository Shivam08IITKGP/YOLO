import cv2
import cvzone
from datetime import datetime

def draw_counting_line(image, limits):
    cv2.line(image, (limits[0], limits[1]), (limits[2], limits[3]), (0, 0, 255), 3)

def draw_detections(image, bbox, ID):
    x1, y1, w, h = bbox
    cvzone.cornerRect(image, (x1, y1, w, h), l=9, rt=2)
    cvzone.putTextRect(image, f'{int(ID)}', (max(x1, 0), max(35, y1)), scale=2, thickness=3, offset=10)

def log_data(writer, in_count, out_count, frame_number):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    writer.writerow([current_time, in_count, out_count, frame_number])

def display_counts(image, in_count, out_count):
    cvzone.putTextRect(image, f'In going: {in_count}', (50, 50))
    cvzone.putTextRect(image, f'Out going: {out_count}', (900, 50))
