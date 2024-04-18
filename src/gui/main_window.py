import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer
from data_processing.serial_reader import SerialReader
from data_processing.signal_processing import apply_filters
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class EMGApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Visualização de EMG em Tempo Real')
        self.setGeometry(100, 100, 800, 600)

        self.reader = SerialReader()
        self.reader.connect('COM3')  # Connect specifically to COM3
        self.paused = False  # Variable to control the pause state

        self.error_label = QLabel()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.error_label)
        self.setLayout(self.layout)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(-1, 1)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_display)
        self.timer.start(50)  # Update every 50 milliseconds

    def update_display(self):
        try:
            if not self.paused:
                data = self.reader.read_data()
                if len(data) < 21:
                    return
                filtered_data = apply_filters(data)
                self.display_data(filtered_data)
        except Exception as e:
            self.error_label.setText(str(e))

    def display_data(self, data):
        self.ax.clear()
        self.ax.plot(data, color='b')
        self.ax.set_xlim(0, len(data))
        self.ax.set_ylim(min(data), max(data))
        self.canvas.draw()

    def keyPressEvent(self, event):
        # Handle pause/resume when the 'p' key is pressed
        if event.key() == ord('p'):
            self.paused = not self.paused

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = EMGApp()
    ex.show()
    sys.exit(app.exec_())
