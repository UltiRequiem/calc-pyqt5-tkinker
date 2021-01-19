from tkinker_calc import TkinkerCalculator
from pyqt5_calc import main


class Calculator:
    def __init__(self):
        calc_type = input('¿Que calculadora vas a usar?: ')
        print(calc_type)

        if calc_type == 'tkinker':
            TkinkerCalculator()

        elif calc_type == 'pyqt5':
            main()

        else:
            print('Esa no es una opción valida')


Calculator()

# main = Calculator('tkinker')
#
# if main.calc_type:
#     main.calc()
# else:
#     print('Esa no es una opción valida')
