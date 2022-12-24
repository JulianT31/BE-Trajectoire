import numpy as np

from MDD import MDD
from MDI import MDI
from MGD import MGD
from MGI import MGI
from Trajectoire import Trajectoire


def test_MGD_MGI():
    print("========== Test MGD - MGI ===============")
    # MGD
    qn = np.array([0, np.pi / 2, np.pi / 2, np.pi / 2])
    print("Qn (deg)= ", np.rad2deg(qn))
    mgd = MGD()
    Xp, theta = mgd.get_values(qn)
    print(" ===== MGD : Résultats :")
    print("Xp = " + str(Xp))
    print("theta = " + str(theta))

    mgi = MGI()
    qn1, qn2 = mgi.calculate_qn(Xp[0], Xp[1], Xp[2], theta)

    print(" ===== MGI : Solutions possibles :")
    print("S1 (deg) = ", np.rad2deg(qn1))
    print("S2 (deg) = ", np.rad2deg(qn2))


def test_MDD_MDI():
    print("========== Test MDD - MDI ===============")
    qn = np.array([0, np.pi / 2, np.pi / 2, np.pi / 2])
    print("Qn (deg)= ", np.rad2deg(qn))
    mdi = MDI()
    X_d = (5, 5, 5, 0)  # xd,yd,zd, theta
    print("X_d = ", X_d)
    qd = mdi.get_values(qn, X_d)
    print(" ===== MDI : Résultats :")
    print("Qnd (deg)= ", np.rad2deg(qd))

    mdd = MDD()
    x_d = mdd.get_values(qn, qd)

    print(" ===== MDD : ")
    print("X_d = ", x_d)


if __name__ == '__main__':
    test_MGD_MGI()
    test_MDD_MDI()  # ne fonctionne pas

    A = (0, 1, 8)
    B = (4, 2, 9)
    # A = (2, 2, 0)
    # B = (2, 2, 2)
    V = 1  # V != 0
    theta = 0  # en rad
    traj = Trajectoire(A, B, theta, V, Te=0.01)
    traj.simulation()
    traj.display()


