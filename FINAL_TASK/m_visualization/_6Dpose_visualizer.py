import cv2
import numpy as np
from copy import copy 


camera_matrix = np.array([[1000, 0, 320],
                              [0, 1000, 240],
                              [0, 0, 1]],
                                dtype=np.float32)

dist_coeffs = np.zeros((4, 1), dtype=np.float32)

def draw_3d_pose(frame, rvec, tvec, camera_matrix, dist_coeffs, bbox_center,window_name):
    """
    Draws a 3D coordinate axis on the detected object to visualize 6DOF pose.
    """
    image=frame.copy()
    axis_length = 50  


    axis_3D = np.array([
        [axis_length, 0, 0],  
        [0, axis_length, 0],  
        [0, 0, axis_length]   
    ], dtype=np.float32)

    # Project the 3D axis points onto the image
    imgpts, _ = cv2.projectPoints(axis_3D, rvec, tvec, camera_matrix, dist_coeffs)
    bbox_center = tuple(map(int, bbox_center))

    # axis lines
    image = cv2.line(image, bbox_center, tuple(imgpts[0].ravel().astype(int)), (0, 0, 255), 3)  # X-axis (Red)
    image = cv2.line(image, bbox_center, tuple(imgpts[1].ravel().astype(int)), (0, 255, 0), 3)  # Y-axis (Green)
    image = cv2.line(image, bbox_center, tuple(imgpts[2].ravel().astype(int)), (255, 0, 0), 3)  # Z-axis (Blue)

    cv2.imshow(window_name, image)
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 800, 600)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return image