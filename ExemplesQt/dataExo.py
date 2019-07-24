import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("dataExo.csv", "rb"), delimiter=";", skiprows=2)
#print(data)

jours = data[:,0] #on recupere les jours, et temperatures
tMax = data[:,1]
tMin = data[:,2]

tMinC = (tMin-32)*5/9 #on convertit en °C
tMaxC = (tMax-32)*5/9

tMoyC = (tMinC+tMaxC)/2

tMinSC = np.array(np.array_split(tMinC,2)) # on coupe le tableau en 2 semaines
tMinS0C = tMinSC[0]
tMinS1C = tMinSC[1]

tMaxSC = np.array(np.array_split(tMaxC,2)) # on coupe le tableau en 2 semaines
tMaxS0C = tMaxSC[0]
tMaxS1C = tMaxSC[1]

print(tMinC)

tempAll = np.concatenate((tMinC, tMaxC))

tempMin = np.min(tempAll)
tempMax = tempAll.max()
tempMoy = tempAll.mean()

#print(tMinS0C)
print(tempMin, tempMax, tempMoy)
#print(tempMax)


labels = ['Lun', 'Mar', 'Merc', 'Jeu', 'Ven', 'Sam', 'Dim']

plt.figure(1)

plt.subplot(221)
plt.plot(np.arange(1,8),tMinS0C, label='Min')
plt.plot(np.arange(1,8),tMaxS0C, label='Max')
plt.gca().set_ylim([0,100]) #gca() permet de recupere l'objet des axes
plt.xticks(np.arange(1,8), labels, rotation=45)
plt.legend()

plt.subplot(222)
plt.plot(np.arange(1,8),tMinS1C, label='Min')
plt.plot(np.arange(1,8),tMaxS1C, label='Max')
plt.xticks(np.arange(1,8), labels, rotation=45)
plt.legend()

plt.subplot(212)
#plt.subplots_adjust(top=20, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
plt.plot(jours,tMoyC, label='Moyenne')
plt.annotate('T°Moy:'+str("%.2f"%tempMoy)+'\nT°Min:'+str("%.2f" %tempMin)+'\nT°Max'+str("%.2f" %tempMax),xy=(18, 25), xytext=(16, 27))
plt.annotate('valeur', xy=(12, 25.27), xytext=(14, 22), arrowprops=dict(facecolor='black'))
plt.legend()

plt.tight_layout(pad=1, w_pad=0.4, h_pad=0.5)
plt.show()