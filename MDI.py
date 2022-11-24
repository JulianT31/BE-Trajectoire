import numpy as np


class MDI:
    def __init__(self, xd, yd, zd):
        self.X_d = np.array([xd, yd, zd])

        self.jacobienne = np.eye(3, dtype=int)
        self.inv_jacobienne = np.array([])
        self.__inv_jacobienne()

    def __generate_jacobienne(self):
        pass
        # todo  avec les trucs de gars

    def __inv_jacobienne(self):
        if np.linalg.det(self.jacobienne) != 0:
            self.inv_jacobienne = np.linalg.inv(self.jacobienne)
        else:
            print("ERROR : jacobienne pas inversible (det = 0)")

    def get_values(self):
        return np.dot(self.inv_jacobienne, self.X_d)


if __name__ == '__main__':
    mdi = MDI(5, 5, 5)
    print(mdi.get_values())
