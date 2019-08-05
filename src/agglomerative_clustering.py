import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
import sys
import joblib

def main():
    if len(sys.argv) < 2:
        print('python3 agglomerative_clustering.py genes/cells (optional)linkage_type')
        exit(1)

    type = None
    if sys.argv[1] == 'genes':
        df = pd.read_csv('../data/filtered_data.csv')
        genes = df.iloc[:, 0].values
        data = df.iloc[:, 1:].to_numpy()
        type='genes'
        n_clust = 9
    else:
        df = pd.read_csv('../data/transposed_data.csv')
        data = df.iloc[1:, :].to_numpy()
        type='cells'
        n_clust = 8

    link = 'ward'
    if len(sys.argv) == 3:
        link = sys.argv[2]

    clusters = {}
    mdl = AgglomerativeClustering(n_clusters=n_clust, affinity="euclidean", \
                                    linkage=link).fit(data)

    labels = mdl.labels_
    score = silhouette_score(data, labels, metric='euclidean')

    if type == 'cells':
        for i in range(data.shape[0]):
            cluster_num = mdl.labels_[i]
            if cluster_num not in clusters:
                clusters[cluster_num] = []
            clusters[cluster_num].append(i)
    else:
        for i in range(data.shape[0]):
            cluster_num = mdl.labels_[i]

            if cluster_num not in clusters:
                clusters[cluster_num] = []
            clusters[cluster_num].append(genes[i])

    print('\n' + 'Silhouette score = {}'.format(score) + '\n')
    for i in clusters:
        print("Cluster {}: ".format(i), len(clusters[i]), "\n")

    output = open('../outputs/agglomerative_{}_{}_{}.txt'.format(sys.argv[1], link, n_clust), 'w')
    if type == 'genes':
        for (cluster, genes) in clusters.items():
            output.write('Cluster ID: {}, Size: {} \n'.format(cluster, len(genes)))
            for gene in genes:
                output.write(gene + ', ')
            output.write('\n\n\n')
    else:
        for (cluster, cells) in clusters.items():
            output.write('Cluster ID: {}, Size: {} \n'.format(cluster, len(cells)))
            for cell in cells:
                output.write(str(cell) + ', ')
            output.write('\n\n\n')

    joblib.dump(mdl, '../models/agglomerative_{}.joblib'.format(sys.argv[1]))

if __name__ == '__main__':
    main()
