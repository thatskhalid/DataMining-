import numpy as np
import pandas as pd

class CustomKMeans:
    def __init__(self, k):
        self.k = k
        self.centroids = None
        self.df = None  # Store the DataFrame

    def fit(self, df):
        self.df = df  # Save the DataFrame for later use
        data = df.to_numpy()
        # Initialize centroids randomly from data points
        self.centroids = data[np.random.choice(data.shape[0], self.k, replace=False)]
    
    def predict(self, df):
        distances = self._compute_distances(df.to_numpy())
        return np.argmin(distances, axis=1)  # Return cluster IDs
    
    def sse(self):
        # Compute sum of squared errors (SSE)
        distances = self._compute_distances(self.df.to_numpy())
        min_distances = np.min(distances, axis=1)
        return np.sum(min_distances ** 2)

    def _compute_distances(self, data):
        # Helper to calculate distances from data points to centroids
        return np.linalg.norm(data[:, np.newaxis] - self.centroids, axis=2)

# Example usage:
# kmeans = CustomKMeans(3)
# kmeans.fit(df)
# labels = kmeans.predict(df)
# print("SSE:", kmeans.sse())





