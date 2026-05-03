# Equations of Motion

This note records the intended modeling direction for dynamic simulations.

## Bearing force as nonlinear support

In the first dynamic stage, the bearing is treated as a nonlinear support force acting on the shaft center:

```text
m*x_ddot + c*x_dot + k*x = F_external_x + F_bearing_x
m*y_ddot + c*y_dot + k*y = F_external_y + F_bearing_y
```

where the bearing force is obtained by summing all active rolling-element contacts.

## Contact-force summation

For rolling element `i`, the normal force is

```text
F_i = k_c * delta_i^p
```

when `delta_i > 0`; otherwise `F_i = 0`.

The bearing reaction force on the shaft is

```text
F_x = -sum(F_i*cos(theta_i))
F_y = -sum(F_i*sin(theta_i))
```

The negative sign means the reaction force opposes the shaft displacement direction that creates compression.

## Future extensions

Later versions should add:

- roller translational degrees of freedom,
- roller rotational degrees of freedom,
- cage rotational dynamics,
- friction and slip,
- lubricant-film effects,
- rotor-bearing coupling,
- defect-induced displacement excitation.
