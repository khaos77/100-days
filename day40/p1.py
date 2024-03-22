import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv ('/kaggle/input/bank-client-attributes-and-marketing-outcomes/Assignment-2_Data.csv')
df

contagem = df.groupby(["marital"]).count()
print(contagem)
