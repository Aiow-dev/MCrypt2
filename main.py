from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("Interfaces/MainWindow.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
# test
app.exec()
