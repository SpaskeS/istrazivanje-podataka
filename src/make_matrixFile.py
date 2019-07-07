import pandas as pd
import numpy as np
import sys

def main():
    if len(sys.argv) != 2:
        print('python3 make_matrixFile.py genes/cells')
        exit(1)

    if (len(sys.argv) > 1 and sys.argv[1] == 'cells'):
        df = pd.read_csv('../data/transposed_data.csv')
        data = df.iloc[1:, :].to_numpy()
        file = open('../data/cells.mat', 'w')
    else:
        df = pd.read_csv('../data/filtered_data.csv')
        genes = df.iloc[:, 0].values
        data = df.iloc[:, 1:].to_numpy()
        file = open('../data/genes.mat', 'w')

    file.write(str(data.shape[0]) + ' ' + str(data.shape[1]) + '\n')

    for gene in data:
        row = ''
        for cell in gene:
            row += str(cell) + ' '
        row = row.strip()
        row += '\n'
        file.write(row)

if __name__ == '__main__':
    main()
