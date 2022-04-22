import glob
import os
import unittest
from typing import Dict

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt, cm

from Model.DMD import DMD
from ViewModel.Parameter import Parameter
from ViewModel.PlotModeStructure import PlotModeStructure
from ViewModel.ViewModel import ViewModel


class testDMD(unittest.TestCase):

    @staticmethod
    def __listup_files(path):
        return [os.path.abspath(p) for p in glob.glob(path)]

    def setUp(self) -> None:
        parameter_dict: Dict[Parameter, int] = {}
        parameter_dict[Parameter.mode_num] = 1
        parameter_dict[Parameter.r_num] = 2
        parameter_dict[Parameter.ene_num] = 1
        parameter_dict[Parameter.theta_num] = 0
        p = './TestData/04P005**.txt'
        file_list = sorted(self.__listup_files(p))
        view_model = ViewModel(parameter_dict, file_list)
        self.time_range = view_model.time_range
        self.energy_list = view_model.energy_list
        self.mode_num = view_model.mode_num
        self.parameter_list = view_model.parameter_list

    def test_plot_DMD(self):
        dmd = DMD(self.time_range, self.energy_list, self.mode_num)
        phi, Psi = dmd.cul_phi_Psi()
        PlotModeStructure.plot_mode_structure(phi, self.parameter_list, self.mode_num)
        plt.show()

    def test_plot(self):
        file_path = './TestData/04P0050.txt'
        table = pd.DataFrame(np.loadtxt(file_path))
        r_list = np.array(sorted(set(table.iloc[:, 0])))
        si_ta_list = np.array(sorted(set(table.iloc[:, 2])))
        phi_list = np.array(table.iloc[:, 1])
        phi = phi_list.reshape(len(r_list), -1).T
        r, si_ta = np.meshgrid(r_list, si_ta_list)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1, polar=True)
        ax.set_title('mode{}'.format(1), fontsize=20, y=0.99)
        ax.axis('off')
        ax.tick_params(labelsize=18)
        plt.tight_layout()
        ctf = ax.contourf(r, si_ta, phi, 100, cmap=cm.jet)
        plt.show()


