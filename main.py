import joblib
from PyQt5 import QtWidgets, uic
import sys
import main_rc
import pickle as pk

car_model = joblib.load("rf_cars.joblib")
with open("col_names.pkl", "rb") as f:
    features = pk.load(f)

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.evaluate.clicked.connect(self.evaluation)
        self.setupUI()
        self.show()

    def setupUI(self):

        self.vehicleType.addItem("Vehicle Type")
        self.gearBox.addItem("Gear Box")
        self.model.addItem("Model")
        self.fuelType.addItem("Fuel Type")
        self.brand.addItem("Brand")
        self.repairedDamage.addItem("Repaired Damage")

        self.repairedDamage.addItem("Yes")
        self.repairedDamage.addItem("No")

        self.gearBox.addItem("Manual")
        self.gearBox.addItem("Automatic")


        for feature in features:
            if feature.startswith("vehicleType_"):
                self.vehicleType.addItem(feature[12:])
            
            elif feature.startswith("model_"):
                self.model.addItem(feature[6:])

            elif feature.startswith("fuelType_"):
                self.fuelType.addItem(feature[9:])

            elif feature.startswith("brand_"):
                self.brand.addItem(feature[7:])
                            


    def evaluation(self):
        print("Hello")
        print(features)

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()