#!/usr/bin/env python3
#coding:utf-8

# Script name: Docpy3
# Description: Documentation python 3
# Made by: Ezeqielle
# Begin: 23/02/2018
# End: 

"""
Nommer une variable : doit commencer par une lettre ou un underscore
                      ne pas contenir de caractères spéciaux
                      ne pas contenir d'espaces
                      utiliser des underscores (_)

Types standards     : entier numérique (int)
                      nombre flottant (float)
                      chaîne de caractères (str)
                      booléen (bool)
                      autres (listes, disctionnaires, tuples, etc.)

Fonction vues       : print()      -> afficher à l'écran
                      input()      -> lire au clavier
                      type()       -> retourne le type d'une donnée, varaible, etc.
                      int(), float(), str(), bool() -> "caster" une donnée, la convertir.
                      str.format() -> formater une chaîne

Opérateurs en Python : + (addition)
                       - (soustraction)
                       * (multiplication)
                       / (division)
                       % (modulo) -> reste d'une division euclidienne
    variable = variable + X
    variable += X
    variable = variable * X
    variable *= X
    variable = variable - X
    variable -= X

Opérateurs de comparaison : == (égale à)
                            != (différent de)
                            <  (plus petit que)
                            >  (plus grand que)
                            <= (plus petit ou égale à)
                            >= (plus grand ou égale à)

Mots clés des conditions : if (SI)
                           elif (SINON SI)
                           else (SINON)

Boucles en Python   : while (temps que)
                      for   (pour)

Mots clés des boucles : break   (casse la boucle)
                        contine (revient au début de la boucle)

Conditions multiples : and (ET)
                       or  (OU)
                       in  (DANS)
                       not in (PAS DANS)

Importer un module : import <nom_module>
                     from <nom_module> import <nom_fonction>
                     from <nom_module> import *
                     import <dossier>.<nom_module> as <racourcit>

Gérer les exceptions : try                       (essaie)
                       except <type_exeception>  (en cas d'erreur)
                       else                      (en cas de réussite)
                       finally                   (dans tout les cas)

Type d'exception : ValueError
                   NameError
                   TypeError
                   ZeroDivisionError
                   OSError
                   AssertionError

------------------------------------------------------------------------------------
            La programmation orienté-objet (POO) avec le language Python
------------------------------------------------------------------------------------

Classe              : plan de conception, genre (ex: Humain)
Objet               : instance de classe (ex: Julien)

Attribut            : variable de clase (ex: prénom, age, sexe, taille, ...)
        Mot clé     : _XXXXX
Propriété           : manière de manipuler/contrôler les attributs => encapsulation (lecture seule, accès non autorisé en dehors de la classe, etc.)
        Mot clé     : property(<guetter>, <setter>, <deleter>, <helper>)

Méthode             : fonction sur une instance => objet (ex: manger, marcher, parler, ...)
        Mot clé     : def .....(self):
Méthode de classe   : fonction d'une classe (explication à venir plustard ...)
        Mot clé     : def .....(cls):
Méthode statique    : fonction indépendante mais "lié" à une classe.

Héritage            : classe Fille qui hérite d'une classe Mère (Fille est une sorte de Mère)
                    : classe Chat hérite de la classe Animal (Chat est sorte d'Animal)


------------------------------------------------------------------------------------
                             Les chaînes de caractères
------------------------------------------------------------------------------------

Une méthode de chaîne travaille sur une copie, et pas sur la chaine elle-même

help(str) --> affiche la doc str
str.upper() --> majuscule
str.lower() --> minuscule
str.capitalize() --> majuscule au début de chaque mot
str.title() 
str.center(<largeur>, <caractère_remplissage>)
str.strip() --> enlève les espaces 
str.find(<chaîne>, <début>, <fin>)
str.index(<chaîne>, <début>, <fin>)
str.replace(<ancienne>, <nouvelle>, <occurences>) --> remplace par la nouvelle
str.split(" ") --> découpe au caractère passer en paramètre (créé une liste)
" ".join() --> joint les caractères d'une liste en une chaîne de caractère 
str.isalpha()
str.isdigit()
str.isdecimal()
str.isnumeric()
str.isalphanum()
str.islower()
str.isupper()
str.isidentifier()
str.iskeyword()


------------------------------------------------------------------------------------
                                   Les listes
------------------------------------------------------------------------------------

help(list) --> affiche la doc de list

liste[]     --> créer un nouvelle liste
liste[a]*X  --> répette l'élément X fois (ex: liste[a]*3 --> [a,a,a])

liste[x]    --> affiche element d indice X
liste[-x]   --> affiche le Xème élément en partant de la fin
liste[:]    --> affiche tous les éléments
liste[:x]   --> affiche les X premiers éléments
liste[-x:]  --> affiche les X derniers éléments
liste[a:b]  --> affiche de l'élément d'indice A à l'élément d'indice B (exclus)

liste.clear()   --> efface la liste
liste.sort()    --> tri par ordre croissant une liste
liste.reverse() --> inverse la liste (ex: 1.2.3.4 --> 4.3.2.1)
liste.count()   --> compte le nombre d'itération dans la liste (ex: ["potion", "potion", "potion"] --> potion = 3)

liste1 += liste2 --> ajoute les éléments de liste2 a la fin de liste1
enumerate()      --> affiche les indices et les éléments de la liste
len(<list>)      --> retourne la taille (le nombre d'éléments)


------------------------------------------------------------------------------------
                                   Les tuples
------------------------------------------------------------------------------------

(!) Tuple : conteneur immuable (dont on ne peut modifier les valeurs)
Création de tuple   : mon_tuple = ()     #vide
                      mon_tuple = 17,    #une seule valeur
                      mon_tuple = (14,)  #une seule valeur
                      mon_tuple = (4, 6) #plusieurs valeurs

Accès au valeurs    : mon_tuple[X]       #valeur d'indice X

2 raisons d'utiliser les tuples : affectation multiple de variable
                                  retour multiple de fonction


------------------------------------------------------------------------------------
                                Les dictionnaires
------------------------------------------------------------------------------------   

help(dict)

Créartion de dictionnaire : dico = {}                                #vide
                            dico = {<clé>:<valeur>, <clé2>:<valeur>} #plusieurs valeur

Accès à une valeur        : dico[<cle>]
Ajout et modification     : dico[<cle>] = <valeur>
Suppression               : dico.pop(<cle>)
                            del dico[<cle>]

dico.keys()   --> retourne les clés
dico.values() --> retourne les valeurs
dico.items()  --> retourne les clés et les valeurs
dico.copy()   --> copie le dictionnaire dans un autre disctionnaire (ex: dico2 = dico1.copy()) 


------------------------------------------------------------------------------------
                                   Les fichiers
------------------------------------------------------------------------------------ 

Modes d'ouverture   : r  (lecture seule)
                      w  (écriture avec remplacement)
                      a  (écriture avec ajout en fin de fichier)
                      x  (lecture et écriture)
                      r+ (lecture/écriture dans un même fichier)

Lecture de fichier  : read()        #lit tout le fichier
                      readline()    #lit une seule ligne
                      redlines()    #lit toutes les lignes a partir du curseur

Ecriture de fichier : write()       #écris en chaîne de caractère

open(<link>, <mode>) --> ouvre un fichier selon le mode
xx.close()           --> ferme le fichier

with open(<link>, <mode>) as XX --> pas besoin de fermer le fichier a la fin


------------------------------------------------------------------------------------
                                     Tkinter
------------------------------------------------------------------------------------ 

import tkinter

mainapp.minsize(640, 480)
mainapp.maxsize(1280, 720)
mainapp.resizable(width=False, height=False)  --> ne peut pas être redimensionner
mainapp.sizefrom("user")
mainapp.positionfrom("user")

geometry("XxY+a+b") --> a (vers la droitre)  /  b (vers le bas)

centrer la fenetre  --> position_X = (largeur_ecran // 2) - (largeur_fentre // 2)
                    --> position_Y = (hauteur_ecran // 2) - (hauteur_fenetre // 2)

<nom_variable> = <nom_widger>(<widget_parent>, <params>...)
message_welcome = tkinter.Message(app, text=" ")
entry_name = tkinter.Entry(app)
entry_name = tkinter.Entry(app, show="*", exportselection=0) --> montre des "****" et peux pas etre copier (ctrl-c)
button_quit = tkinter.Button(app, text="OK", command=<fonction>)

check_widget = tkinter.Checkbutton(app, text="", offvalue=<value>, onvalue=<value>)
radio_widget = tkinter.Radiobutton(app, text="homme", value=<value>)
scale_widget = tkinter.Scale(app, from_=<value>, to=<value>, ...)
spin_widget  = tkinter.Spinbox(app, from_=<value>, to=<value>)
liste_wiget  = tkinter.Listbox(app) --> (puis)  liste_wiget.insert(1, " ")

Boutton : showerror
          showinfo
          showwarning

Modal   : messagebox.askquestion()
                    .askokcancel()
                    .askyesno()
                    .askretrycancel()

Utilisation de sticky   : sticky=n --> nord
                          sticky=s --> sud
                          sticky=e --> est
                          sticky=w --> ouest

Utilisation de place    : place(x= , y= )

add_checkbutton()
add_radiobutton()
add_separator()


------------------------------------------------------------------------------------
                                 La gestion de temps
------------------------------------------------------------------------------------

import time

time.time()
    .sleep()
    .localtime()
    .mktime()
    .strftime()

               localtime()
(TIMESTAMP) ---------------> Structure de temps
            <---------------
                mktime()

Format  : %d ---> jour     (01 à 31)
          %m ---> mois     (01 à 12)
          %Y ---> année    (ex: 2018)
          %H ---> heures   (00 à 23)
          %I ---> minutes  (00 à 59)
          %S ---> secondes (00 à 59)
          %p ---> AM/PM
          %A ---> jour semaine (ex: lundi)
          %B ---> mois         (ex: janvier)
          %Z ---> fuseau horaire (timezone) 


------------------------------------------------------------------------------------
                                La gestion de dates
------------------------------------------------------------------------------------

import datetime


------------------------------------------------------------------------------------
                                     Cx_Freeze
------------------------------------------------------------------------------------

from cx_Freeze import setup, Executable

setup(
    name = "<nom_du_programme>",
    version = "<version>",
    description = "<description>",
    executables = [Executable("<link_programme>")]
)
"""