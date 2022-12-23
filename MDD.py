import numpy as np
from data import *


class MDD:
    def __init__(self):
        self.jacobienne = np.eye(3, dtype=int)
        self.inv_jacobienne = np.array([])

    def __generate_jacobienne(self, list_qi):
        s1 = np.sin(list_qi[0])
        c1 = np.cos(list_qi[0])

        s2 = np.sin(list_qi[1])
        c2 = np.cos(list_qi[1])

        self.jacobienne = np.array([[-L2 * s1 - L3 * c2 * s1 - L3 * s2 * c1 - L4 * c2 * s1 - L4 * s2 * c1,
                                     -L3 * c2 * s1 - L3 * s2 * c1 - L4 * c2 * s1 - L4 * s2 * c1, 0, 0],
                                    [L2 * c2 + L3 * c2 * c1 - L3 * s2 * s1 + L4 * c2 * c1 - L4 * s2 * s1,
                                     L3 * c2 * c1 - L3 * s2 * s1 + L4 * c2 * c1 - L4 * s2 * s1, 0, 0],
                                    [0, 0, 1, 0],
                                    [1, 1, 0, 1]])

    def get_values(self, list_qi, list_qdi):
        self.__generate_jacobienne(list_qi)
        return np.dot(self.jacobienne, list_qdi)  # return Xd
