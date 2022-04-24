from typing import Dict, List

import numpy as np
import pandas as pd

from Model.DMD import DMD
from ViewModel.Parameter import Parameter
from ViewModel.PlotModeStructure import PlotModeStructure


class ViewModel:

    def __init__(self, parameter_dict: Dict[Parameter, int], data_list):
        self.parameter_dict = parameter_dict
        self.data_list = data_list

    @property
    def time_range(self) -> np.ndarray:
        return np.linspace(0, len(self.data_list) - 1, len(self.data_list))

    @property
    def mode_num(self) -> int:
        return self.parameter_dict[Parameter.mode_num]

    @property
    def energy_list(self) -> np.ndarray:
        energy_list = []
        for all_data in self.data_list:
            energy = all_data[:, self.parameter_dict[Parameter.ene_num]]
            energy_list.append(energy)
        return np.array(energy_list).T

    @property
    def parameter_list(self):
        table = pd.DataFrame(self.data_list[0])
        r_list = np.array(sorted(set(table.iloc[:, self.parameter_dict[Parameter.r_num]])))
        theta_list = np.array(sorted(set(table.iloc[:, self.parameter_dict[Parameter.theta_num]])))
        return r_list, theta_list

