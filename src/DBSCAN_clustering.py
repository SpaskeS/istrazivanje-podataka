from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
import numpy as np
import pandas as pd
import sys
import joblib

def main():

    type = None
    if (len(sys.argv) > 1 and sys.argv[1] == 'cells'):
        df = pd.read_csv('../data/transposed_data.csv')
        data = df.iloc[1:, :]
        type = 'cells'
        print('Klasterovanje celija')
    else:
        df = pd.read_csv('../data/filtered_data.csv')
        genes = df.iloc[:, 0].values
        data = df.iloc[:, 1:]
        type = 'genes'
        print('Klasterovanje gena:\n')

    clusters = {}

    score = -1
    best_eps = 0.5
    best_minPts = 5
    eps_vals = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    for eps in eps_vals:
        for minPts in range(4, 9):

            dbscan = DBSCAN(eps=eps, min_samples=minPts).fit(data)
            labels = dbscan.labels_
            try:
                current_score = silhouette_score(data, labels, metric='euclidean')
            except ValueError:
                current_score = -1
            print('Eps: {}, minPts: {}, score: {:.3f}'.format(eps, minPts,current_score))
            if current_score > score:
                score = current_score
                best_eps = eps
                best_minPts = minPts
    print('\n')

    dbscan = DBSCAN(eps=best_eps, min_samples=best_minPts).fit(data)
    labels = dbscan.labels_

    if type == 'cells':
        for i in range(data.shape[0]):
            cluster_num = dbscan.labels_[i]
            if cluster_num not in clusters:
                clusters[cluster_num] = []
            clusters[cluster_num].append(i)
    else:
        for i in range(data.shape[0]):
            cluster_num = dbscan.labels_[i]

            if cluster_num not in clusters:
                clusters[cluster_num] = []
            clusters[cluster_num].append(genes[i])

    print('Eps = {}\nMinPts = {}\n'.format(best_eps,best_minPts))
    print('\n' + 'Silhouette score = {}'.format(score) + '\n')
    for i in clusters:
        if i == -1:
            print("Outliers: ", len(clusters[i]), "\n")
        else:
            print("Cluster {}: ".format(i), len(clusters[i]), "\n")

    print('\n')

    if type == 'genes':
        output = open('../outputs/DBSCAN_genes_eps{}_minPts{}.txt'.format(best_eps, best_minPts), 'w')
        for (cluster, genes) in clusters.items():
            if cluster == -1:
                output.write('Outliers, Size: {} \n'.format(len(genes)))
            else:
                output.write('Cluster ID: {}, Size: {} \n'.format(cluster, len(genes)))
            for gene in genes:
                output.write(gene + ', ')
            output.write('\n\n\n')
    else:
        output = open('../outputs/DBSCAN_cells_eps{}_minPts{}.txt'.format(best_eps, best_minPts), 'w')
        for (cluster, cells) in clusters.items():
            if cluster == -1:
                output.write('Outliers, Size: {} \n'.format(len(cells)))
            else:
                output.write('Cluster ID: {}, Size: {} \n'.format(cluster, len(cells)))
            for cell in cells:
                output.write(str(cell) + ', ')
            output.write('\n\n\n')

    joblib.dump(dbscan, '../models/DBSCAN_{}.joblib'.format(sys.argv[1]))

if __name__ == "__main__":
    main()
