import numpy as np
import pandas as pd

data = np.load("labels.npy")

df = pd.DataFrame(data)

df.to_csv("label-details.csv", index=False)