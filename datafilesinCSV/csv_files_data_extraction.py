import numpy as np
import pandas as pd

data= np.load("C:\\Desktop\\Moosic\\Emotion Detection\\data\\angry.npy")
data1= np.load("C:\\Desktop\\Moosic\\Emotion Detection\\data\\hello.npy")

data2= np.load("C:\\Desktop\\Moosic\\Emotion Detection\\data\\happy.npy")

data3= np.load("C:\\Desktop\\Moosic\\Emotion Detection\\data\\neutral.npy")

data4= np.load("C:\\Desktop\\Moosic\\Emotion Detection\\data\\No.npy")
data5= np.load("C:\\Desktop\\Moosic\\Emotion Detection\\data\\rock.npy")
data6= np.load("C:\\Desktop\\Moosic\\Emotion Detection\\data\\sad.npy")
data7= np.load("C:\\Desktop\\Moosic\\Emotion Detection\\data\\surprise.npy")
data8= np.load("C:\\Desktop\\Moosic\\Emotion Detection\\data\\Thumbsup.npy")

df = pd.DataFrame(data)
df = pd.DataFrame(data1)
df = pd.DataFrame(data2)
df = pd.DataFrame(data3)
df = pd.DataFrame(data4)
df = pd.DataFrame(data5)
df = pd.DataFrame(data6)
df = pd.DataFrame(data7)
df = pd.DataFrame(data8)

df.to_csv("angrydataset.csv", index=False)
df.to_csv("happydataset.csv", index=False)
df.to_csv("hellodataset.csv", index=False)
df.to_csv("neutraldataset.csv", index=False)
df.to_csv("Nodataset.csv", index=False)
df.to_csv("rockdataset.csv", index=False)
df.to_csv("saddataset.csv", index=False)
df.to_csv("surprisedataset.csv", index=False)
df.to_csv("Thumbsupdataset.csv", index=False)
