# Uncertainty Analysis & Bench Test Methodology

## 1. Sensor Error Margins
* **Thermocouples (Type-K):** ±1.5°C jitter at steady state.
* **Mass-Flow Transducers:** ±0.5% hysteresis at 50-100% flow range.
* **Voltage/Current Data-Loggers:** ±0.1% accuracy for power balance summation.

## 2. Statistical Propagation
The total system uncertainty is calculated via the Root-Sum-Square (RSS) method:
$$U_{total} = \sqrt{(U_{MHD})^2 + (U_{TEG})^2 + (U_{Zeo})^2}$$

## 3. Current Confidence Intervals
Based on the current unproven commercial scale, all outputs are marked with a **±12% experimental uncertainty index** until empirical calorimetry data is logged.
