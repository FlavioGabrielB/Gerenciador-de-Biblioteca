# Form implementation generated from reading ui file 'telacadastro.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(640, 480))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(600, 100))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(500, 50))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border-radius:1.5px;\n"
"border:1px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rrgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(245, 245, 245);\n"
"color:Black;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:black;\n"
"color:white;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(100, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border-radius:1.5px;\n"
"border:1px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rrgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(245, 245, 245);\n"
"color:Black;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:black;\n"
"color:white;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setIconSize(QtCore.QSize(1, 1))
        self.tabWidget.setElideMode(QtCore.Qt.TextElideMode.ElideLeft)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("")
        self.tab.setObjectName("tab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_5 = QtWidgets.QFrame(self.tab)
        self.frame_5.setMinimumSize(QtCore.QSize(700, 0))
        self.frame_5.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 71))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 100)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.frame_7)
        self.label_5.setMinimumSize(QtCore.QSize(40, 0))
        self.label_5.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../../../Downloads/2 Sem T??tulo_20220704130353.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 125))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setContentsMargins(64, 30, 64, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"border: 1px solid black;\n"
"border-radius:1.5px;\n"
"}")
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"border: 1px solid black;\n"
"border-radius:1.5px;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_6.addWidget(self.lineEdit_2)
        self.verticalLayout_3.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_5)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 15))
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 15))
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_2 = QtWidgets.QLabel(self.frame_9)
        self.label_2.setGeometry(QtCore.QRect(66, -6, 50, 30))
        self.label_2.setMinimumSize(QtCore.QSize(50, 30))
        self.label_2.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(100, 100, 100);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_9)
        self.label_3.setGeometry(QtCore.QRect(271, -6, 56, 30))
        self.label_3.setMinimumSize(QtCore.QSize(56, 30))
        self.label_3.setMaximumSize(QtCore.QSize(56, 30))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(100, 100, 100);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_9)
        self.label_4.setGeometry(QtCore.QRect(426, -6, 40, 30))
        self.label_4.setMinimumSize(QtCore.QSize(40, 30))
        self.label_4.setMaximumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(100, 100, 100);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.frame_9)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setContentsMargins(60, 0, 57, 60)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.comboBox = QtWidgets.QComboBox(self.frame_6)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(200, 30))
        self.comboBox.setStyleSheet("QComboBox{\n"
"border: 0.5px solid black;\n"
"border-radius:1.5px;\n"
"}\n"
"")
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAtBottom)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_2.setMinimumSize(QtCore.QSize(150, 30))
        self.comboBox_2.setMaximumSize(QtCore.QSize(150, 30))
        self.comboBox_2.setStyleSheet("QComboBox{\n"
"border: 0.5px solid black;\n"
"border-radius:1.5px;\n"
"}\n"
"")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_2)
        self.spinBox = QtWidgets.QSpinBox(self.frame_6)
        self.spinBox.setMinimumSize(QtCore.QSize(45, 30))
        self.spinBox.setMaximumSize(QtCore.QSize(45, 30))
        self.spinBox.setStyleSheet("QSpinBox{\n"
"border: 1px solid black;\n"
"border-radius:1.5px;\n"
"}")
        self.spinBox.setMinimum(0)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_7.addWidget(self.spinBox)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_5.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton_5.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"border-radius:1.5px;\n"
"border:1px solid black;\n"
"background-color: black;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(30, 30, 30);\n"
"color:white;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:white;\n"
"color:black;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_7.addWidget(self.pushButton_5)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.horizontalLayout_5.addWidget(self.frame_5)
        self.tabWidget.addTab(self.tab, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.CustomDashLine)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(127)
        self.horizontalLayout_4.addWidget(self.tableWidget)
        self.frame_4 = QtWidgets.QFrame(self.widget)
        self.frame_4.setMinimumSize(QtCore.QSize(100, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_4.setStyleSheet("QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;\n"
"border-radius: 2px;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_6.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_6.setMaximumSize(QtCore.QSize(120, 90))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"border-radius:1.5px;\n"
"border:1px solid black;\n"
"background-color: black;\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(30, 30, 30);\n"
"color:white;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:white;\n"
"color:black;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(120, 90))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"border-radius:1.5px;\n"
"border:1px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rrgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(245, 245, 245);\n"
"color:Black;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:black;\n"
"color:white;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_4.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_4.setMaximumSize(QtCore.QSize(120, 90))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"border-radius:1.5px;\n"
"border:1px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rrgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(245, 245, 245);\n"
"color:Black;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:black;\n"
"color:white;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_7.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_7.setMaximumSize(QtCore.QSize(120, 30))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"border-radius:1.5px;\n"
"border:1px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rrgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(245, 245, 245);\n"
"color:Black;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:black;\n"
"color:white;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)
        spacerItem = QtWidgets.QSpacerItem(20, 249, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_4.addWidget(self.frame_4)
        self.tabWidget.addTab(self.widget, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "x"))
        self.pushButton.setText(_translate("MainWindow", "Voltar"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Nome do Aluno"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Nome do Livro"))
        self.label_2.setText(_translate("MainWindow", "G??nero"))
        self.label_3.setText(_translate("MainWindow", "S??rie/Ano"))
        self.label_4.setText(_translate("MainWindow", "Dias"))
        self.comboBox.setCurrentText(_translate("MainWindow", "Drama"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Drama"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Fic????o Cient??fica"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Distopia"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Fantasia"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Fic????o Hist??rica"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Romance"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Horror"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Policial"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Com??dia"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Tecnico"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Did??tico"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Did??tico-Enem"))
        self.comboBox.setItemText(12, _translate("MainWindow", "Did??tico-Portugu??s"))
        self.comboBox.setItemText(13, _translate("MainWindow", "Did??tico-Sociologia"))
        self.comboBox.setItemText(14, _translate("MainWindow", "Did??tico-Filosofia"))
        self.comboBox.setItemText(15, _translate("MainWindow", "Did??tico-Qu??mica"))
        self.comboBox.setItemText(16, _translate("MainWindow", "Did??tico-Ingl??s"))
        self.comboBox.setItemText(17, _translate("MainWindow", "Did??tico-Biologia"))
        self.comboBox.setItemText(18, _translate("MainWindow", "Did??tico-Geografia"))
        self.comboBox.setItemText(19, _translate("MainWindow", "Did??tico-Hist??ria"))
        self.comboBox.setItemText(20, _translate("MainWindow", "Did??tico-F??sica"))
        self.comboBox.setItemText(21, _translate("MainWindow", "Did??tico-Matem??tica"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1?? A D.S"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "1?? B D.S"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "1?? A ADM"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "1?? B ADM"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "2?? A D.S"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "2?? B D.S"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "2?? A ADM"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "2?? B ADM"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "3?? A D.S"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "3?? B D.S"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "3?? B ADM"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "3?? A ADM"))
        self.pushButton_5.setText(_translate("MainWindow", "Enviar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Registrar"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "C??digo"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Aluno"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "S??rie/Ano"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Livro"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "G??nero"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Tempo de Aluguel"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Dia de Devolu????o"))
        self.pushButton_6.setText(_translate("MainWindow", "Atualizar"))
        self.pushButton_3.setText(_translate("MainWindow", "Editar"))
        self.pushButton_4.setText(_translate("MainWindow", "Excluir"))
        self.pushButton_7.setText(_translate("MainWindow", "Excel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "Tabela de Registro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
