# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SaveDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(518, 392)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 30, 431, 311))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.saveDirLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.saveDirLabel.setFont(font)
        self.saveDirLabel.setObjectName("saveDirLabel")
        self.horizontalLayout.addWidget(self.saveDirLabel)
        self.saveDirEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.saveDirEdit.setEnabled(True)
        self.saveDirEdit.setReadOnly(True)
        self.saveDirEdit.setObjectName("saveDirEdit")
        self.horizontalLayout.addWidget(self.saveDirEdit)
        self.saveDirButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.saveDirButton.setObjectName("saveDirButton")
        self.horizontalLayout.addWidget(self.saveDirButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.csvBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.csvBox.setObjectName("csvBox")
        self.verticalLayout_3.addWidget(self.csvBox)
        self.xlsxBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.xlsxBox.setObjectName("xlsxBox")
        self.verticalLayout_3.addWidget(self.xlsxBox)
        self.jsonBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.jsonBox.setObjectName("jsonBox")
        self.verticalLayout_3.addWidget(self.jsonBox)
        self.xmlBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.xmlBox.setObjectName("xmlBox")
        self.verticalLayout_3.addWidget(self.xmlBox)
        self.yamlBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.yamlBox.setObjectName("yamlBox")
        self.verticalLayout_3.addWidget(self.yamlBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget_2)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.saveDirLabel.setText(_translate("Dialog", "保存路径"))
        self.saveDirButton.setText(_translate("Dialog", "选择"))
        self.label.setText(_translate("Dialog", "保存文件格式"))
        self.csvBox.setText(_translate("Dialog", "csv"))
        self.xlsxBox.setText(_translate("Dialog", "xlsx"))
        self.jsonBox.setText(_translate("Dialog", "json"))
        self.xmlBox.setText(_translate("Dialog", "xml"))
        self.yamlBox.setText(_translate("Dialog", "yaml"))
