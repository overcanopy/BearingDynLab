import numpy as np

from bearingdyn.visualization import (
    plot_dual_force_time_history,
    plot_dual_spectrum,
    plot_force_time_history,
    plot_roller_load_distribution,
    plot_spectrum,
)


def test_plot_functions_save_files(tmp_path):
    time = np.linspace(0.0, 1.0, 100)
    force_x = np.sin(2.0 * np.pi * 10.0 * time)
    force_y = np.cos(2.0 * np.pi * 10.0 * time)
    freq = np.linspace(0.0, 500.0, 100)
    amp1 = np.abs(np.sin(freq / 100.0))
    amp2 = np.abs(np.cos(freq / 100.0))
    angles = np.linspace(0.0, 2.0 * np.pi, 12, endpoint=False)
    loads = np.linspace(0.0, 100.0, 12)

    plot_force_time_history(
        time,
        force_x,
        force_y,
        output_path=str(tmp_path / "force_history.png"),
        show=False,
    )
    plot_spectrum(
        freq,
        amp1,
        output_path=str(tmp_path / "spectrum.png"),
        show=False,
    )
    plot_dual_force_time_history(
        time,
        force_x,
        force_y,
        output_path=str(tmp_path / "dual_force.png"),
        show=False,
    )
    plot_dual_spectrum(
        freq,
        amp1,
        amp2,
        output_path=str(tmp_path / "dual_spectrum.png"),
        show=False,
    )
    plot_roller_load_distribution(
        angles,
        loads,
        output_path=str(tmp_path / "load_distribution.png"),
        show=False,
    )

    assert (tmp_path / "force_history.png").exists()
    assert (tmp_path / "spectrum.png").exists()
    assert (tmp_path / "dual_force.png").exists()
    assert (tmp_path / "dual_spectrum.png").exists()
    assert (tmp_path / "load_distribution.png").exists()
