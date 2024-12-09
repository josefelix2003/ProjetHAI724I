import sys
nom_fichier = sys.argv[1]
taille = int(sys.argv[2])

import matplotlib.pyplot as plt #bibliotheque de fonctions pour les plots
from intensite import intensite, question_YorN

dictionnaire, intensite, longueurs_onde, intensites_normal  = intensite(nom_fichier, taille)
print("--------------- Indexation -----------------\n", dictionnaire)

def definitionIntervalle(): #On définit une fonction qui demande l'intervalle souhaité à l'utilisateur
  continuer = True
  longueur_min = min(longueurs_onde)
  longueur_max = max(longueurs_onde)
  
  while continuer:
    intervalledebut = float(input("Veuillez indiquer un début d'intervalle pour les longueurs d'onde pour lesquelles vous souhaitez avoir le spectre\n")) #fonction input pour que l'utilisateur définisse les bornes de l'intervalle
    intervallefin = float(input("Veuillez indiquer une fin d'intervalle pour les longueurs d'onde pour lesquelles vous souhaitez avoir le spectre\n"))

    #On vérifie que l'intervalle donné est valide
    if (intervalledebut >= longueur_min and intervallefin <= longueur_max and intervalledebut<=longueur_max and intervallefin >= longueur_min and intervalledebut < intervallefin):
      continuer = False
    else:
      print("L'intervalle doit etre compris entre {} et {}".format(longueur_min, longueur_max))

  return intervalledebut, intervallefin

  
  

def recherche_pics():

  longueurs_onde_pics = []
  intensites_pics = []
  critere_pic = demander_critere()
  intensite_max = max(intensite)
  
  for i in range(1,len(intensite)-1):
    if intensite[i] > intensite[i-1] and intensite[i] > intensite[i+1] and intensite[i]*(1/intensite_max) > critere_pic:
      longueurs_onde_pics.append(longueurs_onde[i])
      if intensites_normal is not None:
        intensites_pics.append(intensites_normal[i])
      else:
        intensites_pics.append(intensite[i])

  return longueurs_onde_pics, intensites_pics

def demander_critere():

  while True:
    try:
      print("Saisisez le critere pour détecter des pics (entre 0 et 1):")
      critere = float(input())
      if critere > 0 and critere <=1:
        return critere
      else:
        print("Veuillez saisir un nombre entre 0 et 1")
    except ValueError:
      print ("Entrée invalide")
      
    
    
def plotSpectre(): # Une fonction qui trace 

  intervalledebut, intervallefin = definitionIntervalle()

  longueurs_ondeint = []
  intensitesint = []

  longueurs_onde_picsint = []
  intensites_picsint = []

  for i in range (0, len(longueurs_onde)):

    if (longueurs_onde[i] > intervalledebut) and (longueurs_onde[i] < intervallefin):

      longueurs_ondeint.append(longueurs_onde[i])

      if intensites_normal is not None:
        intensitesint.append(intensites_normal[i])
      else:
        intensitesint.append(intensite[i])

  longueurs_onde_pics, intensites_pics = recherche_pics()

  for l in range(0,len(longueurs_onde_pics)):
    longueur_pic = longueurs_onde_pics[l]
    intensite_pic = intensites_pics[l]
    if longueur_pic > intervalledebut and longueur_pic < intervallefin:
      longueurs_onde_picsint.append(longueur_pic)
      intensites_picsint.append(intensite_pic)
      
      
  print ("Voici les intensités correspondantes à cet intervalle et la représentation graphique")
  print(intensitesint)
  plt.plot(longueurs_ondeint, intensitesint) #crée le plot, mais ne l'affiche pas
  plt.plot(longueurs_onde_picsint, intensites_picsint, label="Pics d'intensité", marker='x', linestyle = "", color='red')
  plt.legend()
  plt.xlabel("Longueurs d'onde (nm)")
  plt.ylabel("Intensite (a.u.)")
  plt.title("Spectre photoluminescence")
  plt.grid()
  plt.show() #affiche le plot


#On execute la fonction au moins une fois, puis on demande si l'utilisateur veut retracer
continuer = "Y";
while continuer == "Y":
  plotSpectre()
  continuer = question_YorN("Voulez vous retracer le spectre pour un nouvel interval [Y/N]?")
  
  
        

