import cv2
def visualize_keypoints(frame, keypoints, window_name="Keypoints Visualization"):
    frame_with_keypoints = frame.copy()  
    for (x, y) in keypoints:
        cv2.circle(frame_with_keypoints, (int(x), int(y)), 3, (0, 0, 255), -1)  # Red dots

    cv2.imshow(window_name, frame_with_keypoints)
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 800, 600)
    cv2.waitKey(0)
    cv2.destroyAllWindows()