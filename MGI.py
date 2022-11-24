import numpy as np

from data import *


class MGI:
    def __init__(self, theta):
        self.theta = theta

    def calculate_qn(self, X, Y, Z):
        # q3
        q3 = Z - h1 - h2

        # q2
        W2 = L3 + L4
        W = L2
        Z_1 = X - (L5 * np.cos(self.theta)) - L1
        Z_2 = Y - (L5 * np.sin(self.theta))

        cos_q2 = (Z_1 ** 2 + Z_2 ** 2 - W ** 2 - W2 ** 2) / (2 * W * W2)

        sin_q2 = np.sqrt(1 - (cos_q2 ** 2))
        sin_q2_bis = -np.sqrt(1 - (cos_q2 ** 2))

        q2 = np.arctan2(sin_q2, cos_q2)
        q2_bis = np.arctan2(sin_q2_bis, cos_q2)

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
