"""Geometry and kinematic utilities for BearingDynLab."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class BearingGeometry:
    """Minimal bearing geometry container.

    Parameters
    ----------
    n_rollers:
        Number of rolling elements.
    pitch_radius:
        Radius of the rolling-element pitch circle.
    roller_radius:
        Rolling element radius.
    radial_clearance:
        Effective radial clearance used in the first indentation model.
    """

    n_rollers: int
    pitch_radius: float
    roller_radius: float
    radial_clearance: float

    def __post_init__(self) -> None:
        if self.n_rollers <= 0:
            raise ValueError("n_rollers must be positive.")
        if self.pitch_radius <= 0.0:
            raise ValueError("pitch_radius must be positive.")
        if self.roller_radius <= 0.0:
            raise ValueError("roller_radius must be positive.")
        if self.radial_clearance < 0.0:
            raise ValueError("radial_clearance must be non-negative.")


def roller_angles(n_rollers: int, cage_angle: float = 0.0) -> np.ndarray:
    """Return uniformly distributed rolling-element angular positions."""
    if n_rollers <= 0:
        raise ValueError("n_rollers must be positive.")
    return cage_angle + 2.0 * np.pi * np.arange(n_rollers) / n_rollers


def radial_projection(displacement: tuple[float, float], angles: np.ndarray) -> np.ndarray:
    """Project a shaft-center displacement onto local radial directions."""
    x, y = displacement
    return x * np.cos(angles) + y * np.sin(angles)


def contact_indentations(
    displacement: tuple[float, float],
    angles: np.ndarray,
    radial_clearance: float,
) -> np.ndarray:
    """Compute simple radial contact indentation for each rolling element."""
    if radial_clearance < 0.0:
        raise ValueError("radial_clearance must be non-negative.")
    return radial_projection(displacement, angles) - radial_clearance
