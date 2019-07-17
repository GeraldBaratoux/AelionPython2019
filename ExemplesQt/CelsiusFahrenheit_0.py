import sys
from PySide2.QtWidgets import (QLabel, QLCDNumber, QApplication,
    QVBoxLayout, QWidget, QDial, QHBoxLayout)

class TempConverter(QWidget):

    def __init__(self, parent=None):
        super(TempConverter, self).__init__(parent)
        # Create widgets
        self.labelC = QLabel("Celsius")
        self.labelF = QLabel("Fahrenheit")

        self.dialC = QDial()
        self.dialF = QDial()

        self.lcdC = QLCDNumber()
        self.lcdF = QLCDNumber()

        layoutC = QVBoxLayout()
        layoutC.addWidget(self.labelC)
        layoutC.addWidget(self.dialC)
        layoutC.addWidget(self.lcdC)

        layoutF = QVBoxLayout()
        layoutF.addWidget(self.labelF)
        layoutF.addWidget(self.dialF)
        layoutF.addWidget(self.lcdF)

        layoutGeneral = QHBoxLayout()
        layoutGeneral.addLayout(layoutC)
        layoutGeneral.addLayout(layoutF)

        self.setLayout(layoutGeneral)


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    tmpConv = TempConverter()
    tmpConv.show()
    # Run the main Qt loop
    sys.exit(app.exec_())