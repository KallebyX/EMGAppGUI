from scipy.signal import butter, filtfilt, iirnotch
import numpy as np

def apply_filters(data, fs=1000):
    low_cutoff = 20
    b, a = butter(6, low_cutoff / (0.5 * fs), btype='low')
    low_passed = filtfilt(b, a, data)

    notch_freq = 60
    quality_factor = 30
    b, a = iirnotch(notch_freq / (0.5 * fs), quality_factor)
    notch_filtered = filtfilt(b, a, low_passed)

    return notch_filtered
