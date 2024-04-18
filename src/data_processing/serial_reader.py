import serial
import serial.tools.list_ports
import numpy as np

class SerialReader:
    def __init__(self):
        self.ser = None

    def get_available_ports(self):
        ports = [port.device for port in serial.tools.list_ports.comports()]
        return ports

    def connect(self, port, baud_rate=115200):
        if self.ser and self.ser.is_open:
            self.ser.close()
        self.ser = serial.Serial(port, baudrate=baud_rate, timeout=1)

    def read_data(self):
        if not self.ser or not self.ser.is_open:
            raise ValueError("Porta serial não está aberta")
        data = []
        while self.ser.in_waiting > 0:
            line = self.ser.readline().decode('utf-8').strip()
            try:
                data.append(float(line))
            except ValueError:
                continue
        return np.array(data)

if __name__ == "__main__":
    # Instantiate SerialReader
    serial_reader = SerialReader()

    # Get available ports
    available_ports = serial_reader.get_available_ports()
    print("Available ports:", available_ports)

    # Connect to COM3 port
    port_name = 'COM3'
    baud_rate = 115200
    serial_reader.connect(port_name, baud_rate)
    print(f"Connected to port {port_name} at {baud_rate} baud rate.")

    # Read data
    try:
        while True:
            data = serial_reader.read_data()
            if len(data) > 0:
                print("Received data:", data)
    except KeyboardInterrupt:
        print("Keyboard interrupt detected. Closing port.")
        serial_reader.ser.close()
