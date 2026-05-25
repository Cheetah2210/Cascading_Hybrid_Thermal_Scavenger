# CHTS Global Replication Workflow

To successfully deploy and calibrate a CHTS unit, follow this three-stage validation pipeline:

### 1. Physics Validation
- Ensure the environment meets the repository dependency requirements.
- Execute the test suite to verify physics constraints:
  `pytest tests/`
- Confirm all modules (`variables/*.py`) pass within the defined hardware thresholds.

### 2. Hardware Fabrication
- Utilize CAD assets found in `/hardware/mechanical/`.
- Ensure all housing components are constructed using **Yttria-Stabilized Zirconia (YSZ)** for high-temperature structural integrity.
- Verify tolerances against the `SIZING_GUIDE.md`.

### 3. System Calibration
- Configure the manifold according to the fluid-specific Antoine constants found in `GEN_III_zeotropic_mix.py`.
- Initialize the RF-plasma impedance matchers using the parameters defined in `GEN_III_node_amplifiers.py`.
