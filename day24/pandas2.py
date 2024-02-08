import pandas as pd

data = {
    'Carros': ["jesko", "aventador", "gtr", "laferrari", "911"], 
    'Velocity in km/h': ["480", "350", "395", "380", "311"]
}
teste = data["Carros"]
maior = pd.Series(data["Velocity in km/h"], name="v")
fim = pd.DataFrame(data)
print(fim)
print("faster model: " + maior.max())

