class BlinkingMonitor:
    def __init__(self, ear_threshold=0.23, blink_frames=2, fatigue_frames=8):
        self.ear_threshold = ear_threshold
        self.blink_frames = blink_frames
        self.fatigue_frames = fatigue_frames

        self.blink_counter = 0
        self.total_blinks = 0
        self.fatigue_alert = False

    def update(self, avg_ear):
        if avg_ear < self.ear_threshold:
            self.blink_counter += 1

            if self.blink_counter >= self.fatigue_frames:
                self.fatigue_alert = True
        else:
            if self.blink_counter >= self.blink_frames:
                self.total_blinks += 1
            self.blink_counter = 0
            self.fatigue_alert = False

        return self.total_blinks, self.fatigue_alert
