import sys
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QWidget, QLabel, QHBoxLayout)

class Form(QWidget):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.edit = QLineEdit("Ton nom stp !!")
        self.button = QPushButton("Copier")
        self.buttonClear = QPushButton("Effacer")
        self.label = QLabel("")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layoutH = QHBoxLayout()
        layoutH.addWidget(self.button)
        layoutH.addWidget(self.buttonClear)
        layout.addWidget(self.edit)
        layout.addLayout(layoutH)
        layout.addWidget(self.label)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.copieNom)
        self.buttonClear.clicked.connect(self.effaceNom)
    # Greets the user
    def copieNom(self):
        self.label.setText(self.edit.text())

    def effaceNom(self):
        self.label.setText("")

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())