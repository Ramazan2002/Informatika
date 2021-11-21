import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow
from PyQt5.QtGui import QFontDatabase
from typing import Union, Optional
from operator import add, sub, mul, truediv

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("fonts/Rubik-Regular.ttf")
        self.edit_line_max_len = self.ui.lineEdit.maxLength()
        self.ui.btn_0.clicked.connect(self.add_digit)
        self.ui.btn_1.clicked.connect(self.add_digit)
        self.ui.btn_2.clicked.connect(self.add_digit)
        self.ui.btn_3.clicked.connect(self.add_digit)
        self.ui.btn_4.clicked.connect(self.add_digit)
        self.ui.btn_5.clicked.connect(self.add_digit)
        self.ui.btn_6.clicked.connect(self.add_digit)
        self.ui.btn_7.clicked.connect(self.add_digit)
        self.ui.btn_8.clicked.connect(self.add_digit)
        self.ui.btn_9.clicked.connect(self.add_digit)
        self.ui.btn_clear.clicked.connect(self.clear_all)
        self.ui.btn_ce.clicked.connect(self.clear_edit)
        self.ui.btn_point.clicked.connect(self.add_point)
        self.ui.btn_calc.clicked.connect(self.calculate)
        self.ui.btn_add.clicked.connect(self.math_operation)
        self.ui.btn_sub.clicked.connect(self.math_operation)
        self.ui.btn_mul.clicked.connect(self.math_operation)
        self.ui.btn_div.clicked.connect(self.math_operation)
        self.ui.btn_neg.clicked.connect(self.negate)
        self.ui.btn_backspace.clicked.connect(self.backspace)
        self.ui.btn_0.clicked.connect(self.clear_temp_if_equality)
        self.ui.btn_1.clicked.connect(self.clear_temp_if_equality)
        self.ui.btn_2.clicked.connect(self.clear_temp_if_equality)
        self.ui.btn_3.clicked.connect(self.clear_temp_if_equality)
        self.ui.btn_4.clicked.connect(self.clear_temp_if_equality)
        self.ui.btn_5.clicked.connect(self.clear_temp_if_equality)
        self.ui.btn_6.clicked.connect(self.clear_temp_if_equality)
        self.ui.btn_7.clicked.connect(self.clear_temp_if_equality)
        self.ui.btn_8.clicked.connect(self.clear_temp_if_equality)
        self.ui.btn_9.clicked.connect(self.clear_temp_if_equality)


    @staticmethod
    def remove_trailing_zeros(num):
        num = str(float(num))
        return num[:-2] if num[-2:] == '.0' else num

    def add_digit(self):
        btn = self.sender()

        digit_buttons = ('btn_0', 'btn_1', 'btn_2', 'btn_3', 'btn_4',
                         'btn_5', 'btn_6', 'btn_7', 'btn_8', 'btn_9')

        if btn.objectName() in digit_buttons:
            if self.ui.lineEdit.text() == '0':
                self.ui.lineEdit.setText(btn.text())
            else:
                self.ui.lineEdit.setText(self.ui.lineEdit.text() + btn.text())

    def clear_all(self):
        self.ui.lineEdit.setText('0')
        self.ui.label.clear()

    def clear_edit(self):
        self.ui.lineEdit.setText('0')

    def add_point(self):
        if '.' not in self.ui.lineEdit.text():
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + '.')

    def add_temp(self) -> None:
        btn = self.sender()
        edit_line = self.remove_trailing_zeros(self.ui.lineEdit.text())

        if not self.ui.label.text() or self.get_math_sign() == '=':
            self.ui.label.setText(edit_line + f' {btn.text()} ')
            self.ui.lineEdit.setText('0')

    def get_entry_num(self) -> Union[int, float]:
        edit_line = self.ui.lineEdit.text().strip('.')
        return float(edit_line) if '.' in edit_line else int(edit_line)

    def get_temp_num(self) -> Union[int, float, None]:
        if self.ui.label.text():
            label = self.ui.label.text().strip('.').split()[0]
            return float(label) if '.' in label else int(label)

    def get_math_sign(self) -> Optional[str]:
        if self.ui.label.text():
            return self.ui.label.text().strip('.').split()[-1]

    def calculate(self) -> Optional[str]:
        operations = {
            '+': add,
            '-': sub,
            '*': mul,
            '÷': truediv
        }
        edit_line = self.ui.lineEdit.text()
        label = self.ui.label.text()
        if label:
            try:
                result = self.remove_trailing_zeros(str(operations[self.get_math_sign()]
                                                        (self.get_temp_num(), self.get_entry_num())))

                self.ui.label.setText(label + self.remove_trailing_zeros(edit_line) + ' =')
                self.ui.lineEdit.setText(result)
                return result
            except KeyError:
                pass

            except ZeroDivisionError:
                if self.get_temp_num() == 0:
                    self.show_error('Result is undefined')
                else:
                    self.show_error('Division by zero')

    def math_operation(self):
        label = self.ui.label.text()
        btn = self.sender()

        if not label:
            self.add_temp()
        else:
            if self.get_math_sign() != btn.text():
                if self.get_math_sign() == '=':
                    self.add_temp()
                else:
                    self.ui.label.setText(label[:-2] + f'{btn.text()} ')
            else:
                self.ui.label.setText(self.calculate() + f' {btn.text()}')

    def negate(self):
        edit_line = self.ui.lineEdit.text()

        if '-' not in edit_line:
            if edit_line != '0':
                edit_line = '-' + edit_line
        else:
            if edit_line != '0':
                edit_line = edit_line[1:]

        if len(edit_line) == self.edit_line_max_len + 1 and '-' in edit_line:
            self.ui.lineEdit.setMaxLength(self.edit_line_max_len + 1)
        else:
            self.ui.lineEdit.setMaxLength(self.edit_line_max_len)

        self.ui.lineEdit.setText(edit_line)

    def backspace(self):
        entry = self.ui.lineEdit.text()

        if len(entry) != 1:
            if len(entry) == 2 and '-' in entry:
                self.ui.lineEdit.setText('0')
            else:
                self.ui.lineEdit.setText(entry[:-1])
        else:
            self.ui.lineEdit.setText('0')

    def clear_temp_if_equality(self):
        if self.get_math_sign() == '=':
            self.ui.label.clear()

    def show_error(self, text):
        self.ui.lineEdit.setMaxLength(len(text))
        self.ui.lineEdit.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()

    sys.exit(app.exec())