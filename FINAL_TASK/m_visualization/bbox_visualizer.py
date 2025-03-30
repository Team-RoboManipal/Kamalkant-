import cv2
import numpy as np
from copy import copy

class BBoxVisualizer:
    def __init__(self, frame, detections):
        self.frame = frame.copy()
        self.detections = detections
        self.names = detections.names  
        self.draw_bboxes()
        self.show_frame()

    def draw_bboxes(self):
        boxes = self.detections.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].cpu().numpy())  
            label_id = int(box.cls[0].cpu().numpy()) 
            confidence = float(box.conf[0].cpu().numpy()) 
            label = self.names[label_id]
            cv2.rectangle(self.frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            text = f"{label}: {confidence:.2f}"
            cv2.putText(self.frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    def show_frame(self):
        cv2.imshow('Frame', self.frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()