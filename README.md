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
