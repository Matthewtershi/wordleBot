import sys
import seaborn as sns
import matplotlib.pyplot as plt
import threading
import asyncio
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QTextEdit
from PyQt5.QtCore import QTimer, pyqtSignal, pyqtSlot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.ticker import FuncFormatter

from simulation import simRound

class LiveBarChart(QMainWindow):
    # Define a signal to communicate the results between threads
    result_ready = pyqtSignal(str, int)

    def __init__(self):
        super().__init__()

        self.frequencies = [0] * 7 
        self.setWindowTitle("Bot Simulation")
        self.setGeometry(100, 100, 800, 600)

        # Create a QWidget and set it as the central widget
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        layout = QVBoxLayout(self.main_widget)

        sns.set(style="whitegrid")

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.bars = self.ax.bar(range(1, 8), self.frequencies, color=sns.color_palette("deep", 7))
        self.ax.set_xlabel("Number of Attempts")
        self.ax.set_ylabel("Frequency")
        self.ax.set_title("Live Update of Attempt Frequencies")

        self.ax.yaxis.get_major_locator().set_params(integer=True)

        self.ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: '>6' if x == self.frequencies[-1] else str(int(x))))

        self.guess_display = QTextEdit(self)
        self.guess_display.setReadOnly(True)
        layout.addWidget(self.guess_display)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_chart)
        self.timer.start(500) 
        self.round_count = 0
        self.total_rounds = 4

        self.result_ready.connect(self.process_results)

    def run_round(self):
        return asyncio.run(simRound())

    def update_chart(self):
        # print(f"Update chart called. Round count: {self.round_count}")

        if self.round_count >= self.total_rounds:
            self.guess_display.append(f"{self.total_rounds} rounds ran. Program Finished")
            self.timer.stop()
            return

        threading.Thread(target=self.handle_round).start()

    def handle_round(self):
        final_word, attempts = self.run_round()
        self.result_ready.emit(final_word, attempts)

    @pyqtSlot(str, int)
    def process_results(self, guess, attempts):
        self.round_count += 1

        # Update the UI in the main thread
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

        if (self.round_count >= self.total_rounds):
            self.guess_display.append("Stopping program")
            self.timer.stop()

    def closeEvent(self, event):
        """handle closing program"""

        print("Closing application")

        if (self.timer.isActive):
            self.timer.stop()

        if self.thread.isRunning():
            self.thread.quit()
            self.thread.wait()

        QApplication.quit()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LiveBarChart()
    window.show()
    sys.exit(app.exec_())
