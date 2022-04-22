from typing import List

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm


class PlotModeStructure:

    @staticmethod
    def plot_mode_structure(phi_list: np.ndarray, parameter_list: List[np.ndarray], mode_num: int):
        fig = plt.figure()
        r_list, theta_list = parameter_list
        r, theta = np.meshgrid(r_list, theta_list)
        for mode in range(1, mode_num + 1):
            ax = fig.add_subplot(1, mode_num, mode, polar=True)
            ax.set_title('mode{}'.format(mode), fontsize=20, y=0.99)
            ax.axis('off')
            ax.tick_params(labelsize=18)
            phi = phi_list[:, mode-1].reshape(len(r_list), -1).T.real
            plt.tight_layout()
            ctf = ax.contourf(r, theta, phi, cmap=cm.jet)
