from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

def main():
    df = pd.read_csv('../data/filtered_data.csv')

    genes = df.iloc[:, 0].values
    print(genes)

    data = df.iloc[:, 1:]

    km = KMeans(n_clusters=10, n_init=15).fit(data)
    clusters = {}

    for i in range(data.shape[0]):
        cluster_num = km.labels_[i]

        if cluster_num not in clusters:
            clusters[cluster_num] = []
        clusters[cluster_num].append(genes[i])

    for i in clusters:
        print("Cluster {}: ". format(i))
        print(len(clusters[i]))
        print()


if __name__ == "__main__":
    main()
