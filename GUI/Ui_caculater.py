# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'caculater.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(612, 470)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 200, 530, 201))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_dot = QPushButton(self.layoutWidget)
        self.pushButton_dot.setObjectName(u"pushButton_dot")

        self.gridLayout.addWidget(self.pushButton_dot, 0, 0, 1, 1)

        self.pushButton_div = QPushButton(self.layoutWidget)
        self.pushButton_div.setObjectName(u"pushButton_div")

        self.gridLayout.addWidget(self.pushButton_div, 1, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)

        self.pushButton_mul = QPushButton(self.layoutWidget)
        self.pushButton_mul.setObjectName(u"pushButton_mul")

        self.gridLayout.addWidget(self.pushButton_mul, 1, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 3, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 4, 2, 1, 1)

        self.pushButton_1 = QPushButton(self.layoutWidget)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.gridLayout.addWidget(self.pushButton_1, 4, 0, 1, 1)

        self.pushButton_v = QPushButton(self.layoutWidget)
        self.pushButton_v.setObjectName(u"pushButton_v")

        self.gridLayout.addWidget(self.pushButton_v, 0, 1, 1, 1)

        self.pushButton_c = QPushButton(self.layoutWidget)
        self.pushButton_c.setObjectName(u"pushButton_c")

        self.gridLayout.addWidget(self.pushButton_c, 0, 2, 1, 1)

        self.pushButton_and = QPushButton(self.layoutWidget)
        self.pushButton_and.setObjectName(u"pushButton_and")

        self.gridLayout.addWidget(self.pushButton_and, 1, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_to = QPushButton(self.layoutWidget)
        self.pushButton_to.setObjectName(u"pushButton_to")

        self.gridLayout.addWidget(self.pushButton_to, 0, 3, 1, 1)

        self.pushButton_6 = QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 3, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.layoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_sub = QPushButton(self.layoutWidget)
        self.pushButton_sub.setObjectName(u"pushButton_sub")

        self.gridLayout.addWidget(self.pushButton_sub, 1, 3, 1, 1)

        self.pushButton_back = QPushButton(self.layoutWidget)
        self.pushButton_back.setObjectName(u"pushButton_back")

        self.gridLayout.addWidget(self.pushButton_back, 2, 3, 1, 1)

        self.pushButton_e = QPushButton(self.layoutWidget)
        self.pushButton_e.setObjectName(u"pushButton_e")

        self.gridLayout.addWidget(self.pushButton_e, 3, 3, 1, 1)

        self.pushButton_0 = QPushButton(self.layoutWidget)
        self.pushButton_0.setObjectName(u"pushButton_0")

        self.gridLayout.addWidget(self.pushButton_0, 4, 3, 1, 1)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(40, 40, 521, 141))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_dot.setText(QCoreApplication.translate("Form", u".", None))
        self.pushButton_div.setText(QCoreApplication.translate("Form", u"/", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_mul.setText(QCoreApplication.translate("Form", u"*", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_v.setText(QCoreApplication.translate("Form", u"^", None))
        self.pushButton_c.setText(QCoreApplication.translate("Form", u"C", None))
        self.pushButton_and.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_to.setText(QCoreApplication.translate("Form", u"=", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_sub.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_back.setText(QCoreApplication.translate("Form", u"back", None))
        self.pushButton_e.setText(QCoreApplication.translate("Form", u"e", None))
        self.pushButton_0.setText(QCoreApplication.translate("Form", u"0", None))
    # retranslateUi

