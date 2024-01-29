segundos = int(input())
minutos = segundos/60
horas = segundos/3600
dias = segundos/86400

print("{:.5f} dias".format(dias))
print("{:.5f} horas".format(horas))
print(f"{minutos} minutos")
print(f"{segundos} segundos")