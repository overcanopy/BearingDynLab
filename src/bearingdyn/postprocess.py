"""Post-processing utilities for BearingDynLab."""

from __future__ import annotations

import numpy as np


def single_sided_fft(signal: np.ndarray, sampling_rate: float) -> tuple[np.ndarray, np.ndarray]:
    """Return single-sided FFT frequencies and amplitudes."""
    if sampling_rate <= 0.0:
        raise ValueError("sampling_rate must be positive.")
    signal = np.asarray(signal, dtype=float)
    if signal.ndim != 1:
        raise ValueError("signal must be one-dimensional.")
    if signal.size < 2:
        raise ValueError("signal must contain at least two samples.")

    centered = signal - np.mean(signal)
    spectrum = np.fft.rfft(centered)
    freq = np.fft.rfftfreq(signal.size, d=1.0 / sampling_rate)
    amp = 2.0 * np.abs(spectrum) / signal.size
    return freq, amp
