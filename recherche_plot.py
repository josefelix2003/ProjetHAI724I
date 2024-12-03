import sys
nom_fichier = sys.argv[1]
taille = sys.argv[2]

import matplotlib.pyplot as plt #bibliotheque de fonctions pour les plots
from intensite import intensite


intensite=intensite(nom_fichier, taille)[1]
longueurs_ondes=intensite(nom_fichier, taille)[2] #voir siplifier un seul appel


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
