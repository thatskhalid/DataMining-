import cleaning  # Import cleaning module
from CustomKMeans import CustomKMeans  # Import custom KMeans class
import matplotlib.pyplot as plt

def main():
    # Step 1: Clean and visualize data
    file_path = 'DataSet_1/car_prices.csv'
    df = cleaning.clean_and_visualize(file_path)  # Clean data using function from cleaning.py

    # Step 2: Select relevant columns for clustering
    selected_columns = df[['odometer', 'year', 'sellingprice']]  # Adjust columns as necessary
    

    # Step 3: Run Custom KMeans algorithm and plot SSE for different k values
    sse_values = []
    k_values = range(1, 11)  # Test k from 1 to 10

    for k in k_values:
        kmeans = CustomKMeans(k)
        kmeans.fit(selected_columns)
        sse_values.append(kmeans.sse(selected_columns))  # Pass the DataFrame to sse()

    # Step 4: Plot SSE vs k to determine the optimal number of clusters
    plt.plot(k_values, sse_values, marker='o')
    plt.title('SSE vs. k')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('Sum of Squared Errors (SSE)')
    plt.show()

if __name__ == '__main__':
    main()



