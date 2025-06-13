# Hand-Finger-Counter
Hand Finger Counter

📌 Overview
This project uses MediaPipe and OpenCV to detect a hand in real-time using a webcam and count the number of fingers raised. Each finger is individually labeled (e.g., "Thumb", "Index", etc.), and the total finger count is displayed.

 Demo
Include a demo gif or image of the project running here (optional but recommended).

🧰 Requirements
Before running the project, make sure the following Python packages are installed:
pip install opencv-python mediapipe pyautogui


You should also have:

Python 3.7+

A webcam for real-time input

Windows/macOS/Linux (tested on Windows)



📄 requirements.txt
opencv-python
mediapipe
pyautogui


🚀 How to Run
python hand_finger_counter.py  


How It Works
MediaPipe Hands: Detects 21 landmarks on each hand.

Landmark IDs:

Thumb tip: 4

Index tip: 8

Middle tip: 12

Ring tip: 16

Pinky tip: 20

Based on the relative positions of landmarks, it determines whether each finger is up or down.

Finger names and the total count are drawn on the image.


✋ Features
✅ Real-time hand detection
✅ Individual finger labeling
✅ Total fingers displayed
✅ Supports multi-hand detection
✅ Works with both left and right hands


📦 Optional Enhancements
Add sound effects for gestures
