import sys
import os
from qgis.core import QgsApplication, QgsVectorLayer, QgsProject
from PyQt5 import QtWidgets, uic

class ExampleUi(QtWidgets.QDialog):  # Изменено с QWidget на QDialog
    def __init__(self):
        super(ExampleUi, self).__init__()
        ui_path = 'data/example.ui'
        uic.loadUi(ui_path, self)
        self.show()

# Инициализация QGIS без графического интерфейса
qgs = QgsApplication([], False)
qgs.initQgis()

# Получение экземпляра проекта
project = QgsProject.instance()

# Создание векторного слоя из файла GeoJSON
vlayer = QgsVectorLayer('../data/borders.geojson', 'borders1', "ogr")
project.addMapLayer(vlayer)
vlayer = QgsVectorLayer('../data/borders.geojson', 'borders2', "ogr")
project.addMapLayer(vlayer)
vlayer = QgsVectorLayer('../data/borders.geojson', 'borders3', "ogr")
project.addMapLayer(vlayer)

app = QtWidgets.QApplication(sys.argv)
window = ExampleUi()
app.exec_()

qgs.exit()