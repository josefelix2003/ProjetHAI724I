import sys
nom_fichier = sys.argv[1]
taille = int(sys.argv[2])

import matplotlib.pyplot as plt #bibliotheque de fonctions pour les plots
from intensite import intensite, question_YorN

#import du dictionnaire, longueurs d'onde; intensités et intensités normalisés
dictionnaire, intensite, longueurs_onde, intensites_normal  = intensite(nom_fichier, taille)


def definitionIntervalle(): #On définit une fonction qui demande l'intervalle souhaité à l'utilisateur
  continuer = True
  longueur_min = min(longueurs_onde)
  longueur_max = max(longueurs_onde)
  
  while continuer:
    print("Veuillez indiquer un debut d'intervalle entre {} et {}".format(longueur_min, longueur_max))
    intervalledebut = float(input()) #fonction input pour que l'utilisateur définisse les bornes de l'intervalle
    print("Veuillez indiquer une fin d'intervalle entre {} et {}".format(longueur_min, longueur_max))
    intervallefin = float(input())

    #On vérifie que l'intervalle donné est valide
    if (intervalledebut >= longueur_min and intervallefin <= longueur_max and intervalledebut<=longueur_max and intervallefin >= longueur_min and intervalledebut < intervallefin):
      continuer = False
    else:
      print("L'intervalle doit etre compris entre {} et {}".format(longueur_min, longueur_max))

  return intervalledebut, intervallefin

  
  

def recherche_pics(): #Fonction qui renvoie les valeurs correspondantes à des pics
  #On crée les listes ne contenant que les longueurs d'ondes et intensités associées à des pics
  longueurs_onde_pics = []
  intensites_pics = []
  critere_pic = demander_critere()
  intensite_max = max(intensite)
  
  for i in range(1,len(intensite)-4):
    if intensite[i] > intensite[i-1] and intensite[i] > intensite[i-4] and intensite[i] > intensite[i+1] and intensite[i] > intensite[i+4] and intensite[i]*(1/intensite_max) > critere_pic:
      longueurs_onde_pics.append(longueurs_onde[i])
      if intensites_normal is not None: #Si on a normalisé
        intensites_pics.append(intensites_normal[i])#On ajoute les intensités normalisés
      else:
        intensites_pics.append(intensite[i])#Sinon on ajoute les intensités absolues

  return longueurs_onde_pics, intensites_pics

def demander_critere(): #Fonction qui renvoie le critere demandé à l'utilisateur
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

def sauvegarder(longueurs, intensites, longueurs_pics, intensites_pics):
  try:
    if question_YorN("Voulez vous enregistrer les données [Y/N]?") == "Y": #Si on veut sauvegarder les données
      nom_fichier = input("Nom du fichier (avec extension .txt) :\n")
      if not (nom_fichier.endswith(".txt")):
        nom_fichier+=".txt"
        print("L'extension .txt a été ajouté automatiquement")
              
      with open(nom_fichier, 'a') as fichier:
        fichier.write("#La premiere colonne correspond aux longueurs d'onde et la deuxieme colonne correspond aux intensités.\n#Voici les mesures pour l'intervalle specifié\n>>>>>>>>>>>>>Debut<<<<<<<<<<<<<<\n")
      
        for longueur, intensite in zip(longueurs, intensites):
          fichier.write("{} {}\n".format(longueur, intensite))
          
        fichier.write(">>>>>>>>>>>>>Fin<<<<<<<<<<<<<<\n\n#Voici les informations des pics trouvés\n>>>>>>>>>>>>>Debut<<<<<<<<<<<<<<\n")
    
        for longueur_pic, intensite_pic in zip(longueurs_pics, intensites_pics):
          fichier.write("{} {}\n".format(longueur_pic, intensite_pic))
        fichier.write(">>>>>>>>>>>>>Fin<<<<<<<<<<<<<<\n")

      print("Les données ont été ajoutées a {}".format(nom_fichier))
      
  except:
    print("Une erreur est survenue lors de l'écriture du fichier")
    
    
    
def plotSpectre(): # Une fonction qui trace 

  #on définit l'intervalle qu'on veut tracer
  intervalledebut, intervallefin = definitionIntervalle()

  #on créé les listes qui vont contenir les données qui sont comprises dans l'intervalle qu'on vient de définir
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
      
      
  
  plt.plot(longueurs_ondeint, intensitesint) #crée le plot, mais ne l'affiche pas
  plt.plot(longueurs_onde_picsint, intensites_picsint, label="Pics d'intensité", marker='x', linestyle = "", color='red')
  plt.legend()
  plt.xlabel("Longueurs d'onde (nm)")
  plt.ylabel("Intensite (a.u.)")
  plt.title("Spectre photoluminescence")
  plt.grid()
  plt.show() #affiche le plot

  sauvegarder(longueurs_ondeint, intensitesint, longueurs_onde_picsint, intensites_picsint)


#On execute la fonction au moins une fois, puis on demande si l'utilisateur veut retracer
continuer = "Y";
while continuer == "Y":
  plotSpectre()
  continuer = question_YorN("Voulez vous retracer le spectre pour un nouvel interval [Y/N]?")
  
  
        

