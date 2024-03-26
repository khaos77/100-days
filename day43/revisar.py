import pandas as pd

#desvio padrao: 
#desvio = df.['coluna'].std()


data = ['9', '6', '23', '3', '3']
df = pd.DataFrame(data)
print(df.value_counts())