from PySide6.QtWidgets import QApplication,QMainWindow,QWidget,QVBoxLayout,QLineEdit
from Ui_caculater import Ui_Form

class start_window(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.result = ''
        self.bind()

    def bind(self):
        self.pushButton_0.clicked.connect(lambda:self.add_number('0'))
        self.pushButton_1.clicked.connect(lambda:self.add_number('1'))
        self.pushButton_2.clicked.connect(lambda:self.add_number('2'))
        self.pushButton_3.clicked.connect(lambda:self.add_number('3'))
        self.pushButton_4.clicked.connect(lambda:self.add_number('4'))
        self.pushButton_5.clicked.connect(lambda:self.add_number('5'))
        self.pushButton_6.clicked.connect(lambda:self.add_number('6'))
        self.pushButton_7.clicked.connect(lambda:self.add_number('7'))
        self.pushButton_8.clicked.connect(lambda:self.add_number('8'))
        self.pushButton_9.clicked.connect(lambda:self.add_number('9'))
        self.pushButton_dot.clicked.connect(lambda:self.add_number('.'))
        self.pushButton_and.clicked.connect(lambda:self.add_number('+'))
        self.pushButton_sub.clicked.connect(lambda:self.add_number('-'))
        self.pushButton_v.clicked.connect(lambda:self.add_number('^'))
        self.pushButton_e.clicked.connect(lambda:self.add_number('e'))
        self.pushButton_div.clicked.connect(lambda:self.add_number('/'))
        self.pushButton_back.clicked.connect(self.back)
        self.pushButton_mul.clicked.connect(lambda:self.add_number('*'))

        self.pushButton_to.clicked.connect(self.equal)
        self.pushButton_c.clicked.connect(self.clear)



    def add_number(self,number):
        self.lineEdit.clear()
        self.result += number
        self.lineEdit.setText(self.result)

    def equal(self):
        self.number_result = eval(self.result)
        self.lineEdit.setText(str(self.number_result))


    def clear(self):
        self.result = ''
        self.lineEdit.clear()

    def back(self):
        self.lineEdit.clear()
        self.result = self.result[:-1]
        self.lineEdit.setText(self.result)


if __name__ == '__main__':
    app = QApplication()
    window = start_window()
    window.show()
    app.exec()
