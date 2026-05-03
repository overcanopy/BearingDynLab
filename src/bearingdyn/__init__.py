"""BearingDynLab: research-code tools for roller bearing dynamics."""

from .contact import hertz_force
from .defects import OuterRaceDefect
from .geometry import BearingGeometry, roller_angles, radial_projection
from .visualization import (
    plot_dual_force_time_history,
    plot_dual_spectrum,
    plot_force_time_history,
    plot_roller_load_distribution,
    plot_spectrum,
)

__all__ = [
    "BearingGeometry",
    "OuterRaceDefect",
    "hertz_force",
    "plot_dual_force_time_history",
    "plot_dual_spectrum",
    "plot_force_time_history",
    "plot_roller_load_distribution",
    "plot_spectrum",
    "radial_projection",
    "roller_angles",
]
