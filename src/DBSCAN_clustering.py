from sklearn.cluster import DBSCAN
import numpy as np
import pandas as pd
import sys

def main():

    eps = 0.5
    minPts = 5
    if len(sys.argv) > 2:
        eps = float(sys.argv[2])
    if len(sys.argv) > 3:
        minPts = int(sys.argv[3])

    if (len(sys.argv) > 1 and sys.argv[1] == 'cells'):
        df = pd.read_csv('../data/transposed_data.csv')
        data = df.iloc[1:, :]
        print('Klasterovanje celija')
    else:
        df = pd.read_csv('../data/filtered_data.csv')
        data = df.iloc[:, 1:]
        print('Klasterovanje gena:\n')

    clusters = {}
    dbscan = DBSCAN(eps=eps, min_samples=minPts).fit(data)

    for i in range(data.shape[0]):
        cluster_num = dbscan.labels_[i]
        if cluster_num not in clusters:
            clusters[cluster_num] = []
        clusters[cluster_num].append(i)

    for i in clusters:
        if i == -1:
            print("Outliers: ", len(clusters[i]), "\n")
        else:
            print("Cluster {}: ".format(i), len(clusters[i]), "\n")

if __name__ == "__main__":
    main()
