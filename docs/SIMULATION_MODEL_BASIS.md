# CHTS Physics & Implementation Matrix

| Principle | Governing Equation | Implementation Module |
| :--- | :--- | :--- |
| **Exergy Aggregation** | Y = Pin * 0.468 * (1 + sum(B)) * (ZT * 0.1) | variables/GEN_III_node_amplifiers.py |
| **Coulomb Pressure** | Pc = (sigma / mu_i) * E | variables/variable_theory_3.py |
| **EHD Freq Boost** | f = sqrt(Pc / (1000 * d)) | variables/variable_theory_3.py |
| **Seebeck Efficiency** | n = (dT / Th) * (1 / (1 + Rc * 100)) | variables/teg_sandwich.py |
| **Antoine Saturation** | Ts = B / (A - log10(P/1000)) - C | variables/GEN_III_zeotropic_mix.py |
| **Thermal Radiation** | Q = eps * sigma * A * (T^4 - Ts^4) | docs/SPACE_ADAPTATION.md |

---

## 🧩 Physical Principles & Code Mapping

### 1. The Core Aggregator
The exergy yield logic balances baseline thermodynamic potential with hardware-level remediation gains.
* **Physics:** $Y_{net} = P_{in} \cdot 0.468 \cdot (1 + \sum \beta) \cdot (ZT \cdot 0.1)$
* **Code Usage:** `get_optimized_realistic_yield` dynamically scales the baseline 46.8% based on the `phys_vars` dictionary.


### 2. Electro-Hydrodynamic (EHD) Dynamics
We use EHD to control phase-change instabilities within the scavenger channels.
* **Physics:** $f_{EHD} = \sqrt{\frac{P_c}{1000 \cdot d}}$
* **Code Usage:** `calculate_ehd_dynamics` determines the frequency multiplier applied to vapor-liquid bubble collapse.


### 3. Thermoelectric Interface
Contact resistance is modeled as a thermal shunt, reducing the effective Seebeck coefficient of the TEG sandwich.
* **Physics:** $\eta_{TEG} \propto \text{Carnot} \cdot \frac{1}{1 + (R_c \cdot 100)}$
* **Code Usage:** `simulate_teg_core` applies this penalty factor to ensure real-world accuracy.


### 4. Zeotropic Vapor Glide
Zeotropic mixtures enable non-isothermal phase transitions to minimize entropy generation.
* **Physics:** $\log_{10}(P) = A - \frac{B}{T + C}$
* **Code Usage:** `calculate_zeotropic_glide_recovery` predicts the saturation temperature to match the heat source glide.
