import csv

with open('insects.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print row