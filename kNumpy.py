import numpy as np

data = np.genfromtxt("0.txt", delimiter=' ') #read data from txt


def kNumpy(k):
    nRow = data.shape[0]
    nCol = data.shape[1]
    rep = 100

    cluster = np.random.randint(low=0, high=k, size=nRow) #randomly initialized array

    centroids = np.random.uniform(low=0, high=1, size=(k, nCol))
    centroids = centroids * (np.max(data) - np.min(data)) + np.min(data)

    for i in range(rep):
        distances = np.array(
            [np.linalg.norm(data - c, axis=1) for c in centroids]) #disltance between datapoint and centroids

        new_cluster = np.argmin(distances, axis=0)

        if (cluster == new_cluster).all():
            cluster = new_cluster
            out_file.write('Clusters Unchanged.' + "\n")
            break
        else:

            difference = np.mean(cluster != new_cluster)
            out_file.write('%4f%% clusters changed' % (difference * 100) + "\n")
            cluster = new_cluster
            for c in range(k):
                centroids[c] = np.mean(data[cluster == c], axis=0)
    return cluster, centroids


def silhoutte(centroids):  # calculateSC function with parameters
    s = 0
    y = []
    for i in range(len(centroids)):  # go through each instance of clusters
        for j in range(len(centroids[i])):
            x_val = data[centroids[i][j]][2]
            y_val = data[centroids[i][j]][3]
            d = 0
            for l in range(len(centroids[i])):
                dist1 = ((data[centroids[i][j]][2] - data[centroids[i][l]][2]) ** 2)
                dist2 = ((data[centroids[i][j]][3] - data[centroids[i][l]][3]) ** 2)
                eud = (dist1 + dist2) ** .5
                d += eud
            a = d / (len(centroids[i]) - 1)
            b_vals = []
    for m in range(len(centroids)):
        if m == i:
            continue
            c = 0
            for j in range(len(centroids[m])):
                dist3 = ((x_val - data[centroids[m][j]][2]) ** 2)
                dist4 = ((y_val - data[centroids[m][j]][3]) ** 2)
                eu = (dist3 + dist4) ** .5
                c += eu
                avg = float(c / len(centroids[m]))
                b_vals.append(avg)
                b = min(b_vals)
        s = float((b - a) / max(a, b))  # after calculation, s is the silhoutte coefficient for one centroid
    return s  # returns the silhoutte coefficient


def distance(dist1, dist2):  # distance function to calculate the euclidean distance easier
    x = [(a - b) ** 2 for a, b in zip(dist1, dist2)]
    y = np.sqrt(float(sum(x)))


with open("kNumpy.txt", "w") as out_file:
    out_file.write(str(kNumpy(1)) + "\n")
    out_file.write(str(kNumpy(2)) + "\n")
    out_file.write(str(kNumpy(3)) + "\n")
    out_file.write(str(kNumpy(4)) + "\n")
  
