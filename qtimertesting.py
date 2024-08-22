import sys
import random
import matplotlib.pyplot as plt
import asyncio
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class LiveBarChart(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the frequencies for numbers 1-6
        self.frequencies = [0] * 6

        # Set up the main window
        self.setWindowTitle("Live Bar Chart Example")
        self.setGeometry(100, 100, 800, 600)

        # Create a QWidget and set it as the central widget
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        # Create a QVBoxLayout for the central widget
        layout = QVBoxLayout(self.main_widget)

        # Create the matplotlib figure and bar chart
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # Initialize the bar chart with the initial frequencies
        self.bars = self.ax.bar(range(1, 7), self.frequencies)

        # Set labels and title
        self.ax.set_xlabel("Number")
        self.ax.set_ylabel("Frequency")
        self.ax.set_title("Live Update of Number Frequencies")

        # Set Y-axis to only show integer ticks
        self.ax.yaxis.get_major_locator().set_params(integer=True)

        # Start a QTimer to update the chart periodically
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_chart)
        self.timer.start(500)  # Update every 500 milliseconds

    def generate_random_number(self):
        self.timer.start(1000)
        return random.randint(1, 6)

    def update_chart(self):
        # Update the frequency list with the newly generated random number
        random_number = self.generate_random_number()
        self.frequencies[random_number - 1] += 1

        # Update the heights of the bars
        for bar, freq in zip(self.bars, self.frequencies):
            bar.set_height(freq)

        # Adjust the Y-axis to accommodate the maximum frequency
        self.ax.set_ylim(0, max(self.frequencies) + 1)

        # Redraw the canvas with the updated data
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LiveBarChart()
    window.show()
    sys.exit(app.exec_())
