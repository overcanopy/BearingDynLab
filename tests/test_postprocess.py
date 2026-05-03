import numpy as np
import pytest

from bearingdyn.postprocess import single_sided_fft


def test_single_sided_fft_detects_sine_frequency():
    sampling_rate = 1000.0
    target_frequency = 50.0
    time = np.arange(1000) / sampling_rate
    signal = np.sin(2.0 * np.pi * target_frequency * time)

    freq, amp = single_sided_fft(signal, sampling_rate)
    peak_index = 1 + int(np.argmax(amp[1:]))

    assert freq[peak_index] == pytest.approx(target_frequency)
    assert amp[peak_index] == pytest.approx(1.0, rel=1.0e-2)
