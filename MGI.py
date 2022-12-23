import numpy as np

from data import *


class MGI:
    def __init__(self):
        pass

    def calculate_qn(self, X, Y, Z, theta):
        # q3
        q3 = Z - h1 - h2

        # q2
        W2 = L3 + L4
        W = L2
        Z_1 = X - (L5 * np.cos(theta)) - L1
        Z_2 = Y - (L5 * np.sin(theta))

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
        q4 = theta - q1 - q2
        q4_bis = theta - q1_bis - q2_bis

        deux_pi = 2 * np.pi
        # return [q1, q2, q3, q4], [q1_bis, q2_bis, q3, q4_bis]
        return [(q1 + deux_pi) % deux_pi, (q2 + deux_pi) % deux_pi, q3, (q4 + deux_pi) % deux_pi], \
               [(q1_bis + deux_pi) % deux_pi, (q2_bis + deux_pi) % deux_pi, q3, (q4_bis + deux_pi) % deux_pi]
