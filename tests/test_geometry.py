import numpy as np
import pytest

from bearingdyn.geometry import BearingGeometry, radial_projection, roller_angles


def test_bearing_geometry_rejects_invalid_values():
    with pytest.raises(ValueError):
        BearingGeometry(n_rollers=0, pitch_radius=0.025, roller_radius=0.004, radial_clearance=0.0)


def test_roller_angles_count_and_spacing():
    angles = roller_angles(4)
    assert len(angles) == 4
    np.testing.assert_allclose(angles, [0.0, np.pi / 2.0, np.pi, 3.0 * np.pi / 2.0])


def test_radial_projection_x_direction():
    angles = np.array([0.0, np.pi / 2.0, np.pi])
    projections = radial_projection((2.0, 0.0), angles)
    np.testing.assert_allclose(projections, [2.0, 0.0, -2.0], atol=1.0e-12)
