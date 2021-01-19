from functools import partial
import sys
from tkinter import *

class tkinkerCalculator:
    def __init__(self):

        root = Tk()
        root.title('Python Calculator')

        e = Entry(root, width=35, borderwidth=5)
        e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        f_num = 0
        math = ''

        def button_click(self, number):
            current = e.get()
            e.delete(0, END)
            e.insert(0, str(current) + str(number))

        def button_clear(self):
            e.delete(0, END)

        def button_equal(self):
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

        def set_calc(self, value):
            first_number = e.get()
            global math, f_num
            math = value
            f_num = float(first_number)
            e.delete(0, END)

        def button_add(self):
            set_calc(self, "Addition")

        def button_divide(self):
            set_calc(self, "Divide")

        def button_multiply(self):
            set_calc(self, "Multiply")

        def button_subtract(self):
            set_calc(self, "Subtract")

        def buttons_builder(self,text, x, y, cmd):
            return Button(root, text=text, padx=x, pady=y, command=cmd)

        # Number Buttons

        button_1 = buttons_builder(self, "1", 40, 20, lambda: button_click(self, 1))
        button_2 = buttons_builder(self, "2", 40, 20, lambda: button_click(self, 2))
        button_3 = buttons_builder(self, "3", 40, 20, lambda: button_click(self, 3))
        button_4 = buttons_builder(self, "4", 40, 20, lambda: button_click(self, 4))
        button_5 = buttons_builder(self, "5", 40, 20, lambda: button_click(self, 5))
        button_6 = buttons_builder(self, "6", 40, 20, lambda: button_click(self, 6))
        button_7 = buttons_builder(self, "7", 40, 20, lambda: button_click(self, 7))
        button_8 = buttons_builder(self, "8", 40, 20, lambda: button_click(self, 8))
        button_9 = buttons_builder(self, "9", 40, 20, lambda: button_click(self, 9))
        button_0 = buttons_builder(self, "0", 40, 20, lambda: button_click(self, 0))

        # Signs Buttons
        button_add = buttons_builder(self, "+", 40, 20, button_add)
        button_equal = buttons_builder(self, "=", 91, 20, button_equal)
        button_clear = buttons_builder(self, "Clear", 79, 20, button_clear)
        button_subtract = buttons_builder(self, "-", 41, 20, button_subtract)
        button_multiply = buttons_builder(self, "*", 40, 20, button_multiply)
        button_divide = buttons_builder(self, "/", 41, 20, button_divide)

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
