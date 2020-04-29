# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testUI1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import CloudStack


api = 'http://10.12.0.144:8080/client/api'
apikey = 'bHyYDDIPGP5AZK7R4n1zS2TvxlSYjPLDzDoh3_4CZh7N8-jspXBWc3jeROdF-pdSf5v8IG_IKoUFGL3FmcpJNQ'
secret = 'sNrk-8eUayk2dpjlvZizC85-IXjZZgO6LQkhsTwlGxe1IxWl2d_wFI1yVzAY6Pt4P8qPJR7VY186lNF0LurnLw'
cloudstack = CloudStack.Client(api, apikey, secret)

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
        return QtGui.QAppl

class Ui_Dialog(object):

    def __init__(self):
        self.currentStackIndex = 0

        self.zones = ['epc-expr-kr-0']
        self.computeOfferings = cloudstack.listServiceOfferings()
        self.diskOfferings = ['No Thanks', 'Small', 'Medium', 'Large']
        self.templates = ''
        self.networks = ''

        self.seleted_zone = ''
        self.seleted_template = ''
        self.seleted_computeOffering = ''
        self.seleted_diskOffering = ''


    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(419, 464)

        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.stackedWidget = QtGui.QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))

        self.stack1UI()
        self.stack2UI()
        self.stack3UI()


        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(self.currentStackIndex)
        self.tabWidget.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Connect function to push button
        self.btn_test.clicked.connect(self.goNextStack)
        self.btn_main.clicked.connect(self.goNextStack)
        self.btn_start.clicked.connect(self.goNextStack)

        self.btn_back.clicked.connect(self.goPreviousStack)
        self.btn_back_2.clicked.connect(self.goPreviousStack)

        # Connect function to "zone" combo box
        self.combo_zone.currentIndexChanged.connect(self.loadComboBoxText)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.btn_history.setText(_translate("Dialog", "History", None))
        self.btn_test.setText(_translate("Dialog", "Start test", None))
        self.check_performance_2.setText(_translate("Dialog", "Performance", None))
        self.label_zone.setText(_translate("Dialog", "Zone : ", None))
        self.label_template.setText(_translate("Dialog", "Template : ", None))
        self.label_computeOf.setText(_translate("Dialog", "Compute Offering : ", None))
        self.label_diskOf.setText(_translate("Dialog", "Disk Offering : ", None))
        self.label_network.setText(_translate("Dialog", "Network : ", None))
        self.check_function_2.setText(_translate("Dialog", "Function", None))
        self.btn_back.setText(_translate("Dialog", "Back", None))
        self.btn_start.setText(_translate("Dialog", "Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_vm), _translate("Dialog", "VM", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_gpu), _translate("Dialog", "GPU", None))
        self.label_result.setText(_translate("Dialog", "Result", None))
        self.btn_back_2.setText(_translate("Dialog", "Back", None))
        self.btn_main.setText(_translate("Dialog", "Main", None))

    def stack1UI(self):
        self.page_1 = QtGui.QWidget()
        self.page_1.setObjectName(_fromUtf8("page_1"))

        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page_1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))

        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.btn_history = QtGui.QPushButton(self.page_1)
        self.btn_history.setObjectName(_fromUtf8("btn_history"))
        self.horizontalLayout.addWidget(self.btn_history)

        self.btn_test = QtGui.QPushButton(self.page_1)
        self.btn_test.setObjectName(_fromUtf8("btn_test"))
        self.horizontalLayout.addWidget(self.btn_test)

        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.stackedWidget.addWidget(self.page_1)

    def stack2UI(self):
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.gridLayout = QtGui.QGridLayout(self.page_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.page_2)

        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_vm = QtGui.QWidget()
        self.tab_vm.setObjectName(_fromUtf8("tab_vm"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_vm)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.check_performance_2 = QtGui.QCheckBox(self.tab_vm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_performance_2.sizePolicy().hasHeightForWidth())
        self.check_performance_2.setSizePolicy(sizePolicy)
        self.check_performance_2.setObjectName(_fromUtf8("check_performance_2"))
        self.gridLayout_2.addWidget(self.check_performance_2, 0, 1, 1, 1)

        self.lay_vmInfo = QtGui.QFormLayout()
        self.lay_vmInfo.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.lay_vmInfo.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.lay_vmInfo.setRowWrapPolicy(QtGui.QFormLayout.DontWrapRows)
        self.lay_vmInfo.setFormAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lay_vmInfo.setContentsMargins(-1, 0, -1, 30)
        self.lay_vmInfo.setHorizontalSpacing(0)
        self.lay_vmInfo.setVerticalSpacing(30)
        self.lay_vmInfo.setObjectName(_fromUtf8("lay_vmInfo"))

        self.label_zone = QtGui.QLabel(self.tab_vm)
        self.label_zone.setObjectName(_fromUtf8("label_zone"))
        self.lay_vmInfo.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_zone)
        self.combo_zone = QtGui.QComboBox(self.tab_vm)
        self.combo_zone.setObjectName(_fromUtf8("combo_zone"))
        self.lay_vmInfo.setWidget(0, QtGui.QFormLayout.FieldRole, self.combo_zone)

        self.combo_zone.addItems(self.zones)

        self.label_template = QtGui.QLabel(self.tab_vm)
        self.label_template.setObjectName(_fromUtf8("label_template"))
        self.lay_vmInfo.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_template)
        self.combo_template = QtGui.QComboBox(self.tab_vm)
        self.combo_template.setObjectName(_fromUtf8("combo_template"))
        self.lay_vmInfo.setWidget(1, QtGui.QFormLayout.FieldRole, self.combo_template)

        self.label_computeOf = QtGui.QLabel(self.tab_vm)
        self.label_computeOf.setObjectName(_fromUtf8("label_computeOf"))
        self.lay_vmInfo.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_computeOf)
        self.combo_computeOf = QtGui.QComboBox(self.tab_vm)
        self.combo_computeOf.setObjectName(_fromUtf8("combo_computeOf"))
        self.lay_vmInfo.setWidget(2, QtGui.QFormLayout.FieldRole, self.combo_computeOf)

        self.label_diskOf = QtGui.QLabel(self.tab_vm)
        self.label_diskOf.setObjectName(_fromUtf8("label_diskOf"))
        self.lay_vmInfo.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_diskOf)
        self.combo_diskOf = QtGui.QComboBox(self.tab_vm)
        self.combo_diskOf.setObjectName(_fromUtf8("combo_diskOf"))
        self.lay_vmInfo.setWidget(3, QtGui.QFormLayout.FieldRole, self.combo_diskOf)

        self.label_network = QtGui.QLabel(self.tab_vm)
        self.label_network.setObjectName(_fromUtf8("label_network"))
        self.lay_vmInfo.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_network)
        self.combo_network = QtGui.QComboBox(self.tab_vm)
        self.combo_network.setObjectName(_fromUtf8("combo_network"))
        self.lay_vmInfo.setWidget(4, QtGui.QFormLayout.FieldRole, self.combo_network)

        self.gridLayout_2.addLayout(self.lay_vmInfo, 1, 0, 1, 2)
        self.check_function_2 = QtGui.QCheckBox(self.tab_vm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_function_2.sizePolicy().hasHeightForWidth())
        self.check_function_2.setSizePolicy(sizePolicy)
        self.check_function_2.setObjectName(_fromUtf8("check_function_2"))

        self.gridLayout_2.addWidget(self.check_function_2, 0, 0, 1, 1)
        self.btn_back = QtGui.QPushButton(self.tab_vm)
        self.btn_back.setObjectName(_fromUtf8("btn_back"))
        self.gridLayout_2.addWidget(self.btn_back, 2, 0, 1, 1)
        self.btn_start = QtGui.QPushButton(self.tab_vm)
        self.btn_start.setObjectName(_fromUtf8("btn_start"))
        self.gridLayout_2.addWidget(self.btn_start, 2, 1, 1, 1)
        self.check_function_2.raise_()
        self.check_performance_2.raise_()
        self.btn_back.raise_()
        self.btn_start.raise_()
        self.tabWidget.addTab(self.tab_vm, _fromUtf8(""))

        self.tab_gpu = QtGui.QWidget()
        self.tab_gpu.setObjectName(_fromUtf8("tab_gpu"))
        self.tabWidget.addTab(self.tab_gpu, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)

        self.loadComboBoxText()


    def stack3UI(self):
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.label_result = QtGui.QLabel(self.page_3)
        self.label_result.setGeometry(QtCore.QRect(20, 30, 81, 31))
        self.label_result.setObjectName(_fromUtf8("label_result"))

        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.page_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(160, 340, 221, 80))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))

        self.lay_select_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.lay_select_2.setObjectName(_fromUtf8("lay_select_2"))

        self.btn_back_2 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_back_2.setObjectName(_fromUtf8("btn_back_2"))

        self.lay_select_2.addWidget(self.btn_back_2)
        self.btn_main = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_main.setObjectName(_fromUtf8("btn_main"))
        self.lay_select_2.addWidget(self.btn_main)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout.addWidget(self.stackedWidget)

    def goNextStack(self):
        if self.currentStackIndex >= 2 :
            self.currentStackIndex = 0
        else :
            self.currentStackIndex += 1
        self.stackedWidget.setCurrentIndex(self.currentStackIndex)

    def goPreviousStack(self):
        if self.currentStackIndex <= 0 :
            self.currentStackIndex = 0
        else:
            self.currentStackIndex -= 1
        self.stackedWidget.setCurrentIndex(self.currentStackIndex)

    # Load texts in combo boxes
    def loadComboBoxText(self):
        print("loadComboBoxText")
        print(str(self.combo_zone.currentText()))

        if str(self.combo_zone.currentText()) == 'epc-expr-kr-0':
            print("loadComboBoxText -  str(self.combo_zone.currentText()) == 'epc-expr-kr-0'")
            self.seleted_zone = '7327e4c4-3b7e-408e-a7f2-eec586ec93ee'
            self.templates = cloudstack.listTemplates({'templatefilter': 'executable', 'zoneid': self.seleted_zone})
            self.networks = cloudstack.listNetworks({'zoneid': self.seleted_zone})

            self.clearComboBoxItem()
            self.addComboBoxItem()

    def clearComboBoxItem(self):
        print("clearComboBoxItem")
        self.combo_network.clear()
        self.combo_template.clear()
        self.combo_computeOf.clear()
        self.combo_diskOf.clear()

    def addComboBoxItem(self):
        print("addComboBoxItem")

        for diskOffering in self.diskOfferings:
            self.combo_diskOf.addItem(diskOffering)

        for network in self.networks:
            self.combo_network.addItem(str(network['name']))

        for template in self.templates:
            self.combo_template.addItem(str(template['name']))

        for computeOffering in self.computeOfferings:
            self.combo_computeOf.addItem(str(computeOffering['name']))

    def getSelectedZone(self):
        self.seleted_zone = self.combo_zone.currentText()
        return self.seleted_zone

    def getSelectedTemplate(self):
        self.seleted_template = self.combo_template.currentText()
        return self.seleted_template

    def getSelectedComputeOf(self):
        self.seleted_computeOffering = self.combo_computeOf.currentText()
        return self.seleted_computeOffering

    def getSelectedDiskOf(self):
        self.seleted_diskOffering = self.combo_diskOf.currentText()
        return self.seleted_diskOffering



    # Start test
    def startTest(self):
        return

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

