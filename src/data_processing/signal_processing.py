from scipy.signal import butter, filtfilt, iirnotch
import numpy as np

class SignalProcessor:
    def __init__(self, low_cutoff=20, notch_freq=60, fs=1000):
        self.low_cutoff = low_cutoff
        self.notch_freq = notch_freq
        self.fs = fs

    def apply_filters(self, data):
        b, a = butter(6, self.low_cutoff / (0.5 * self.fs), btype='low')
        low_passed = filtfilt(b, a, data)

        quality_factor = 30
        b, a = iirnotch(self.notch_freq / (0.5 * self.fs), quality_factor)
        notch_filtered = filtfilt(b, a, low_passed)

        return notch_filtered

# Example of how to use:
if __name__ == "__main__":
    processor = SignalProcessor()
    test_data = np.random.randn(100)
    filtered_data = processor.apply_filters(test_data)
    print("Filtered data:", filtered_data)

