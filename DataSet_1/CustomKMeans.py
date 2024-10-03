import numpy as np

class CustomKMeans:
    def __init__(self, k):
        self.k = k
        self.centroids = None
        self.labels = None
    
    def fit(self, df):
        # Step 1: Initialize centroids randomly from the data
        self.centroids = df.sample(n=self.k).values

        for _ in range(100):  # Maximum number of iterations
            # Step 2: Assign clusters based on the closest centroid
            distances = self._calculate_distances(df.values)
            self.labels = np.argmin(distances, axis=1)

            new_centroids = []
            for i in range(self.k):
                points_in_cluster = df.values[self.labels == i]
                if len(points_in_cluster) == 0:
                    # Reinitialize centroid if no points are assigned
                    new_centroids.append(df.sample(n=1).values[0])
                else:
                    # Calculate new centroid as the mean of assigned points
                    new_centroids.append(points_in_cluster.mean(axis=0))

            new_centroids = np.array(new_centroids)

            # Step 4: Check for convergence
            if np.all(new_centroids == self.centroids):
                break

            self.centroids = new_centroids
    
    def _calculate_distances(self, points):
        # Calculate the distance between points and centroids
        return np.linalg.norm(points[:, np.newaxis] - self.centroids, axis=2)

    def sse(self, df):
        # Calculate the sum of squared errors (SSE) for the current clustering
        sse = 0
        for i in range(self.k):
            points_in_cluster = df.values[self.labels == i]  # Filter data points, not centroids
            if len(points_in_cluster) > 0:
                distances = np.linalg.norm(points_in_cluster - self.centroids[i], axis=1)
                sse += np.sum(distances ** 2)
        return sse





