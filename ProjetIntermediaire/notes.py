import sys, json
from PySide2.QtWidgets import QApplication, QWidget
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


        #self.ui.twNotes.horizontalHeaderItem(0).setText(QApplication.translate("Form", "gggg", None, -1))
        #self.ui.twNomsEleves.setColumnCount(2)
        #self.ui.twNomsEleves.horizontalHeaderItem(0).setText(QApplication.translate("Form", "Nom", None, -1))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())