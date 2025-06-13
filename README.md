
#  Hand-Finger-Counter

A real-time finger counting and labeling system using **MediaPipe** and **OpenCV**.

---

## 📌 Overview

This project uses **MediaPipe** and **OpenCV** to detect a hand in real-time using a webcam and count the number of fingers raised. Each finger is individually labeled (e.g., **Thumb**, **Index**, etc.), and the total number of fingers is displayed on the screen.

---
 

##  Requirements

Install the required Python packages using:

```bash
pip install opencv-python mediapipe pyautogui
```

You’ll need:

- Python **3.7+**
- A webcam
- OS: Windows/macOS/Linux (✅ Tested on Windows)

---

## 📄 requirements.txt

```
opencv-python
mediapipe
pyautogui
```

To install all dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

Clone the repository or download the source code.

```bash
git clone https://github.com/yourusername/hand-finger-counter.git
cd hand-finger-counter
```

Run the Python script:

```bash
python hand_finger_counter.py
```

Press **`q`** to quit the webcam window.

---

##  How It Works

- **MediaPipe Hands** detects 21 landmarks per hand in real-time.
- **Finger Landmarks Used**:
  - **Thumb tip**: ID `4`
  - **Index tip**: ID `8`
  - **Middle tip**: ID `12`
  - **Ring tip**: ID `16`
  - **Pinky tip**: ID `20`
- Compares finger tip positions with previous joints to determine whether each finger is **up** or **down**.
- Labels each finger and displays the total raised fingers live on the video feed.

---

##  Features

 Real-time hand and finger detection  
  Finger labeling (Thumb, Index, etc.)  
 Total fingers displayed  
 Supports multiple hands  
 Works with both **left** and **right** hands

---

##  Optional Enhancements
  
 Log finger counts over time  
  Integrate with gesture-controlled media players  
 

---


