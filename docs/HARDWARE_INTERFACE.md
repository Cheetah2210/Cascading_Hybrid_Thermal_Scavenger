# Hardware-Software Interface Map

The following Python modules act as the digital twins for the physical hardware components:

- **`php_oscillations.py`**: Governs physical capillary micro-channel pulse-flow dynamics.
- **`teg_sandwich.py`**: Maps to physical thermoelectric stack manufacturing tolerances and contact resistance (0.15 mΩ).
- **`GEN_III_node_amplifiers.py`**: Defines control logic for the RF-plasma impedance matching network.
- **`GEN_III_zeotropic_mix.py`**: Defines pressure-glide constants for the vapor-liquid manifold assembly.
