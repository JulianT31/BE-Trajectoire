import math

import matplotlib.pyplot as plt
import numpy as np

import afficheCourbesTP as ac
from MGD import MGD
from MGI import MGI


class Trajectoire:
    """
    Classe trajectoire qui permet à partir de 4 paramètres A, B, theta, V,
    de simuler une trajectoire.
    """
    # Variable statique
    num_fig = 0

    def __init__(self, A, B, theta, V, Te=0.1):
        # ====================
        # Constantes
        # ====================
        # Tuple (x,y,z)
        self.A = A
        self.B = B
        self.d = math.sqrt((self.B[0] - self.A[0]) ** 2 +
                           (self.B[1] - self.A[1]) ** 2 +
                           (self.B[2] - self.A[2]) ** 2)

        self.CI = -self.d

        # vitesse
        self.V = V
        self.tetha = theta

        # Temps
        self.t0 = 0
        self.t1 = self.d / V
        self.t2 = 2 * self.t1
        self.Te = Te
        self.size_vector_t = 0
        self.t_vector = np.array([])

        # Stocker avec des tuples
        self.a = (self.V / self.t1)  # coefficient directeur (ax +b)
        self.b = self.V  # ordonnée à l'origine (ax +b)

        self.s = np.array([])
        self.sd = np.array([])
        self.sdd = np.array([])

        # Vecteur unitaire entre A et B
        self.u = ((self.B[0] - self.A[0]) / self.d,
                  (self.B[1] - self.A[1]) / self.d,
                  (self.B[2] - self.A[2]) / self.d)

        # Trajectoire opérationnelle
        self.pos = np.array([])
        self.speed = np.array([])
        self.acc = np.array([])

        self.speed_O5 = np.array([])

        # qn
        self.q1 = np.array([])
        self.q1_bis = np.array([])
        self.q2 = np.array([])
        self.q2_bis = np.array([])
        self.q3 = np.array([])
        self.q4 = np.array([])
        self.q4_bis = np.array([])

        # MGI
        self.mgi = MGI(self.tetha)
        self.mgd = MGD()

        # init
        self.__init()

    def __get_discret(self):
        """
        Calcul toutes les valeurs discrete selon la période d'échantillonnage donnée dans un temps de temps calculé (t0 à t2).
        """
        self.size_vector_t = (self.t2 // self.Te) + 1
        self.t_vector = np.array([self.t0 + i * self.Te for i in range(int(self.size_vector_t))])

    def __init(self):
        # Calcul de tous les instants d'échantillonnage
        self.__get_discret()
        self.__generate_all_s()

    def __generate_sd(self):
        self.sd = np.array([self.a * self.t_vector[i] if self.t_vector[i] <= self.t1 else (
                (-1 * self.a) * (self.t_vector[i] - self.t1) + self.b) for i in
                            range(int(self.size_vector_t))])

    def __generate_s(self):
        self.s = np.array(
            [(self.t_vector[i] * self.sd[i]) / 2 if self.t_vector[i] <= self.t1 else (self.t1 * self.V) - (
                    ((self.t1 * 2 - self.t_vector[i]) * self.sd[i]) / 2)
             for i in
             range(int(self.size_vector_t))])

    def __generate_sdd(self):
        self.sdd = np.array([self.a if self.t_vector[i] <= self.t1 else (-1 * self.a) for i in
                             range(int(self.size_vector_t))])

    def __generate_all_s(self):
        self.__generate_sd()
        self.__generate_s()
        self.__generate_sdd()

    def __generate_opp(self):
        # Position
        self.pos = (np.array(self.A[0] + (self.s * self.u[0])),
                    np.array(self.A[1] + (self.s * self.u[1])),
                    np.array(self.A[2] + (self.s * self.u[2])))

        # Vitesse
        self.speed = (np.array(self.u[0] * self.sd),
                      np.array(self.u[1] * self.sd),
                      np.array(self.u[2] * self.sd))

        # Acc
        self.acc = (np.array(self.u[0] * self.sdd),
                    np.array(self.u[1] * self.sdd),
                    np.array(self.u[2] * self.sdd))

    def __vitesse_O5(self):
        self.speed_O5 = np.array(
            [math.sqrt((self.speed[0][i] ** 2) + (self.speed[1][i] ** 2) + (self.speed[2][i] ** 2)) for i in
             range(int(len(self.speed[0])))])

    def simulation(self):
        # Calcul de s(t)  s°(t) s°°(t)
        self.__generate_all_s()

        # Calcul de x(s), y(s), z(s) et  x°(s), y°(s), z°(s) etc..
        self.__generate_opp()

        # Calcul de la vitesse du point O5
        self.__vitesse_O5()

        # Calcul des q avec MGI
        self.__generate_qn()

    def __increment_num_fig(self):
        Trajectoire.num_fig += 1
        return Trajectoire.num_fig

    def display(self, mouvement=True, operationnelle=True, O5=True, threeD=True):
        # Loi de mouvement
        if mouvement:
            ac.affiche3courbes(self.__increment_num_fig(), ("s", "sd", "sdd"),
                               "Représentation graphique de s, sd et sdd",
                               self.s, self.sd, self.sdd, self.t_vector, [self.t1])

        # Trajectoire opérationnelle
        if operationnelle:
            ac.affiche3courbes(self.__increment_num_fig(), ("x", "y", "z"),
                               "Représentation graphique de x(s), y(s), z(s)",
                               self.pos[0], self.pos[1], self.pos[2], self.t_vector, [self.t1])

            ac.affiche3courbes(self.__increment_num_fig(), ("xd", "yd", "zd"),
                               "Représentation graphique de xd(s), yd(s), zd(s)",
                               self.speed[0], self.speed[1], self.speed[2], self.t_vector, [self.t1])

            ac.affiche3courbes(self.__increment_num_fig(), ("xdd", "ydd", "zdd"),
                               "Représentation graphique de xdd(s), ydd(s), zdd(s)",
                               self.acc[0], self.acc[1], self.acc[2], self.t_vector, [self.t1])

        # Vitesse point O5
        if O5:
            ac.affiche_courbe2D(self.__increment_num_fig(), ("temps", "vitesse"), "Vitesse du point O5", self.t_vector,
                                self.speed_O5, "#2E86C1")

        if threeD:
            ac.affichage_3D(self.__increment_num_fig(), self.pos, "Position")

        ac.affiche4courbes(self.__increment_num_fig(), ("q1", "q2", "q3", "q4"),
                           "Représentation graphique de q1,q2,q3 et q4",
                           (self.q1, self.q1_bis), (self.q4, self.q4_bis), self.q3, (self.q4, self.q4_bis),
                           self.t_vector, [self.t1])

        plt.show()

    def __generate_qn(self):
        for i in range(int(len(self.t_vector))):
            q1, q1_bis, q2, q2_bis, q3, q4, q4_bis = self.mgi.calculate_qn(self.pos[0][i], self.pos[1][i],
                                                                           self.pos[2][i])

            self.q1 = np.append(self.q1, q1)
            self.q1_bis = np.append(self.q1_bis, q1_bis)
            self.q2 = np.append(self.q2, q2)
            self.q2_bis = np.append(self.q2_bis, q2_bis)
            self.q3 = np.append(self.q3, q3)
            self.q4 = np.append(self.q4, q4)
            self.q4_bis = np.append(self.q4_bis, q4_bis)


if __name__ == '__main__':
    A = (1, 6, 8)
    B = (1, 7, 8)
    V = 1  # V != 0
    theta = 1.5
    traj = Trajectoire(A, B, theta, V)
    traj.simulation()
    traj.display()

    # A = (0, 0, 0)
    # B = (5, 5, 50)
    # traj2 = Trajectoire(A, B, theta, V)
    # traj2.simulation()
    # # traj2.display()
    # traj2.display(mouvement=False, O5=False)
