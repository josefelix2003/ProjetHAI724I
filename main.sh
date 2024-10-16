#tester si le fichier existe
if [ -z $@ ]
then
    echo "Aucun fichier specifié"
elif [ -f $@ ]
then
     echo "Le fichier existe"
else
    echo "Le fichier specifié n'existe pas ou n'est pas un fichier"
fi

#importer le fichier avec python


#stocker la colonne i 
