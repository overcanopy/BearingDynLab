"""Outer-race defect force-signal example.

A localized outer-race defect is represented as a local increase in radial clearance. When a
rolling element passes through the defect zone, its contact indentation is reduced, producing
a transient disturbance in the bearing reaction force.
"""

from __future__ import annotations

import numpy as np

from bearingdyn.defects import OuterRaceDefect
from bearingdyn.geometry import BearingGeometry, contact_indentations, roller_angles
from bearingdyn.postprocess import single_sided_fft
from bearingdyn.solver import bearing_reaction_force


def bearing_reaction_force_with_outer_defect(
    displacement: tuple[float, float],
    angles: np.ndarray,
    radial_clearance: float,
    contact_stiffness: float,
    defect: OuterRaceDefect,
    contact_exponent: float = 10.0 / 9.0,
) -> tuple[float, float, np.ndarray]:
    """Compute bearing reaction force with a simple outer-race clearance defect."""
    from bearingdyn.contact import hertz_force

    local_clearance = radial_clearance + defect.clearance_offset(angles)
    indentations = contact_indentations(displacement, angles, local_clearance)
    normal_forces = np.array(
        [hertz_force(delta, contact_stiffness, contact_exponent) for delta in indentations]
    )

    fx = -float(np.sum(normal_forces * np.cos(angles)))
    fy = -float(np.sum(normal_forces * np.sin(angles)))
    return fx, fy, normal_forces


def simulate_outer_race_defect_signal(
    duration: float = 0.5,
    sampling_rate: float = 20_000.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Compare healthy and outer-race-defected bearing force signals."""
    geometry = BearingGeometry(
        n_rollers=12,
        pitch_radius=0.025,
        roller_radius=0.004,
        radial_clearance=5.0e-6,
    )

    displacement = (20.0e-6, 0.0)
    cage_frequency = 30.0  # Hz, prescribed rolling-element train frequency
    omega_cage = 2.0 * np.pi * cage_frequency
    contact_stiffness = 1.0e9

    defect = OuterRaceDefect(
        center_angle=0.0,
        angular_width=np.deg2rad(8.0),
        depth=10.0e-6,
        smooth=True,
    )

    n_steps = int(duration * sampling_rate)
    time = np.arange(n_steps) / sampling_rate
    healthy_fx = np.zeros_like(time)
    defect_fx = np.zeros_like(time)

    for step, t in enumerate(time):
        angles = roller_angles(geometry.n_rollers, cage_angle=omega_cage * t)

        healthy_fx[step], _, _ = bearing_reaction_force(
            displacement=displacement,
            angles=angles,
            radial_clearance=geometry.radial_clearance,
            contact_stiffness=contact_stiffness,
        )

        defect_fx[step], _, _ = bearing_reaction_force_with_outer_defect(
            displacement=displacement,
            angles=angles,
            radial_clearance=geometry.radial_clearance,
            contact_stiffness=contact_stiffness,
            defect=defect,
        )

    freq, healthy_amp = single_sided_fft(healthy_fx, sampling_rate)
    _, defect_amp = single_sided_fft(defect_fx, sampling_rate)
    return time, healthy_fx, defect_fx, freq, healthy_amp, defect_amp


def main() -> None:
    time, healthy_fx, defect_fx, freq, healthy_amp, defect_amp = simulate_outer_race_defect_signal()

    print("Outer-race defect force-signal example")
    print(f"Number of samples: {time.size}")
    print(f"Healthy Fx range: {healthy_fx.min():.3f} N to {healthy_fx.max():.3f} N")
    print(f"Defected Fx range: {defect_fx.min():.3f} N to {defect_fx.max():.3f} N")

    peak_index = 1 + int(np.argmax(defect_amp[1:]))
    print(f"Dominant defected Fx frequency: {freq[peak_index]:.3f} Hz")
    print(f"Dominant defected Fx amplitude: {defect_amp[peak_index]:.6f} N")

    # The prescribed outer-race pass frequency in this simplified example is approximately
    # n_rollers * cage_frequency = 12 * 30 Hz = 360 Hz.
    target_frequency = 360.0
    target_index = int(np.argmin(np.abs(freq - target_frequency)))
    print(f"Amplitude near expected BPFO-like frequency ({target_frequency:.1f} Hz):")
    print(f"  healthy:  {healthy_amp[target_index]:.6f} N")
    print(f"  defected: {defect_amp[target_index]:.6f} N")


if __name__ == "__main__":
    main()
