# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:17:54 2020

@author: taix
"""
import matplotlib.pylab as plt;
import matplotlib.pyplot as pplt
import numpy as np


#############################################################################
# Affichage de la fonction f(t) et de ses dérivées fd(t) et fdd(t) 
#           et des temps de commutation
# INPUT:
#    numfig: numéro de la figure (entier)
#    nom: chaîne de caractèreS qui correspond à la fonction à afficher
#    f: valeurs discrètes de la fonction s en ordonnée du subplot haut
#    fd: valeurs discrètes de la fonction fd en ordonnée du subplot milieu
#    fdd: valeurs discrètes de la fonction fdd en ordonnée du subplot bas
#    t: valeurs discrètes du temps de 0 à tf en abscisse des 3 subplot
#    tc: liste des instants de commutation 
#
#    ATTENTION: il faut que les dimensions de f,fd,fdd et t soient identiques
#############################################################################
def affiche3courbes(numfig, nom, f, fd, fdd, t, tc):
    plt.figure(numfig)

    plt.subplot(311)
    plt.plot(t, f, "b+")
    plt.xlabel('Temps')
    plt.ylabel('Valeur de ' + nom)
    plt.grid(True)
    for x in tc:
        plt.axvline(x, color="g", linestyle="--")
    plt.title('Affichage des courbes fonction de ' + nom)
    plt.subplot(312)
    plt.plot(t, fd, "b+")
    plt.xlabel('Temps')
    plt.ylabel('Valeur de ' + nom + 'd')
    plt.grid(True)
    for x in tc:
        plt.axvline(x, color="g", linestyle="--")
    plt.subplot(313)
    plt.plot(t, fdd, "b+")
    plt.xlabel('Temps')
    plt.ylabel('Valeur de ' + nom + 'dd')
    plt.grid(True)
    for x in tc:
        plt.axvline(x, color="g", linestyle="--")

    plt.show()


def affichage_3D(pos_op, speed_op, acc_op, title=""):
    fig = plt.figure()

    ax = fig.add_subplot(131, projection='3d')
    ax.scatter(pos_op[0], pos_op[1], pos_op[2])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    ax = fig.add_subplot(132, projection='3d')
    ax.scatter(speed_op[0], speed_op[1], speed_op[2])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    ax = fig.add_subplot(133, projection='3d')
    ax.scatter(acc_op[0], acc_op[1], acc_op[2])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    plt.show()


#############################################################################
# Affichage d'une courbe 2D d'abscisse t et d'ordonnée d(t)
# INPUT:
#    numfig: numéro de la figure (entier)
#    nom: chaîne de caractèreS qui correspond à la fonction à afficher
#    t: valeurs discrètes du temps  en abscisse
#    d: valeurs discrètes de la fonction s en ordonnée 
#    coul: couleur de la courbe (exemple "r" pour rouge)
#
#    ATTENTION: il faut que les dimensions de d et t soient identiques
#############################################################################  
def affiche_courbe2D(numfig, nom, t, d, coul):
    plt.figure(numfig)
    plt.axis([-1.0, np.max(t), 0, 1.2 * np.max(d)])
    plt.plot(t, d, "-", label="ligne -", color=coul)
    plt.xlabel('Temps')
    plt.ylabel('Valeur de ' + nom)
    plt.title('Affichage de la courbe ' + nom)
    plt.show(block=True)  # affiche la figure a l'ecran


################################
def bloque_affiche():
    plt.show(block=True)
