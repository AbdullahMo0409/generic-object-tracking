# Generic Object Tracking

A computer vision project where the user selects an object in the first video frame, then the system tracks it throughout the rest of the video.

This project demonstrates the basic workflow of object tracking in video processing, including frame reading, target selection, tracker initialization, and continuous object localization across frames.

---

## Overview

Object tracking is a computer vision task used to follow a selected target across video frames. Unlike object detection, where the system detects objects independently in each frame, object tracking focuses on following a specific object over time after it has been selected.

In this project, the user manually selects the target object in the first frame, and the tracking algorithm follows that object throughout the video.

---

## Features

- User-selected target object in the first frame
- Object tracking across video frames
- Works with sample video data
- Frame-by-frame video processing
- Visual tracking output
- Practical implementation of computer vision tracking concepts

---

## Approach

The project workflow includes:

1. Loading the input video
2. Reading the first frame
3. Allowing the user to select the target object
4. Initializing the tracking algorithm
5. Processing the video frame by frame
6. Updating the target position
7. Displaying the tracked object in the video output

---

## Technologies Used

- Python
- OpenCV
- Computer Vision
- Video Processing
- Object Tracking
- Jupyter Notebook

---

## Repository Structure

```text
generic-object-tracking/
├── computer-vision/
│   └── notebooks/        # Computer vision notebook files
├── data/                 # Sample video data
├── .gitignore
└── README.md
```

---

## Data

Small sample videos are included in the `data/` folder so the project can be tested directly.

The videos are used as input for the tracking notebook, where the user selects the object to track from the first frame.

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/AbdullahMo0409/generic-object-tracking.git
```

2. Open the notebook inside:

```text
computer-vision/notebooks/
```

3. Run the notebook cells.

4. Select the target object in the first frame when prompted.

5. The tracker will follow the selected object through the remaining video frames.

---

## Notes

This project was built as a practical introduction to object tracking using traditional computer vision techniques.

The project focuses on understanding the tracking pipeline rather than building a deep learning-based object detector.

---

## Future Improvements

- Compare multiple tracking algorithms such as CSRT, KCF, and MOSSE
- Add automatic object detection before tracking
- Add support for multiple object tracking
- Export the tracked output video
- Add a simple user interface for uploading and tracking videos

---

## Author

**Abdullah Mohammed**  
AI Engineering Student — Mansoura University
