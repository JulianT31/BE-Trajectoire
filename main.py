import math
import numpy as np
import matplotlib.pyplot as plt


def get_discret(t0, t2, Te):
    """
    Retourne une numpy array à n valeurs discrete selon la période d'échantillonnage donnée dans un temps donnée .
    :param t0: debut intervalle
    :param t2: fin intervalle
    :param Te: période d'échantillonnage
    :return: tuple => la taille du vecteur et une numpy array à n valeurs t (selon l'échantillonnage => (t2 // Te) + 1) )
    """
    # size of the vector
    size_vector_t = (t2 // Te) + 1
    t_vector = np.array([t0 + i * Te for i in range(int(size_vector_t))])

    return size_vector_t, t_vector


def affichage_3_courbes(V, t0, t2, Te, CI=0):
    """
    Calcul et retourne une numpy array
    :param V: valeur en ordonnée du point N
    :param t0: debut intervalle
    :param t2: fin intervalle
    :param Te: période d'échantillonnage
    :param CI: condition initiale
    :return:
    """
    size_vector_t, t_vector = get_discret(t0, t2, Te)
    t1 = t2 / 2  # attention peut etre division entiere

    # paramètre fonction affine
    a = (V / t1)
    b = V
    c = CI

    # calcul de s°(t) en fonction de la valeur de t (vitesse)
    # si t1 < t < t2 => -ab+V
    # si  0 > t < t1 => ab+V
    speed_vector = get_s_point_t(a, b, size_vector_t, t_vector)
    affichage_courbe(t_vector, speed_vector, "Vitesse en fonction de t (en discret)", "bX")

    # calcul de s(t) (position)
    # pos_vector = get_s_t(a, b, c, size_vector_t, t_vector)
    # affichage_courbe(t_vector, pos_vector, "Courbe de s(t) en fonction de t (en discret)", "bX")

    # calcul de s°°(t) (acceleration)
    ac_vector = get_s_seconde_t(a, b, size_vector_t, t_vector)
    affichage_courbe(t_vector, ac_vector, "Acceleration en fonction de t (en discret)", "bX")

    pos_vector = aire(t_vector, speed_vector, V, t1)
    affichage_courbe(t_vector, pos_vector,
                     "Distance en fonction du temps", "rX")

    sans_nom(pos_vector, t_vector, (0, 0, 0), (1, 1, 1))

    plt.show()


def get_s_t(a, b, c, size_vector_t, t_vector):
    return np.array(
        [(a / 2) * (t_vector[i] ** 2) + (b * t_vector[i]) + c if t_vector[i] <= t1 else
         ((-1 * a) / 2) * (t_vector[i] ** 2) + b * (t_vector[i]) + c for i in
         range(int(size_vector_t))])


def get_s_point_t(a, b, size_vector_t, t_vector):
    return np.array([a * t_vector[i] if t_vector[i] <= t1 else ((-1 * a) * (t_vector[i] - t1) + b) for i in
                     range(int(size_vector_t))])


def get_s_seconde_t(a, b, size_vector_t, t_vector):
    return np.array([a if t_vector[i] <= t1 else (-1 * a) for i in
                     range(int(size_vector_t))])


def aire(t_vector, s_vector, V, t1):
    size_vector_t = len(t_vector)

    return np.array(
        [(t_vector[i] * s_vector[i]) / 2 if t_vector[i] <= t1 else (t1 * V) - (
                ((t1 * 2 - t_vector[i]) * s_vector[i]) / 2)
         for i in
         range(int(size_vector_t))])


def sans_nom(s_vector, t_vector, A, B):
    # (x, y, z)
    l = math.sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2 + (A[2] - B[2]) ** 2)

    d = np.array(
        [t_vector[i] * s_vector[i] for i in range(int(len(s_vector)))])

    affichage_courbe(t_vector, d, "Position en fonction de la vitesse", "rX")


def affichage_courbe(x, y, title="", style=""):
    """
    Affiche une courbe selon x et y passé en paramètre
    :param x: numpy array à N valeurs
    :param y: numpy array à N valeurs
    :param title: titre de la courbe
    :param style: style de la courbe (par defaut ligne)
    :return:
    """

    plt.figure()
    plt.plot(x, y, style)
    plt.title(title)
    plt.xlabel('t')
    plt.ylabel('s(t)')


if __name__ == '__main__':
    # Paramètres variables
    V = 10  # V != 0
    t0 = 0  # fixe
    t1 = 5
    t2 = 2 * t1
    Te = 0.5  # Te != 0 (souvent entre 1 et 10 ms)

    affichage_3_courbes(V, t0, t2, Te, CI=0)
