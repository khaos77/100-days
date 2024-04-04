words = ["leet","code"]
x = "e"
lista = []
for indice, elemento in enumerate(words):
    if x in elemento:
        lista.append(indice)

print(lista)