from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

def main():
    df = pd.read_csv('../data/transposed_data.csv')
    print(df.shape)

    data = df.iloc[1:, :]
    n=10
    km = KMeans(n_clusters=n).fit(data)
    clusters = {}

    for i in range(data.shape[0]):
        cluster_num = km.labels_[i]

        if cluster_num not in clusters:
            clusters[cluster_num] = []
        clusters[cluster_num].append(i)

    for i in clusters:
        print("Cluster {}: ". format(i))
        print(len(clusters[i]))
        print()


if __name__ == "__main__":
    main()
