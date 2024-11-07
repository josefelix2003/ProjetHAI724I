

#------------------------------------------------------------------------
#A decommenter :
    
#stocker paramètres d'entrée    
#import sys

#fichier = sys.argv[1]

#if len(sys.argv) == 3:
#    taille = int(sys.argv[2])
#else:
#    taille = 10

#------------------------------------------------------------------------
fichier = open("Spectre_photoluminescence.txt")
taille = 10


lignecherche = False
debut = False

longueur_in=0
longueur_fi=0

longueurs_onde = []
intensites = []

for lignecourant in fichier:
    if lignecourant.strip() == "# >>>>>Begin Spectral Data<<<<<":
        lignecherche = True
        continue
        
    if lignecherche == True :
        if lignecourant.strip() == ">>>>>End Spectral Data<<<<<":
            break
        else :
            #ligne courant correspond à une ligne de données
            l=lignecourant.strip().split()
            
            if debut == False:
                longueur_in = float(l[0])
                debut = True
                
            longueur_fi = float(l[0]) 
            
            longueurs_onde.append(float(l[0]))
            intensites.append(float(l[1]))
            
                
 

fenetres = []
longueur_a = int(longueur_in)

    
while longueur_a < longueur_fi:
    fenetres.append((longueur_a,longueur_a+taille))
    longueur_a+=taille
    
nb_fenetres = len(fenetres)

valeurs_dict = []

for n in range(nb_fenetres):
    valeurs_dict.append([])



for n in range(nb_fenetres):
    a=fenetres[n][0] #debut fenetre
    b=fenetres[n][1] #fin fenetre
    
    for p in range(len(longueurs_onde)):
        l=longueurs_onde[p]
        i=intensites[p] #intensite associé a la longueur d'onde l
        if l>=a and l<b :
            valeurs_dict[n].append(i) #on ajoute cette intensité à la liste d'indice n 
        

data = {}
for n in range(nb_fenetres):
    data[fenetres[n]]=valeurs_dict[n]
print(data)

fichier.close()
    
