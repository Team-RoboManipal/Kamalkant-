from m_2d_keypoints import *
from m_6dof import *
from m_grasp_pointdet import *
from m_object_detection import *
from m_visualization import *



frame_path="/Users/kamal/GripNGrab/ROBOCUP_OBJECTS_2024/train/images/20190501_frame0190_jpg.rf.2483fea8e24bcfda703ed1cc926383c6.jpg"
frame = cv2.imread(frame_path)
frame_ = cv2.imread(frame_path)

#Object Detection
bbox_pred=ObjectDetector("/Users/kamal/gripngrab/best.pt")
detection=bbox_pred.detect_objects(frame_path)
bbox_visual=BBoxVisualizer(frame,detection[0])



for obj in detection[0]:
    object_name = obj.names[obj.boxes.cls[0].item()]
    x1, y1, x2, y2 = map(int, obj.boxes.xyxy[0]) 
    bbox_center = ((x1 + x2) // 2, (y1 + y2) // 2)
    cropped_frame = frame_[y1:y2, x1:x2]
    keypoints_obj=extract_keypoints(cropped_frame,object_name)
    visualize_keypoints(cropped_frame, keypoints_obj, f"Detected Keypoints of {object_name}")
    grasp_points, image=get_grasp_points(frame_,obj.boxes.xyxy[0],object_name)
    success, rvec, tvec,keypoints_2D=compute_6dof_pose(object_name,keypoints_obj,obj)
    bbox_center = ((x1 + x2) // 2, (y1 + y2) // 2)
    draw_3d_pose(frame, rvec, tvec, camera_matrix, dist_coeffs,bbox_center,f"Detected 6DOF pose of {object_name}")

