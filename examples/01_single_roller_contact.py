"""Single rolling-element Hertzian contact example."""

from bearingdyn.contact import hertz_force


def main() -> None:
    stiffness = 1.0e9
    exponent = 10.0 / 9.0

    for indentation in [0.0, 1.0e-6, 5.0e-6, 1.0e-5]:
        force = hertz_force(indentation, stiffness, exponent)
        print(f"indentation = {indentation:.3e} m, force = {force:.3f} N")


if __name__ == "__main__":
    main()
