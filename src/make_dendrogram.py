import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import sys

def main():
    if len(sys.argv) != 2:
        print('python3 make_dendrogram.py genes/cells')
        exit(1)

    if sys.argv[1] == 'genes':
        df = pd.read_csv('../data/filtered_data.csv')
        genes = df.iloc[:, 0].values
        data = df.iloc[:, 1:]
    else:
        df = pd.read_csv('../data/transposed_data.csv')
        data = df.iloc[1:, :]

    plt.figure(figsize = (10, 7))
    link = linkage(data, method='ward', metric='euclidean')
    dendo = dendrogram(link, p=100, show_leaf_counts=False, truncate_mode='lastp')
    plt.title('{} dendrogram'.format(sys.argv[1]))
    plt.xlabel('{} clusters'.format(sys.argv[1]))
    plt.ylabel('Distance')
    plt.savefig('dendrogram_{}.png'.format(sys.argv[1]))

if __name__ == '__main__':
    main()
