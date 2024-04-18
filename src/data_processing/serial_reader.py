import serial
import serial.tools.list_ports
import numpy as np

class SerialReader:
    def __init__(self, port=None, baud_rate=115200):
        self.ser = None
        self.port = port
        self.baud_rate = baud_rate
        self.connect()

    def get_available_ports(self):
        ports = [port.device for port in serial.tools.list_ports.comports()]
        return ports

    def connect(self):
        if self.ser:
            self.ser.close()
        if self.port:
            try:
                self.ser = serial.Serial(self.port, baudrate=self.baud_rate, timeout=1)
                print(f"Connected to {self.port} at {self.baud_rate} baud rate.")
            except serial.SerialException as e:
                print(f"Failed to connect to {self.port}: {e}")
                self.ser = None

    def read_data(self):
        if not self.ser or not self.ser.is_open:
            self.connect()  # Attempt to reconnect
            if not self.ser:
                raise ValueError("Unable to open serial port.")
        data = []
        while self.ser.in_waiting > 0:
            line = self.ser.readline().decode('utf-8').strip()
            try:
                data.append(float(line))
            except ValueError:
                continue
        return np.array(data)

if __name__ == "__main__":
    serial_reader = SerialReader('COM3')
    available_ports = serial_reader.get_available_ports()
    print("Available ports:", available_ports)
    while True:
        data = serial_reader.read_data()
        if data.size > 0:
            print("Received data:", data)


    # Read data
    try:
        while True:
            data = serial_reader.read_data()
            if len(data) > 0:
                print("Received data:", data)
    except KeyboardInterrupt:
        print("Keyboard interrupt detected. Closing port.")
        serial_reader.ser.close()
