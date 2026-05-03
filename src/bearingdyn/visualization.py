"""Visualization utilities for BearingDynLab."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def _prepare_output_path(output_path: str | None) -> Path | None:
    """Create parent folders for an output figure path if needed."""
    if output_path is None:
        return None
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def plot_force_time_history(
    time: np.ndarray,
    force_x: np.ndarray,
    force_y: np.ndarray | None = None,
    title: str = "Bearing reaction force history",
    output_path: str | None = None,
    show: bool = True,
) -> None:
    """Plot bearing reaction force versus time."""
    plt.figure(figsize=(8, 4.5))
    plt.plot(time, force_x, label="Fx")

    if force_y is not None:
        plt.plot(time, force_y, label="Fy")

    plt.xlabel("Time [s]")
    plt.ylabel("Force [N]")
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    path = _prepare_output_path(output_path)
    if path is not None:
        plt.savefig(path, dpi=300)

    if show:
        plt.show()
    else:
        plt.close()


def plot_spectrum(
    frequency: np.ndarray,
    amplitude: np.ndarray,
    title: str = "Amplitude spectrum",
    xlim: tuple[float, float] | None = None,
    output_path: str | None = None,
    show: bool = True,
) -> None:
    """Plot a single-sided amplitude spectrum."""
    plt.figure(figsize=(8, 4.5))
    plt.plot(frequency, amplitude)

    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.grid(True)

    if xlim is not None:
        plt.xlim(*xlim)

    plt.tight_layout()

    path = _prepare_output_path(output_path)
    if path is not None:
        plt.savefig(path, dpi=300)

    if show:
        plt.show()
    else:
        plt.close()


def plot_dual_force_time_history(
    time: np.ndarray,
    healthy_force: np.ndarray,
    defect_force: np.ndarray,
    title: str = "Healthy vs defected force history",
    output_path: str | None = None,
    show: bool = True,
) -> None:
    """Plot healthy and defected force signals together."""
    plt.figure(figsize=(8, 4.5))
    plt.plot(time, healthy_force, label="Healthy")
    plt.plot(time, defect_force, label="Defected")

    plt.xlabel("Time [s]")
    plt.ylabel("Force [N]")
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    path = _prepare_output_path(output_path)
    if path is not None:
        plt.savefig(path, dpi=300)

    if show:
        plt.show()
    else:
        plt.close()


def plot_dual_spectrum(
    frequency: np.ndarray,
    healthy_amplitude: np.ndarray,
    defect_amplitude: np.ndarray,
    title: str = "Healthy vs defected spectrum",
    xlim: tuple[float, float] | None = None,
    output_path: str | None = None,
    show: bool = True,
) -> None:
    """Plot healthy and defected spectra together."""
    plt.figure(figsize=(8, 4.5))
    plt.plot(frequency, healthy_amplitude, label="Healthy")
    plt.plot(frequency, defect_amplitude, label="Defected")

    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.grid(True)
    plt.legend()

    if xlim is not None:
        plt.xlim(*xlim)

    plt.tight_layout()

    path = _prepare_output_path(output_path)
    if path is not None:
        plt.savefig(path, dpi=300)

    if show:
        plt.show()
    else:
        plt.close()


def plot_roller_load_distribution(
    angles: np.ndarray,
    normal_forces: np.ndarray,
    title: str = "Rolling-element load distribution",
    output_path: str | None = None,
    show: bool = True,
) -> None:
    """Plot rolling-element normal force versus angular position."""
    angles_deg = np.rad2deg(angles)

    plt.figure(figsize=(8, 4.5))
    plt.plot(angles_deg, normal_forces, marker="o")

    plt.xlabel("Rolling-element angle [deg]")
    plt.ylabel("Normal force [N]")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()

    path = _prepare_output_path(output_path)
    if path is not None:
        plt.savefig(path, dpi=300)

    if show:
        plt.show()
    else:
        plt.close()
