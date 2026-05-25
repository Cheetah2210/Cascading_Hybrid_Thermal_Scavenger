# Experimental Calorimetry Methodology: GEN-III CHTS

## 1. Instrumentation Specifications
- **Flow Sensors:** Coriolis-effect meters (±0.05% mass flow accuracy).
- **Thermal Sensors:** Class A PT100 RTDs, vacuum-sealed, sampled at 10Hz.

## 2. Uncertainty Propagation
- Total system uncertainty is derived by the root-sum-square (RSS) of individual sensor errors, propagated through the exergy efficiency function $f(T_h, T_c, \dot{m})$. 
- Target aggregate error margin: < 2.5% of total recovery.

## 3. Data Provenance
- All raw data streams are serialized to local `.bin` files via signed SHA-256 hash to prevent post-collection modification.
- Bench tests must be run in triplicate to establish a standard deviation and confirm repeatability.
