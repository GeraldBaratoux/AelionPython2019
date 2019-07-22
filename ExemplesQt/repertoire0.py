import sys, json
from PySide2.QtWidgets import (QLabel, QApplication,QPushButton,
    QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QListWidget, QSpacerItem, QInputDialog, QSizePolicy)

filename = "repertoire.data"

class Repertoire(QWidget):

    def __init__(self, parent=None):
        super(Repertoire, self).__init__(parent)
        global filename
        self.monRepertoire = {}
        self.labelNom = QLabel("Nom")
        self.labelPrenom = QLabel("Prenom")
        self.labelTel = QLabel("Tel")
        self.leNom = QLineEdit()
        self.lePrenom =  QLineEdit()
        self.leTel = QLineEdit()
        self.lwListeNoms = QListWidget()
        self.pbAjouter = QPushButton("Ajouter")
        self.pbModifier = QPushButton("Modifier")

        layoutLabels = QVBoxLayout()
        layoutLabels.addWidget(self.labelNom)
        layoutLabels.addWidget(self.labelPrenom)
        layoutLabels.addWidget(self.labelTel)
        layoutLabels.addSpacerItem(QSpacerItem(10, 100, QSizePolicy.Expanding, QSizePolicy.Expanding))

        layoutLineEdit = QVBoxLayout()
        layoutLineEdit.addWidget(self.leNom)
        layoutLineEdit.addWidget(self.lePrenom)
        layoutLineEdit.addWidget(self.leTel)
        layoutLineEdit.addSpacerItem(QSpacerItem(10, 100, QSizePolicy.Expanding, QSizePolicy.Expanding))

        HLayout = QHBoxLayout()
        HLayout.addWidget(self.lwListeNoms)
        HLayout.addLayout(layoutLabels)
        HLayout.addLayout(layoutLineEdit)

        HLayoutButtons = QHBoxLayout()
        HLayoutButtons.addSpacerItem(QSpacerItem(10, 10, QSizePolicy.Expanding))
        HLayoutButtons.addWidget(self.pbModifier)
        HLayoutButtons.addWidget(self.pbAjouter)

        genLayout = QVBoxLayout()
        genLayout.addLayout(HLayout)
        genLayout.addLayout(HLayoutButtons)

        self.setLayout(genLayout)

    #def updateListw(self):

    #def addUser(self):

    #def modifyUser(self):

    #def userSelected(self):

    #def lireJSON(self,fileName):

    #def sauveJSON(self, fileName):



if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    rep = Repertoire()
    rep.show()
    # Run the main Qt loop
    sys.exit(app.exec_())

