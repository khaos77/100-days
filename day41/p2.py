import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
colors = ['#4285F4', '#FBBC05','#34A853', '#EA4335' ]
facecolor= '#FFFFFF'

df = pd.read_csv ('/kaggle/input/bank-client-attributes-and-marketing-outcomes/Assignment-2_Data.csv')

conta = df['marital'].value_counts()
print(conta)

married = conta.iloc[0] /100
single = conta.iloc[1] /100
divorced = conta.iloc[2] /100
#teste
print(married)
print(single)
print(divorced)

valores = [married, single, divorced]
a = pd.DataFrame(valores, columns=['a'])
print(a)