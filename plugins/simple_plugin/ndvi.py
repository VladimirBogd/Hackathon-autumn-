from qgis.PyQt.QtWidgets import QAction
from .form import NdviWidget

class NdviPlugin:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.action = QAction("Calc ")
