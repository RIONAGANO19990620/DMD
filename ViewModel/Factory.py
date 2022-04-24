from Model.DMD import DMD
from ViewModel.PlotModeStructure import PlotModeStructure
from ViewModel.ViewModel import ViewModel


class Factory:

    def __init__(self, view_model: ViewModel):
        self.view_model = view_model

    def __create_dmd(self):
        return DMD(self.view_model.time_range, self.view_model.energy_list, self.view_model.mode_num)

    def create_fig(self):
        dmd = self.__create_dmd()
        phi, Psi = dmd.cul_phi_Psi()
        fig = PlotModeStructure.plot_mode_structure(phi, self.view_model.parameter_list, self.view_model.mode_num)
        return fig