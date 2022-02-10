import sys
import requests
import os

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

IP = '127.0.0.1'
PORT = '8000'

qtCreatorFile = "npv.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calc)

    def calc(self):
        """Расчет"""
        self.error.setText("")
        url = f"http://{IP}:{PORT}/".format(IP, PORT)
        year = int(self.year.toPlainText())
        rate = float(self.rate.toPlainText())
        r = requests.post(url, data={'year': year, "rate": rate})
        json = r.json()

        try:
            answer = json['npv']
            self.npv.setText(str(answer))
        except KeyError:
            error = json['error']['year'][0]
            self.error.setText(str(error))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
