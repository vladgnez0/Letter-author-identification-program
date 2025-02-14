# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: #E6FFE6; /* Зеленый фон */\n"
"    color: #003300; /* Темный текст */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #4CAF50; /* Зеленая кнопка */\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    cursor: pointer;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049; /* Темнозеленый при наведении */\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #f2f2f2; /* Светлый цвет фона для поля ввода */\n"
"    padding: 6px;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #006600; /* Зеленый текст */\n"
"    font-size: 16px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(654, 530, 111, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(494, 530, 161, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 50, 351, 241))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(530, 310, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(50, 320, 431, 171))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(540, 30, 245, 261))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_2.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_2.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_2.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout_2.addWidget(self.radioButton_6)
        #self.radioButton_7 = QtWidgets.QRadioButton(self.widget)
        #self.radioButton_7.setObjectName("radioButton_7")
        #self.verticalLayout_2.addWidget(self.radioButton_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Анализ авторства"))
        self.pushButton.setText(_translate("MainWindow", " Анализ"))
        self.pushButton_2.setText(_translate("MainWindow", "Выход"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Выберите метод расспознования"))
        self.radioButton.setText(_translate("MainWindow", " наивный классификатор Байеса"))
        self.radioButton_2.setText(_translate("MainWindow", "Логистическая регрессия"))
        self.radioButton_3.setText(_translate("MainWindow", "Метод опорных векторов."))
        self.radioButton_4.setText(_translate("MainWindow", "AdaBoost"))
        self.radioButton_5.setText(_translate("MainWindow", "Градиентный бустинг"))
        self.radioButton_6.setText(_translate("MainWindow", "Полносвязнная модель"))
#        self.radioButton_7.setText(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
