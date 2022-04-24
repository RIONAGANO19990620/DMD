from enum import Enum


class Parameter(Enum):
    theta_num = 'θの列番号'#defalut 2
    ene_num = 'ポテンシャルエネルギーの列番号' #defalut 1
    r_num = 'rの列番号' #defalut 0
    mode_num = 'モード数'