import csv

with open('POP2025_20260828.csv', mode='r') as file:
    reader = csv.DictReader(file, delimiter=';')
    for linha in reader:
        print(linha)