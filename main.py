import sys
from PyQt5.QtWidgets import QApplication
from CounterWindow.mainWindow import Window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = Window()
    mywindow.show()
    sys.exit(app.exec_())
