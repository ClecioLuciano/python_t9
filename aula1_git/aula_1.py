import csv

with open('./aula1_git/POP2025_20260828.csv', mode='r') as file:
    reader = csv.DictReader(file, delimiter=';')
    for linha in reader:
        print(linha)