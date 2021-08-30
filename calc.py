from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 590)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OutPutLabel = QtWidgets.QLabel(self.centralwidget)
        self.OutPutLabel.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.OutPutLabel.setFont(font)
        self.OutPutLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.OutPutLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OutPutLabel.setLineWidth(2)
        self.OutPutLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.OutPutLabel.setIndent(-1)
        self.OutPutLabel.setObjectName("OutPutLabel")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.prees_it(self.percentButton.text())) #self.percentButton.text() == % or any value typed in this bt
        self.percentButton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.cButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.prees_it(self.cButton.text()))
        self.cButton.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.remove_it()) #self.arrowButton.text()
        self.arrowButton.setGeometry(QtCore.QRect(190, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.prees_it(self.divideButton.text()))
        self.divideButton.setGeometry(QtCore.QRect(275, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.prees_it(self.nineButton.text()))
        self.nineButton.setGeometry(QtCore.QRect(190, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.prees_it(self.sevenButton.text()))
        self.sevenButton.setGeometry(QtCore.QRect(10, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.prees_it(self.eightButton.text()))
        self.eightButton.setGeometry(QtCore.QRect(100, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.prees_it('*'))
        self.multiplyButton.setGeometry(QtCore.QRect(275, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.prees_it(self.sixButton.text()))
        self.sixButton.setGeometry(QtCore.QRect(190, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.prees_it(self.fourButton.text()))
        self.fourButton.setGeometry(QtCore.QRect(10, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.prees_it(self.fiveButton.text()))
        self.fiveButton.setGeometry(QtCore.QRect(100, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.minesButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.prees_it(self.minesButton.text()))
        self.minesButton.setGeometry(QtCore.QRect(275, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minesButton.setFont(font)
        self.minesButton.setObjectName("minesButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.prees_it(self.threeButton.text()))
        self.threeButton.setGeometry(QtCore.QRect(190, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.prees_it(self.oneButton.text()))
        self.oneButton.setGeometry(QtCore.QRect(10, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.prees_it(self.twoButton.text()))
        self.twoButton.setGeometry(QtCore.QRect(100, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.prees_it(self.addButton.text()))
        self.addButton.setGeometry(QtCore.QRect(275, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.dot_it())
        self.decimalButton.setGeometry(QtCore.QRect(190, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimalButton.setFont(font)
        self.decimalButton.setObjectName("decimalButton")
        self.plusminesButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.make_negetive_and_pos())
        self.plusminesButton.setGeometry(QtCore.QRect(10, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusminesButton.setFont(font)
        self.plusminesButton.setObjectName("plusminesButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.prees_it(self.zeroButton.text()))
        self.zeroButton.setGeometry(QtCore.QRect(100, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.equal_math())
        self.equalButton.setGeometry(QtCore.QRect(275, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    

    def prees_it(self, pressed):
        ''' every button in app like 7,8 & etc.. pressed typed in label of app '''

        if pressed == 'C': # if press button c clear all data in label and put 0
            self.OutPutLabel.setText('0')
        else:
            # check if first number (prees first number) is 0 to delete 0  --> 012 --> 12 
            if self.OutPutLabel.text() == '0':
                self.OutPutLabel.setText('')
            self.OutPutLabel.setText(f'{self.OutPutLabel.text()}{pressed}')  # show all pressed buttons in lable

    
    def dot_it(self):
        ''' convert int number to float or decimal --> 12 --> 12.4 '''

        screen = self.OutPutLabel.text()
        if '.' in screen: #if in label data have dot dont need any more 
            pass
        else:   # if we dont have decimal number in data you can make number to decimal 
            self.OutPutLabel.setText(f'{screen}.')
            
        if '+' or '-' or '/' or '%' or '*' in screen:    # after use this op you can make number to decimal 
            self.OutPutLabel.setText(f'{screen}.')


    def remove_it(self):
        ''' remove last number of data if you press <<  --> 123 --> 12 '''
        
        screen = self.OutPutLabel.text()
        
        screen = screen[:-1] #remove last item
        if screen == '':   # if delete all data put 0 in label
            self.OutPutLabel.setText('0')
        else:
            self.OutPutLabel.setText(f'{screen}')


    def make_negetive_and_pos(self):
        ''' make number tp positive or negetive  but we have some bug here '''

        screen = self.OutPutLabel.text()
        if '-' in screen:
            self.OutPutLabel.setText(f'{screen.replace("-", "")}')
        elif '-' not in screen:
            self.OutPutLabel.setText(f'-{screen}')
    

    def equal_math(self):
        ''' Mathematical processing in calc'''
        screen = self.OutPutLabel.text()
        try:
            screen = str(round(eval(screen), 5))  # do math and round it if have few Decimal number after . and convert to string
        except:
            self.OutPutLabel.setText('error!')    # if client press wrong math like 2* and press = we have err
        else:
            self.OutPutLabel.setText(f'{screen}')  # if try work so else box is run


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "calculator"))
        self.OutPutLabel.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.multiplyButton.setText(_translate("MainWindow", "X"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.minesButton.setText(_translate("MainWindow", "-"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.plusminesButton.setText(_translate("MainWindow", "+/-"))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.equalButton.setText(_translate("MainWindow", "="))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# def make_negetive_and_pos(self):
#     screen = int(self.OutPutLabel.text())
#     if screen > 0:
#         screen = 0 - screen
#         self.OutPutLabel.setText(f'{screen}')
#     elif screen < 0:
#         screen = abs(screen)
#         self.OutPutLabel.setText(f'{screen}')
    


