import numpy as np


class MGD:

    def __init__(self, list_qi, list_longueur, h1, h2):
        self.nb_liaison = len(list_qi)
        self.list_qi = list_qi
        self.list_longueur = list_longueur
        self.h1 = h1
        self.h2 = h2
        self.list_tij = []

        self.__generate_matrices_H()

    def __generate_matrices_H(self):
        t01 = np.array([[np.cos(self.list_qi[0]), -np.sin(self.list_qi[0]), 0, self.list_longueur[0]],
                        [np.sin(self.list_qi[0]), np.cos(self.list_qi[0]), 0, 0],
                        [0, 0, 1, self.h1],
                        [0, 0, 0, 1],
                        ])

        t12 = np.array([[np.cos(self.list_qi[1]), -np.sin(self.list_qi[1]), 0, self.list_longueur[1]],
                        [np.sin(self.list_qi[1]), np.cos(self.list_qi[1]), 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1],
                        ])

        t23 = np.array([[1, 0, 0, self.list_longueur[2]],
                        [0, 1, 0, 0],
                        [0, 0, 1, self.list_qi[2]],
                        [0, 0, 0, 1],
                        ])

        t34 = np.array([[np.cos(self.list_qi[3]), -np.sin(self.list_qi[3]), 0, self.list_longueur[3]],
                        [np.sin(self.list_qi[3]), np.cos(self.list_qi[3]), 0, 0],
                        [0, 0, 1, self.h2],
                        [0, 0, 0, 1],
                        ])

        self.list_tij = [t01, t12, t23, t34]

    def get_T_0_N(self):
        return self.generate_t_i_j(0, len(self.list_tij))

    def generate_t_i_j(self, i, j):
        if 0 <= i < j <= self.nb_liaison:
            t_i_j = self.list_tij[i]
            for k in range(i + 1, j):
                t_i_j = np.dot(t_i_j, self.list_tij[k])

            return t_i_j

        else:
            print("generate_t_i_j : Probleme d'index")


# def is_inversible(mat):
#     return True if determinant(mat) != 0 else False
#
#
# def determinant(mat):
#     return np.linalg.det(mat)

if __name__ == '__main__':
    qn = np.array([0, 0, 5, 0])
    L = np.array([0, 0, 0, 0])
    h1 = 10
    h2 = 5

    mgd = MGD(qn, L, h1, h2)

    t24 = mgd.generate_t_i_j(2, 4)
    t04 = mgd.generate_t_i_j(0, 4)
    print("T24 = \n" + str(t24))
    print("T04 = \n" + str(t04))
