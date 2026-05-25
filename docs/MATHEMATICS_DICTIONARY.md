# CHTS MATHEMATICS DICTIONARY

This dictionary defines the governing physical equations used within the CHTS simulation modules. 

---

## 1. Exergy Aggregation
The net exergy yield ($Y_{net}$) is calculated by applying remediation coefficients to the baseline thermodynamic efficiency.

$$Y_{net} = \text{Gross}_{in} \cdot 0.468 \cdot (1 + \sum \text{Coeff}_{\text{remediation}}) \cdot (\frac{ZT}{1.0} \cdot 0.1)$$

* Where $\sum \text{Coeff}_{\text{remediation}} = \beta_s + f_{EHD} + B_{gain}$

## 2. EHD Frequency Boost
The acceleration of the vapor-liquid interface is governed by the Coulomb force density ($\rho_e E$).

$$f_{EHD} = \sqrt{\frac{\sigma \cdot E^2}{1000 \cdot d}}$$

* $\sigma$: Fluid conductivity ($S/m$)
* $E$: Electric field strength ($V/m$)
* $d$: Channel gap ($m$)

## 3. Radiative Thermal Rejection (Space Mode)
For vacuum-rated hardware, thermal rejection follows the Stefan-Boltzmann law.

$$Q_{rad} = \epsilon \sigma A (T_{surf}^4 - T_{space}^4)$$

* $\epsilon$: Surface emissivity
* $\sigma$: Stefan-Boltzmann constant ($5.67 \times 10^{-8} W/m^2K^4$)

## 4. Antoine Pressure-Temperature Glide
Used to determine saturation temperature ($T_{sat}$) based on system pressure ($P$).

$$\log_{10}(P) = A - \left( \frac{B}{T + C} \right)$$

---

### 🧩 Visualizing the Thermodynamic Relationships



*For implementation details, refer to the source code in [variables/](../variables/).*
