# 6DOF Pose Estimation using 2D-3D Keypoint Matching and PnP

## 📌 Overview
This module estimates the **6 Degrees of Freedom (6DOF) pose** of an object using **2D keypoints detected in an image** and **3D keypoints from a known object model**. The core process consists of:

1. **Matching 2D and 3D keypoints** using the **Hungarian Algorithm**.
2. **Estimating the object's pose** using a **custom PnP (Perspective-n-Point) solver**.
3. **Returning the rotation (rvec) and translation (tvec)** of the object in 3D space.


## 🚀 How It Works
### 1️⃣ Match Keypoints using the Hungarian Algorithm
👉 **Function: `match_keypoints_hungarian()`**

**Purpose:**
- Matches **2D keypoints (from image detection)** to **3D keypoints (from object model)**.
- Uses the **Hungarian Algorithm** to find the best pairings based on **Euclidean distance**.

**Process:**
1. Compute a **cost matrix**, where each value represents the distance between a 2D and a 3D keypoint.
2. Use **`scipy.optimize.linear_sum_assignment`** to solve the **assignment problem** optimally.
3. Optionally, filter out matches that exceed a `cost_threshold`.

### 2️⃣ Custom SolvePnP Implementation
👉 **Function: `custom_solve_pnp()`**

**Purpose:**
- Computes the **rotation (rvec)** and **translation (tvec)** of the object using **nonlinear optimization**.

**Process:**
1. Define an **error function** that measures how close the projected 3D points are to the detected 2D points.
2. Use the **Levenberg-Marquardt (LM) optimization** algorithm to minimize the error.
3. Convert the rotation vector (`rvec`) to a rotation matrix (`R`) and apply perspective projection.
4. Solve for `rvec` and `tvec` iteratively until convergence.

📌 **Mathematical Background:**
- The **projection equation** used:
  
  $$
  \begin{bmatrix} u \\ v \end{bmatrix} = K \cdot \left( R \cdot X + T \right)
  $$
  
  Where:
  - \( K \) is the camera intrinsic matrix.
  - \( R \) is the rotation matrix (converted from `rvec`).
  - \( T \) is the translation vector.
  - \( X \) is the 3D point.
  - \( (u, v) \) is the projected 2D coordinate.

- **Error function:**
  - Compute the difference between projected 2D points and detected 2D points.
  - Minimize this difference using **least squares optimization**.

### 3️⃣ Compute 6DOF Pose
👉 **Function: `compute_6dof_pose()`**

**Purpose:**
- Runs the entire pipeline to estimate the object's **final pose**.

**Process:**
1. Extract **2D keypoints** from keypoint detections.
2. Retrieve the **corresponding 3D keypoints** from the object model.
3. **Match keypoints** using `match_keypoints_hungarian()`.
4. Run `custom_solve_pnp()` to estimate the **pose**.
5. Return **rotation (rvec) and translation (tvec)**.

## 📊 Results
The output of this pipeline includes:
- **Rotation vector (`rvec`)**: Defines how the object is rotated in 3D.
- **Translation vector (`tvec`)**: Defines the object's position in 3D space.
- **Matched keypoints**: The final matched 2D-3D keypoints used for pose estimation.



