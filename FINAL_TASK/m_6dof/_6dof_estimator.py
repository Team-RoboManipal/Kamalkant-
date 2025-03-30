##3D-data extracted form rulebook
object_3D_keypoints = {
    # 1️⃣ Allen Key (L-shaped)
    0: "AllenKey",
    "AllenKey": [
        (0, 0, 0),        # Bend corner
        (0, 0, 50),       # Short end tip
        (0, 30, 50),      # Long end bend
        (0, 30, 100)      # Long end tip
    ],

    # 2️⃣ Axis2 (Cylindrical, 68mm long, 17mm diameter)
    1: "Axis2",
    "Axis2": [
        (0, 0, 0),        # Center base
        (0, 0, 68),       # Center top
        (-8.5, 0, 0),     # Left edge base
        (8.5, 0, 0),      # Right edge base
        (-8.5, 0, 68),    # Left edge top
        (8.5, 0, 68)      # Right edge top
    ],

    # 3️⃣ Bearing2 (Circular, Outer Diameter = 25mm)
    2: "Bearing2",
    "Bearing2": [
        (0, 0, 0),         # Center
        (-12.5, 0, 0),     # Left edge
        (12.5, 0, 0),      # Right edge
        (0, -12.5, 0),     # Top edge
        (0, 12.5, 0)       # Bottom edge
    ],

    # 4️⃣ Drill (Handle, Chuck)
    3: "Drill",
    "Drill": [
        (0, 0, 0),         # Handle base
        (50, 0, 0),        # Middle of handle
        (100, 0, 0),       # Drill chuck tip
        (75, 20, 0),       # Side grip
        (75, -20, 0)       # Opposite side
    ],

    # 5️⃣ F20_20_B (Box-like)
    4: "F20_20_B",
    "F20_20_B": [
        (0, 0, 0),        # Bottom-left-front
        (20, 0, 0),       # Bottom-right-front
        (20, 20, 0),      # Top-right-front
        (0, 20, 0),       # Top-left-front
        (0, 0, 20),       # Bottom-left-back
        (20, 0, 20)       # Bottom-right-back
    ],

    # 6️⃣ F20_20_G (Same as F20_20_B)
    5: "F20_20_G",
    "F20_20_G": [
        (0, 0, 0), (20, 0, 0), (20, 20, 0), (0, 20, 0), (0, 0, 20), (20, 0, 20)
    ],

    # 7️⃣ Housing (Box-like, 70x30x40mm)
    6: "Housing",
    "Housing": [
        (0, 0, 0), (70, 0, 0), (70, 30, 0), (0, 30, 0), (0, 0, 40), (70, 0, 40)
    ],

    # 8️⃣ M20 (Cylindrical, 20mm diameter)
    7: "M20",
    "M20": [
        (0, 0, 0), (0, 0, 20), (-10, 0, 0), (10, 0, 0), (-10, 0, 20), (10, 0, 20)
    ],

    # 9️⃣ M20_100 (Longer version of M20)
    8: "M20_100",
    "M20_100": [
        (0, 0, 0), (0, 0, 100), (-10, 0, 0), (10, 0, 0), (-10, 0, 100), (10, 0, 100)
    ],

    # 🔟 M30 (Cylindrical, 30mm diameter)
    9: "M30",
    "M30": [
        (0, 0, 0), (0, 0, 30), (-15, 0, 0), (15, 0, 0), (-15, 0, 30), (15, 0, 30)
    ],

    # 1️⃣1️⃣ Motor2 (66.7x42mm)
    10: "Motor2",
    "Motor2": [
        (0, 0, 0), (0, 0, 66.7), (-21, 0, 0), (21, 0, 0), (-21, 0, 66.7), (21, 0, 66.7)
    ],

    # 1️⃣2️⃣ S40_40_B (Box)
    11: "S40_40_B",
    "S40_40_B":[
    (0, 0, 40),     # Bottom-left corner
    (40, 0, 40),    # Bottom-right corner
    (40, 100, 40),  # Top-right corner
    (0, 100, 40)    # Top-left corner
],

    # 1️⃣3️⃣ S40_40_G (Same as S40_40_B)
    12: "S40_40_G",
    "S40_40_G": [
    (0, 0, 40),     # Bottom-left corner
    (40, 0, 40),    # Bottom-right corner
    (40, 100, 40),  # Top-right corner
    (0, 100, 40)    # Top-left corner
],

    # 1️⃣4️⃣ Screwdriver (Handle + Shaft)
    13: "Screwdriver",
    "Screwdriver": [
        (0, 0, 0), (50, 0, 0), (120, 0, 0), (75, 10, 0), (75, -10, 0)
    ],

    # 1️⃣5️⃣ Spacer (Cylinder, 30mm diameter)
    14: "Spacer",
    "Spacer": [
        (0, 0, 0), (0, 0, 70), (-15, 0, 0), (15, 0, 0), (-15, 0, 70), (15, 0, 70)
    ],

    # 1️⃣6️⃣ Wrench (Handle + Head)
    15: "Wrench",
    "Wrench": [
        (0, 0, 0), (150, 0, 0), (75, 10, 0), (150, 30, 0), (150, -30, 0)
    ],

    # 1️⃣7️⃣ Container Box Blue (Box, 100x50x50mm)
    16: "container_box_blue",
    "container_box_blue": [
        (0, 0, 0), (100, 0, 0), (100, 50, 0), (0, 50, 0), (0, 0, 50), (100, 0, 50)
    ],

    # 1️⃣8️⃣ Container Box Red (Same as Blue)
    17: "container_box_red",
    "container_box_red": [
        (0, 0, 0), (100, 0, 0), (100, 50, 0), (0, 50, 0), (0, 0, 50), (100, 0, 50)
    ]
}

