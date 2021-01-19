from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from functools import partial
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from tkinter import *

ERROR_MSG = 'ERROR'

what_calc = str(input('Que calculadora quieres usar: '))

if what_calc == 'tkinker':
    root = Tk()
    root.title('Python Calculator')

    e = Entry(root, width=35, borderwidth=5)
    e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    f_num = 0
    math = ''


    def button_click(number):
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))


    def button_clear():
        e.delete(0, END)


    def button_equal():
        second_number = e.get()
        e.delete(0, END)

        if math == "Addition":
            e.insert(0, f_num + float(second_number))
        elif math == "Subtract":
            e.insert(0, f_num - float(second_number))
        elif math == "Multiply":
            e.insert(0, f_num * float(second_number))
        elif math == "Divide":
            e.insert(0, f_num / float(second_number))


    def set_calc(value):
        first_number = e.get()
        global math, f_num
        math = value
        f_num = float(first_number)
        e.delete(0, END)


    def button_add():
        set_calc("Addition")


    def button_divide():
        set_calc("Divide")


    def button_multiply():
        set_calc("Multiply")


    def button_subtract():
        set_calc("Subtract")


    def buttons_builder(text, x, y, cmd):
        return Button(root, text=text, padx=x, pady=y, command=cmd)


    # Number Buttons

    button_1 = buttons_builder("1", 40, 20, lambda: button_click(1))
    button_2 = buttons_builder("2", 40, 20, lambda: button_click(2))
    button_3 = buttons_builder("3", 40, 20, lambda: button_click(3))
    button_4 = buttons_builder("4", 40, 20, lambda: button_click(4))
    button_5 = buttons_builder("5", 40, 20, lambda: button_click(5))
    button_6 = buttons_builder("6", 40, 20, lambda: button_click(6))
    button_7 = buttons_builder("7", 40, 20, lambda: button_click(7))
    button_8 = buttons_builder("8", 40, 20, lambda: button_click(8))
    button_9 = buttons_builder("9", 40, 20, lambda: button_click(9))
    button_0 = buttons_builder("0", 40, 20, lambda: button_click(0))

    # Signs Buttons
    button_add = buttons_builder("+", 40, 20, button_add)
    button_equal = buttons_builder("=", 91, 20, button_equal)
    button_clear = buttons_builder("Clear", 79, 20, button_clear)
    button_subtract = buttons_builder("-", 41, 20, button_subtract)
    button_multiply = buttons_builder("*", 40, 20, button_multiply)
    button_divide = buttons_builder("/", 41, 20, button_divide)

    # Put The buttons on the screen

    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_0.grid(row=4, column=0)
    button_clear.grid(row=4, column=1, columnspan=2)
    button_add.grid(row=5, column=0)
    button_equal.grid(row=5, column=1, columnspan=2)

    button_subtract.grid(row=6, column=0)
    button_multiply.grid(row=6, column=1)
    button_divide.grid(row=6, column=2)

    # Loop

    root.mainloop()

elif what_calc == 'pyqt5':
    class PyCalcCtrl:

        def __init__(self, model, view):
            self._evaluate = model
            self._view = view
            self._connectSignals()

        def _calculateResult(self):
            result = self._evaluate(expression=self._view.displayText())
            self._view.setDisplayText(result)

        def _buildExpression(self, sub_exp):
            if self._view.displayText() == ERROR_MSG:
                self._view.clearDisplay()

            expression = self._view.displayText() + sub_exp
            self._view.setDisplayText(expression)

        def _connectSignals(self):
            for btnText, btn in self._view.buttons.items():
                if btnText not in {'=', 'C'}:
                    btn.clicked.connect(partial(self._buildExpression, btnText))

            self._view.buttons['='].clicked.connect(self._calculateResult)
            self._view.display.returnPressed.connect(self._calculateResult)
            self._view.buttons['C'].clicked.connect(self._view.clearDisplay)


    class PyCalcUi(QMainWindow):

        def setDisplayText(self, text):
            self.display.setText(text)
            self.display.setFocus()

        def displayText(self):
            return self.display.text()

        def clearDisplay(self):
            self.setDisplayText('')

        def _createDisplay(self):
            self.display = QLineEdit()
            self.display.setFixedHeight(35)
            self.display.setAlignment(Qt.AlignRight)
            self.display.setReadOnly(True)
            self.generalLayout.addWidget(self.display)

        def _createButtons(self):
            self.buttons = {}
            buttonsLayout = QGridLayout()
            buttons = {'7': (0, 0),
                       '8': (0, 1),
                       '9': (0, 2),
                       '/': (0, 3),
                       'C': (0, 4),
                       '4': (1, 0),
                       '5': (1, 1),
                       '6': (1, 2),
                       '*': (1, 3),
                       '(': (1, 4),
                       '1': (2, 0),
                       '2': (2, 1),
                       '3': (2, 2),
                       '-': (2, 3),
                       ')': (2, 4),
                       '0': (3, 0),
                       '00': (3, 1),
                       '.': (3, 2),
                       '+': (3, 3),
                       '=': (3, 4),
                       }
            for btnText, pos in buttons.items():
                self.buttons[btnText] = QPushButton(btnText)
                self.buttons[btnText].setFixedSize(40, 40)
                buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
            self.generalLayout.addLayout(buttonsLayout)

        def __init__(self):
            super().__init__()
            self.setWindowTitle('PyCalc')
            self.setFixedSize(235, 235)
            self.generalLayout = QVBoxLayout()
            self._centralWidget = QWidget(self)
            self.setCentralWidget(self._centralWidget)
            self._centralWidget.setLayout(self.generalLayout)
            self._createDisplay()
            self._createButtons()


    def evaluate_expression(expression):
        try:
            result = str(eval(expression, {}, {}))
        except Exception:
            result = ERROR_MSG

        return result


    def main():
        pycalc = QApplication(sys.argv)
        view = PyCalcUi()
        view.show()
        model = evaluate_expression
        PyCalcCtrl(model=model, view=view)
        sys.exit(pycalc.exec_())

    main()