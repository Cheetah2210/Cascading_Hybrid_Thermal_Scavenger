# TEG Signal Management: GEN-III CHTS

## 1. Multiplexing Architecture
The system employs an analog-to-digital converter (ADC) array to monitor thermal voltage across the four cascade stages:
- **Stage 1 & 2:** High-sensitivity differential signaling.
- **Stage 3 & 4:** Impedance-matched signal path for zeotropic/adsorption monitoring.

## 2. Signal Integrity
- **Noise Mitigation:** All signal traces are isolated from the high-load thermal transfer lines to prevent common-mode noise.
- **Precision:** RTD inputs are fed through an instrumentation amplifier with a CMRR > 100dB.

## 3. Telemetry Output
- Standardized serial communication format (RS-485) for integration with the main controller logic.
