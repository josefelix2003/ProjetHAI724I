
import matplotlib.pyplot as plt #bibliotheque de fonctions pour les plots

longueurs_ondesint=[] #initialisation de mon tableau de valeur d'intérêt pour lambda et I
intensitesint=[]


float(intervalledebut)=input('veuillez indiquer un début d intervalle pour les longueurs d onde pour lesquelles vous souhaitez avoir les intensités correspondantes') #fonction input pour que l'utilisateur définisse les brones de l'intervalle
float(intervallefin)=input('veuillez indiquer une fin d intervalle pour les longueurs d ondes pour lesquelles vous souhaitez avoir les intensités correspondantes')

print 'voici les intensités correspondantes à cet intervalle et la représentation graphique' 


for i in range (0, len(longueurs_onde)) 

if longueurs_onde[i] > intervalledebut

longueurs_ondesint.append(longueurs_onde[i])
intensitesint.append(intensite[i])




plt.plot(longueurs_ondesint, intensitesint) #crée le plot, mais ne l'affiche pas
plt.show() #affiche le plot
