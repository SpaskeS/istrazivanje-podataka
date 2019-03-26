import csv

def main():

    filtered = []

    with open('../data/010_Pericytes_or_pericyte-derived_induced_neuronal_cells_csv.csv', newline='') as csvfile:
    # with open('proba.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if len(list(filter(lambda x: x != '0', list(row)))) > 1:
                filtered.append(row)
    with open('../data/filtered_data.csv', 'w', newline= '') as csvfile2:
        writer = csv.writer(csvfile2, quoting=csv.QUOTE_MINIMAL)

        for row in filtered:
            writer.writerow(row)

if __name__ == "__main__":
    main()
