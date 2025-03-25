import streamlit as st
import cv2
import numpy as np
import pandas as pd
from PIL import Image
import time
from collections import deque
import winsound
from tracking.eye_detector import FaceMeshDetector
from tracking.ear import compute_EAR
from tracking.blinking_monitor import BlinkingMonitor

# Config Streamlit
st.set_page_config(page_title="FatiguEye", layout="wide")
st.title("😴 FatiguEye – Real-time Eye Fatigue Detection")

# Eye landmark indices from Mediapipe
RIGHT_EYE_IDX = [33, 160, 158, 133, 153, 144]
LEFT_EYE_IDX = [263, 387, 385, 362, 380, 373]

detector = FaceMeshDetector()
monitor = BlinkingMonitor()

# Streamlit session state
if "run_app" not in st.session_state:
    st.session_state.run_app = False
if "ear_df" not in st.session_state:
    st.session_state.ear_df = pd.DataFrame(columns=["EAR"])

# Start/Stop
start_col, stop_col = st.columns(2)
if start_col.button("▶️ Start", key="start_btn"):
    st.session_state.run_app = True
if stop_col.button("❌ Stop", key="stop_btn"):
    st.session_state.run_app = False

# Layout
video_placeholder = st.empty()
stats_col, graph_col = st.columns(2)
ear_display = stats_col.empty()
blink_display = stats_col.empty()
alert_display = stats_col.empty()

# Initial chart
ear_chart = graph_col.line_chart(st.session_state.ear_df, y="EAR", use_container_width=True)

# Webcam
cap = cv2.VideoCapture(0)

if st.session_state.run_app:
    while st.session_state.run_app:
        ret, frame = cap.read()
        if not ret:
            st.warning("No camera feed.")
            break

        frame = cv2.flip(frame, 1)
        landmarks = detector.get_landmarks(frame)

        if landmarks:
            right_eye_pts = [landmarks[i] for i in RIGHT_EYE_IDX]
            left_eye_pts = [landmarks[i] for i in LEFT_EYE_IDX]

            right_ear = compute_EAR(right_eye_pts)
            left_ear = compute_EAR(left_eye_pts)
            avg_ear = (right_ear + left_ear) / 2.0

            # EAR logs and update chart
            st.session_state.ear_df.loc[len(st.session_state.ear_df)] = [avg_ear]
            ear_chart.add_rows(st.session_state.ear_df.tail(1))

            total_blinks, fatigue_alert = monitor.update(avg_ear)

            # Values display
            ear_display.metric("EAR", f"{avg_ear:.2f}")
            blink_display.metric("Total Blinks", f"{total_blinks}")
            if fatigue_alert:
                alert_display.error("⚠️ Fatigue Detected")
                winsound.Beep(1500, 1000)

            else:
                alert_display.success("No Fatigue")

            # Draw eye landmarks
            for (x, y) in right_eye_pts + left_eye_pts:
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        # Webcam display
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        video_placeholder.image(Image.fromarray(frame_rgb), channels="RGB")

        time.sleep(0.03)

cap.release()
st.info("Click ▶️ Start to begin.")
