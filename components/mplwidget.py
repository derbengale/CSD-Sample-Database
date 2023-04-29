# Imports
from PySide6 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib
matplotlib.use('QT5Agg')

class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)   # Inherit from QWidget
        self.fig = Figure()
        self.fig.tight_layout()
        self.canvas = Canvas(self.fig)                  # Create canvas object
        self.canvas.setSizePolicy( QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.canvas.updateGeometry()
        self.ax = self.fig.add_subplot(111)
        self.ax.axes.margins(x = 0, y = 0)
        self.vbl = QtWidgets.QVBoxLayout()         # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        self.ax.set_xlabel("X_axis_title")
        self.ax.set_ylabel("Y_axis_title")
