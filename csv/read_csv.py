import pandas as pd
import csv
df = pd.read_csv("maelkeproduktion.csv", sep=";", encoding='utf8')
print(df)
