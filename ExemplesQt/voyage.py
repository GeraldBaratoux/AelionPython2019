import sys
from PySide2.QtWidgets import (QLabel, QLCDNumber, QApplication,
    QVBoxLayout, QWidget, QComboBox, QHBoxLayout, QSizePolicy)
#from PySide2 import Qt


class Voyage(QWidget):

    def __init__(self, parent=None):
        super(Voyage, self).__init__(parent)

        self.cbCompagnie = QComboBox()
        self.cbDestination = QComboBox()
        self.imgCourbe = QLabel()
        self.imgCourbe.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        genLayout = QHBoxLayout()
        layoutCombo = QVBoxLayout()

        layoutCombo.addWidget(self.cbCompagnie)
        layoutCombo.addWidget(self.cbDestination)

        genLayout.addLayout(layoutCombo)
        genLayout.addWidget(self.imgCourbe)
        self.setLayout(genLayout)

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    voy = Voyage()
    voy.show()
    # Run the main Qt loop
    sys.exit(app.exec_())