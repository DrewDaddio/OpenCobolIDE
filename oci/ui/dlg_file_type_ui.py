# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlg_file_type.ui'
#
# Created: Sun Sep  1 15:56:40 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from pyqode.qt import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(356, 144)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ide-icons/rc/silex-64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.comboBoxType = QtGui.QComboBox(Dialog)
        self.comboBoxType.setObjectName("comboBoxType")
        self.comboBoxType.addItem("")
        self.comboBoxType.addItem("")
        self.comboBoxType.addItem("")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBoxType)
        self.labelDir = QtGui.QLabel(Dialog)
        self.labelDir.setObjectName("labelDir")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelDir)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditPath = QtGui.QLineEdit(Dialog)
        self.lineEditPath.setObjectName("lineEditPath")
        self.horizontalLayout.addWidget(self.lineEditPath)
        self.toolButton = QtGui.QToolButton(Dialog)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.labelName = QtGui.QLabel(Dialog)
        self.labelName.setObjectName("labelName")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelName)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditName = QtGui.QLineEdit(Dialog)
        self.lineEditName.setObjectName("lineEditName")
        self.horizontalLayout_2.addWidget(self.lineEditName)
        self.comboBoxExtension = QtGui.QComboBox(Dialog)
        self.comboBoxExtension.setObjectName("comboBoxExtension")
        self.comboBoxExtension.addItem("")
        self.comboBoxExtension.addItem("")
        self.comboBoxExtension.addItem("")
        self.comboBoxExtension.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBoxExtension)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.buttonBox, self.comboBoxType)
        Dialog.setTabOrder(self.comboBoxType, self.lineEditName)
        Dialog.setTabOrder(self.lineEditName, self.comboBoxExtension)
        Dialog.setTabOrder(self.comboBoxExtension, self.lineEditPath)
        Dialog.setTabOrder(self.lineEditPath, self.toolButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "New file", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxType.setItemText(0, QtGui.QApplication.translate("Dialog", "Program", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxType.setItemText(1, QtGui.QApplication.translate("Dialog", "Module", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxType.setItemText(2, QtGui.QApplication.translate("Dialog", "Empty", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDir.setText(QtGui.QApplication.translate("Dialog", "Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.labelName.setText(QtGui.QApplication.translate("Dialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxExtension.setItemText(0, QtGui.QApplication.translate("Dialog", ".cbl", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxExtension.setItemText(1, QtGui.QApplication.translate("Dialog", ".cob", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxExtension.setItemText(2, QtGui.QApplication.translate("Dialog", ".CBL", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxExtension.setItemText(3, QtGui.QApplication.translate("Dialog", ".COB", None, QtGui.QApplication.UnicodeUTF8))

from . import ide_rc