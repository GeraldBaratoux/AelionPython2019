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

        self.monRepertoire = self.lireJSON(filename)

        #self.lwListeNoms.itemClicked.connect(self.userSelected)
        #self.pbAjouter.clicked.connect(self.addUser)
        #self.pbModifier.clicked.connect(self.modifyUser)

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
        self.updateListw()

    def updateListw(self):
        self.lwListeNoms.clear()
        for fiche in self.monRepertoire["repertoire"]:
            self.lwListeNoms.addItem(fiche["nom"])

    def addUser(self):
        retour = QInputDialog().getText(self, "Ajout Utilisateur", "Nom:")
        if retour[0] == "":
            return
        # A completer

    #def modifyUser(self):

    #def userSelected(self):

    def lireJSON(self,fileName):
        with open(fileName) as json_file:
            dico = json.load(json_file)
            return dico
        return None

    #def sauveJSON(self, fileName):



if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    rep = Repertoire()
    rep.show()
    # Run the main Qt loop
    sys.exit(app.exec_())

