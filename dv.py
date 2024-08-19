import sys
import numpy as np
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from simulation import simRound

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wordle Bot Simulation")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.input_label = QLabel("Enter a number of rounds to feed the simulation:")
        self.layout.addWidget(self.input_label)

        self.input_field = QLineEdit()
        self.layout.addWidget(self.input_field)

        self.update_button = QPushButton("Update Chart")
        self.update_button.clicked.connect(self.start_simulation)
        self.layout.addWidget(self.update_button)

        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red;")
        self.layout.addWidget(self.error_label)

        self.x = ['1', '2', '3', '4', '5', '6', ">6"]
        self.y = np.zeros(len(self.x))
        self.bars = self.ax.bar(self.x, self.y, color='blue')

        self.ax.set_xlabel('Attempts')
        self.ax.set_ylabel('Values')
        self.ax.set_title('Dynamic Bar Chart')

    def retrieveData(self):
        try:
            return int(self.input_field.text())
        except ValueError:
            self.error_label.setText("Invalid input")
            return 0

    def start_simulation(self):
        number_of_rounds = self.retrieveData()
        if number_of_rounds > 0:
            threading.Thread(target=self.run_simulation, args=(number_of_rounds,)).start()

    def run_simulation(self, number_of_rounds):
        for i in range(number_of_rounds):
            try:
                guess, attempts = simRound()
                attempts = 7 if attempts > 6 else attempts
                self.y[attempts - 1] += 1

                self.update_chart()
                print(f"round {i + 1} ran")
            except Exception as e:
                self.error_label.setText(f"Error during simRound: {e}")
                break

    def update_chart(self):
        for i, bar in enumerate(self.bars):
            bar.set_height(self.y[i])

        self.ax.set_ylim(0, max(self.y) + 10)
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
