import re
import unittest

import numpy as np


class TestViewModel(unittest.TestCase):

    def setUp(self) -> None:
        file = open('./TestData/data.txt', 'r')
        self.file_dict = {}
        self.file_dict['data'] = file.read()

    def test_view_model(self):
        list = self.file_dict['data'].split("\\n")

        for data in list:
            array = np.array(re.sub("\\D", "", data))
        list[0] = re.sub(r'[^0-9]', ' ', list[0])
        array = np.array(self.file_dict['data'].split('\\n'))
        array = np.asfarray(array, dtype=float)
        print(type(array))