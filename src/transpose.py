import csv
import numpy as np

def main():
    elements_trans = []
    with open('../data/filtered_data.csv', newline= '') as csvfile:
        reader = csv.reader(csvfile)

        elements = list(reader)
        elements_trans =   list(map(list, zip(*elements)))

    with open('../data/transposed_data.csv', 'w', newline= '') as csvfile2:
        writer = csv.writer(csvfile2, quoting=csv.QUOTE_MINIMAL)

        for row in elements_trans:
            writer.writerow(row)

if __name__ == "__main__":
    main()
