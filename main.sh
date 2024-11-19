#L'usager peut saisir le nom du fichier et la taille souhaitée
echo "Veuillez saisir le nom du fichier contenant le spectre"
read fichier
echo "Veuillez saisir la taille de la fenêtre"
read taille


#tester si le fichier existe
if [ -z $fichier ]
then
    echo "Aucun fichier specifié"
    exit 1
elif [ -f $fichier ]
then
     echo "Le fichier existe"
else
    echo "Le fichier specifié n'existe pas ou n'est pas un fichier"
    exit 1
fi



#importer le fichier avec le script python intensite.py

python3 intensite.py $fichier $taille



