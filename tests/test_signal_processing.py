# tests/test_signal_processing.py
import unittest
import numpy as np
from src.data_processing.signal_processing import SignalProcessor

class TestSignalProcessing(unittest.TestCase):

    def test_apply_filters(self):
        # Cria um array de teste com sinais senoidais
        t = np.linspace(0, 1, 1000, endpoint=False)
        data = np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 50 * t)
        
        processor = SignalProcessor()
        # Aplica filtragem
        filtered_data = processor.apply_filters(data)
        
        # Testa se o filtro está funcionando corretamente (e.g., reduzindo a amplitude do ruído de alta frequência)
        self.assertTrue(np.all(np.abs(filtered_data) < np.abs(data)))

if __name__ == '__main__':
    unittest.main()

        self.assertTrue(np.all(np.abs(filtered_data) < np.abs(data)))

if __name__ == '__main__':
    unittest.main()
