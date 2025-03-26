# 😴 FatiguEye – Real-Time Fatigue Detection via Webcam

## 🚀 Overview
![Main Preview](assets/img/main.png)
A smart computer vision system that detects signs of fatigue, eye strain, and microsleep using a standard webcam.

---

## 🎯 Purpose

**FatiguEye** is a real-time fatigue detection system based on eye tracking and facial landmark analysis.  
It helps identify early signs of drowsiness by measuring:
- 👁️ Eye Aspect Ratio (EAR)
- 🔁 Blink frequency
- ⏱️ Prolonged eyelid closure
- ⚠️ Microsleep events

Ideal for driver monitoring, industrial safety, or ergonomic fatigue prevention.

---

## 🧠 How It Works

FatiguEye uses [MediaPipe Face Mesh](https://google.github.io/mediapipe/) to extract eye landmarks, and computes the **EAR (Eye Aspect Ratio)** on each video frame.

### 📡 Processing pipeline:
1. 🎥 Webcam feed is captured in real-time
2. 🧠 Facial landmarks (eyes) are detected with Mediapipe
3. 📏 EAR is calculated per eye
4. 🧮 Blink count and eye closure duration are analyzed
5. 🔔 Fatigue alerts are raised (visual + audio)

---

## 🚀 Demo Preview

> 

<img src="assets/demo.gif" alt="FatiguEye demo" width="700">

---

## 💻 Technologies Used

| Tech        | Description                             |
|-------------|-----------------------------------------|
| Python      | Core language                           |
| OpenCV      | Webcam video processing + overlays      |
| MediaPipe   | Face mesh & eye landmark detection      |
| NumPy       | EAR computation                         |
| Streamlit   | Live web dashboard                      |
| winsound    | Audio alert (Windows only)              |

---

## 📦 Installation

```bash
git clone https://github.com/Tirovo/fatigueye.git
cd fatigueye
python -m venv venv
source venv/bin/activate  # Or venv\Scripts\activate on Windows
pip install -r requirements.txt
