plt.figure(figsize=(8,6), facecolor=facecolor)
x = ['married', 'single', 'divorced']
y = [married, single, divorced]

plt.bar(x, y, color=colors)
plt.title('Situaçao matrimonital')
plt.tight_layout()

plt.savefig('plot-pclass-bar.svg', format='svg')
plt.show()
