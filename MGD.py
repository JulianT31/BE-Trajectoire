import numpy as np

from MGI import MGI


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

    def __get_Xp(self):
        t04 = self.get_T_0_N()
        R04 = t04[:3, :3]
        translation = np.transpose(np.array([t04[0, 3], t04[1, 3], t04[2, 3]]))
        vect_col = np.array([self.list_longueur[4], 0, 0])

        Xp = translation + np.dot(R04, vect_col)
        return Xp

    def get_values(self):
        Xp = self.__get_Xp()
        t04 = self.get_T_0_N()

        arcos = np.arccos(t04[0][0])
        arsin = np.arcsin(t04[1][0])
        if arsin < 0:
            teta = -arcos
        else:
            teta = arcos

        return Xp, teta


# def is_inversible(mat):
#     return True if determinant(mat) != 0 else False
#
#
# def determinant(mat):
#     return np.linalg.det(mat)

if __name__ == '__main__':
    # MGD
    # qn = np.array([0, 0, 6, 0])
    L = np.array([1, 1, 1, 1, 1])
    h1 = 1
    h2 = 1
    #
    # mgd = MGD(qn, L, h1, h2)
    #
    # t24 = mgd.generate_t_i_j(2, 4)
    # t04 = mgd.generate_t_i_j(0, 4)
    # print("T24 = \n" + str(t24))
    # print("T04 = \n" + str(t04))
    #
    # Xp = mgd.get_Xp()
    # print("Xp = " + str(Xp))
    #
    # # MGI
    # mgi = MGI(L)
    # # q1, q2, q3, q4 = mgi.calculate_qn(6, 1, 8)
    # q1, q1_bis, q2, q2_bis, q3, q4, q4_bis = mgi.calculate_qn(Xp[0], Xp[1], Xp[2])
    #
    # print(q1)
    # print(q1_bis)
    # print(q2)
    # print(q2_bis)
    # print(q3)
    # print(q4)
    # print(q4_bis)

    # MGI
    # mgi = MGI(L,0)
    # q1, q1_bis, q2, q2_bis, q3, q4, q4_bis = mgi.calculate_qn(6, 0, 3)
    # print(q1, q1_bis, q2, q2_bis, q3, q4, q4_bis)
    #
    # qn = np.array([q1, q2, q3, q4])
    # mgd = MGD(qn, L, h1, h2)
    # Xp, theta = mgd.get_values()
    # print("Xp = " + str(Xp))
    # print("theta = " + str(theta))
    #
    # qn = np.array([q1_bis, q2_bis, q3, q4_bis])
    # mgd = MGD(qn, L, h1, h2)
    # Xp, theta = mgd.get_values()
    # print("Xp = " + str(Xp))
    # print("theta = " + str(theta))

    qn = np.array([0, np.pi / 2, np.pi / 2, np.pi / 2])
    mgd = MGD(qn, L, h1, h2)
    Xp, theta = mgd.get_values()
    print("Xp = " + str(Xp))
    print("theta = " + str(theta))

    mgi = MGI(L, theta)
    # q1, q2, q3, q4 = mgi.calculate_qn(6, 1, 8)
    q1, q1_bis, q2, q2_bis, q3, q4, q4_bis = mgi.calculate_qn(Xp[0], Xp[1], Xp[2])

    print(q1)
    print(q2)
    print(q3)
    print(q4)

    print("")
    print(q1_bis)
    print(q2_bis)
    print(q3)
    print(q4_bis)
