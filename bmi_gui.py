# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bmi_gui.ui'
#
# Created: Sat Jul  4 19:22:48 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(333, 217)
        MainWindow.setMinimumSize(QtCore.QSize(333, 217))
        MainWindow.setMaximumSize(QtCore.QSize(333, 217))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/gui-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_meteric = QtGui.QWidget()
        self.tab_meteric.setObjectName(_fromUtf8("tab_meteric"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab_meteric)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEdit_weight_in_kg = QtGui.QLineEdit(self.tab_meteric)
        self.lineEdit_weight_in_kg.setObjectName(_fromUtf8("lineEdit_weight_in_kg"))
        self.verticalLayout.addWidget(self.lineEdit_weight_in_kg)
        self.lineEdit_height_in_m = QtGui.QLineEdit(self.tab_meteric)
        self.lineEdit_height_in_m.setObjectName(_fromUtf8("lineEdit_height_in_m"))
        self.verticalLayout.addWidget(self.lineEdit_height_in_m)
        self.pushButton_cal_bmi_kg_m = QtGui.QPushButton(self.tab_meteric)
        self.pushButton_cal_bmi_kg_m.setObjectName(_fromUtf8("pushButton_cal_bmi_kg_m"))
        self.verticalLayout.addWidget(self.pushButton_cal_bmi_kg_m)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.tab_meteric)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_bmi_meteric = QtGui.QLineEdit(self.tab_meteric)
        self.lineEdit_bmi_meteric.setObjectName(_fromUtf8("lineEdit_bmi_meteric"))
        self.horizontalLayout.addWidget(self.lineEdit_bmi_meteric)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab_meteric, _fromUtf8(""))
        self.tab_imperial = QtGui.QWidget()
        self.tab_imperial.setObjectName(_fromUtf8("tab_imperial"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.tab_imperial)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.lineEdit_weight_in_lb = QtGui.QLineEdit(self.tab_imperial)
        self.lineEdit_weight_in_lb.setObjectName(_fromUtf8("lineEdit_weight_in_lb"))
        self.verticalLayout_4.addWidget(self.lineEdit_weight_in_lb)
        self.lineEdit_height_in_inches = QtGui.QLineEdit(self.tab_imperial)
        self.lineEdit_height_in_inches.setObjectName(_fromUtf8("lineEdit_height_in_inches"))
        self.verticalLayout_4.addWidget(self.lineEdit_height_in_inches)
        self.pushButton_cal_bmi_lb_ft = QtGui.QPushButton(self.tab_imperial)
        self.pushButton_cal_bmi_lb_ft.setObjectName(_fromUtf8("pushButton_cal_bmi_lb_ft"))
        self.verticalLayout_4.addWidget(self.pushButton_cal_bmi_lb_ft)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.tab_imperial)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_bmi_imperial = QtGui.QLineEdit(self.tab_imperial)
        self.lineEdit_bmi_imperial.setObjectName(_fromUtf8("lineEdit_bmi_imperial"))
        self.horizontalLayout_3.addWidget(self.lineEdit_bmi_imperial)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_imperial, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_5.addWidget(self.label_5)
        self.pushButton_3 = QtGui.QPushButton(self.tab)
        self.pushButton_3.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: transparent;\n"
"border: none;\n"
"}"))
        self.pushButton_3.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/iib-logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(100, 60))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout_5.addWidget(self.pushButton_3)
        self.label_15 = QtGui.QLabel(self.tab)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_5.addWidget(self.label_15)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 333, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PyBMI", None))
        self.lineEdit_weight_in_kg.setToolTip(_translate("MainWindow", "Input your weight in kilograms", None))
        self.lineEdit_weight_in_kg.setPlaceholderText(_translate("MainWindow", "Weight in kilgrams", None))
        self.lineEdit_height_in_m.setToolTip(_translate("MainWindow", "Input your eight in meters", None))
        self.lineEdit_height_in_m.setPlaceholderText(_translate("MainWindow", "Height in meters", None))
        self.pushButton_cal_bmi_kg_m.setText(_translate("MainWindow", "Calculate BMI", None))
        self.label.setText(_translate("MainWindow", "Your BMI", None))
        self.lineEdit_bmi_meteric.setToolTip(_translate("MainWindow", "Your BMI in meteric system", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_meteric), _translate("MainWindow", "Metric System", None))
        self.lineEdit_weight_in_lb.setToolTip(_translate("MainWindow", "Input your weight in pounds", None))
        self.lineEdit_weight_in_lb.setPlaceholderText(_translate("MainWindow", "Weight in pounds", None))
        self.lineEdit_height_in_inches.setToolTip(_translate("MainWindow", "Input your height in inches", None))
        self.lineEdit_height_in_inches.setPlaceholderText(_translate("MainWindow", "Height in inches", None))
        self.pushButton_cal_bmi_lb_ft.setText(_translate("MainWindow", "Calculate BMI", None))
        self.label_2.setText(_translate("MainWindow", "Your BMI", None))
        self.lineEdit_bmi_imperial.setToolTip(_translate("MainWindow", "Your BMI in imperial system", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_imperial), _translate("MainWindow", "Imperial System", None))
        self.label_5.setText(_translate("MainWindow", "   Created by Atiq-Ur-Rehman, Anees Hayat, and Azmat Ali", None))
        self.label_15.setText(_translate("MainWindow", "This work is licensed under a \n"
"Creative Commons\n"
"Attribution 4.0 International License.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "About", None))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

