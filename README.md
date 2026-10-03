# Spring-Mass-Damper System

Free body diagram, equation of motion, component sizing and Simulink simulation of a spring-mass-damper system under a 5 N pulse force.

## Overview

The system consists of a mass $m$, a spring $k$ and a damper $c$ (MKT3822 Lab 3, Application 2, Yildiz Technical University). The work covers four parts: drawing the free body diagram, deriving the equation of motion, designing the physical elements from material properties, and simulating the response in MATLAB/Simulink.

![Spring-mass-damper system](Homework%202.1.png)

## Modelling

The spring force is $-kx$ and the damping force is $-c\dot{x}$. Newton's second law gives

$$m\ddot{x} + c\dot{x} + kx = F(t)$$

For the free response ($F = 0$) the report gives the general solution

$$x(t) = C_1 \exp\left(\frac{t(-c - \sqrt{c^2 - 4km})}{2m}\right) + C_2 \exp\left(\frac{t(-c + \sqrt{c^2 - 4km})}{2m}\right)$$

The simulation uses $m = 1$ kg, $c = 1$ Ns/m, $k = 20$ N/m and the input force

$$F(t) = \begin{cases} 5 \text{ N} & 0 \le t \le 5 \text{ s} \\ 0 & t > 5 \text{ s} \end{cases}$$

## Component design

From the report:

- **Mass:** aluminium (density about 2700 kg/m³), 1 kg, volume about 0.00037 m³, a cube of about 0.071 m per side.
- **Damper:** silicone oil, $c = \delta A$ designed for $c = 1$ Ns/m.
- **Spring:** spring steel with shear modulus $G \approx 79.3$ GPa, $k = 20$ N/m, wire diameter $d = 0.01$ m and $N = 20$ active coils. The mean coil diameter follows from

$$k = \frac{G d^4}{8 D^3 N} \quad \Rightarrow \quad D = \left(\frac{G d^4}{8 k N}\right)^{1/3} \approx 0.628 \text{ m}$$

## Repository structure

```
.
├── spring_mass_damper.slx                       # Simulink model (force input, gains, two integrators, scope)
├── spring_mass_damper.m                         # Sets m, c, k and the model name
├── free_body.py                                 # Matplotlib sketch of the free body diagram
├── d_calculation.py                             # Mean coil diameter of the spring
├── Homework 2.1.png                             # System figure from the assignment
└── 22067606_LAB3_GR1_AR2_GöktuğCan-Şimay.pdf    # Lab report
```

## How to run

MATLAB/Simulink:

```matlab
spring_mass_damper            % defines m, c, k
open_system('spring_mass_damper')
sim('spring_mass_damper')
```

The report also lists the full MATLAB script that builds the Simulink model programmatically (Part 4).

Python (requires `matplotlib` with the TkAgg backend for `free_body.py`):

```bash
python d_calculation.py   # prints the mean coil diameter D
python free_body.py       # shows the free body diagram sketch
```

## Results

The report shows the applied force and the mass displacement over a 15 s simulation. It describes the response as underdamped: the mass oscillates while the 5 N force is applied, and after the force is removed at 5 s the oscillation amplitude decays until the mass returns to equilibrium.

## Author

Goktug Can Simay ([GitHub](https://github.com/simaygoktug) | [Website](https://goktugcansimay.com))
