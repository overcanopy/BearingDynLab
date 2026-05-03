"""Time-domain bearing reaction-force signal under prescribed rolling-element motion.

This example is intentionally simple. It does not yet solve the full coupled dynamics of
shaft, rollers, and cage. Instead, it prescribes a small shaft-center displacement and a
constant rolling-element train speed, then computes the nonlinear contact reaction force
as the rolling elements pass through the load zone.
"""

from __future__ import annotations

import numpy as np

from bearingdyn.geometry import BearingGeometry, roller_angles
from bearingdyn.postprocess import single_sided_fft
from bearingdyn.solver import bearing_reaction_force


def simulate_force_signal(
    duration: float = 0.2,
    sampling_rate: float = 20_000.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Simulate bearing reaction force under prescribed cage rotation."""
    geometry = BearingGeometry(
        n_rollers=12,
        pitch_radius=0.025,
        roller_radius=0.004,
        radial_clearance=5.0e-6,
    )

    # A small static shaft-center offset creates a load zone.
    displacement = (20.0e-6, 0.0)

    # This is a prescribed rolling-element train speed, not yet solved cage dynamics.
    cage_frequency = 30.0  # Hz
    omega_cage = 2.0 * np.pi * cage_frequency

    contact_stiffness = 1.0e9
    contact_exponent = 10.0 / 9.0

    n_steps = int(duration * sampling_rate)
    time = np.arange(n_steps) / sampling_rate
    force_x = np.zeros_like(time)
    force_y = np.zeros_like(time)

    for step, t in enumerate(time):
        angles = roller_angles(geometry.n_rollers, cage_angle=omega_cage * t)
        fx, fy, _ = bearing_reaction_force(
            displacement=displacement,
            angles=angles,
            radial_clearance=geometry.radial_clearance,
            contact_stiffness=contact_stiffness,
            contact_exponent=contact_exponent,
        )
        force_x[step] = fx
        force_y[step] = fy

    freq, amp_x = single_sided_fft(force_x, sampling_rate)
    return time, force_x, force_y, freq, amp_x


def main() -> None:
    time, force_x, force_y, freq, amp_x = simulate_force_signal()

    print("Time-domain bearing force example")
    print(f"Number of samples: {time.size}")
    print(f"Fx range: {force_x.min():.3f} N to {force_x.max():.3f} N")
    print(f"Fy range: {force_y.min():.3f} N to {force_y.max():.3f} N")

    # Ignore the zero-frequency component when searching for the dominant oscillatory peak.
    peak_index = 1 + int(np.argmax(amp_x[1:]))
    print(f"Dominant Fx frequency: {freq[peak_index]:.3f} Hz")
    print(f"Dominant Fx amplitude: {amp_x[peak_index]:.6f} N")


if __name__ == "__main__":
    main()
