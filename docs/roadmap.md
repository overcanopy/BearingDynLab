# BearingDynLab Roadmap

## Stage 0: Repository foundation

- Define project scope and repository structure.
- Add initial theory notes.
- Add basic Python package layout.
- Add simple examples and tests.

## Stage 1: Quasi-static bearing mechanics

Goal: compute roller angular positions, local indentation, Hertzian contact force, and global bearing reaction force.

Main tasks:

- bearing geometry data model,
- roller position generation,
- radial clearance model,
- normal contact indentation,
- line-contact Hertzian force law,
- load distribution visualization.

## Stage 2: Time-domain bearing force prediction

Goal: simulate time-varying bearing forces under prescribed rotation.

Main tasks:

- time integration loop,
- rotating inner race kinematics,
- optional contact damping,
- force history output,
- FFT-based vibration analysis.

## Stage 3: Defect excitation

Goal: represent common localized and distributed bearing faults.

Main tasks:

- outer-race defect,
- inner-race defect,
- roller defect,
- waviness and roughness placeholders,
- comparison with characteristic defect frequencies.

## Stage 4: Rotor-bearing coupling

Goal: connect nonlinear bearing forces to a simple rotor model.

Main tasks:

- Jeffcott rotor model,
- unbalance excitation,
- nonlinear support force from bearing module,
- response comparison with linearized bearing support.

## Stage 5: Cage and roller dynamics

Goal: move beyond prescribed roller kinematics and include cage interaction.

Main tasks:

- cage rotational degree of freedom,
- roller-pocket contact,
- friction and slip,
- skidding indicators,
- energy dissipation checks.

## Stage 6: Validation and software packaging

Goal: make the project credible and reusable.

Main tasks:

- benchmark cases from literature,
- dimensional consistency checks,
- automated tests,
- example gallery,
- documentation site,
- optional GUI or web interface.
