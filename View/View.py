from typing import Dict

import numpy as np
import streamlit as st

from ViewModel.Factory import Factory
from ViewModel.Parameter import Parameter


class View:

    @staticmethod
    def __side_menu() -> Dict[Parameter, int]:
        parameter_dict: Dict[Parameter, int] = {}
        st.sidebar.markdown('Set Parameter')
        for parameter in Parameter:
            param_num = st.sidebar.number_input(parameter.value)
            parameter_dict[parameter] = int(param_num)
        return parameter_dict

    @staticmethod
    def __create_view_model(parameter_dict, data_list):
        from ViewModel.ViewModel import ViewModel
        return ViewModel(parameter_dict, data_list)

    @staticmethod
    def __create_plot(view_model):
        factory = Factory(view_model)
        fig = factory.create_fig()
        st.subheader('Calculation Result')
        st.pyplot(fig)

    @staticmethod
    def __create_data_list(txt_file_list):
        data_list = []
        for file_list in txt_file_list:
            data = file_list.read().decode()
            array = np.array(data.split(), dtype=float)
            array = array.reshape(len(array) // 3, 3)
            data_list.append(array)
        return data_list

    @staticmethod
    def view() -> None:
        parameter_dict = View.__side_menu()
        txt_file_list = st.file_uploader('ファイルアップロード', type='txt', accept_multiple_files=True)

        if st.button('DMD'):
            data_list = View.__create_data_list(txt_file_list)
            view_model = View.__create_view_model(parameter_dict, data_list)
            View.__create_plot(view_model)







