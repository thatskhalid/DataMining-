import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from CustomKMeans import CustomKMeans  # Assuming your CustomKMeans is saved in CustomKMeans.py

# Load the data
df = pd.read_csv('data/cleaned/cleaned_data.csv')

# Select relevant columns for clustering
cluster_df = df[['condition', 'odometer', 'mmr', 'sellingprice']].dropna()

# Step 1: Try several k values using your CustomKMeans
for k in range(2, 6):  # Trying k = 2 to 5
    custom_kmeans = CustomKMeans(k)
    custom_kmeans.fit(cluster_df)
    print(f"Custom KMeans - k={k}, SSE: {custom_kmeans.sse()}")

# Step 2: Compare with sklearn's KMeans
for k in range(2, 6):  # Same k values
    sklearn_kmeans = KMeans(n_clusters=k, random_state=42).fit(cluster_df)
    sse = sklearn_kmeans.inertia_
    print(f"Sklearn KMeans - k={k}, SSE: {sse}")

    # Print cluster centers for comparison
    print(f"Cluster Centers (k={k}):\n", sklearn_kmeans.cluster_centers_)

# Step 3: Choose the best k value
# Here, you could choose k by looking at the "elbow" in SSE values.

