# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IHM.ui',
# licensing of 'IHM.ui' applies.
#
# Created: Fri Jul 26 09:53:42 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(968, 675)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setMinimumSize(QtCore.QSize(500, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(250, 16777215))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.cbClasse = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbClasse.sizePolicy().hasHeightForWidth())
        self.cbClasse.setSizePolicy(sizePolicy)
        self.cbClasse.setObjectName("cbClasse")
        self.gridLayout.addWidget(self.cbClasse, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.cbEtablissement = QtWidgets.QComboBox(self.groupBox)
        self.cbEtablissement.setObjectName("cbEtablissement")
        self.gridLayout.addWidget(self.cbEtablissement, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 434, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.cbAcademie = QtWidgets.QComboBox(self.groupBox)
        self.cbAcademie.setObjectName("cbAcademie")
        self.gridLayout.addWidget(self.cbAcademie, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pbAjoutAcademie = QtWidgets.QPushButton(self.groupBox)
        self.pbAjoutAcademie.setObjectName("pbAjoutAcademie")
        self.gridLayout.addWidget(self.pbAjoutAcademie, 4, 0, 1, 2)
        self.pbAjoutEtablissement = QtWidgets.QPushButton(self.groupBox)
        self.pbAjoutEtablissement.setObjectName("pbAjoutEtablissement")
        self.gridLayout.addWidget(self.pbAjoutEtablissement, 5, 0, 1, 2)
        self.pbAjoutClasse = QtWidgets.QPushButton(self.groupBox)
        self.pbAjoutClasse.setObjectName("pbAjoutClasse")
        self.gridLayout.addWidget(self.pbAjoutClasse, 6, 0, 1, 2)
        self.horizontalLayout.addWidget(self.groupBox)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.leNom = QtWidgets.QLineEdit(self.tab)
        self.leNom.setObjectName("leNom")
        self.gridLayout_2.addWidget(self.leNom, 3, 1, 1, 1)
        self.sbCoeff = QtWidgets.QDoubleSpinBox(self.tab)
        self.sbCoeff.setObjectName("sbCoeff")
        self.gridLayout_2.addWidget(self.sbCoeff, 2, 1, 1, 1)
        self.pbAjouterNotes = QtWidgets.QPushButton(self.tab)
        self.pbAjouterNotes.setObjectName("pbAjouterNotes")
        self.gridLayout_2.addWidget(self.pbAjouterNotes, 5, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.twNotes = QtWidgets.QTableWidget(self.tab)
        self.twNotes.setColumnCount(2)
        self.twNotes.setObjectName("twNotes")
        self.twNotes.setColumnCount(2)
        self.twNotes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twNotes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twNotes.setHorizontalHeaderItem(1, item)
        self.twNotes.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.twNotes, 4, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cbMatiere = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbMatiere.sizePolicy().hasHeightForWidth())
        self.cbMatiere.setSizePolicy(sizePolicy)
        self.cbMatiere.setObjectName("cbMatiere")
        self.horizontalLayout_3.addWidget(self.cbMatiere)
        self.pbAjoutMatiere = QtWidgets.QPushButton(self.tab)
        self.pbAjoutMatiere.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pbAjoutMatiere.setObjectName("pbAjoutMatiere")
        self.horizontalLayout_3.addWidget(self.pbAjoutMatiere)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.twNomsEleves = QtWidgets.QTableWidget(self.tab_2)
        self.twNomsEleves.setMaximumSize(QtCore.QSize(300, 16777215))
        self.twNomsEleves.setColumnCount(2)
        self.twNomsEleves.setObjectName("twNomsEleves")
        self.twNomsEleves.setColumnCount(2)
        self.twNomsEleves.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twNomsEleves.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.twNomsEleves.setHorizontalHeaderItem(3, item)
        self.horizontalLayout_2.addWidget(self.twNomsEleves)
        self.lRadar = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lRadar.sizePolicy().hasHeightForWidth())
        self.lRadar.setSizePolicy(sizePolicy)
        self.lRadar.setObjectName("lRadar")
        self.horizontalLayout_2.addWidget(self.lRadar)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Etablissement", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Classe", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Academie", None, -1))
        self.pbAjoutAcademie.setText(QtWidgets.QApplication.translate("Form", "Ajouter Academie", None, -1))
        self.pbAjoutEtablissement.setText(QtWidgets.QApplication.translate("Form", "Ajouter Etablissement", None, -1))




        self.pbAjoutClasse.setText(QtWidgets.QApplication.translate("Form", "Ajouter Classe", None, -1))
        self.pbAjouterNotes.setText(QtWidgets.QApplication.translate("Form", "Ajouter Notes", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Form", "Nom", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "Coeff", None, -1))
        self.twNotes.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Form", "Nom", None, -1))
        self.twNotes.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("Form", "Note", None, -1))
        self.pbAjoutMatiere.setText(QtWidgets.QApplication.translate("Form", "Ajouter Matiere", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "Matiere", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("Form", "Saisie", None, -1))
#        self.twNomsEleves.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Form", "Nom", None, -1))
#        self.twNomsEleves.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("Form", "Prenom", None, -1))
        self.lRadar.setText(QtWidgets.QApplication.translate("Form", "Radar", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("Form", "Données", None, -1))

