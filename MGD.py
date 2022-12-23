import numpy as np
from data import *


class MGD:

    def __init__(self):
        self.nb_liaison = 4
        self.list_qi = []
        self.list_tij = []

    def __generate_matrices_H(self):
        t01 = np.array([[np.cos(self.list_qi[0]), -np.sin(self.list_qi[0]), 0, L1],
                        [np.sin(self.list_qi[0]), np.cos(self.list_qi[0]), 0, 0],
                        [0, 0, 1, h1],
                        [0, 0, 0, 1],
                        ])

        t12 = np.array([[np.cos(self.list_qi[1]), -np.sin(self.list_qi[1]), 0, L1],
                        [np.sin(self.list_qi[1]), np.cos(self.list_qi[1]), 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1],
                        ])

        t23 = np.array([[1, 0, 0, L3],
                        [0, 1, 0, 0],
                        [0, 0, 1, self.list_qi[2]],
                        [0, 0, 0, 1],
                        ])

        t34 = np.array([[np.cos(self.list_qi[3]), -np.sin(self.list_qi[3]), 0, L4],
                        [np.sin(self.list_qi[3]), np.cos(self.list_qi[3]), 0, 0],
                        [0, 0, 1, h2],
                        [0, 0, 0, 1],
                        ])

        self.list_tij = [t01, t12, t23, t34]

    def __get_T_0_N(self):
        return self.__generate_T_i_j(0, self.nb_liaison)

    def __generate_T_i_j(self, i, j):
        if 0 <= i < j <= self.nb_liaison:
            t_i_j = self.list_tij[i]
            for k in range(i + 1, j):
                t_i_j = np.dot(t_i_j, self.list_tij[k])

            return t_i_j

        else:
            print("generate_t_i_j : Probleme d'index")

    def __get_Xp(self):
        t04 = self.__get_T_0_N()
        R04 = t04[:3, :3]
        translation = np.transpose(np.array([t04[0, 3], t04[1, 3], t04[2, 3]]))
        vect_col = np.array([L5, 0, 0])

        Xp = translation + np.dot(R04, vect_col)
        return Xp

    def get_values(self, list_qi):
        # Config
        self.list_qi = list_qi
        self.__generate_matrices_H()

        Xp = self.__get_Xp()
        t04 = self.__get_T_0_N()

        arcos = np.arccos(t04[0][0])
        arsin = np.arcsin(t04[1][0])
        if arsin < 0:
            teta = -arcos
        else:
            teta = arcos

        return Xp, teta

    def get_values_robot(self, list_qi):
        # Config
        self.list_qi = list_qi
        self.__generate_matrices_H()

        # ajout centre robot
        x = [0]
        y = [0]
        z = [0]

        # calcul des coords de chaque centre des liaisons
        for i in range(1, self.nb_liaison + 1):
            t0i = self.__generate_T_i_j(0, int(i))
            coord = np.dot(t0i, np.array([0, 0, 0, 1]))
            x.append(coord[0])
            y.append(coord[1])
            z.append(coord[2])

        # Ajout coords organe terminal
        Xp = self.__get_Xp()
        x.append(Xp[0])
        y.append(Xp[1])
        z.append(Xp[2])

        return x, y, z
