# import necessary modules
import csv

with open('F:\data.csv', 'rt') as f:
    data = csv.reader(f)
    for row in data:
        print(row)

reader = csv.DictReader(open("F:\data.csv"))
for raw in reader:
    print(raw)
