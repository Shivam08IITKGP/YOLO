# Vehicle Detection and Tracking System

## Overview

This project implements a robust vehicle detection and tracking system using YOLO (You Only Look Once) model and SORT (Simple Online and Realtime Tracking) algorithm. The system is designed to process video feeds, detect vehicles, track their movements, and count incoming and outgoing vehicles. The results are saved as annotated video and logged in a CSV file. Additionally, detected vehicle images are saved in respective directories for further analysis.

## Features

- **Vehicle Detection**: Utilizes the YOLOv8 model to detect vehicles, including cars, trucks, buses, and motorbikes, in a given video feed.
- **Vehicle Tracking**: Employs the SORT algorithm to track detected vehicles across frames.
- **Counting Vehicles**: Counts ingoing and outgoing vehicles crossing a predefined line.
- **Data Logging**: Logs detection counts and timestamps in a CSV file.
- **Image Saving**: Captures and saves images of detected vehicles into categorized directories.
- **Video Annotation**: Saves processed video with bounding boxes, counts, and other annotations.

## Requirements

To run this project, ensure you have the following dependencies installed:

- OpenCV
- Ultralytics YOLO
- Cvzone
- Sort
- Numpy

You can install these dependencies using the following command:
```sh
pip install -r requirements.txt
```

Installation
Clone this repository:
```sh
git clone https://github.com/Shivam08IITKGP/YOLO.git
cd YOLO
```

Place your mask image in the project root directory.
Run the vehicle detection and tracking script:

```sh
python main.py
```
## Usage
The script processes a video file (Cars.mp4), detects and tracks vehicles, and saves the results as an annotated video (processed_video.mp4). The vehicle images are saved in the Detected Ingoing and Detected Outgoing directories based on their movement direction. A CSV file (Detection_log.csv) logs the counts and timestamps.

## Configurations
**Counting Line**: Adjust the limits variable in the script to change the position of the counting line.
**Classes for Detection**: Modify the current class list to include or exclude specific vehicle types for detection.

## Code Description
- **Initialization**: The script initializes video capture, model loading, and directory setup.
- **Detection and Tracking**: The YOLO model detects vehicles, and the SORT algorithm tracks them across frames.
- **Counting and Logging**: Vehicles crossing the counting line are counted and logged.
- **Saving Results**: The script saves annotated frames as a video and logs detection counts to a CSV file.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments
- YOLO
- SORT
- OpenCV
- Cvzone

## Contact
For any inquiries, please contact [pran8sh@gmail.com].