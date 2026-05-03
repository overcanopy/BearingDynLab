"""Basic rolling-element load distribution example."""

import numpy as np

from bearingdyn.geometry import BearingGeometry, roller_angles
from bearingdyn.solver import bearing_reaction_force
from bearingdyn.visualization import plot_roller_load_distribution


def main() -> None:
    geometry = BearingGeometry(
        n_rollers=12,
        pitch_radius=0.025,
        roller_radius=0.004,
        radial_clearance=5.0e-6,
    )

    angles = roller_angles(geometry.n_rollers, cage_angle=0.0)
    displacement = (20.0e-6, 0.0)

    fx, fy, normal_forces = bearing_reaction_force(
        displacement=displacement,
        angles=angles,
        radial_clearance=geometry.radial_clearance,
        contact_stiffness=1.0e9,
    )

    print(f"Bearing reaction force: Fx = {fx:.3f} N, Fy = {fy:.3f} N")
    print("Rolling-element normal forces:")
    print(np.array2string(normal_forces, precision=3, suppress_small=True))

    plot_roller_load_distribution(
        angles,
        normal_forces,
        title="Rolling-element load distribution",
        output_path="outputs/load_distribution.png",
        show=True,
    )


if __name__ == "__main__":
    main()
