import numpy as np


class MGI:
    def __init__(self, list_l, theta):
        self.h1 = 1  #
        self.h2 = 1

        self.L1 = list_l[0]
        self.L2 = list_l[1]
        self.L3 = list_l[2]
        self.L4 = list_l[3]
        self.L5 = list_l[4]
        self.theta = theta

    def calculate_qn(self, X, Y, Z):
        # q3
        q3 = Z - self.h1 - self.h2

        # q2
        W2 = self.L3 + self.L4
        W = self.L2
        Z_1 = X - (self.L5 * np.cos(self.theta)) - self.L1
        Z_2 = Y - (self.L5 * np.sin(self.theta))

        cos_q2 = (Z_1 ** 2 + Z_2 ** 2 - W ** 2 - W2 ** 2) / (2 * W * W2)

        # if cos_q2 > 1:
        #     cos_q2 = 1

        sin_q2 = np.sqrt(1 - (cos_q2 ** 2))
        sin_q2_bis = -np.sqrt(1 - (cos_q2 ** 2))

        q2 = np.arctan2(sin_q2, cos_q2)
        q2_bis = np.arctan2(sin_q2_bis, cos_q2)
        # todo deux valeurs à prendre en compte

        # q1
        B1 = W + W2 * cos_q2
        B2 = W2 * sin_q2
        sin_q1 = ((B1 * Z_2) - (B2 * Z_1)) / (B1 ** 2 + B2 ** 2)
        cos_q1 = ((B1 * Z_1) + (B2 * Z_2)) / (B1 ** 2 + B2 ** 2)
        q1 = np.arctan2(sin_q1, cos_q1)

        B2_bis = W2 * sin_q2_bis
        sin_q1_bis = ((B1 * Z_2) - (B2_bis * Z_1)) / (B1 ** 2 + B2_bis ** 2)
        cos_q1_bis = ((B1 * Z_1) + (B2_bis * Z_2)) / (B1 ** 2 + B2_bis ** 2)
        q1_bis = np.arctan2(sin_q1_bis, cos_q1_bis)

        # q4
        q4 = self.theta - q1 - q2
        q4_bis = self.theta - q1_bis - q2_bis

        return q1, q1_bis, q2, q2_bis, q3, q4, q4_bis
