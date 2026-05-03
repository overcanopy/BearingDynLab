import numpy as np
import pytest

from bearingdyn.defects import OuterRaceDefect, wrap_to_pi


def test_wrap_to_pi_range():
    angles = np.array([-4.0 * np.pi, -np.pi, 0.0, np.pi, 4.0 * np.pi])
    wrapped = wrap_to_pi(angles)
    assert np.all(wrapped >= -np.pi)
    assert np.all(wrapped < np.pi)


def test_outer_race_defect_peak_at_center():
    defect = OuterRaceDefect(center_angle=0.0, angular_width=np.pi / 6.0, depth=10.0e-6)
    offsets = defect.clearance_offset(np.array([0.0]))
    assert offsets[0] == pytest.approx(10.0e-6)


def test_outer_race_defect_zero_outside_region():
    defect = OuterRaceDefect(center_angle=0.0, angular_width=np.pi / 6.0, depth=10.0e-6)
    offsets = defect.clearance_offset(np.array([np.pi / 2.0]))
    assert offsets[0] == pytest.approx(0.0)


def test_outer_race_rectangular_defect_profile():
    defect = OuterRaceDefect(
        center_angle=0.0,
        angular_width=np.pi / 6.0,
        depth=10.0e-6,
        smooth=False,
    )
    offsets = defect.clearance_offset(np.array([0.0, np.pi / 2.0]))
    np.testing.assert_allclose(offsets, [10.0e-6, 0.0])
