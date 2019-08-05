from minisom import MiniSom
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
import sys
import pandas as pd
import math
import joblib

def main():
    if len(sys.argv) != 3:
        print('python3 SOM_clustering.py genes/cells batch/random')
        exit(1)

    if sys.argv[1] == 'genes':
        df = pd.read_csv('../data/filtered_data.csv')
        genes = df.iloc[:, 0].values
        data = df.iloc[:, 1:].to_numpy()
    else:
        df = pd.read_csv('../data/transposed_data.csv')
        data = df.iloc[1:, :].to_numpy()

    N = math.ceil(math.sqrt(5 * math.sqrt(data.shape[0])))

    mdl = MiniSom(N, N, data.shape[1])
    mdl.random_weights_init(data)
    if sys.argv[2] == 'random':
        mdl.train_random(data, 100)
    else:
        mdl.train_batch(data, 100)

    plt.pcolor(mdl.distance_map().T)
    if sys.argv[1] == 'genes':
        if sys.argv[2] == 'random':
            plt.savefig('train_random_genes')
        else:
            plt.savefig('train_batch_genes')
    else:
        if sys.argv[2] == 'random':
            plt.savefig('train_random_cells')
        else:
            plt.savefig('train_batch_cells')
    plt.show()

    labels = []
    for x in data:
        winner = mdl.winner(x)
        i = (winner[0], winner[1])
        labels.append(i)

    clusters = {}

    if sys.argv[1] == 'cells':
        for i in range(data.shape[0]):
            cluster_num = labels[i]
            if cluster_num not in clusters:
                clusters[cluster_num] = []
            clusters[cluster_num].append(i)
    else:
        for i in range(data.shape[0]):
            cluster_num = labels[i]

            if cluster_num not in clusters:
                clusters[cluster_num] = []
            clusters[cluster_num].append(genes[i])

    if sys.argv[1] == 'genes':
        output = open('../outputs/SOM_genes_{}.txt'.format(sys.argv[2]), 'w')
        for (cluster, genes) in clusters.items():
            output.write('Cluster: {}, Size: {} \n'.format(cluster, len(genes)))
            for gene in genes:
                output.write(gene + ', ')
            output.write('\n\n\n')
    else:
        output = open('../outputs/SOM_cells_{}.txt'.format(sys.argv[2]), 'w')
        for (cluster, cells) in clusters.items():
            output.write('Cluster: {}, Size: {} \n'.format(cluster, len(cells)))
            for cell in cells:
                output.write(str(cell) + ', ')
            output.write('\n\n\n')

    joblib.dump(mdl, '../models/SOM_{}.joblib'.format(sys.argv[1]))

if __name__ == '__main__':
    main()
