from ultralytics import YOLO

class ObjectDetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect_objects(self, image_path):
        results = self.model(image_path)
        return results