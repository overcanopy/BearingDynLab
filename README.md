# BearingDynLab

BearingDynLab is a research-code project for roller bearing dynamics simulation.

The long-term goal is to build a transparent, extensible platform for studying nonlinear bearing contact, roller/race interactions, cage dynamics, defect excitation, and rotor-bearing coupled vibration.

## Initial scope

The first development stage focuses on a minimal two-dimensional bearing model:

- fixed outer race,
- rotating inner race or prescribed shaft motion,
- rigid rolling elements,
- radial clearance,
- Hertzian normal contact,
- optional contact damping,
- bearing reaction force prediction,
- time-domain and frequency-domain post-processing.

## Development philosophy

1. Start from simple but verifiable models.
2. Keep theory, implementation, examples, and validation separate.
3. Add nonlinearities gradually.
4. Prefer readable code over premature optimization.
5. Treat validation cases as first-class project assets.

## Planned milestones

- **M1:** Bearing geometry and kinematic utilities.
- **M2:** Hertzian contact model for line contact.
- **M3:** Static load distribution under radial load and clearance.
- **M4:** Time-domain simulation of bearing reaction forces.
- **M5:** Local defects on outer race, inner race, and rollers.
- **M6:** Rotor-bearing coupling with a Jeffcott rotor.
- **M7:** Cage dynamics and roller-pocket contact.

## Quick start

Clone the repository and install it in editable mode:

```bash
git clone https://github.com/overcanopy/BearingDynLab.git
cd BearingDynLab
pip install -e ".[dev]"
```

Run the tests:

```bash
pytest
```

Run the first examples:

```bash
python examples/01_single_roller_contact.py
python examples/02_basic_load_distribution.py
python examples/03_time_domain_force_signal.py
```

## Current examples

- `01_single_roller_contact.py`: scalar Hertzian contact force under different indentations.
- `02_basic_load_distribution.py`: rolling-element load distribution under a prescribed shaft offset.
- `03_time_domain_force_signal.py`: prescribed rolling-element train rotation, nonlinear force history, and FFT peak detection.

## Current limitations

The current code does not yet solve full multibody roller-bearing dynamics. The rolling-element train motion is prescribed in the first time-domain example. Future versions should introduce shaft dynamics, cage dynamics, roller translational/rotational degrees of freedom, friction, defects, and experimental validation cases.
