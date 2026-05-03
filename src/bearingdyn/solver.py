"""Minimal solver utilities for BearingDynLab."""

from __future__ import annotations

import numpy as np

from .contact import hertz_force
from .geometry import contact_indentations


def bearing_reaction_force(
    displacement: tuple[float, float],
    angles: np.ndarray,
    radial_clearance: float,
    contact_stiffness: float,
    contact_exponent: float = 10.0 / 9.0,
) -> tuple[float, float, np.ndarray]:
    """Compute the bearing reaction force from active rolling-element contacts.

    The force direction convention is the force exerted by rolling elements on the shaft.
    """
    indentations = contact_indentations(displacement, angles, radial_clearance)
    normal_forces = np.array(
        [hertz_force(delta, contact_stiffness, contact_exponent) for delta in indentations]
    )

    fx = -float(np.sum(normal_forces * np.cos(angles)))
    fy = -float(np.sum(normal_forces * np.sin(angles)))
    return fx, fy, normal_forces
