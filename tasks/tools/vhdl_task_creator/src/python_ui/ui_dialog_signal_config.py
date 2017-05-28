# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../qt5_ui/dialog_signal_config.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogSignalConfig(object):
    def setupUi(self, DialogSignalConfig):
        DialogSignalConfig.setObjectName("DialogSignalConfig")
        DialogSignalConfig.resize(510, 258)
        self.gridLayout = QtWidgets.QGridLayout(DialogSignalConfig)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 5, 1, 1)
        self.label_signal_name = QtWidgets.QLabel(DialogSignalConfig)
        self.label_signal_name.setObjectName("label_signal_name")
        self.gridLayout.addWidget(self.label_signal_name, 1, 1, 1, 1)
        self.signal_name = QtWidgets.QLineEdit(DialogSignalConfig)
        self.signal_name.setAutoFillBackground(True)
        self.signal_name.setText("")
        self.signal_name.setObjectName("signal_name")
        self.gridLayout.addWidget(self.signal_name, 1, 2, 1, 3)
        self.label_signal_type = QtWidgets.QLabel(DialogSignalConfig)
        self.label_signal_type.setObjectName("label_signal_type")
        self.gridLayout.addWidget(self.label_signal_type, 2, 1, 1, 1)
        self.signal_type = QtWidgets.QComboBox(DialogSignalConfig)
        self.signal_type.setObjectName("signal_type")
        self.signal_type.addItem("")
        self.signal_type.addItem("")
        self.signal_type.addItem("")
        self.signal_type.addItem("")
        self.signal_type.addItem("")
        self.gridLayout.addWidget(self.signal_type, 2, 2, 1, 3)
        self.custom_signal_type = QtWidgets.QLineEdit(DialogSignalConfig)
        self.custom_signal_type.setEnabled(False)
        self.custom_signal_type.setAutoFillBackground(True)
        self.custom_signal_type.setObjectName("custom_signal_type")
        self.gridLayout.addWidget(self.custom_signal_type, 2, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.label_length_type = QtWidgets.QLabel(DialogSignalConfig)
        self.label_length_type.setObjectName("label_length_type")
        self.gridLayout.addWidget(self.label_length_type, 3, 1, 1, 1)
        self.option_fixed_length = QtWidgets.QRadioButton(DialogSignalConfig)
        self.option_fixed_length.setObjectName("option_fixed_length")
        self.gridLayout.addWidget(self.option_fixed_length, 3, 2, 1, 2)
        self.option_variable_length = QtWidgets.QRadioButton(DialogSignalConfig)
        self.option_variable_length.setChecked(True)
        self.option_variable_length.setObjectName("option_variable_length")
        self.gridLayout.addWidget(self.option_variable_length, 3, 4, 1, 2)
        self.option_single = QtWidgets.QRadioButton(DialogSignalConfig)
        self.option_single.setEnabled(False)
        self.option_single.setCheckable(True)
        self.option_single.setObjectName("option_single")
        self.gridLayout.addWidget(self.option_single, 3, 6, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(9, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 7, 1, 1)
        self.label_length_placeholder = QtWidgets.QLabel(DialogSignalConfig)
        self.label_length_placeholder.setObjectName("label_length_placeholder")
        self.gridLayout.addWidget(self.label_length_placeholder, 4, 1, 1, 2)
        self.length_placeholder = QtWidgets.QLineEdit(DialogSignalConfig)
        self.length_placeholder.setAutoFillBackground(True)
        self.length_placeholder.setObjectName("length_placeholder")
        self.gridLayout.addWidget(self.length_placeholder, 4, 3, 1, 3)
        self.label_resulting_definition = QtWidgets.QLabel(DialogSignalConfig)
        self.label_resulting_definition.setObjectName("label_resulting_definition")
        self.gridLayout.addWidget(self.label_resulting_definition, 5, 1, 1, 2)
        self.resulting_definition = QtWidgets.QLineEdit(DialogSignalConfig)
        self.resulting_definition.setEnabled(True)
        self.resulting_definition.setAutoFillBackground(False)
        self.resulting_definition.setReadOnly(True)
        self.resulting_definition.setObjectName("resulting_definition")
        self.gridLayout.addWidget(self.resulting_definition, 5, 3, 1, 4)
        self.line = QtWidgets.QFrame(DialogSignalConfig)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 6, 1, 1, 6)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogSignalConfig)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 7, 6, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 8, 4, 1, 1)
        self.label_signal_name.setBuddy(self.signal_name)
        self.label_signal_type.setBuddy(self.signal_type)
        self.label_length_type.setBuddy(self.option_fixed_length)
        self.label_length_placeholder.setBuddy(self.length_placeholder)
        self.label_resulting_definition.setBuddy(self.resulting_definition)

        self.retranslateUi(DialogSignalConfig)
        self.buttonBox.accepted.connect(DialogSignalConfig.accept)
        self.buttonBox.rejected.connect(DialogSignalConfig.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogSignalConfig)

    def retranslateUi(self, DialogSignalConfig):
        _translate = QtCore.QCoreApplication.translate
        DialogSignalConfig.setWindowTitle(_translate("DialogSignalConfig", "Signal Config "))
        self.label_signal_name.setText(_translate("DialogSignalConfig", "Signal name"))
        self.label_signal_type.setText(_translate("DialogSignalConfig", "Signal type"))
        self.signal_type.setCurrentText(_translate("DialogSignalConfig", "std_logic_vector"))
        self.signal_type.setItemText(0, _translate("DialogSignalConfig", "std_logic_vector"))
        self.signal_type.setItemText(1, _translate("DialogSignalConfig", "std_logic"))
        self.signal_type.setItemText(2, _translate("DialogSignalConfig", "signed"))
        self.signal_type.setItemText(3, _translate("DialogSignalConfig", "unsigned"))
        self.signal_type.setItemText(4, _translate("DialogSignalConfig", "custom"))
        self.label_length_type.setText(_translate("DialogSignalConfig", "Length type"))
        self.option_fixed_length.setText(_translate("DialogSignalConfig", "Fixed"))
        self.option_variable_length.setText(_translate("DialogSignalConfig", "Variable"))
        self.option_single.setText(_translate("DialogSignalConfig", "Single"))
        self.label_length_placeholder.setText(_translate("DialogSignalConfig", "Length Placeholder"))
        self.label_resulting_definition.setText(_translate("DialogSignalConfig", "Resulting definition"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogSignalConfig = QtWidgets.QDialog()
    ui = Ui_DialogSignalConfig()
    ui.setupUi(DialogSignalConfig)
    DialogSignalConfig.show()
    sys.exit(app.exec_())
