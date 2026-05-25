# RF Ionization Tuning Protocol

## Plasma Coupling
- **Impedance Matching:** The matching network must be tuned for a dynamic load impedance of 50Ω + j10Ω, representing the plasma-gas state at 1.2e4 S/m conductivity.
- **RF Feedback Loop:** Use a bidirectional power meter to monitor reflected power ($P_{refl}$). System must auto-attenuate if $P_{refl} > 5\%$ of forward power.

## Sensor Integration
- **Electron Density Sensing:** Langmuir probe array located at 25mm downstream from the inlet to verify active ionization density.
