import mediapipe as mp
import cv2

mp_face_mesh = mp.solutions.face_mesh

class FaceMeshDetector:
    def __init__(self, static_image_mode=False, max_faces=1, detection_confidence=0.5, tracking_confidence=0.5):
        self.face_mesh = mp_face_mesh.FaceMesh(
            static_image_mode=static_image_mode,
            max_num_faces=max_faces,
            refine_landmarks=True,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )
        self.drawing_spec = mp.solutions.drawing_utils.DrawingSpec(thickness=1, circle_radius=1)

    def get_landmarks(self, image):
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb)

        if not results.multi_face_landmarks:
            return None

        landmarks = results.multi_face_landmarks[0]
        h, w, _ = image.shape
        return [(int(lm.x * w), int(lm.y * h)) for lm in landmarks.landmark]
