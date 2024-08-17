import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from simulation import simRound

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wordle Bot Simulation")
        self.setGeometry(100, 100, 800, 600)

        # Create a QWidget for the central area and a QVBoxLayout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create the matplotlib figure and canvas
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # Create input section
        self.input_label = QLabel("Enter a number of rounds to feed the simulation:")
        self.layout.addWidget(self.input_label)

        self.input_field = QLineEdit()
        self.layout.addWidget(self.input_field)

        self.update_button = QPushButton("Update Chart")
        self.update_button.clicked.connect(self.update_chart)
        self.layout.addWidget(self.update_button)

        # Initialize bar chart data
        self.x = ['1', '2', '3', '4', '5', '6', ">6"]
        self.y = np.zeros(len(self.x))  # Start with zeros
        self.bars = self.ax.bar(self.x, self.y, color='blue')

        self.ax.set_xlabel('Attempts')
        self.ax.set_ylabel('Values')
        self.ax.set_title('Dynamic Bar Chart')

        self.current_index = 0
        self.update_chart()

    def retrieveData(self):
        # Read number from input field
        try:
            return float(self.input_field.text())
        except ValueError:
            return 0  # Default to 0 if input is invalid

    def update_chart(self):
        # Get number from input field
        number = self.retrieveData()
        
        # Print the number to the console
        print(f"Input number: {number}")

        for i in range (int(number)):
            guess, attempts = simRound()

            attempts = 7 if attempts > 6 else attempts
            # Increment the height of the bar at the current index
            self.y[attempts-1] += 1

            # Update the bars
            for i, bar in enumerate(self.bars):
                bar.set_height(self.y[i])

            # Set the y-axis limit to ensure all bars are visible
            self.ax.set_ylim(0, max(self.y) + 10)

            # Update index for the next update
            # self.current_index = (self.current_index + 1) % len(self.x)
            self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
