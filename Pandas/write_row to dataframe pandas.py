import pandas as pd
mydict = {'red': {2012: 22, 2013: 33},
          'white': {2011: 13, 2012: 22, 2013: 16},
          'blue': {2011: 17, 2012: 27, 2013: 18}}
frame = pd.DataFrame(mydict)
print(frame)

def addRow(frame, row, collum):
    frame = frame.T
    print(frame)
    frame[row] = collum
    frame = frame.T
    print(frame)


row = input("row: \n ")
collum = input("collum: \n")
addRow(frame, row, collum)

'''
For at tilføje en row til et Pandas DataFrame.

Flip DF med Transposition frame.T
Tilføj collum
Flip DF igen. 

Collum er derfor blevet til et row

'''
