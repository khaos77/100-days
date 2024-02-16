import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dados = np.random.random((5, 5))
df = pd.DataFrame(dados)
plt.plot(df.index, df.iloc[:,0], "ro-")
plt.show()