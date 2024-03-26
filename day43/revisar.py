import pandas as pd

#desvio padrao: 
#desvio = df.['coluna'].std()


data = ['9', '6', '23', '3', '3']
df = pd.DataFrame(data)
print(df.value_counts())
#ascending controla a ordem com qual aparece o resultado, o normalize resulta o valor da frequencia relativa

plt.axvline(x=5, color='red', linestyle='--')
#aparece no grafico uma linha pontilhada

df = df.dropna(subset=['2022-23'])
#dropna retira valores vazios da coluna

sns.boxplot()
#boxplot so vai com import sns

.flatten()
#a multi-dimensional array, flatten() will convert it into a one-dimensional array 
