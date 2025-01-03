# Unsupervised learning

# SVM (Support Vector Machine)

Support Vector Machine (SVM) is a powerful supervised machine learning algorithm widely used for classification and regression tasks. It works by finding a hyperplane that best separates the data into different classes in an N-dimensional space (where N is the number of features). SVM is particularly effective in high-dimensional spaces and is known for its robustness in handling linear and non-linear problems.

## Key Concepts

### 1. **Hyperplane**
A hyperplane is a decision boundary that separates data points into classes. In a 2D space, it is a line, while in a 3D space, it is a plane. SVM identifies the hyperplane that maximizes the margin between the nearest data points of each class (support vectors). For datasets with more than three dimensions, the hyperplane becomes a subspace of the feature space.

### 2. **Margin**
The margin is the distance between the hyperplane and the nearest data points of any class. A larger margin indicates better generalization to unseen data. SVM aims to maximize this margin to ensure that the model is not only accurate but also robust to variations in the data.

### 3. **Support Vectors**
Support vectors are the data points closest to the hyperplane. These points are critical in defining the position and orientation of the hyperplane. Removing or changing these points can alter the hyperplane, demonstrating their significance in the SVM algorithm.

### 4. **Kernels**
Kernels allow SVM to handle non-linear separable data by transforming it into a higher-dimensional space. This transformation makes it easier to find a linear boundary in the new space. Common kernel functions include:
   - **Linear Kernel**: Suitable for linearly separable data.
   - **Polynomial Kernel**: Captures interactions between features up to a certain degree.
   - **Radial Basis Function (RBF) Kernel**: Useful for non-linear problems.
   - **Sigmoid Kernel**: Similar to a neural network’s activation function.

### 5. **C Parameter**
The C parameter controls the trade-off between achieving a low error on the training data and maintaining a large margin. A high value of C prioritizes low training error, potentially leading to overfitting, while a low value focuses on a larger margin, which may underfit the data.

### Advantages and Applications
- Effective in high-dimensional spaces.
- Memory efficient since it uses only a subset of the training data.
- Can handle both linear and non-linear problems with the appropriate kernel.
- Applications include text classification, image recognition, bioinformatics (e.g., gene classification), and spam email detection.

---

# PCA (Principal Component Analysis)

Principal Component Analysis (PCA) is an unsupervised dimensionality reduction technique. It transforms the data into a new coordinate system where the axes (principal components) are aligned with the directions of maximum variance. PCA helps simplify complex datasets while retaining as much information as possible.

## Key Steps

### 1. **Standardize the Data**
Since PCA is sensitive to the scale of the data, it is essential to standardize the features to have a mean of 0 and a standard deviation of 1. This ensures that all features contribute equally to the analysis.

### 2. **Covariance Matrix**
Calculate the covariance matrix to understand the relationship between features. The covariance matrix captures how changes in one variable are associated with changes in another.

### 3. **Eigenvalues and Eigenvectors**
Compute eigenvalues and eigenvectors of the covariance matrix. Eigenvectors represent the directions (principal components) of variance, while eigenvalues indicate the amount of variance explained by each component. The eigenvector with the highest eigenvalue represents the principal component.

### 4. **Principal Components**
Select the top k eigenvectors corresponding to the largest eigenvalues to form the principal components. The number of components (k) is usually chosen based on the amount of variance to retain (e.g., 95%).

### 5. **Projection**
Project the original data onto the new subspace defined by the selected principal components. This reduces the dimensionality while preserving the essential patterns in the data.

### Applications
- **Data Visualization**: PCA reduces high-dimensional data to two or three dimensions for visualization.
- **Noise Reduction**: By retaining only significant components, PCA removes noise and redundancy.
- **Preprocessing**: PCA is often a preprocessing step for machine learning algorithms, especially when dealing with large datasets.

### Advantages
- Simplifies complex datasets.
- Reduces computation time for downstream tasks.
- Helps identify patterns and relationships in data.

---

# Decision Trees (Random Forest, Bagging, Boosting)

Decision Trees are hierarchical models used for classification and regression tasks. They split the data into subsets based on feature values, creating a tree-like structure where each path from root to leaf represents a decision rule.

## Key Components

### 1. **Nodes and Splits**
Each internal node represents a decision based on a feature, and branches represent possible outcomes. The splitting criteria are typically chosen to maximize the separation of the data.

### 2. **Leaf Nodes**
Leaf nodes provide the final output or prediction. For classification tasks, they indicate the class label, while for regression, they represent the predicted value.

### 3. **Impurity Measures**
Metrics like Gini Impurity and Entropy are used to determine the quality of splits. Lower impurity means better separation of classes.

## Ensemble Methods

### Random Forest
- Combines multiple decision trees (bagging) to improve accuracy and robustness.
- Reduces overfitting by averaging predictions of individual trees.

### Bagging (Bootstrap Aggregating)
- Trains multiple models on bootstrapped datasets (random subsets with replacement) and aggregates their predictions.
- Increases stability and accuracy.

### Boosting
- Combines weak learners sequentially, where each learner focuses on errors made by the previous one.
- Examples include AdaBoost and Gradient Boosting. Boosting often results in highly accurate models but may be prone to overfitting.

### Applications
- **Fraud Detection**: Identifying anomalous patterns in transactions.
- **Customer Segmentation**: Grouping customers based on behavior.
- **Predictive Modeling**: Forecasting trends and outcomes.

---

# Clustering (K-Means & DBSCAN)

Clustering is an unsupervised learning method to group data points into clusters based on similarity. Unlike supervised methods, clustering does not rely on labeled data.

## K-Means Clustering

### 1. **Algorithm**
1. Initialize k centroids randomly.
2. Assign each data point to the nearest centroid based on distance (e.g., Euclidean).
3. Update centroids by calculating the mean of assigned points.
4. Repeat until centroids stabilize (convergence).

### 2. **Challenges**
- Choosing the value of k (number of clusters).
- Sensitive to outliers and noise.
- May converge to local minima depending on the initialization.

### Advantages
- Simple and easy to implement.
- Works well with spherical clusters.

### Applications
- Customer segmentation.
- Market basket analysis.
- Image compression.

## DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

### 1. **Algorithm**
- Groups points that are closely packed together based on a density threshold (minPts and epsilon).
- Identifies core points (dense areas), border points (edges of clusters), and noise points (outliers).

### 2. **Advantages**
- Can find arbitrarily shaped clusters.
- Robust to noise and outliers.
- Does not require specifying the number of clusters in advance.

### Applications
- **Image Segmentation**: Grouping pixels with similar characteristics.
- **Anomaly Detection**: Identifying unusual patterns in data.
- **Geospatial Data Analysis**: Clustering points on maps.
