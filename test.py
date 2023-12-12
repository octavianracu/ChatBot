import csv
names = "data.csv"
with open(names) as file:
        data = csv.reader(file, delimiter="#")
        dict = {row[0]:row[1] for row in data}

print(dict)