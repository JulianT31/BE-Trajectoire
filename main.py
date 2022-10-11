import numpy as np
import matplotlib.pyplot as plt


def get_discret(t0, t2, Te):
    """
    Retourne une numpy array à n valeurs discrete selon la période d'échantillonnage donnée dans un temps donnée .
    :param t0: debut intervalle
    :param t2: fin intervalle
    :param Te: période d'échantillonnage
    :return: une numpy array à n valeurs t (selon l'échantillonnage => (t2 // Te) + 1) )
    """
    # size of the vector
    size_vector_t = (t2 // Te) + 1
    t_vector = np.array([t0 + i * Te for i in range(int(size_vector_t))])

    return size_vector_t, t_vector


def creation_s_de_t(V, t0, t2, Te):
    """
    Calcul et retourne une numpy array
    :param V: valeur en ordonnée du point N
    :param t0: debut intervalle
    :param t2: fin intervalle
    :param Te: période d'échantillonnage
    :return: une numpy array à n valeurs
    """
    size_vector_t, t_vector = get_discret(t0, t2, Te)
    t1 = t2 / 2

    # paramètre fonction affine
    a = (V / t1)
    b = V

    # calcul de s(t) en fonction de la valeur de t
    # si t1 < t < t2 => -ab+V
    # si  0 > t < t1 => ab+V
    s_vector = np.array([a * t_vector[i] if t_vector[i] <= t1 else ((-1 * a) * (t_vector[i] - t1) + b) for i in
                         range(int(size_vector_t))])

    affichage_courbe(t_vector, s_vector, "bX")
    return s_vector

def affichage_courbe(x, y, style=""):
    """
    Affiche une courbe selon x et y passé en paramètre
    :param x: numpy array à N valeurs
    :param y: numpy array à N valeurs
    :param style: style de la courbe (par defaut ligne)
    :return:
    """
    plt.plot(x, y, style)
    plt.title("Courbe de .s(t) en fonction de t (en discret)")
    plt.xlabel('t')
    plt.ylabel('s(t)')
    plt.show()


if __name__ == '__main__':
    # Paramètres variables
    V = 10  # V != 0
    t0 = 0  # fixe
    t1 = 5
    t2 = 2 * t1
    Te = 0.5  # Te != 0 (souvent entre 1 et 10 ms)

    creation_s_de_t(V, t0, t2, Te)
