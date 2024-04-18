import sys
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer
from data_processing.serial_reader import SerialReader
from data_processing.signal_processing import apply_filters

class EMGApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Visualização de EMG em Tempo Real')
        self.setGeometry(100, 100, 800, 600)

        self.reader = SerialReader()
        self.reader.connect('COM3')
        self.paused = False

        self.error_label = QLabel()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.error_label)
        central_widget = pg.GraphicsLayoutWidget()
        self.layout.addWidget(central_widget)
        self.setCentralWidget(central_widget)

        self.plot = central_widget.addPlot(title="EMG Data")
        self.plot.setLabel('left', 'Amplitude')
        self.plot.setLabel('bottom', 'Time')

        self.x_data = np.array([])
        self.y_data = np.array([])

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_display)
        self.timer.start(50)  # Update every 50 milliseconds

    def update_display(self):
        if not self.paused:
            data = self.reader.read_data()
            if len(data) > 0:
                filtered_data = apply_filters(data)
                self.append_data(filtered_data)
                self.display_data()

    def append_data(self, data):
        self.x_data = np.append(self.x_data, len(self.y_data) + np.arange(len(data)))
        self.y_data = np.append(self.y_data, data)

    def display_data(self):
        self.plot.clear()
        self.plot.plot(self.x_data, the_y_data, pen=(255,0,0), name="EMG Data")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = EMGApp()
    ex.show()
    sys.exit(app.exec_())

    app = QApplication(sys.argv)
    ex = EMGApp()
    ex.show()
    sys.exit(app.exec_())
