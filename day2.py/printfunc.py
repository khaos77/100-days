if __name__ == '__main__':
    n = int(input())
    cont = 0
    lis = [] 
    for i in range(n):
        cont += 1
        lis.append(cont)
    print(*lis,sep="")
# o * printa elementos da lista em uma linha com espaços separando-os