import numpy as np


def get_T0N(qn, L1, L2, L3, L4, h1, h2):
    liste_m = generate_matrices_H(qn, L1, L2, L3, L4, h1, h2)
    print(liste_m)

    t0N = liste_m[0]
    for i in range(1, len(liste_m)):
        t0N = np.dot(t0N, liste_m[i])

    return t0N


def generate_matrices_H(qn, L1, L2, L3, L4, h1, h2):
    t01 = np.array([[np.cos(qn[0]), -np.sin(qn[0]), 0, L1],
                    [np.sin(qn[0]), np.cos(qn[0]), 0, 0],
                    [0, 0, 1, h1],
                    [0, 0, 0, 1],
                    ])
    t12 = np.array([[np.cos(qn[1]), -np.sin(qn[1]), 0, L2],
                    [np.sin(qn[1]), np.cos(qn[1]), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1],
                    ])
    t23 = np.array([[1, 0, 0, L3],
                    [0, 1, 0, 0],
                    [0, 0, 1, qn[2]],
                    [0, 0, 0, 1],
                    ])
    t34 = np.array([[np.cos(qn[3]), -np.sin(qn[3]), 0, L4],
                    [np.sin(qn[3]), np.cos(qn[3]), 0, 0],
                    [0, 0, 1, h2],
                    [0, 0, 0, 1],
                    ])

    return [t01, t12, t23, t34]


if __name__ == '__main__':
    L1 = 5
    L2 = 3
    L3 = 2
    L4 = 7
    h1 = 10
    h2 = 5

    qn = np.array([0, 0, 5, 0])
    print(get_T0N(qn, L1, L2, L3, L4, h1, h2))
