# Bearing Kinematics

This note defines the first kinematic assumptions used in BearingDynLab.

## Minimal 2D bearing model

The initial model is two-dimensional and assumes:

- fixed outer race,
- prescribed inner race or shaft motion,
- uniformly distributed rolling elements,
- rigid rolling elements,
- radial clearance,
- contact force acting along the local radial direction.

## Roller angular positions

For a bearing with `n` rolling elements, the nominal angular position of rolling element `i` is

```text
theta_i = theta_cage + 2*pi*i/n
```

where `theta_cage` is the cage or rolling-element train angle.

In the first implementation, `theta_cage` may be prescribed as

```text
theta_cage = omega_cage * t
```

A later version will compute cage dynamics from roller-cage interactions.

## Local radial approach

Let the shaft center displacement be

```text
u = [x, y]
```

The radial displacement projected along rolling-element direction `theta_i` is

```text
u_r_i = x*cos(theta_i) + y*sin(theta_i)
```

A simple local indentation model is

```text
delta_i = u_r_i - clearance
```

The rolling element is active in contact only when

```text
delta_i > 0
```

This is the simplest load-zone model. It is useful for building intuition, but later versions should include more detailed raceway geometry and roller deformation assumptions.
