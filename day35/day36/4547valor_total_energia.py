consumo = int(input())

pag = (consumo * 0.75)
ilumi = pag * 0.05

print(f'Valor do consumo: R$ {pag}')
print(f'Valor taxa iluminacao: R$ {ilumi}')
print(f'Valor total a pagar: R$ {ilumi+pag}')