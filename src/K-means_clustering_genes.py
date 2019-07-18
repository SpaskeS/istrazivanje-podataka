from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np
import pandas as pd
import sys
import joblib

def main():
    df = pd.read_csv('../data/filtered_data.csv')

    genes = df.iloc[:, 0].values
    data = df.iloc[:, 1:]

    clusters = {}

    k = 8
    if (len(sys.argv) == 2 and sys.argv[1] == 'default'):
        print("klasterovanje se vrši sa podrazumevanim brojem klastera, n_clusters = 8")
        km = KMeans().fit(data)

    else:
        interias = []

        for i in range(1,20):
            interia = KMeans(n_clusters=i).fit(data).inertia_
            interias.append(interia)

        c = interias[0]
        k = 0
        for i in range(0, 17):
            a = interias[i]-interias[i+1]
            b = interias[i]-interias[i+2]
            if (abs(a - b) + abs(a-b)*0.2) < c:
                c = abs(a - b)
                k = i

        print("broj klastera: ", k, "\n")
        km = KMeans(n_clusters=k).fit(data)


    labels = km.labels_
    score = silhouette_score(data, labels, metric='euclidean')
    print('\n' + 'Silhouette score = {}'.format(score) + '\n')

    for i in range(data.shape[0]):
        cluster_num = km.labels_[i]

        if cluster_num not in clusters:
            clusters[cluster_num] = []
        clusters[cluster_num].append(genes[i])

    for i in clusters:
        print("Cluster {}: ".format(i), len(clusters[i]), "\n")


    output = open('../outputs/K-means_genes_{}.txt'.format(k), 'w')
    for (cluster, genes) in clusters.items():
        output.write('Cluster ID: {}, Size: {} \n'.format(cluster, len(genes)))
        for gene in genes:
            output.write(gene + ', ')
        output.write('\n\n\n')

    joblib.dump(km, '../models/K-means_genes.joblib')

if __name__ == "__main__":
    main()
