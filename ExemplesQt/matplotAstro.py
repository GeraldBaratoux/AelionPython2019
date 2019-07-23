import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("donneesAstro.csv", "rb"), delimiter=",", skiprows=1)

data2 = data[:2000]

xMoy = np.array(np.array_split(data2[:,0], 40))
yMoy = np.array(np.array_split(data2[:,1], 40))
errMoy = np.array(np.array_split(data2[:,2],40))

devStd = np.std(yMoy,1) #deviation standard

print(devStd.size)

xPoints = xMoy.mean(axis=1)
yPoints = yMoy.mean(axis=1)

print(yPoints.size)

ya = yPoints+devStd
yb = yPoints-devStd

print(ya)

fig, ax = plt.subplots()
ax.scatter(data[:,0], data[:,1])

ax.plot(xPoints, yPoints, color='tab:orange')
ax.plot(xPoints, ya, color='tab:green')
ax.plot(xPoints, yb, color='tab:red')

ax.grid(True)
plt.show()
