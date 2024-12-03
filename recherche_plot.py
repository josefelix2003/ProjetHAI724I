import sys
nom_fichier = sys.argv[1]
taille = int(sys.argv[2])

import matplotlib.pyplot as plt #bibliotheque de fonctions pour les plots
from intensite import intensite



dictionnaire, intensite, longueurs_onde =intensite(nom_fichier, taille)
print(dictionnaire)


longueurs_ondesint=[] #initialisation de mon tableau de valeur d'intérêt pour lambda et I
intensitesint=[]


intervalledebut=float(input('veuillez indiquer un début d intervalle pour les longueurs d onde pour lesquelles vous souhaitez avoir les intensités correspondantes')) #fonction input pour que l'utilisateur définisse les brones de l'intervalle
intervallefin=float(input('veuillez indiquer une fin d intervalle pour les longueurs d ondes pour lesquelles vous souhaitez avoir les intensités correspondantes'))

print ('voici les intensités correspondantes à cet intervalle et la représentation graphique')



for i in range (0, len(longueurs_onde)):

  if (longueurs_onde[i] > intervalledebut) and (longueurs_onde[i] < intervallefin):

    longueurs_ondesint.append(longueurs_onde[i])
    intensitesint.append(intensite[i])

print (intensitesint)


plt.plot(longueurs_ondesint, intensitesint) #crée le plot, mais ne l'affiche pas
plt.show() #affiche le plot
