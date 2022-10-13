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
    :return: une numpy array à n valeurs
    """
    size_vector_t, t_vector = get_discret(t0, t2, Te)
    t1 = t2 / 2  # attention peut etre division entiere

    # paramètre fonction affine
    a = (V / t1)
    b = V
    c = CI

    # calcul de s(t) en fonction de la valeur de t
    # si t1 < t < t2 => -ab+V
    # si  0 > t < t1 => ab+V
    speed_vector = np.array([a * t_vector[i] if t_vector[i] <= t1 else ((-1 * a) * (t_vector[i] - t1) + b) for i in
                             range(int(size_vector_t))])

    affichage_courbe(t_vector, speed_vector, "Courbe de .s(t) en fonction de t (en discret)", "bX")

    # calcul de s(t) (position)
    pos_vector = np.array(
        [(a / 2) * (t_vector[i] ** 2) + (b * t_vector[i]) + c if t_vector[i] <= t1 else
         ((-1 * a) / 2) * (t_vector[i] ** 2 - t1) + b * (t_vector[i] - t1) + c for i in
         range(int(size_vector_t))])

    affichage_courbe(t_vector, pos_vector, "Courbe de s(t) en fonction de t (en discret)", "bX")

    # calcul de s(t) (position)
    ac_vector = np.array([a if t_vector[i] <= t1 else (-1 * a) for i in
                          range(int(size_vector_t))])

    affichage_courbe(t_vector, ac_vector, "Courbe de s(t) seconde en fonction de t (en discret)", "bX")

    plt.show()


def affichage_courbe(x, y, title="", style=""):
    """
    Affiche une courbe selon x et y passé en paramètre
    :param x: numpy array à N valeurs
    :param y: numpy array à N valeurs
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

    affichage_3_courbes(V, t0, t2, Te)
