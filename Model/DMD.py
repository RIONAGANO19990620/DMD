from numpy import dot, multiply, power
from numpy.linalg import pinv
from numpy.dual import svd
import numpy as np


class DMD:

    def __init__(self, time_range: np.ndarray, energy_list: np.ndarray, mode_num: int):
        self.time_range = time_range
        self.energy_list = energy_list
        self.mode_num = mode_num

    def cul_phi_Psi(self):
        X1 = self.__get_X1()
        X0 = self.__get_X0()
        U, Sig, Vh2 = svd(X0, False)
        t = self.time_range
        dt = 1
        r = self.mode_num
        Sig_r = np.eye(r)
        V = Vh2.conj().T[:, :r]
        for a in range(r):
            Sig_r[a][a] = 1 / Sig[a]
        U_r = U[:, :r]
        n_A = dot(dot(dot(np.conjugate(U_r.T), X1), V[:, :r]), Sig_r)

        lam, W = np.linalg.eig(n_A)

        phi = dot(dot(dot(X1, V[:, :r]), Sig_r), W)

        b = dot(pinv(phi), X0[:, 0])
        Psi = np.zeros([r, len(t)], dtype='complex')
        for i, _t in enumerate(t):
            Psi[:, i] = multiply(power(lam, _t / dt), b)

        return phi, Psi

    def __get_X1(self) -> np.ndarray:
        return self.energy_list[:, 1:]

    def __get_X0(self) -> np.ndarray:
        return self.energy_list[:, :-1]
