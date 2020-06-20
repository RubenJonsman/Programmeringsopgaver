import pandas as pd
mydict = {'red': {2012: 22, 2013: 33},
          'white': {2011: 13, 2012: 22, 2013: 16},
          'blue': {2011: 17, 2012: 27, 2013: 18}}
df = pd.DataFrame(mydict)
print(df)

def addRow(df, row, collum):
    df = df.T
    df[row] = collum
    df = df.T
    df.to_csv('file_name.csv')

row = input("row: \n ")
collum = input("collum: \n")
addRow(df, row, collum)


'''
For at tilføje en row til et Pandas DataFrame.

Flip DF med Transposition frame.T
Tilføj collum
Flip DF igen. 

Collum er derfor blevet til et row

'''
