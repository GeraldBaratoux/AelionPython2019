import sys
from PySide2.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout
from PySide2.QtGui import QPainter, QPaintEvent, QPen
from PySide2.QtCore import QTimer, Qt, QTime

class monHorloge(QWidget):
    def __init__(self, parent=None):
        super(monHorloge, self).__init__(parent)

        currentTime= QTime.currentTime()
        self.heure = currentTime.hour()
        self.minute = currentTime.minute()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.increaseTime)
        self.timer.start()

    def changeFreq(self,val):
        self.timer.setInterval(val)
        self.timer.start()

    def increaseTime(self):
        self.minute += 1
        if self.minute == 60:
            self.minute = 0
            self.heure += 1
            if self.heure == 12:
                self.heure = 0
        self.update()

    def paintEvent(self, event:QPaintEvent):
        p = QPainter(self)
        p.setBrush(Qt.blue)
        p.drawRect(10,10,self.width()-20, self.height()-20)
        p.setBrush(Qt.yellow)
        p.drawEllipse(20,20,self.width()-40, self.height()-40)

        p.save()

        p.translate(self.width()/2,self.height()/2)

        p.save()

        p.rotate((-90 + self.heure*30)+(self.minute)/2)
        pen = QPen(Qt.green,10)
        p.setPen(pen)
        p.drawLine(0,0,(self.width()-40)/5,0)

        p.restore()

        p.rotate(-90 + self.minute*6)
        pen = QPen(Qt.black, 10)
        p.setPen(pen)
        p.drawLine(0, 0, (self.width() - 40) / 3, 0)

        p.restore()

        p.setBrush(Qt.red)
        p.drawEllipse((self.width()/2)-20,(self.height()/2)-20,40, 40)

class maFenetrePrincipale(QWidget):
    def __init__(self, parent=None):
        super(maFenetrePrincipale, self).__init__(parent)

        self.setMinimumSize(200,200)
        self.horloge = monHorloge()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(1,1000)

        layout = QVBoxLayout()
        layout.addWidget(self.horloge)
        layout.addWidget(self.slider)
        self.setLayout(layout)

        self.slider.valueChanged.connect(self.horloge.changeFreq)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fen = maFenetrePrincipale()
    fen.show()
    sys.exit(app.exec_())