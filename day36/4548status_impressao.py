pag = int(input())
per = float(input())
sub = 100 - per
c = (sub * pag) / per

print('O documento possui %d paginas'%(c + pag))
print(f'Ja foram impressas {pag} paginas')
print('Faltam %d paginas'%(c))