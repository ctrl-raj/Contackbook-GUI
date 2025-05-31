import csv
from tabulate import tabulate 

with open("database.csv", "r") as file:
    reader = csv.DictReader(file)
    rows = list(reader) 
    content = tabulate(rows, headers="keys", tablefmt="grid")