import cv2
from tracking.eye_detector import FaceMeshDetector
from tracking.ear import compute_EAR
from tracking.blinking_monitor import BlinkingMonitor
import winsound


# Eye landmark indices from Mediapipe
RIGHT_EYE_IDX = [33, 160, 158, 133, 153, 144]
LEFT_EYE_IDX  = [263, 387, 385, 362, 380, 373]

detector = FaceMeshDetector()
blinking_monitor = BlinkingMonitor()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    landmarks = detector.get_landmarks(frame)

    if landmarks:
        # Eye landmark retrieval
        right_eye_pts = [landmarks[i] for i in RIGHT_EYE_IDX]
        left_eye_pts = [landmarks[i] for i in LEFT_EYE_IDX]

        # Draw eye landmarks
        for (x, y) in right_eye_pts:
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
        for (x, y) in left_eye_pts:
            cv2.circle(frame, (x, y), 2, (255, 0, 0), -1)

        # Medium EAR
        right_ear = compute_EAR(right_eye_pts)
        left_ear = compute_EAR(left_eye_pts)
        avg_ear = (right_ear + left_ear) / 2.0

        # Blinking and fatigue updates
        total_blinks, fatigue_alert = blinking_monitor.update(avg_ear)

        # Display
        cv2.putText(frame, f"EAR: {avg_ear:.2f}", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(frame, f"Blinks: {total_blinks}", (30, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)
        if fatigue_alert:
            cv2.putText(frame, "⚠️ FATIGUE DETECTED", (30, 130),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            winsound.Beep(1500, 1000)


    else:
        cv2.putText(frame, "No face detected", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Video
    cv2.imshow("FatiguEye", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
