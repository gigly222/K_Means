import sys
import numpy as np
from K_Means import k_means


# Calculates the sum of squared error for the clusters
def calc_sse(centroids_list, sse_cluster_assignments):
    sse_sum = 0
    for cluster, k in zip(sse_cluster_assignments, centroids_list):  # For each array per cluster assignment
        for data_Point in cluster:
            sse_sum += np.sum((data_Point - k) ** 2)
    return sse_sum

if __name__ == "__main__":

    # check to see if argument input is the right length
    if len(sys.argv) != 3:  # Need to input number of clusters and test data path
        print("Not enough information provided!")
        sys.exit(0)

    # get paths
    num_centroids, input_path = sys.argv[1], sys.argv[2]  # k_means <numberOfClusters> <input-file-name>
    print("Number of Centroids : ", int(num_centroids))

    # get input data
    data = np.genfromtxt(input_path, delimiter='\t', skip_header=1, dtype=float)

    # shuffle data
    X = []
    np.random.shuffle(data)
    for row in data:
        X.append(row[1:])

    # Run k_means and return the final set of centroids and the Cluster Assingments
    centroids, cluster_assignment = k_means(np.array(X), int(num_centroids))

    # Initialize array with 0's equal to the number of centroids. Used arrays for SSE Calculations
    cluster_assignment_array = []
    sse_cluster_assignment_array = []
    for i in range(int(num_centroids)):
        cluster_assignment_array.append([])
        sse_cluster_assignment_array.append([])

    # Get data ready for SSE
    for clusterID, row in zip(cluster_assignment, data):
        cluster_assignment_array[clusterID].append(row[0])
        sse_cluster_assignment_array[clusterID].append(row[1:])

    # Calculate the Sum of Squared Error
    sse = calc_sse(centroids, sse_cluster_assignment_array)
    print("Total SSE : ", sse)  # SSE is 0 when k is equal to the number of data points in the data set (EX: 100)
