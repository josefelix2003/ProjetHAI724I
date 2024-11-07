#Le parametre 1 correspond au nom du fichier, parametre 2 correspond a la taille 
fichier=$1
taille=$2

#tester si le fichier existe
if [ -z $1 ]
then
    echo "Aucun fichier specifié"
    exit 1
elif [ -f $1 ]
then
     echo "Le fichier existe"
else
    echo "Le fichier specifié n'existe pas ou n'est pas un fichier"
    exit 1
fi

echo "Etape suivante"

#importer le fichier avec le script python intensite.py

python3 intensite.py $fichier $taille



#stocker la colonne i 
