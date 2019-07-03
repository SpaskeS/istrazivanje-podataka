from minisom import MiniSom
import numpy as np
import matplotlib.pyplot as plt
import sys
import pandas as pd
import math

def main():
    if len(sys.argv) != 2:
        print('python3 SOM_clustering.py genes/cells')
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
    mdl.train_random(data, 100)
    # mdl.train_batch(data, 100)

    plt.pcolor(mdl.distance_map().T)
    if sys.argv[1] == 'genes':
        plt.savefig('./train_random_genes')
        # plt.savefig('train_batch_genes')
    else:
        plt.savefig('./train_random_cells')
        # plt.savefig('train_batch_cells')
    plt.show()

if __name__ == '__main__':
    main()
