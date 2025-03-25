# EAR means Eye Aspect Ratio

import numpy as np

def euclidean_dist(pt1, pt2):
    return np.linalg.norm(np.array(pt1) - np.array(pt2))

def compute_EAR(eye_landmarks):
    A = euclidean_dist(eye_landmarks[1], eye_landmarks[5])
    B = euclidean_dist(eye_landmarks[2], eye_landmarks[4])
    C = euclidean_dist(eye_landmarks[0], eye_landmarks[3])
    ear = (A + B) / (2.0 * C)
    return ear
