#Write a Python program to find the index of an item 
#in a specified list.

index = int(input("list index: "))
lista = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(lista[index+1])

#Write a Python program to get the frequency of elements in a list.
lista2 = [2,3,4,7,3,5,6,3,5,7,5,7]
user = int(input("numero procurado: "))
print(lista2.count(user))

#teste
lista = ['o cortiço', 'capitaes de areia', 'dom quixote', 'minie','lapis','garrafa', "cama"]
lis_o = [x for x in lista if 'o' in x]
print(lis_o) 

#teste
lista2 = ["mudar", "mouse", "musica"]
res = [lista2.count(x) for x in lista2]
#user = int(input("numero procurado: "))
print(res)