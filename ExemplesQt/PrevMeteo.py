import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("previsionsMeteo.csv", "r"), delimiter=";", skiprows=56)
lieu = 1
nbAnnees = 29
nbJoursJanvier = 31

allDays = data[nbAnnees*nbJoursJanvier*(lieu-1):nbAnnees*nbJoursJanvier*(lieu),0]
days_X_Years = np.array_split(allDays,nbAnnees)

allMaxTemp = data[nbAnnees*nbJoursJanvier*(lieu-1):nbAnnees*nbJoursJanvier*(lieu),4] - 273.15
maxTemp_X_Days = np.array_split(allMaxTemp,nbAnnees)

#test on affiche les temperaturesMax et les jours de l'annee 0
print(days_X_Years[0])
print(maxTemp_X_Days[0])


