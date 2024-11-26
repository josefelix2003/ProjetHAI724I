#L'usager peut saisir le nom du fichier et la taille souhaitée
echo "Veuillez saisir le nom du fichier contenant le spectre"
read fichier
echo "Veuillez saisir la taille de la fenêtre"
read taille


#tester la validité du fichier
if [ -z "$fichier" ] # vérifier si une chaîne a été fourni
then
    echo "Aucun fichier specifié"
    exit 1
elif [ -f "$fichier" ]#tester si le fichier existe dans le dossier courant et que c'est bien un fichier
then
     echo "Le fichier existe"
     echo $fichier
else
    echo "Le fichier specifié n'existe pas ou n'est pas un fichier"
    exit 1
fi

#tester la validité de la fenêtre

#if [ -z "$taille" ]
#then
 #   echo "Aucune valeur a été saisie; La valeur par défaut sera 10 nm"
  #  taille=10
   # echo $taille
#elif [[ $taille =~ ^[0-9]+$ ]]
#then 
 #   echo "La taille saisie est bien un entier positif : " 
  #  echo $taille
#else
 #   echo "La taille saisie n'est pas valide"
  #  exit 1
#fi



#importer le fichier avec le script python intensite.py

python3 intensite.py $fichier $taille



