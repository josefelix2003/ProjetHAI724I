
import re
#fonction qui récupere Y ou N suite à une question 
def question_YorN(question):
        reponse_valide = False
        while reponse_valide == False:
            print(question)
            reponse_clavier = input()
            if reponse_clavier == "Y" or reponse_clavier == "N":
                reponse_valide = True
                if reponse_clavier == "Y":
                    return "Y"
                else :
                    return "N"
            else:
                print("Veuillez répondre Y pour Oui ou N pour Non")

                
def intensite(nom_fichier, taille): #fonction qui renvoie le dictionnaire, les longueurs d'onde et intensités
        
    fichier = open(nom_fichier) #les données seront stockés dans cet variable
    #On extrait ces donées pour les stocker sous forme de listes
    
    
    lignecherche = False #boolean indiquant si on a commencé a parcourir les lignes contenant les données; On l'initialise en False car les premieres lignes corresponent a l'information générale des mesures
    longueurs_onde = []
    intensites = []
    
    for lignecourant in fichier:
        res = re.search("Begin", lignecourant)
        if res : #Si la regexp a été trouvée dans la ligne courante
            lignecherche = True #on indique qu'on a commence a parcourir les lignes contenant les données
            continue #On passe directement a la ligne suivante
            
        if lignecherche == True :
            res = re.search("End", lignecourant) #On veut vérifier qu'on est toujours dans la partie données
            if res: #Dans ce cas on a fini de récuperer les données, on arrete de lire le document
                break
            else : 
                #la ligne courante correspond a des données qu'on veut extraire
                l=lignecourant.strip().split() #on transforme la ligne en une liste contenant la longueur d'onde et l'intensité associée 
                
                longueurs_onde.append(float(l[0])) #on ajoute l'élément d'indice 0 aux longueurs d'onde
                intensites.append(float(l[1])) #on ajoute l'élément d'indice 1 aux intensités
                
                    
     
    
    fenetres = [] #La liste contenant les intervalles de longueurs d'onde
    longueur_min = int(min(longueurs_onde))
    derniere_longueur = int(max(longueurs_onde))
    
        #on crée les clés pour le dictionnaire
    while longueur_min < derniere_longueur: #Tant qu'on n'est pas arrivé a la derniere longueur en crée une fenetre
        fenetres.append((longueur_min,longueur_min+taille))
        longueur_min+=taille
        
    nb_fenetres = len(fenetres)
    valeurs_dict = []
    
    for n in range(nb_fenetres):
        valeurs_dict.append([]) #on ajoute une liste vide pour chaque intervalle de longueurs d'onde
    
    
    
    for n in range(nb_fenetres):
        a=fenetres[n][0] #limite inférieure de la fenetre
        b=fenetres[n][1] #limite supérieure de la fenetre
        
        for l in range(len(longueurs_onde)):
            longueur=longueurs_onde[l]
            intensite=intensites[l] #intensite associé a la longueur d'onde l
            if longueur>=a and longueur<b : #si la longueur est comprise entre la limite inf et sup de la fenetre
                valeurs_dict[n].append(intensite) #on ajoute cette intensité à la liste d'indice n 
            
    
    dictionnaire = {}
    for n in range(nb_fenetres): #on va parcourir les différentes fenetres
        dictionnaire[fenetres[n]]=valeurs_dict[n] #fenetres[n] correspond a la clé du dictionnaire; valeurs_dict[n] définit la valeurs associée a chaque clé
    
    #fichier.close()
    
    #Print max, min, moyenne pour chaque fenêtre
    for k in dictionnaire:
        cle = k
        liste_intensites = dictionnaire[k]
        print("----------------------------\nFenêtre : ", cle)
        print("Nombre de mesures : ", len(liste_intensites))
        print("Maximum : ", max(liste_intensites))
        print("Minimum : ", min(liste_intensites))
        
        if len(liste_intensites) == 0:
            moy = 0
        else:
            moy = sum(liste_intensites)/len(liste_intensites)
        print("Moyenne : ", moy)
        
    

    #Normalisation des intensités
    intensites_normal = None

    normalisation = question_YorN("Voulez vous tracer le spectre normalisé [Y/N]?")
    if normalisation == "Y":
        intensites_normal = []
        intensite_max = max(intensites)
        for i in intensites:
            i_norm = i*(1/intensite_max)
            intensites_normal.append(i_norm)

        
    
    return dictionnaire, intensites, longueurs_onde, intensites_normal




    
    
    
    
   
