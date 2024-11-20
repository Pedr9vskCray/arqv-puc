import matplotlib.pyplot as plt

coordx = []
coordy = []

for x in range(1, 11):
    coordx.append(x * 2)
    coordy.append(x ** 2)

plt.plot(coordx, coordy)

plt.show()