import sys
import seaborn as sns
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QTextEdit
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from simulation import simRound

class LiveBarChart(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the frequencies for numbers 1-6
        self.frequencies = [0] * 7  # Including the ">6" category

        # Set up the main window
        self.setWindowTitle("Bot Simulation")
        self.setGeometry(100, 100, 800, 600)

        # Create a QWidget and set it as the central widget
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        # Create a QVBoxLayout for the central widget
        layout = QVBoxLayout(self.main_widget)

        # Set Seaborn style for the plots
        sns.set(style="whitegrid")

        # Create the matplotlib figure and bar chart
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.bars = self.ax.bar(range(1, 8), self.frequencies, color=sns.color_palette("deep", 7))
        self.ax.set_xlabel("Number of Attempts")
        self.ax.set_ylabel("Frequency")
        self.ax.set_title("Live Update of Attempt Frequencies")

        # Set Y-axis to only show integer ticks
        self.ax.yaxis.get_major_locator().set_params(integer=True)

        # Add a QTextEdit widget to display guesses
        self.guess_display = QTextEdit(self)
        self.guess_display.setReadOnly(True)
        layout.addWidget(self.guess_display)

        # Set up the timer for updating the chart
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_chart)
        self.timer.start(1000)  # Adjust as necessary

        self.round_count = 0
        self.total_rounds = 4

    async def run_round(self):
        # Run a single round and return the guess and attempts
        guess, attempts = await simRound()
        return guess, attempts

    def update_chart(self):
        print(f"Update chart called. Round count: {self.round_count}")

        # Run the simulation until the total rounds are completed
        if self.round_count >= self.total_rounds:
            self.guess_display.append(f"{self.total_rounds} rounds ran. Program Finished")
            self.timer.stop()  # Stop the timer when all rounds are completed
            return

        # Run a single round
        guess, attempts = self.run_round()
        self.round_count += 1

        # Display the guesses
        self.guess_display.append(f"Round {self.round_count}: {', '.join(guess)}")

        # Update the frequencies
        if attempts > 6:
            self.frequencies[-1] += 1
        else:
            self.frequencies[attempts - 1] += 1

        # Update the heights of the bars in the chart
        for bar, freq in zip(self.bars, self.frequencies):
            bar.set_height(freq)

        # Adjust Y-axis to better fit the data
        self.ax.set_ylim(0, max(self.frequencies) + 5)
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LiveBarChart()
    window.show()
    sys.exit(app.exec_())
