import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
import sys

def main():
    if len(sys.argv) < 2:
        print('python3 agglomerative_clustering.py genes/cells linkage_type(optional)')
        exit(1)

    if sys.argv[1] == 'genes':
        df = pd.read_csv('../data/filtered_data.csv')
        genes = df.iloc[:, 0].values
        data = df.iloc[:, 1:].to_numpy()
        n_clust = 9
    else:
        df = pd.read_csv('../data/transposed_data.csv')
        data = df.iloc[1:, :].to_numpy()
        n_clust = 8

    link = 'ward'
    if len(sys.argv) == 3:
        link = sys.argv[2]

    clusters = {}
    mdl = AgglomerativeClustering(n_clusters=n_clust, affinity="euclidean", \
                                    linkage=link).fit(data)

    for i in range(data.shape[0]):
        cluster_num = mdl.labels_[i]

        if cluster_num not in clusters:
            clusters[cluster_num] = []
        clusters[cluster_num].append(i)

    for i in clusters:
        print("Cluster {}: ". format(i), len(clusters[i]))
        print()

if __name__ == '__main__':
    main()
