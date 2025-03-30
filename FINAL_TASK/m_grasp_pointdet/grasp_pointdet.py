import cv2
import numpy as np
import matplotlib.pyplot as plt

def get_grasp_points(image, bbox,obj):
    """
    Extracts grasp points using Canny edge detection and PCA, focusing only on the object within bbox.
    """
    x1, y1, x2, y2 = map(int, bbox)
    cropped_image = image[y1:y2, x1:x2]
    
    gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 1.4)
    edges = cv2.Canny(blurred, 50, 150)


    fig = plt.figure(figsize=(6, 3))
    fig.canvas.manager.set_window_title(" ")
    plt.title("Canny Edge Detection")
    plt.imshow(edges, cmap='gray')
    plt.axis("off")
    plt.show(block=True)  


    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        print("No contours found!")
        return None, image


    largest_contour = max(contours, key=cv2.contourArea)
    contour_points = largest_contour.reshape(-1, 2)  


    mean, eigenvectors = cv2.PCACompute(contour_points.astype(np.float32), mean=None)


    center = tuple(mean[0].astype(int)) 
    grasp_offset = 20  # Distance from the center to grasp
    minor_axis = eigenvectors[1]  


    grasp_point1 = (int(center[0] + grasp_offset * minor_axis[0]), int(center[1] + grasp_offset * minor_axis[1]))
    grasp_point2 = (int(center[0] - grasp_offset * minor_axis[0]), int(center[1] - grasp_offset * minor_axis[1]))

    # Convert grasp points back to the original image coordinates
    grasp_point1 = (grasp_point1[0] + x1, grasp_point1[1] + y1)
    grasp_point2 = (grasp_point2[0] + x1, grasp_point2[1] + y1)

    grasp_points = np.array([grasp_point1, grasp_point2])


    fig, ax = plt.subplots(figsize=(8, 4))
    fig.canvas.manager.set_window_title(" ")
    ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    ax.scatter(grasp_point1[0], grasp_point1[1], c='r', s=50, label="Grasp Point 1")
    ax.scatter(grasp_point2[0], grasp_point2[1], c='b', s=50, label="Grasp Point 2")
    ax.plot([grasp_point1[0], grasp_point2[0]], [grasp_point1[1], grasp_point2[1]], 'y-', linewidth=2, label="Grasp Line")
    ax.set_title(f"Grasp Points on {obj}")
    ax.legend()
    plt.axis("off")
    plt.show(block=True) 

    return grasp_points, image

