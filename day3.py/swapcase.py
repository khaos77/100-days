def swap_case(s):
    ff = []
    for i in s:
        if i.isupper() == True:
            lista = i.lower()
            ff.append(lista)
            
        else:
            lista = i.upper()
            ff.append(lista)
    print(*ff,sep="")


s = input()
swap_case(s)