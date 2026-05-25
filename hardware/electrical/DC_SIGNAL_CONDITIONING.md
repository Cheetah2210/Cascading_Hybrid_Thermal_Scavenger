# DC Signal Conditioning & Monitoring
This document outlines the signal path for the GEN-III 4-Stage TEG Cascade.

## 1. Circuit Topology
- The system employs passive DC-coupled instrumentation amplifiers to capture millivolt-level output from the TEG modules.
- No RF oscillation, plasma tuning, or impedance matching is required.

## 2. Signal Path
1. **TEG Source:** Low-voltage DC.
2. **Amplification:** Precision DC-coupled gain stages.
3. **Filtering:** Low-pass RC filters (cutoff < 10Hz) to eliminate environmental thermal noise.
4. **Data Acquisition:** High-resolution ADC (analog-to-digital converter) for telemetry logging.
