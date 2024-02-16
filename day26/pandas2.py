import matplotlib.pyplot as plt


fig, ax = plt.subplots(); plt.xlabel('Combustivel no tanque(L)'); plt.ylabel('Distancia percorrida(km)')
ax.plot([500, 400, 300, 200, 100, 0], [0, 10, 20, 30, 40, 50])

plt.grid(True, c = "red", lw = 0.2)
plt.show()