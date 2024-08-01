import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtCore import QTimer

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Real-Time Plotting')
        self.setGeometry(100, 100, 800, 500)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        layout = QVBoxLayout(self.central_widget)
        
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        layout.addWidget(self.canvas)
        
        self.data = np.random.normal(size=100)
        self.line, = self.canvas.axes.plot(self.data)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(100)  # Update every 100 ms

        self.simulation_count = 0

    def update_plot(self):
        if self.simulation_count < 100:
            new_data = np.random.normal()  # Generate new data point
            self.data = np.roll(self.data, -1)
            self.data[-1] = new_data
            self.line.set_ydata(self.data)
            self.canvas.draw()
            self.simulation_count += 1
        else:
            self.timer.stop()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
