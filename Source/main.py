from tkinker_calc import TkinkerCalculator
from pyqt5_calc import main


class Calculator:
    def __init__(self):
        calc_type = input('What calculator are you going to use?: ')

        if calc_type == 'tkinker':
            TkinkerCalculator()

        elif calc_type == 'pyqt5':
            main()

        else:
            print("That's not a valide option.Valide Options: PyQt5 and Tkinker.")


Calculator()
