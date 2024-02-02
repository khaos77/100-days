#mudar nome do arquivo
n = int(input())

buracos = "ADOPQR"
b = "B"
palavras = []
count = 0

for i in range(n):
    palavra = input()
    for a in palavra:
        if a in buracos:
            count += 1
        else:
            if a in b:
                count += 2
    print(count)
    count = 0