import cv2
import numpy as np
from scipy.optimize import linear_sum_assignment


camera_matrix = np.array([
    [1200, 0, 320],  # fx, 0, cx
    [0, 1200, 240],  # 0, fy, cy
    [0, 0, 1]        # 0,  0,  1
], dtype=np.float32)
dist_coeffs = np.zeros((4,1))  # Assuming no distortion


def match_keypoints_hungarian(keypoints_2D, keypoints_3D, cost_threshold=None):
    """
    Matches 2D image keypoints to 3D object keypoints using the Hungarian Algorithm.
    Only returns pairs that form the optimal assignment.
    """
    num_2D = keypoints_2D.shape[0]
    num_3D = keypoints_3D.shape[0]
    
    # Compute cost matrix based on Euclidean distance between 2D keypoints and 
    # the first two coordinates of 3D keypoints.
    cost_matrix = np.zeros((num_2D, num_3D), dtype=np.float32)
    for i in range(num_2D):
        for j in range(num_3D):
            cost_matrix[i, j] = np.linalg.norm(keypoints_2D[i] - keypoints_3D[j, :2])
    
    # Solve the assignment problem using the Hungarian algorithm.
    row_indices, col_indices = linear_sum_assignment(cost_matrix)
    
    # Optionally filter out matches with high cost.
    if cost_threshold is not None:
        valid_matches = cost_matrix[row_indices, col_indices] < cost_threshold
        row_indices = row_indices[valid_matches]
        col_indices = col_indices[valid_matches]
    
    matched_2D = keypoints_2D[row_indices]
    matched_3D = keypoints_3D[col_indices]
    
    return matched_2D, matched_3D


def custom_solve_pnp(points_3d, points_2d, camera_matrix, dist_coeffs):
    """
    Custom PnP solver using optimization approach
    """
    from scipy.optimize import least_squares
    import numpy as np
    
    def project_points(params):
        rvec = params[:3]
        tvec = params[3:]
        

        R, _ = cv2.Rodrigues(rvec)
        
        # Project 3D points to 2D
        projected_points = []
        for p3d in points_3d:
            # Apply rotation and translation
            p = R @ p3d.reshape(3,1) + tvec.reshape(3,1)
            

            if abs(p[2,0]) < 1e-10:  
                p[2,0] = 1e-10
                

            x = p[0,0] / p[2,0]
            y = p[1,0] / p[2,0]
            

            u = camera_matrix[0,0] * x + camera_matrix[0,2]
            v = camera_matrix[1,1] * y + camera_matrix[1,2]
            
            projected_points.append([u,v])
            
        return np.array(projected_points).reshape(-1) - points_2d.reshape(-1)
    
    # Better initial guess using direct linear estimation
    # Use the centroid of points as initial translation
    centroid_3d = np.mean(points_3d, axis=0)
    centroid_2d = np.mean(points_2d, axis=0)
    
    # Initial guess for translation using the centroids
    z_init = np.mean(np.linalg.norm(points_3d - centroid_3d, axis=1)) * 2  # Rough depth estimate
    x_init = (centroid_2d[0] - camera_matrix[0,2]) * z_init / camera_matrix[0,0]
    y_init = (centroid_2d[1] - camera_matrix[1,2]) * z_init / camera_matrix[1,1]
    
    params0 = np.zeros(6) 
    params0[3:] = [x_init, y_init, z_init]  # Initial translation
    
    try:
        # Optimize using Levenberg-Marquardt with bounds
        bounds = ([-np.pi, -np.pi, -np.pi, -1000, -1000, 0],  
                 [np.pi, np.pi, np.pi, 1000, 1000, 5000])     
        
        result = least_squares(project_points, params0, 
                             method='trf',  
                             bounds=bounds,
                             loss='huber')  
        
        success = result.success
        
        if success:
            rvec = result.x[:3].reshape(3,1).astype(np.float32)
            tvec = result.x[3:].reshape(3,1).astype(np.float32)
            return success, rvec, tvec
            
    except Exception as e:
        print(f"Custom PnP solver failed: {e}")
        
    return False, None, None


def compute_6dof_pose(object_name, keypoints_obj, obj):
    x1, y1, x2, y2 = map(int, obj.boxes.xyxy[0])
    keypoints_2D = [(kp[0] + x1, kp[1] + y1) for kp in keypoints_obj]
    keypoints_3D = object_3D_keypoints.get(object_name, [])

   
    if len(keypoints_2D) < 4:
        print("Not enough 2D keypoints")
        return False, None, None, keypoints_2D  
    

    keypoints_3D = np.array(keypoints_3D, dtype=np.float32).reshape(-1, 3)  # Ensure (N,3) shape
    keypoints_2D = np.array(keypoints_2D, dtype=np.float32).reshape(-1, 2)  # Ensure (N,2) shape

    # Match 2D and 3D Keypoints Using Hungarian Algorithm
    keypoints_2D, keypoints_3D = match_keypoints_hungarian(keypoints_2D, keypoints_3D)


    try:
        success = False
        if len(keypoints_2D) >= 4:  
            success, rvec, tvec = custom_solve_pnp(
                keypoints_3D, 
                keypoints_2D,
                camera_matrix, 
                dist_coeffs
            )

    except Exception as e:
        print("PnP solver Error:", e)
        return False, None, None, keypoints_2D 


    if not success:
        print("PnP failed to estimate the pose!")
        return False, None, None, keypoints_2D


    return success, rvec, tvec, keypoints_2D
