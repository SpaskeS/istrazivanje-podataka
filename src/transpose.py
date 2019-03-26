import csv
import pandas as pd
import numpy as np

def main():
    df = pd.read_csv('../data/filtered_data.csv')

    df_trans = df.transpose()

    with open('../data/transposed_data.csv', 'w', newline= '') as csvfile2:
        writer = csv.writer(csvfile2, quoting=csv.QUOTE_MINIMAL)

        for row in df_trans.values:
            writer.writerow(row)

if __name__ == "__main__":
    main()
