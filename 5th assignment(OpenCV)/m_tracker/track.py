import pickle
import os
import cv2
import numpy as np
import math

def progress_bar(progress, total, bar_length=50, task=' '):
    percent = (progress / float(total)) * 100
    filled_length = int(bar_length * progress // total)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f'{task}: \r|{bar}| {percent:.2f}%', end='\r')

    if progress == total:
        print()

class Tracker:
    def __init__(self, dnn_model, dnn_weights, class_names_file):
        with open(class_names_file, 'r') as f:
            self.class_names = f.read().strip().split('\n')
        self.model = cv2.dnn.readNet(dnn_weights, dnn_model)
        layer_names = self.model.getLayerNames()
        self.output_layers = [layer_names[i - 1] for i in self.model.getUnconnectedOutLayers()]

    def detect(self, frames):
        print("Detecting!!")
        detections = []
        for frame_index, frame in enumerate(frames):
            detections.append([])
            image_height, image_width, _ = frame.shape
            blob = cv2.dnn.blobFromImage(frame, scalefactor=1 / 255.0, size=(416, 416), swapRB=True, crop=False)
            self.model.setInput(blob)
            outputs = self.model.forward(self.output_layers)
            # Separating outputs
            boxes = []
            confidences = []
            class_ids = []
            centers = []
            for output in outputs:
                for detection in output:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.5:
                        # Rescaling
                        center_x = int(detection[0] * image_width)
                        center_y = int(detection[1] * image_height)
                        w = int(detection[2] * image_width)
                        h = int(detection[3] * image_height)
                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)

                        if w>0 and h>0:
                            boxes.append([x, y, w, h])
                            confidences.append(float(confidence))
                            class_ids.append(class_id)
                            centers.append((center_x, center_y))
            indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
            if len(indices) > 0:
                for i in indices.flatten():
                    detections[frame_index].append([class_ids[i], boxes[i], centers[i]])

            progress_bar(frame_index + 1, len(frames))
        
        return detections

    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def get_object_track(self, frames, read_from_file=False, file_path='tracks_storage/tracks.pkl'):
        if read_from_file and file_path and os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                tracks = pickle.load(f)
            return tracks

        detections = self.detect(frames)
        print("Tracking")
        tracks = {'players': [], 'referees': [], 'ball': []}
        tracking_objects = {}  # {object_id: [(x_center, y_center), disappeared_frames]}
        player_id_count = 1
        max_disappeared = 5

        

        for frame_no, detection in enumerate(detections):
            non_player_count = 0
            player_count = 0
            current_object = {}

            tracks['players'].append({})
            tracks['referees'].append({})
            tracks['ball'].append({})


            for obj in detection:
                class_id, box, centers = obj
                x, y, w, h = box
                x_center, y_center = centers
                bbox = [x, y, x + w, y + h]

                # Convert Goalkeepers to players
                if class_id == 1:
                    class_id = 2

                # Handle non-player classes
                if class_id == 3:  # Referees
                    non_player_count += 1
                    tracks['referees'][frame_no][non_player_count] = bbox
                elif class_id == 0:  # Ball
                    non_player_count += 1
                    tracks['ball'][frame_no][non_player_count] = bbox
                elif class_id == 2:  # Players
                    current_object[player_count] = (x_center, y_center, bbox)
                    player_count += 1

            updated_tracking_object = {}
            for player_id, (prev_centroid, disappeared_frames) in tracking_objects.items():
                matched = False
                for idx, (x_c, y_c, bbox) in current_object.items():
                    dist = self.distance(prev_centroid[0], prev_centroid[1], x_c, y_c)
                    if dist < 50:
                        updated_tracking_object[player_id] = [(x_c, y_c), 0]
                        tracks['players'][frame_no][player_id] = bbox
                        del current_object[idx]
                        matched = True
                        break
                if not matched:
                    if disappeared_frames + 1 < max_disappeared:
                        updated_tracking_object[player_id] = [prev_centroid, disappeared_frames + 1]

            for _, (xc, yc, bbox) in current_object.items():
                updated_tracking_object[player_id_count] = [(xc, yc), 0]
                tracks['players'][frame_no][player_id_count] = bbox
                player_id_count += 1

            tracking_objects = updated_tracking_object

            

            progress_bar(frame_no + 1, len(detections))

        
        # Save tracks to file
        with open(file_path, 'wb') as f:
            pickle.dump(tracks, f)

        return tracks

