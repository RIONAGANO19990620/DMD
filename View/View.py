from typing import Dict

import streamlit as st

from ViewModel.Parameter import Parameter


class View:

    @staticmethod
    def __side_menu() -> Dict[Parameter, int]:
        parameter_dict: Dict[Parameter, int] = {}
        st.sidebar.markdown('Set Parameter')
        for parameter in Parameter:
            param_num = st.sidebar.number_input(parameter.value)
            parameter_dict[parameter] = param_num
        return parameter_dict

    @staticmethod
    def view() -> None:
        parameter_dict = View.__side_menu()
        txt_file_list = st.file_uploader('ファイルアップロード', type='txt', accept_multiple_files=True)







