# 😴 FatiguEye – Real-Time Fatigue Detection via Webcam

> 👁️ A smart computer vision system that detects signs of fatigue, eye strain, and microsleep using a standard webcam.

---

## 🎯 Purpose

**FatiguEye** is a real-time fatigue detection system based on eye tracking and facial landmark analysis.  
It helps identify early signs of drowsiness by measuring:
- Eye blinks and blink frequency
- Prolonged eyelid closure
- Visual attention drop or microsleep episodes

---

## 🔧 Tech Stack

| Component        | Role                                      |
|------------------|-------------------------------------------|
| Python           | Main programming language                 |
| OpenCV           | Video capture and display                 |
| Mediapipe        | Face and eye landmark detection           |
| NumPy            | Mathematical calculations (EAR, stats)    |
| Streamlit        | Web interface for live visual feedback    |

---

## 🧠 How It Works

FatiguEye uses the **Eye Aspect Ratio (EAR)** to track how open or closed the eyes are across video frames.

**Pipeline overview**:
1. Webcam feed is captured in real-time
2. Face and eyes are detected via Mediapipe
3. EAR is calculated frame-by-frame
4. Eye closure and blink patterns are analyzed
5. Alerts are triggered when drowsiness is detected

---

## 🚀 Getting Started

```bash
git clone https://github.com/Tirovo/fatigueye.git
cd fatigueye
pip install -r requirements.txt
streamlit run app.py
