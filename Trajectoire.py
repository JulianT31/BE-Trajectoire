import math

import numpy as np


class Trajectoire:

    def __init__(self, A, B, V, theta=0, Te=0.1):
        # ====================
        # Constantes
        # ====================
        # Tuple (x,y,z)
        self.A = A
        self.B = B
        # vitesse
        self.V = V
        self.tetha = theta

        # Temps
        self.t0 = 0
        self.t1 = 0
        self.t2 = 0
        self.Te = Te
        self.size_vector_t = 0
        self.t_vector = 0

        # Stocker avec des tuples
        self.a = (self.V / self.t1)
        self.b = self.V
        self.s = 0
        self.sd = 0
        self.sdd = 0

        self.u = 0
        self.d = 0

        # Trajectoire opérationnelle
        self.pos = 0
        self.speed = 0
        self.acc = 0

        # init
        self.__init()

    def __get_discret(self):
        self.size_vector_t = (self.t2 // self.Te) + 1
        self.t_vector = np.array([self.t0 + i * self.Te for i in range(int(self.size_vector_t))])

    def __init(self):
        self.__generate_t()

        # Calcul de la distance entre A et B
        self.d = math.sqrt((self.B[0] - self.A[0]) ** 2 +
                           (self.B[1] - self.A[1]) ** 2 +
                           (self.B[2] - self.A[2]) ** 2)

        # Vecteur unitaire entre A et B
        self.u = ((self.B[0] - self.A[0]) / self.d,
                  (self.B[1] - self.A[1]) / self.d,
                  (self.B[2] - self.A[2]) / self.d)

        # Calcul de tous les instants d'échantillonnage
        self.__get_discret()

    def __generate_sd(self):
        self.sd = np.array([self.a * self.t_vector if self.t_vector <= self.t1 else
                            (-1 * self.a) * (self.t_vector - self.t1) + self.b])

    def __generate_s(self):
        # todo verifier ca
        self.s = np.array(
            (self.t_vector * self.sd) / 2 if self.t_vector <= self.t1 else (self.t1 * self.V) - (
                    ((self.t1 * 2 - self.t_vector) * self.sd) / 2))

    def __generate_sdd(self):
        self.sdd = np.array([self.a if self.t_vector <= self.t1 else (-1 * self.a)])

    def __generate_all_s(self):
        self.__generate_sd()
        self.__generate_s()
        self.__generate_sdd()

    def __generate_t(self):
        # calcul de t2 & t1
        pass

    def __generate_opp(self):
        # Position
        self.pos = (np.array(self.A[0] + (self.s * self.u[0])),
                    np.array(self.A[1] + (self.s * self.u[1])),
                    np.array(self.A[2] + (self.s * self.u[2])))

        # Vitesse
        self.speed = (np.array([self.u[0] * self.sd]),
                      np.array([self.u[1] * self.sd]),
                      np.array([self.u[2] * self.sd]))

        # Vitesse
        self.acc = (np.array([self.u[0] * self.sdd]),
                    np.array([self.u[1] * self.sdd]),
                    np.array([self.u[2] * self.sdd]))

    def vitesse_o5(self):
        # todo : A tester
        return np.array([math.sqrt((self.speed[0] ** 2) + (self.speed[1] ** 2) + (self.speed[2] ** 2))])

    def simulation(self):
        # Calcul de s(t)  s°(t) s°°(t)
        self.__generate_all_s()

        # Calcul de x(s), y(s), z(s) et  x°(s), y°(s), z°(s) etc..
        self.__generate_opp()


if __name__ == '__main__':
    traj = Trajectoire()
    traj.simulation()
