import pandas as pd
import datetime
import numpy as np

i = -1
my_dict = {}
for chunk in pd.read_csv("./data/FirstThreeMonth.csv", chunksize=100):
    i += 1
    pirList = chunk["pir"].to_numpy()
    nonzero_indices = np.nonzero(pirList)

    #in excel the first elemst starts from index 2
    excel_nonzero_indices = (nonzero_indices[0] + 2) + i * 100 
    print(chunk.iloc[nonzero_indices[0], [0, 6]])
    print((nonzero_indices[0] + 2) + i * 100)
    print(pirList[nonzero_indices[0]])
