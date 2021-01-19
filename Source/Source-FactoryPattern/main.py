from functools import partial
import sys
from tkinker_calc import tkinkerCalculator
from pyqt5_calc import PyCalcCtrl


class Calculator():
    def __init__(self, calc_type):
        if('tk' in calc_type):
            self.calc_type = 'tkinker'
            self.calc = tkinkerCalculator()
        elif ('qt' in calc_type):
            self.calc_type = 'pyqt5'
            self.calc = PyCalcCtrl()


main = Calculator('tkinker')

if(main.calc_type):
    main.calc()
else:
    print('Esa no es una opcion valida')
