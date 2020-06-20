import pandas as pd
import csv
import numpy as np

frame = pd.DataFrame(np.arange(16).reshape(4, 4), index=['white', 'black', 'red', 'blue'], columns=['up', 'down', 'right', 'left'])

# JSON
frame.to_json('frame.json')

# CSV
frame.to_csv('frame.csv')

# PICKLE
frame.to_pickle('frame.pickle')



