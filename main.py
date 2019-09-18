import joblib
from PyQt5 import QtWidgets, uic
import sys
import main_rc

car_model = joblib.load("rf_cars.joblib")

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.evaluate.clicked.connect(self.evaluation)
        self.show()

    def evaluation(self):
        print("Hello")

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()