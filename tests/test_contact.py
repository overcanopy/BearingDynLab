from bearingdyn.contact import hertz_force


def test_hertz_force_inactive_contact_is_zero():
    assert hertz_force(0.0, stiffness=1.0e9) == 0.0
    assert hertz_force(-1.0e-6, stiffness=1.0e9) == 0.0


def test_hertz_force_positive_contact():
    force = hertz_force(1.0e-6, stiffness=1.0e9, exponent=10.0 / 9.0)
    assert force > 0.0


def test_hertz_force_clips_negative_damped_result():
    force = hertz_force(
        indentation=1.0e-6,
        stiffness=1.0,
        exponent=1.0,
        damping=10.0,
        indentation_rate=-1.0,
    )
    assert force == 0.0
