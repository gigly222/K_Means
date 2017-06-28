import numpy as np
MAX_ITERATIONS = 25


# Get Random Centroids from the data
def randomize_centroids(data, k):
    centroids = []
    centers = data.copy()
    np.random.shuffle(centers)
    for i, row in zip(range(k), centers):
        centroids.append(row)
    return centroids


# Computer KMeans on the data
def k_means(data, K):
    centroids= randomize_centroids(data, K)

    for i in range(MAX_ITERATIONS):
        clusters = np.array([np.argmin([np.dot(x - k, x - k) ** .5 for k in centroids]) for x in data]) #Eucldiean distance is the same as distance = (np.dot(a-b,a-b))**.5, where in our case, a is a row, and b is a centroid.
        centroids = [data[clusters == k].mean(axis = 0) for k in range(K)] #Sum

    return np.array(centroids), clusters