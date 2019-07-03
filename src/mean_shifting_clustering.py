from sklearn.cluster import MeanShift
import numpy as np
import sys
import pandas as pd
import math

def main():
    if len(sys.argv) != 2:
        print('python3 mean_shifting_clustering.py genes/cells')
        exit(1)

    if sys.argv[1] == 'genes':
        df = pd.read_csv('../data/filtered_data.csv')
        data = df.iloc[:, 1:]
        print('Klasterovanje gena:\n')
    else:
        df = pd.read_csv('../data/transposed_data.csv')
        data = df.iloc[1:, :]
        print('Klasterovanje celija')

    clusters = {}
    ms = MeanShift().fit(data)

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

if __name__ == '__main__':
    main()
