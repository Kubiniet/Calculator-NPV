import sys
import requests
import os

from PyQt5 import uic, QtWidgets

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
        url = str(self.url.toPlainText())
        year = int(self.year.toPlainText())
        rate = float(self.rate.toPlainText())
        try:
            r = requests.post(url, data={'year': year, "rate": rate})
            json = r.json()
            answer = json['npv']
            self.npv.setText(str(answer))

        except KeyError:
            r = requests.post(url, data={'year': year, "rate": rate})
            json = r.json()
            error = json['error']['year'][0]
            self.error.setText(str(error))
        except requests.exceptions.ConnectionError:
            self.error.setText(
                "Не удалось соединениться,попробуйте другой URL")
        except requests.exceptions.InvalidURL:
            self.error.setText(
                "Неправильный URL")
            self.url.setText("http://127.0.0.1:8000")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
