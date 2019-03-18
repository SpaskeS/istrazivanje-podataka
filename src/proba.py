import csv

with open('../data/transposed_data.csv', newline= '') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
