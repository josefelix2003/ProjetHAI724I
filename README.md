# TP spectre de photoluminescence
Programme d’aide à l’exploitation des spectres de photoluminescence

#auteurs
Jose-Miguel Felix-De-Los-Rios et Alban Desoutter

#Description
L’utilisateur doit fournir un fichier .txt contenant les data du spectre de photoluminescence. 
Le programme demandera des valeurs de longueurs d’onde min et max et plotera les intensités dans cet intervalle. 

#version Python
Python 3.12.7

#Licence
Ce fichier est sous licence Python Software Foundation License

![image](https://github.com/user-attachments/assets/3336af74-ee52-426e-b919-d077c5f54c53)




Spectre de photoluminescence

Contexte

Les diodes, éléments essentiels des circuits électroniques, fonctionnent comme des commutateurs à sens unique, permettant ou bloquant le passage du courant selon la polarité. Une application spécifique des diodes est la diode laser, un dispositif utilisant des semi-conducteurs, notamment l'Arséniure de Gallium (GaAs) dont l'emission est d'environ 850 nm. À l'aide d'un spectromètre on peut récuperer le spectre d'emission de cet matériau. Le fichier contenant ces données est accessible et constitue l'entrée principale de notre programme.
Cet script permet d'indexer les intensités mesurées par intervalle de longeur d'onde et de fournir des informations importantes pour chaque fenêtre (minimum, maximum, moyenne).

Fonctionnement général

Ce script est constitué de trois fichiers. Le fichier main.sh est le fichier principal est c'est le seul fichier à executer par l'usager. Ce fichier a comme but de récuperer le nom du fichier contenant le spectre d'intensité. Il donne la possibilité aussi de fournir une taille de fenêtre spécifique, sinon la taille sera 10 nm par défaut. Ensuite ce script appelle le script intensite.py. Ce script python permet de stocker les données sous forme d'un dictionnaire pour ensuite faire une analyse du spectre. Le troisième fichier recherche_plot.py permet d'étudier graphiquement une intervalle concrète qui sera spécifiée par l'utilisateur. 

Le programme main

le main est, en python , est l'éxécuteur principal, celui qui sera appelé par l'utilisateur en bout de chaine. En ce sens, le main peut appeler des fonctions qui seront développé à part, ce qui est le cas présentement pour nos données d'intensité en fonction de la longueur d'onde, ainsi que pour l














Spécifications

Cet programme prend en entrée un fichier contenant les données du spectromètre. Un extract du fichier utilisé pour concevoir cet script est annexé comme exemple. De même un exemple de ce qui est renvoyé en sortie est annexé. 

