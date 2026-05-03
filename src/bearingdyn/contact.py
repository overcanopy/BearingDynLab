"""Contact-force utilities for BearingDynLab."""

from __future__ import annotations


def hertz_force(
    indentation: float,
    stiffness: float,
    exponent: float = 10.0 / 9.0,
    damping: float = 0.0,
    indentation_rate: float = 0.0,
) -> float:
    """Return a scalar Hertzian normal contact force.

    Parameters
    ----------
    indentation:
        Local normal indentation. Contact is active only when this value is positive.
    stiffness:
        Effective Hertzian contact stiffness coefficient.
    exponent:
        Contact exponent. Use 10/9 as a simple line-contact approximation and 3/2 for
        point contact.
    damping:
        Optional normal contact damping coefficient.
    indentation_rate:
        Time derivative of indentation.

    Returns
    -------
    float
        Non-negative normal contact force.
    """
    if indentation <= 0.0:
        return 0.0

    elastic_force = stiffness * indentation**exponent
    damping_force = damping * indentation_rate
    return max(elastic_force + damping_force, 0.0)
