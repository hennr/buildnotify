# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data/preferences.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName("Preferences")
        Preferences.resize(462, 357)
        Preferences.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(Preferences)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Preferences)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Preferences)
        self.tabWidget.setObjectName("tabWidget")
        self.serversTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serversTab.sizePolicy().hasHeightForWidth())
        self.serversTab.setSizePolicy(sizePolicy)
        self.serversTab.setObjectName("serversTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.serversTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.serversTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cctrayPathList = QtWidgets.QListView(self.groupBox_2)
        self.cctrayPathList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.cctrayPathList.setObjectName("cctrayPathList")
        self.gridLayout_3.addWidget(self.cctrayPathList, 0, 0, 1, 7)
        self.configureProjectButton = QtWidgets.QPushButton(self.groupBox_2)
        self.configureProjectButton.setEnabled(False)
        self.configureProjectButton.setObjectName("configureProjectButton")
        self.gridLayout_3.addWidget(self.configureProjectButton, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 1, 1, 1)
        self.addButton = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setObjectName("addButton")
        self.gridLayout_3.addWidget(self.addButton, 1, 4, 1, 1)
        self.removeButton = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeButton.sizePolicy().hasHeightForWidth())
        self.removeButton.setSizePolicy(sizePolicy)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout_3.addWidget(self.removeButton, 1, 3, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.serversTab, "")
        self.notificationsTab = QtWidgets.QWidget()
        self.notificationsTab.setObjectName("notificationsTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.notificationsTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.notificationsTab)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.successfulBuildsCheckbox = QtWidgets.QCheckBox(self.groupBox)
        self.successfulBuildsCheckbox.setObjectName("successfulBuildsCheckbox")
        self.gridLayout_2.addWidget(self.successfulBuildsCheckbox, 0, 0, 1, 1)
        self.brokenBuildsCheckbox = QtWidgets.QCheckBox(self.groupBox)
        self.brokenBuildsCheckbox.setObjectName("brokenBuildsCheckbox")
        self.gridLayout_2.addWidget(self.brokenBuildsCheckbox, 0, 1, 1, 1)
        self.fixedBuildsCheckbox = QtWidgets.QCheckBox(self.groupBox)
        self.fixedBuildsCheckbox.setObjectName("fixedBuildsCheckbox")
        self.gridLayout_2.addWidget(self.fixedBuildsCheckbox, 1, 0, 1, 1)
        self.stillFailingBuildsCheckbox = QtWidgets.QCheckBox(self.groupBox)
        self.stillFailingBuildsCheckbox.setObjectName("stillFailingBuildsCheckbox")
        self.gridLayout_2.addWidget(self.stillFailingBuildsCheckbox, 1, 1, 1, 1)
        self.connectivityIssuesCheckbox = QtWidgets.QCheckBox(self.groupBox)
        self.connectivityIssuesCheckbox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.connectivityIssuesCheckbox.setObjectName("connectivityIssuesCheckbox")
        self.gridLayout_2.addWidget(self.connectivityIssuesCheckbox, 2, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.notificationsTab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scriptCheckbox = QtWidgets.QCheckBox(self.groupBox_3)
        self.scriptCheckbox.setObjectName("scriptCheckbox")
        self.verticalLayout_3.addWidget(self.scriptCheckbox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scriptLabel = QtWidgets.QLabel(self.groupBox_3)
        self.scriptLabel.setObjectName("scriptLabel")
        self.horizontalLayout_3.addWidget(self.scriptLabel)
        self.scriptLineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.scriptLineEdit.setEnabled(False)
        self.scriptLineEdit.setText("")
        self.scriptLineEdit.setObjectName("scriptLineEdit")
        self.horizontalLayout_3.addWidget(self.scriptLineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.tabWidget.addTab(self.notificationsTab, "")
        self.miscTab = QtWidgets.QWidget()
        self.miscTab.setObjectName("miscTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.miscTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pollingIntervalSpinBox = QtWidgets.QSpinBox(self.miscTab)
        self.pollingIntervalSpinBox.setMinimumSize(QtCore.QSize(130, 0))
        self.pollingIntervalSpinBox.setMaximumSize(QtCore.QSize(130, 16777215))
        self.pollingIntervalSpinBox.setWrapping(False)
        self.pollingIntervalSpinBox.setMinimum(1)
        self.pollingIntervalSpinBox.setMaximum(60)
        self.pollingIntervalSpinBox.setSingleStep(1)
        self.pollingIntervalSpinBox.setObjectName("pollingIntervalSpinBox")
        self.gridLayout_5.addWidget(self.pollingIntervalSpinBox, 4, 1, 1, 1)
        self.pollingIntervalLabel = QtWidgets.QLabel(self.miscTab)
        self.pollingIntervalLabel.setObjectName("pollingIntervalLabel")
        self.gridLayout_5.addWidget(self.pollingIntervalLabel, 4, 0, 1, 1)
        self.showLastBuildTimeCheckbox = QtWidgets.QCheckBox(self.miscTab)
        self.showLastBuildTimeCheckbox.setObjectName("showLastBuildTimeCheckbox")
        self.gridLayout_5.addWidget(self.showLastBuildTimeCheckbox, 5, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_5)
        self.groupBox_4 = QtWidgets.QGroupBox(self.miscTab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.sortBuildByName = QtWidgets.QRadioButton(self.groupBox_4)
        self.sortBuildByName.setObjectName("sortBuildByName")
        self.verticalLayout_4.addWidget(self.sortBuildByName)
        self.sortBuildByLastBuildTime = QtWidgets.QRadioButton(self.groupBox_4)
        self.sortBuildByLastBuildTime.setChecked(True)
        self.sortBuildByLastBuildTime.setObjectName("sortBuildByLastBuildTime")
        self.verticalLayout_4.addWidget(self.sortBuildByLastBuildTime)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.tabWidget.addTab(self.miscTab, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.scriptLabel.setBuddy(self.scriptLineEdit)
        self.pollingIntervalLabel.setBuddy(self.pollingIntervalSpinBox)

        self.retranslateUi(Preferences)
        self.tabWidget.setCurrentIndex(0)
        self.scriptCheckbox.toggled['bool'].connect(self.scriptLineEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Preferences)

    def retranslateUi(self, Preferences):
        _translate = QtCore.QCoreApplication.translate
        Preferences.setWindowTitle(_translate("Preferences", "Preferences"))
        self.groupBox_2.setTitle(_translate("Preferences", "Monitored servers"))
        self.configureProjectButton.setText(_translate("Preferences", "Configure"))
        self.addButton.setToolTip(_translate("Preferences", "Add"))
        self.addButton.setText(_translate("Preferences", "+"))
        self.removeButton.setToolTip(_translate("Preferences", "Remove"))
        self.removeButton.setText(_translate("Preferences", "-"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.serversTab), _translate("Preferences", "Servers"))
        self.groupBox.setTitle(_translate("Preferences", "Notification settings"))
        self.successfulBuildsCheckbox.setText(_translate("Preferences", "successful builds"))
        self.brokenBuildsCheckbox.setText(_translate("Preferences", "broken builds"))
        self.fixedBuildsCheckbox.setText(_translate("Preferences", "fixed builds"))
        self.stillFailingBuildsCheckbox.setText(_translate("Preferences", "still failing builds"))
        self.connectivityIssuesCheckbox.setText(_translate("Preferences", "connectivity issues"))
        self.groupBox_3.setTitle(_translate("Preferences", "Custom notifications"))
        self.scriptCheckbox.setText(_translate("Preferences", "Execute script for notifications"))
        self.scriptLabel.setText(_translate("Preferences", "Script"))
        self.scriptLineEdit.setToolTip(_translate("Preferences", "#status# and #projects# would be replaced by the build status and projects respectively"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.notificationsTab), _translate("Preferences", "Notifications"))
        self.pollingIntervalSpinBox.setSuffix(_translate("Preferences", " seconds"))
        self.pollingIntervalLabel.setText(_translate("Preferences", "Server polling interval"))
        self.showLastBuildTimeCheckbox.setText(_translate("Preferences", "show last build time for each project"))
        self.groupBox_4.setTitle(_translate("Preferences", "Build Sort order"))
        self.sortBuildByName.setText(_translate("Preferences", "Sort builds by name"))
        self.sortBuildByLastBuildTime.setText(_translate("Preferences", "Sort builds by last build time"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.miscTab), _translate("Preferences", "Misc"))

from . import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Preferences = QtWidgets.QDialog()
    ui = Ui_Preferences()
    ui.setupUi(Preferences)
    Preferences.show()
    sys.exit(app.exec_())
