# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HesapMakinesi(object):
    def setupUi(self, HesapMakinesi):
        HesapMakinesi.setObjectName("HesapMakinesi")
        HesapMakinesi.resize(420, 625)
        HesapMakinesi.setMinimumSize(QtCore.QSize(420, 625))
        HesapMakinesi.setMaximumSize(QtCore.QSize(420, 625))
        HesapMakinesi.setWindowOpacity(1.0)
        HesapMakinesi.setStyleSheet("background-color: #1A2030;")
        self.centralwidget = QtWidgets.QWidget(HesapMakinesi)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, -30, 423, 661))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(420, 625))
        self.tabWidget.setSizeIncrement(QtCore.QSize(83, 0))
        self.tabWidget.setBaseSize(QtCore.QSize(78, 0))
        self.tabWidget.setWindowOpacity(1.0)
        self.tabWidget.setStyleSheet("border:none;\n"
"margin:0;")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.dockButton = QtWidgets.QPushButton(self.tab)
        self.dockButton.setGeometry(QtCore.QRect(15, 26, 41, 31))
        self.dockButton.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgba(255, 255, 255, 40);\n"
"    border-radius:3px;\n"
"}")
        self.dockButton.setText("")
        self.dockButton.setObjectName("dockButton")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(20, 30, 31, 2))
        self.line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(20, 40, 31, 2))
        self.line_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.tab)
        self.line_3.setGeometry(QtCore.QRect(20, 50, 31, 2))
        self.line_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.baslikLabel = QtWidgets.QLabel(self.tab)
        self.baslikLabel.setGeometry(QtCore.QRect(66, 24, 191, 41))
        self.baslikLabel.setStyleSheet("QLabel{\n"
"color: #FFF;\n"
"font-family: Microsoft YaHei;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}")
        self.baslikLabel.setObjectName("baslikLabel")
        self.yukariSonucLineEdit = QtWidgets.QLineEdit(self.tab)
        self.yukariSonucLineEdit.setGeometry(QtCore.QRect(10, 80, 400, 20))
        self.yukariSonucLineEdit.setStyleSheet("QLineEdit{\n"
"color: #A6A6A6;\n"
"text-align: right;\n"
"font-family: Microsoft YaHei;\n"
"font-size: 15px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}")
        self.yukariSonucLineEdit.setText("")
        self.yukariSonucLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.yukariSonucLineEdit.setDragEnabled(False)
        self.yukariSonucLineEdit.setReadOnly(True)
        self.yukariSonucLineEdit.setClearButtonEnabled(False)
        self.yukariSonucLineEdit.setObjectName("yukariSonucLineEdit")
        self.sonucLineEdit = QtWidgets.QLineEdit(self.tab)
        self.sonucLineEdit.setGeometry(QtCore.QRect(10, 100, 400, 101))
        self.sonucLineEdit.setStyleSheet("QLineEdit{\n"
"color: #FFF;\n"
"text-align: right;\n"
"font-family: Microsoft YaHei;\n"
"font-size: 40px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"}")
        self.sonucLineEdit.setMaxLength(15)
        self.sonucLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sonucLineEdit.setObjectName("sonucLineEdit")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 200, 423, 431))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.cikarmaButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cikarmaButton.setStyleSheet("QPushButton{\n"
"background-color:rgba(50, 50, 50, 0.4) ;\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Sans Serif Collection;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(50, 50, 50, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(50, 50, 50, 0.7);\n"
"}")
        self.cikarmaButton.setObjectName("cikarmaButton")
        self.gridLayout.addWidget(self.cikarmaButton, 3, 3, 1, 1)
        self.bolmeButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bolmeButton.setStyleSheet("QPushButton{\n"
"background-color:rgba(50, 50, 50, 0.4) ;\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Sans Serif Collection;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(50, 50, 50, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(50, 50, 50, 0.7);\n"
"}")
        self.bolmeButton.setObjectName("bolmeButton")
        self.gridLayout.addWidget(self.bolmeButton, 1, 3, 1, 1)
        self.CButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.CButton.setStyleSheet("QPushButton{\n"
"background-color:rgba(50, 50, 50, 0.4) ;\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Sans Serif Collection;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(50, 50, 50, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(50, 50, 50, 0.7);\n"
"}")
        self.CButton.setObjectName("CButton")
        self.gridLayout.addWidget(self.CButton, 0, 2, 1, 1)
        self.kokAlButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.kokAlButton.setStyleSheet("QPushButton{\n"
"background-color:rgba(50, 50, 50, 0.4) ;\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family:Lucida Calligraphy;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(50, 50, 50, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(50, 50, 50, 0.7);\n"
"}")
        self.kokAlButton.setObjectName("kokAlButton")
        self.gridLayout.addWidget(self.kokAlButton, 1, 2, 1, 1)
        self.deleteButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.deleteButton.setStyleSheet("QPushButton{\n"
"background-color:rgba(50, 50, 50, 0.4) ;\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Sans Serif Collection;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(50, 50, 50, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(50, 50, 50, 0.7);\n"
"}")
        self.deleteButton.setObjectName("deleteButton")
        self.gridLayout.addWidget(self.deleteButton, 0, 3, 1, 1)
        self.toplamaButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.toplamaButton.setStyleSheet("QPushButton{\n"
"background-color:rgba(50, 50, 50, 0.4) ;\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Sans Serif Collection;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(50, 50, 50, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(50, 50, 50, 0.7);\n"
"}")
        self.toplamaButton.setObjectName("toplamaButton")
        self.gridLayout.addWidget(self.toplamaButton, 4, 3, 1, 1)
        self.CEButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.CEButton.setStyleSheet("QPushButton{\n"
"background-color:rgba(50, 50, 50, 0.4) ;\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Sans Serif Collection;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(50, 50, 50, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(50, 50, 50, 0.7);\n"
"}")
        self.CEButton.setObjectName("CEButton")
        self.gridLayout.addWidget(self.CEButton, 0, 1, 1, 1)
        self.kareAlButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.kareAlButton.setStyleSheet("QPushButton{\n"
"background-color:rgba(50, 50, 50, 0.4) ;\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Lucida Calligraphy;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(50, 50, 50, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(50, 50, 50, 0.7);\n"
"}")
        self.kareAlButton.setObjectName("kareAlButton")
        self.gridLayout.addWidget(self.kareAlButton, 1, 1, 1, 1)
        self.birBoluButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.birBoluButton.setStyleSheet("QPushButton{\n"
"background-color:rgba(50, 50, 50, 0.4) ;\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Lucida Calligraphy;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"line-height: normal;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(50, 50, 50, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(50, 50, 50, 0.7);\n"
"}")
        self.birBoluButton.setObjectName("birBoluButton")
        self.gridLayout.addWidget(self.birBoluButton, 1, 0, 1, 1)
        self.carpmaButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.carpmaButton.setStyleSheet("QPushButton{\n"
"background-color:rgba(50, 50, 50, 0.4) ;\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Sans Serif Collection;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(50, 50, 50, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(50, 50, 50, 0.7);\n"
"}")
        self.carpmaButton.setObjectName("carpmaButton")
        self.gridLayout.addWidget(self.carpmaButton, 2, 3, 1, 1)
        self.yuzdeButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.yuzdeButton.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color:rgba(50, 50, 50, 0.4) ;\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Sans Serif Collection;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(50, 50, 50, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(50, 50, 50, 0.7);\n"
"}")
        self.yuzdeButton.setObjectName("yuzdeButton")
        self.gridLayout.addWidget(self.yuzdeButton, 0, 0, 1, 1)
        self.esittirButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.esittirButton.setStyleSheet("QPushButton{\n"
"    background-color: rgba(62, 81, 255, 0.4);\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Sans Serif Collection;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(62, 81, 255, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(62, 81, 255, 0.7);\n"
"}")
        self.esittirButton.setObjectName("esittirButton")
        self.gridLayout.addWidget(self.esittirButton, 5, 3, 1, 1)
        self.sifirButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.sifirButton.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color:rgba(93, 93, 93, 0.4);\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Sans Serif Collection;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(93, 93, 93, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(93, 93, 93, 0.7);\n"
"}")
        self.sifirButton.setObjectName("sifirButton")
        self.gridLayout.addWidget(self.sifirButton, 5, 1, 1, 1)
        self.virgulButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.virgulButton.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color:rgba(93, 93, 93, 0.4);\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Sans Serif Collection;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(93, 93, 93, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(93, 93, 93, 0.7);\n"
"}")
        self.virgulButton.setObjectName("virgulButton")
        self.gridLayout.addWidget(self.virgulButton, 5, 2, 1, 1)
        self.artiEksiButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.artiEksiButton.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color:rgba(93, 93, 93, 0.4);\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Sans Serif Collection;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(93, 93, 93, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(93, 93, 93, 0.7);\n"
"}")
        self.artiEksiButton.setObjectName("artiEksiButton")
        self.gridLayout.addWidget(self.artiEksiButton, 5, 0, 1, 1)
        self.birButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.birButton.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color:rgba(93, 93, 93, 0.4);\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Sans Serif Collection;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(93, 93, 93, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(93, 93, 93, 0.7);\n"
"}")
        self.birButton.setObjectName("birButton")
        self.gridLayout.addWidget(self.birButton, 4, 0, 1, 1)
        self.ikiButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ikiButton.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color:rgba(93, 93, 93, 0.4);\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Sans Serif Collection;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(93, 93, 93, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(93, 93, 93, 0.7);\n"
"}")
        self.ikiButton.setObjectName("ikiButton")
        self.gridLayout.addWidget(self.ikiButton, 4, 1, 1, 1)
        self.ucButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ucButton.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color:rgba(93, 93, 93, 0.4);\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Sans Serif Collection;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(93, 93, 93, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(93, 93, 93, 0.7);\n"
"}")
        self.ucButton.setObjectName("ucButton")
        self.gridLayout.addWidget(self.ucButton, 4, 2, 1, 1)
        self.dortButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.dortButton.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color:rgba(93, 93, 93, 0.4);\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Sans Serif Collection;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(93, 93, 93, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(93, 93, 93, 0.7);\n"
"}")
        self.dortButton.setObjectName("dortButton")
        self.gridLayout.addWidget(self.dortButton, 3, 0, 1, 1)
        self.besButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.besButton.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color:rgba(93, 93, 93, 0.4);\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Sans Serif Collection;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(93, 93, 93, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(93, 93, 93, 0.7);\n"
"}")
        self.besButton.setObjectName("besButton")
        self.gridLayout.addWidget(self.besButton, 3, 1, 1, 1)
        self.altiButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.altiButton.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color:rgba(93, 93, 93, 0.4);\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Sans Serif Collection;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(93, 93, 93, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(93, 93, 93, 0.7);\n"
"}")
        self.altiButton.setObjectName("altiButton")
        self.gridLayout.addWidget(self.altiButton, 3, 2, 1, 1)
        self.yediButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.yediButton.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color:rgba(93, 93, 93, 0.4);\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Sans Serif Collection;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(93, 93, 93, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(93, 93, 93, 0.7);\n"
"}")
        self.yediButton.setObjectName("yediButton")
        self.gridLayout.addWidget(self.yediButton, 2, 0, 1, 1)
        self.sekizButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.sekizButton.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color:rgba(93, 93, 93, 0.4);\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Sans Serif Collection;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(93, 93, 93, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(93, 93, 93, 0.7);\n"
"}")
        self.sekizButton.setObjectName("sekizButton")
        self.gridLayout.addWidget(self.sekizButton, 2, 1, 1, 1)
        self.dokuzButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.dokuzButton.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color:rgba(93, 93, 93, 0.4);\n"
"width: 100px;\n"
"height: 65px;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Sans Serif Collection;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(93, 93, 93, 0.6);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(93, 93, 93, 0.7);\n"
"}")
        self.dokuzButton.setObjectName("dokuzButton")
        self.gridLayout.addWidget(self.dokuzButton, 2, 2, 1, 1)
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.dockButton.raise_()
        self.baslikLabel.raise_()
        self.yukariSonucLineEdit.raise_()
        self.sonucLineEdit.raise_()
        self.gridLayoutWidget.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        HesapMakinesi.setCentralWidget(self.centralwidget)

        self.retranslateUi(HesapMakinesi)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(HesapMakinesi)

    def retranslateUi(self, HesapMakinesi):
        _translate = QtCore.QCoreApplication.translate
        HesapMakinesi.setWindowTitle(_translate("HesapMakinesi", "Hesap Makinesi"))
        self.baslikLabel.setText(_translate("HesapMakinesi", "<html><head/><body><p><span style=\" font-size:20pt;\">Standart</span></p></body></html>"))
        self.sonucLineEdit.setText(_translate("HesapMakinesi", "0"))
        self.cikarmaButton.setText(_translate("HesapMakinesi", "-"))
        self.bolmeButton.setText(_translate("HesapMakinesi", "÷"))
        self.CButton.setText(_translate("HesapMakinesi", "C"))
        self.kokAlButton.setText(_translate("HesapMakinesi", "²√x"))
        self.deleteButton.setText(_translate("HesapMakinesi", "←"))
        self.toplamaButton.setText(_translate("HesapMakinesi", "+"))
        self.CEButton.setText(_translate("HesapMakinesi", "CE"))
        self.kareAlButton.setText(_translate("HesapMakinesi", "x²"))
        self.birBoluButton.setText(_translate("HesapMakinesi", "⅟x"))
        self.carpmaButton.setText(_translate("HesapMakinesi", "ⅹ"))
        self.yuzdeButton.setText(_translate("HesapMakinesi", "%"))
        self.esittirButton.setText(_translate("HesapMakinesi", "="))
        self.sifirButton.setText(_translate("HesapMakinesi", "0"))
        self.virgulButton.setText(_translate("HesapMakinesi", ","))
        self.artiEksiButton.setText(_translate("HesapMakinesi", "±"))
        self.birButton.setText(_translate("HesapMakinesi", "1"))
        self.ikiButton.setText(_translate("HesapMakinesi", "2"))
        self.ucButton.setText(_translate("HesapMakinesi", "3"))
        self.dortButton.setText(_translate("HesapMakinesi", "4"))
        self.besButton.setText(_translate("HesapMakinesi", "5"))
        self.altiButton.setText(_translate("HesapMakinesi", "6"))
        self.yediButton.setText(_translate("HesapMakinesi", "7"))
        self.sekizButton.setText(_translate("HesapMakinesi", "8"))
        self.dokuzButton.setText(_translate("HesapMakinesi", "9"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("HesapMakinesi", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("HesapMakinesi", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HesapMakinesi = QtWidgets.QMainWindow()
    ui = Ui_HesapMakinesi()
    ui.setupUi(HesapMakinesi)
    HesapMakinesi.show()
    sys.exit(app.exec_())
