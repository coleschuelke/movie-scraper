import csv

header = ["date", 'barbie', 'oppenheimer']

with open("./data.csv", "w") as f:
    writer = csv.writer(f)

    writer.writerow(header)
