"""Defect models for BearingDynLab.

The first defect implementation is intentionally simple: a localized outer-race defect is
represented as an additional local clearance when a rolling element passes through the
defect angular region.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


def wrap_to_pi(angle: np.ndarray | float) -> np.ndarray | float:
    """Wrap angle values to the interval [-pi, pi)."""
    return (np.asarray(angle) + np.pi) % (2.0 * np.pi) - np.pi


@dataclass(frozen=True)
class OuterRaceDefect:
    """Localized outer-race defect represented by an added radial clearance.

    Parameters
    ----------
    center_angle:
        Angular location of the defect in the fixed outer-race coordinate system.
    angular_width:
        Angular width of the defect region.
    depth:
        Additional local clearance caused by the defect.
    smooth:
        If true, use a cosine-smoothed defect profile. If false, use a rectangular profile.
    """

    center_angle: float
    angular_width: float
    depth: float
    smooth: bool = True

    def __post_init__(self) -> None:
        if self.angular_width <= 0.0:
            raise ValueError("angular_width must be positive.")
        if self.depth < 0.0:
            raise ValueError("depth must be non-negative.")

    def clearance_offset(self, angles: np.ndarray) -> np.ndarray:
        """Return additional clearance for rolling elements at the given angles."""
        angles = np.asarray(angles, dtype=float)
        relative = wrap_to_pi(angles - self.center_angle)
        half_width = 0.5 * self.angular_width
        inside = np.abs(relative) <= half_width
        offset = np.zeros_like(angles, dtype=float)

        if not np.any(inside):
            return offset

        if self.smooth:
            xi = relative[inside] / half_width
            offset[inside] = 0.5 * self.depth * (1.0 + np.cos(np.pi * xi))
        else:
            offset[inside] = self.depth

        return offset
