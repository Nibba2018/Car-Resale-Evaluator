import joblib
from PyQt5 import QtWidgets, uic
import sys
import main_rc
import pickle as pk
import pandas as pd
import numpy as np

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
                self.brand.addItem(feature[6:])
                            


    def evaluation(self):
        query = pd.DataFrame(index = np.arange(0, 1), columns = features).fillna(0)
        query.drop('price', axis = 1, inplace = True)

        vehicleType = str(self.vehicleType.currentText())
        model = str(self.model.currentText())
        fuelType = str(self.fuelType.currentText())
        brand = str(self.brand.currentText())
        repDamage = str(self.repairedDamage.currentText())
        gearBox = str(self.gearBox.currentText())

        power = self.power.text()
        distance = self.distance.text()
        age = self.age.text()
        

        query['vehicleType_' + vehicleType] = 1
        query['model_' + model] = 1
        query['fuelType_' + fuelType] = 1
        query['brand_' + brand] = 1
        
        query['powerPS'] = power
        query['kilometer'] = distance
        query['Age'] = age

        if repDamage == "No":
            query['notRepairedDamage_yes'] = 1

        if gearBox == "Manual":
            query['gearbox_manual'] = 1


        print(vehicleType, model, fuelType, brand, repDamage, gearBox, power, distance, age)

        print(query)

        result = car_model.predict(query)
        print(result)

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()