import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
#from layout_colorwidget import Color

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
                
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class myapp(QWidget):
    def __init__(self):
        super().__init()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Icon')
        self.setWindwoIcon(QIcon('test_icon.png'))
        self.setGeometry(300,300,300,200)
        self.show()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
