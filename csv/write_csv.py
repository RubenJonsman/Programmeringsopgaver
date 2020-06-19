import pandas as pd
import csv

df = pd.read_csv("maelkeproduktion.csv", sep=";", encoding='utf8')
csv.register_dialect("semikolon", delimiter=";")
with open(r'maelkeproduktion.csv', 'a') as f:
    writer = csv.writer(f, dialect="semikolon")
    a = input()
    writer.writerow(a)
