from typing import Dict, List

import numpy as np
import pandas as pd

from ViewModel.Parameter import Parameter


class ViewModel:

    def __init__(self, parameter_dict: Dict[Parameter, int], text_file_list):
        self.parameter_dict = parameter_dict
        self.text_file_list = sorted(text_file_list)

    @property
    def time_range(self) -> np.ndarray:
        return np.linspace(0, len(self.text_file_list) - 1, len(self.text_file_list))

    @property
    def mode_num(self) -> int:
        return self.parameter_dict[Parameter.mode_num]

    @property
    def energy_list(self) -> np.ndarray:
        energy_list = []
        for text_file in self.text_file_list:
            all_data = np.loadtxt(text_file)
            energy = all_data[:, self.parameter_dict[Parameter.ene_num]]
            energy_list.append(energy)
        return np.array(energy_list).T

    @property
    def parameter_list(self):
        table = pd.DataFrame(np.loadtxt(self.text_file_list[0]))
        r_list = np.array(sorted(set(table.iloc[:, self.parameter_dict[Parameter.r_num]])))
        theta_list = np.array(sorted(set(table.iloc[:, self.parameter_dict[Parameter.theta_num]])))
        return r_list, theta_list

