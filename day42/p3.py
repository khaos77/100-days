#updates no projeto
valores = [married, single, divorced]
valores = pd.DataFrame(valores, columns=['valores'])
valores.index = ['married', 'single', 'divorced']
print(valores) 

#plotar o negocio
plt.figure(figsize=(12,6), facecolor=facecolor)
#erro no plt.bar
x = np.array[valores[0]]
y = np.array['valores']
plt.bar(x,y)
plt.xlabel('situaçao matrimonial')
plt.ylabel('valores')
plt.title('vou ver e te aviso')
plt.tight_layout()

plt.savefig('plot-pclass-bar.svg', format='svg')
plt.show()