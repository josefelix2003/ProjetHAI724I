import sys
nom_fichier = sys.argv[1]
taille = int(sys.argv[2])

import matplotlib.pyplot as plt #bibliotheque de fonctions pour les plots
from intensite import intensite

dictionnaire, intensite, longueurs_onde = intensite(nom_fichier, taille)
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
  
  


def plotSpectre(): # Une fonction qui trace 

  intervalledebut, intervallefin = definitionIntervalle()

  print ("Voici les intensités correspondantes à cet intervalle et la représentation graphique")

  longueurs_ondeint = []
  intensitesint = []

  for i in range (0, len(longueurs_onde)):

    if (longueurs_onde[i] > intervalledebut) and (longueurs_onde[i] < intervallefin):

      longueurs_ondeint.append(longueurs_onde[i])
      intensitesint.append(intensite[i])

  print(intensitesint)
  plt.plot(longueurs_ondeint, intensitesint) #crée le plot, mais ne l'affiche pas
  plt.xlabel("Longueurs d'onde")
  plt.ylabel("Intensite (a.u.)")
  plt.title("Spectre photoluminescence")
  plt.grid()
  plt.show() #affiche le plot


#On execute la fonction au moins une fois, puis on demande si l'utilisateur veut retracer
continuer = True;
while continuer:
  plotSpectre()
  reponse_valide = False
  while (reponse_valide == False):
    reponse_clavier = input("Voulez vous retracer le spectre pour un nouvel intervalle [Y/N]?\n")
    if (reponse_clavier == "Y" or reponse_clavier == "N"):
      reponse_valide = True
      if reponse_clavier == "N":
        continuer = False
    else:
      print("Veuillez répondre Y pour continuer ou N pour arreter le programme")
        

