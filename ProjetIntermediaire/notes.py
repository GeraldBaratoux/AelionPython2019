import sys, json
import numpy as np
from PySide2.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QDoubleSpinBox
from notes_ui import Ui_Form


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.dico = {}
        with open("Donnees.json") as json_file:
            self.dico = json.load(json_file)

        self.ui.cbAcademie.currentIndexChanged.connect(self.updateEtablissements)
        self.ui.cbEtablissement.currentIndexChanged.connect(self.updateClasse)
        self.ui.cbClasse.currentIndexChanged.connect(self.updateMatiere)
        self.ui.cbMatiere.currentIndexChanged.connect(self.updateSaisieEleve)

        self.updateAcademies()

    def updateAcademies(self):
        self.ui.cbAcademie.clear()
        for a in self.dico["academies"]:
            self.ui.cbAcademie.addItem(a["nom"])

    def updateEtablissements(self):
        self.ui.cbEtablissement.clear()
        for e in self.dico["academies"][self.ui.cbAcademie.currentIndex()]["etablissements"]:
            self.ui.cbEtablissement.addItem(e["nom"])

    def updateClasse(self):
        self.ui.cbClasse.clear()
        for a in self.dico["academies"][self.ui.cbAcademie.currentIndex()]["etablissements"][self.ui.cbEtablissement.currentIndex()]["classes"]:
            self.ui.cbClasse.addItem(a["nom"])

    def updateMatiere(self):
        dicoClasse = self.dico["academies"][self.ui.cbAcademie.currentIndex()]["etablissements"][self.ui.cbEtablissement.currentIndex()]["classes"][self.ui.cbClasse.currentIndex()]
        listeMatieres = []
        for eleve in dicoClasse["eleves"]:
            for matiere in eleve["matieres"]:
                listeMatieres.append(matiere["nom"])

        listeMatieresUniques = np.unique(listeMatieres)
        self.ui.cbMatiere.addItems(listeMatieresUniques)

    def updateSaisieEleve(self):
        cpt = 0
        self.ui.twNotes.clear()
        self.ui.twNotes.setColumnCount(2)
        dicoClasse = self.dico["academies"][self.ui.cbAcademie.currentIndex()]["etablissements"][self.ui.cbEtablissement.currentIndex()]["classes"][self.ui.cbClasse.currentIndex()]
        for eleve in dicoClasse["eleves"]:
            for matiere in eleve["matieres"]:
                mat = self.ui.cbMatiere.currentText()
                if matiere["nom"] == mat:
                    nomE = eleve["nom"]
                    self.ui.twNotes.setRowCount(cpt+1)
                    itemE = QTableWidgetItem(nomE)
                    self.ui.twNotes.setItem(cpt, 0, itemE)
                    spinB = QDoubleSpinBox()
                    spinB.setProperty("nom", nomE)
                    self.ui.twNotes.setCellWidget(cpt,1,spinB)
                    cpt = cpt+1

        self.ui.twNotes.setHorizontalHeaderLabels(['Nom', 'Note'])


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())