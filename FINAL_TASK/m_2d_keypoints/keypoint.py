import cv2
import numpy as np
import matplotlib.pyplot as plt

def extract_corner_points(image, min_contour_length=50, max_corners=10, epsilon_factor=0.02):

    def process_corners(epsilon_factor, min_contour_length):

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 1.4)
        edges = cv2.Canny(blurred, 50, 150)


        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            return np.array([]), edges  

        contour_scores = [(contour, cv2.arcLength(contour, closed=True)) for contour in contours]
        sorted_contours = sorted(contour_scores, key=lambda x: x[1], reverse=True)
        filtered_contours = [contour[0] for contour in sorted_contours if contour[1] > min_contour_length]


        corner_points = []
        for contour in filtered_contours:
            epsilon = epsilon_factor * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            for point in approx:
                corner_points.append(point[0])  

        return np.array(corner_points, dtype=np.float32), edges


    corner_points, edges = process_corners(epsilon_factor, min_contour_length)


    attempts = 0
    while len(corner_points) < 4 and attempts < 3:
        epsilon_factor *= 0.8  
        min_contour_length *= 0.7  
        corner_points, edges = process_corners(epsilon_factor, min_contour_length)
        attempts += 1


    if len(corner_points) < 4:
        print(f"error: Only {len(corner_points)} keypoints found! Repeating points to meet requirement.")
        while len(corner_points) < 4:
            corner_points = np.vstack([corner_points, corner_points[:1]]) 
    
    if len(corner_points) > max_corners:
        corner_points = corner_points[:max_corners]

    return corner_points

def extract_keypoints(frame,obj):
    return extract_corner_points(frame)