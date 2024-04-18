import unittest
import numpy as np
from src.data_processing.signal_processing import SignalProcessor

class TestEMGFilter(unittest.TestCase):
    def test_filter(self):
        # Simula uma onda EMG com ruído
        emg_signal = self.generate_emg_signal()
        processor = SignalProcessor()
        # Aplica o filtro ao sinal simulado
        filtered_signal = processor.apply_filters(emg_signal)
        # Verifica se os dados filtrados estão dentro do intervalo esperado
        self.assertTrue(np.all(filtered_signal >= -1) and np.all(filtered_signal <= 1))

    def generate_emg_signal(self):
        # Parâmetros da onda EMG
        fs = 1000  # Frequência de amostragem (Hz)
        t = np.arange(0, 1, 1/fs)  # Tempo (1 segundo)
        frequency = 50  # Frequência do sinal EMG (Hz)
        amplitude = 1  # Amplitude do sinal EMG
        emg_signal = amplitude * np.sin(2 * np.pi * frequency * t)
        # Adiciona ruído ao sinal EMG
        noise = np.random.normal(0, 0.5, len(emg_signal))  # Ruído gaussiano com média 0 e desvio padrão 0.5
        emg_with_noise = emg_signal + noise
        return emg_with_noise

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
