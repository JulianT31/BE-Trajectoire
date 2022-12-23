# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:17:54 2020

@author: taix
adapté par Julian TRANI
"""
import matplotlib.pylab as plt


#############################################################################
# Affichage de la fonction f(t) et de ses dérivées fd(t) et fdd(t) 
#           et des temps de commutation
# INPUT:
#    numfig: numéro de la figure (entier)
#    axes: n-uplet des noms des axes y
#    title: chaîne de caractèreS qui correspond à la fonction à afficher
#    f: valeurs discrètes de la fonction s en ordonnée du subplot haut
#    fd: valeurs discrètes de la fonction fd en ordonnée du subplot milieu
#    fdd: valeurs discrètes de la fonction fdd en ordonnée du subplot bas
#    t: valeurs discrètes du temps de 0 à tf en abscisse des 3 subplot
#    tc: liste des instants de commutation 
#
#    ATTENTION: il faut que les dimensions de f,fd,fdd et t soient identiques
#############################################################################
def affiche3courbes(numfig, axes, title, f, fd, fdd, t, tc):
    plt.figure(numfig)

    plt.subplot(311)
    plt.plot(t, f, color="#2E86C1", marker='+')
    plt.xlabel('Temps')
    plt.ylabel(axes[0])
    plt.grid(True)
    for x in tc:
        plt.axvline(x, color="g", linestyle="--")
    plt.title(title)

    plt.subplot(312)
    plt.plot(t, fd, color="#2E86C1", marker='+')
    plt.xlabel('Temps')
    plt.ylabel(axes[1])
    plt.grid(True)
    for x in tc:
        plt.axvline(x, color="g", linestyle="--")

    plt.subplot(313)
    plt.plot(t, fdd, color="#2E86C1", marker='+')
    plt.xlabel('Temps')
    plt.ylabel(axes[2])
    plt.grid(True)
    for x in tc:
        plt.axvline(x, color="g", linestyle="--")


def affiche4courbes_q(numfig, axes, title, q1, q2, q3, q4, t, tc):
    plt.figure(numfig)

    plt.subplot(411)
    if len(q1) != 1:
        plt.scatter(t, q1[0], color="#2E86C1", marker='+', label="q1")
        plt.scatter(t, q1[1], color="#FFD500", marker='+', label="q1 bis")
    plt.xlabel('Temps')
    plt.ylabel(axes[0])
    plt.legend()
    plt.grid(True)
    for x in tc:
        plt.axvline(x, color="g", linestyle="--")
    plt.title(title)

    plt.subplot(412)
    plt.scatter(t, q2[0], color="#2E86C1", marker='+', label="q2")
    plt.scatter(t, q2[1], color="#FFD500", marker='+', label="q2 bis")
    plt.xlabel('Temps')
    plt.ylabel(axes[1])
    plt.legend()
    plt.grid(True)
    for x in tc:
        plt.axvline(x, color="g", linestyle="--")

    plt.subplot(413)
    plt.scatter(t, q3, color="#2E86C1", marker='+', label="q3")
    plt.xlabel('Temps')
    plt.ylabel(axes[2])
    plt.legend()
    plt.grid(True)
    for x in tc:
        plt.axvline(x, color="g", linestyle="--")

    plt.subplot(414)
    plt.scatter(t, q4[0], color="#2E86C1", marker='+', label="q4")
    plt.scatter(t, q4[1], color="#FFD500", marker='+', label="q4 bis")
    plt.xlabel('Temps')
    plt.ylabel(axes[3])
    plt.legend()
    plt.grid(True)
    for x in tc:
        plt.axvline(x, color="g", linestyle="--")


def affiche4courbes_qd(numfig, axes, title, q1, q2, q3, q4, t, tc):
    plt.figure(numfig)

    plt.subplot(411)
    plt.scatter(t, q1[0], color="#2E86C1", marker='+', label="qd1")
    plt.xlabel('Temps')
    plt.ylabel(axes[0])
    plt.legend()
    plt.grid(True)
    for x in tc:
        plt.axvline(x, color="g", linestyle="--")
    plt.title(title)

    plt.subplot(412)
    plt.scatter(t, q2, color="#2E86C1", marker='+', label="qd2")
    plt.xlabel('Temps')
    plt.ylabel(axes[1])
    plt.legend()
    plt.grid(True)
    for x in tc:
        plt.axvline(x, color="g", linestyle="--")

    plt.subplot(413)
    plt.scatter(t, q3, color="#2E86C1", marker='+', label="q3")
    plt.xlabel('Temps')
    plt.ylabel(axes[2])
    plt.legend()
    plt.grid(True)
    for x in tc:
        plt.axvline(x, color="g", linestyle="--")

    plt.subplot(414)
    plt.scatter(t, q4, color="#2E86C1", marker='+', label="q4")
    plt.xlabel('Temps')
    plt.ylabel(axes[2])
    plt.legend()
    plt.grid(True)
    for x in tc:
        plt.axvline(x, color="g", linestyle="--")


def affichage_3D(numfig, pos_op, title):
    plt.figure(numfig)
    ax = plt.axes(projection='3d')
    ax.scatter(pos_op[0], pos_op[1], pos_op[2])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title(title)


def affichage_robot(numfig, x, y, z, title):
    plt.figure(numfig)

    color_list = ['k', 'b', 'b', 'b', 'b', 'r']
    ax = plt.axes(projection='3d')

    for i in range(len(x)):
        ax.scatter(x[i], y[i], z[i], c=color_list[i], s=100)

    ax.plot(x, y, z, color='b')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title(title)


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
def affiche_courbe2D(numfig, axes, title, t, d, coul):
    plt.figure(numfig)
    # plt.axis([-1.0, np.max(t), 0, 1.2 * np.max(d)])
    plt.plot(t, d, "-", label="ligne -", color=coul)
    plt.xlabel(axes[0])
    plt.ylabel(axes[1])
    plt.title(title)


################################
def bloque_affiche():
    plt.show(block=True)
