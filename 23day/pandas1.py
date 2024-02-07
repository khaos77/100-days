import pandas as pd

data = {
    'carros': ["jesko", "aventador", "gtr", "laferrari", "911"], 
    'velocity': ["480km/h", "350km/h", "395km/h", "380 km/h", "311km/h"]
}
#num = pd.Series(data)
fim = pd.DataFrame(data)
print(fim)