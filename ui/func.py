# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myFunc.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import ui.myQrc

qssStyle = '''
        QCheckBox, QComboBox, QSpinBox ,QLineEdit {
        border: 1px solid rgb(204,204,204);
        border-radius: 2px;
        }
        QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 15px;
        border-left-width: 1px;
        border-left-style: solid;
        border-left-color: rgb(204,204,204);
        border-top-right-radius: 3px;
        border-bottom-right-radius: 3px;
        }
        QComboBox:down-arrow {
        background: transparent;
        image: url(:/src/off.png);
        width: 8px; height: 8px;
        }
        QComboBox:down-arrow:on {
        image: url(:/src/on.png);
        }
        QComboBox:drop-down:focus,QComboBox:focus, QLineEdit:focus {
        border-top: 1px solid QLinearGradient(y0:0, y1:1,stop: 0 #DADADA, stop: 1 transparent);
        border-left: 1px solid QLinearGradient(x0:0, x1:1,stop: 0 #DADADA, stop: 1 transparent);
        border-bottom: 1px solid QLinearGradient(y0:0, y1:1,stop: 0 transparent, stop: 1  #DADADA);
        border-right: 1px solid QLinearGradient(x0:0, x1:1,stop:  0 transparent, stop: 1 #DADADA);

        border-top-right-radius: 3px;
        border-bottom-right-radius: 3px;
        }
        '''

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(695, 525)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/src/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 261, 511))
        self.label.setStyleSheet("background-image:url(:/src/girl.png);\n"
"background-repeat: no-repeat;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 80, 401, 71))
        self.label_3.setStyleSheet("font: 87 20pt \"Arial Black\";")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 40, 241, 41))
        self.label_2.setStyleSheet("font: 87 20pt \"Arial Black\";")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 170, 121, 16))
        self.label_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_4.setStyleSheet("font: 10pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(510, 170, 121, 16))
        self.label_5.setStyleSheet("font: 10pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 230, 121, 16))
        self.label_6.setStyleSheet("font: 10pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(340, 250, 331, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_newname_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_newname_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_newname_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("JetBrainsMonoExtraBold Nerd Font Mono")
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_newname_2.setStyleSheet(qssStyle)
        self.lineEdit_newname_2.setFont(font)
        self.lineEdit_newname_2.setObjectName("lineEdit_newname_2")
        self.horizontalLayout.addWidget(self.lineEdit_newname_2)
        self.lineEdit_newname = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_newname.sizePolicy().hasHeightForWidth())
        self.lineEdit_newname.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("JetBrainsMonoExtraBold Nerd Font Mono")
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_newname.setStyleSheet(qssStyle)
        self.lineEdit_newname.setFont(font)
        self.lineEdit_newname.setObjectName("lineEdit_newname")
        self.horizontalLayout.addWidget(self.lineEdit_newname)
        self.lineEdit_newname_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_newname_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_newname_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("JetBrainsMonoExtraBold Nerd Font Mono")
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_newname_3.setFont(font)
        self.lineEdit_newname_3.setStyleSheet(qssStyle)
        self.lineEdit_newname_3.setObjectName("lineEdit_newname_3")
        self.horizontalLayout.addWidget(self.lineEdit_newname_3)
        self.lineEdit_newname_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_newname_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_newname_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("JetBrainsMonoExtraBold Nerd Font Mono")
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_newname_4.setFont(font)
        self.lineEdit_newname_4.setStyleSheet(qssStyle)
        self.lineEdit_newname_4.setObjectName("lineEdit_newname_4")
        self.horizontalLayout.addWidget(self.lineEdit_newname_4)
        
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(340, 190, 321, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("JetBrainsMonoMedium Nerd Font")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setMouseTracking(True)
        self.comboBox_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboBox_2.setAcceptDrops(True)
        self.comboBox_2.setAutoFillBackground(False)
        self.comboBox_2.setStyleSheet(qssStyle)
        self.comboBox_2.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox_2.setDuplicatesEnabled(False)
        self.comboBox_2.setFrame(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("JetBrainsMonoMedium Nerd Font")
        self.comboBox.setFont(font)
        self.comboBox.setMouseTracking(True)
        self.comboBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboBox.setAcceptDrops(True)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(qssStyle)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(False)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(408, 232, 16, 71))
        self.label_7.setStyleSheet("font: 87 20pt \"Arial Black\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(496, 232, 16, 71))
        self.label_8.setStyleSheet("font: 87 20pt \"Arial Black\";")
        self.label_8.setObjectName("label_8")
        
        self.btn_sureadd = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sureadd.setGeometry(QtCore.QRect(570, 320, 91, 41))
        font = QtGui.QFont()
        font.setFamily("JetBrainsMonoMedium Nerd Font Mono")
        self.btn_sureadd.setFont(font)
        self.btn_sureadd.setStyleSheet("background-color: rgb(29, 123, 255);\n"
"color: rgb(255, 255, 255);")
        self.btn_sureadd.setObjectName("btn_sureadd")
        
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(340, 380, 321, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "预约小工具"))
        self.label_3.setText(_translate("MainWindow", "Welcome here!"))
        self.label_2.setText(_translate("MainWindow", "Hello"))
        self.label_4.setText(_translate("MainWindow", "Court:"))
        self.label_5.setText(_translate("MainWindow", "Time:"))
        self.label_6.setText(_translate("MainWindow", "Post Time:"))
        self.label_7.setText(_translate("MainWindow", ":"))
        self.label_8.setText(_translate("MainWindow", ":"))
        self.btn_sureadd.setText(_translate("MainWindow", "Sure"))
        self.comboBox_2.addItems(["Badminton Court 1", "Badminton Court 2", "Badminton Court 3", "Badminton Court 4", "Badminton Court 5", "Badminton Court 6"])
        self.comboBox.addItems(["15:x0 - 16:00", "16:00 - 17:00", "17:00 - 18:00", "18:00 - 19:00", "19:00 - 20:00", "20:00 - 21:00"])
