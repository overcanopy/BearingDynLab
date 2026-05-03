# Hertzian Contact Model

This note defines the first contact-force model used in BearingDynLab.

## Normal contact law

For a local indentation `delta`, the normal contact force is modeled as

```text
F_n = k * delta^p,    delta > 0
F_n = 0,              delta <= 0
```

where:

- `k` is the effective contact stiffness coefficient,
- `p` is the contact exponent,
- `delta` is the local normal indentation.

Typical exponents are:

- `p = 3/2` for point contact, often used for ball bearings,
- `p = 10/9` as a simplified exponent for line contact, often used for roller bearings.

## Contact damping

A simple damping extension is

```text
F_n = k * delta^p + c * delta_dot
```

when `delta > 0`. To avoid nonphysical tensile contact forces, the result should be clipped as

```text
F_n = max(F_n, 0)
```

## First implementation choice

The first code version uses a scalar utility function:

```text
hertz_force(delta, stiffness, exponent, damping, delta_dot)
```

This function is intentionally independent of bearing geometry, so it can be tested separately.

## Limitations

The current model does not yet include:

- finite roller length correction,
- edge stress concentration,
- elastohydrodynamic lubrication,
- frictional tangential contact,
- thermal effects,
- local raceway roughness.

These effects should be added only after the minimal nonlinear contact model is tested and validated.
