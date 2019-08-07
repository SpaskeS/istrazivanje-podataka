import pandas as pd
import sys

def main():
    type = None
    if len(sys.argv) != 3:
        print('./python3 cluto_objects_dist.py clusters_file output_file')
        exit(1)

    if sys.argv[1][0] == 'g':
        type = 'genes'
    else:
        type = 'cells'

    input_file = '../outputs/CLUTO/vcluster_outputs/{}'.format(sys.argv[1])
    output_file = '../outputs/{}'.format(sys.argv[2])

    if type == 'genes':
        df = pd.read_csv('../data/filtered_data.csv')
        genes = df.iloc[:, 0].values
        data = df.iloc[:, 1:]
    else:
        df = pd.read_csv('../data/transposed_data.csv')
        data = df.iloc[1:, :]

    in_file = open(input_file, 'r')
    out_file = open(output_file, 'w')

    clusters = {}

    if type == 'cells':
        for i in range(data.shape[0]):
            cluster_num = int(in_file.readline())
            if cluster_num not in clusters:
                clusters[cluster_num] = []
            clusters[cluster_num].append(i)
    else:
        for i in range(data.shape[0]):
            cluster_num = int(in_file.readline())

            if cluster_num not in clusters:
                clusters[cluster_num] = []
            clusters[cluster_num].append(genes[i])

    if type == 'genes':
        for(cluster, genes) in clusters.items():
            out_file.write('Cluster ID: {}, Size: {} \n'.format(cluster, len(genes)))
            for gene in genes:
                out_file.write(gene + ', ')
            out_file.write('\n\n\n')
    else:
        for(cluster, cells) in clusters.items():
            out_file.write('Cluster ID: {}, Size: {} \n'.format(cluster, len(cells)))
            for cell in cells:
                out_file.write(str(cell) + ', ')
            out_file.write('\n\n\n')

if __name__ == '__main__':
    main()
