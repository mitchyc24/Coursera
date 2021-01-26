import numpy as np
import pandas as pd 
import sys
import os



df = pd.read_csv(os.path.join(sys.path[0],"census.csv"))
print(df.head(5))