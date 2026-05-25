# Stage 4: Adsorption Desiccant Bottoming Cycle (Thermal Offset)

## ⚖️ License
Author: Emily 🌻 (Cheetahs Creations)
Licensed under the [CERN Open Hardware Licence v1.2](../License.txt).

---

## 🔬 Physics & Thermodynamic Foundations

Stage 4 of the **Cascading Hybrid Thermal Scavenger (CHTS)** addresses the ultra-low-grade thermal boundary ($60°C - 90°C$) exiting the Stage 3 zeotropic condenser. 

At this low temperature drop, attempting further direct mechanical or solid-state electrical conversion encounters a punishingly low Carnot efficiency ceiling. Instead of fighting a losing battle against electrical conversion efficiency penalties, Stage 4 transitions the energy from a **thermal-to-electrical** vector to a **thermal-to-cooling offset** vector.

### The Adsorption Cycle Mechanics
The loop utilizes a solid-state **Silica Gel–Water** working pair configured as a cyclic, zero-parasitic desiccant bed. The cycle operates by separating the physical processes into two alternating phases driven entirely by the residual exergy stream:

1. **Desorption (Regeneration Phase):** Low-grade thermal fluid from Stage 3 flows through the internal heat exchanger of the saturated desiccant bed. The thermal energy breaks the physical van der Waals bonds holding the water molecules to the silica gel matrix, driving off water vapor at high pressure to the condenser.
2. **Adsorption (Cooling Phase):** Once dry, the bed is isolated and cooled to ambient temperature. It is then re-exposed to the low-pressure evaporator loop. The silica gel aggressively draws in water vapor, causing rapid low-pressure evaporation in the remote chiller block. This phase change extracts heat directly from the data center's chilled water loop, producing facility-grade cooling water ($7°C$).

[attachment_0](attachment)

---

## 📊 Mathematical Validation & Exergy Framework

The environmental reference state (dead state) is defined as:
* $T_0 = 298.15 \text{ K}$ ($25°C$)
* Ambient rejection temperature: $T_{\text{amb}} = 303.15 \text{ K}$ ($30°C$)
* Target chilled water generation: $T_{\text{chilled}} = 280.15 \text{ K}$ ($7°C$)

### 1. Thermal Coefficient of Performance ($\text{COP}_{\text{th}}$)
The realistic thermal coefficient of performance for the low-grade silica gel matrix is modeled conservatively to account for real-world losses:
$$\text{COP}_{\text{th}} = \frac{Q_{\text{cooling}}}{Q_{\text{input}}} \approx 0.60$$

### 2. Exergy Input ($E_{\text{in}}$)
The thermodynamic quality of the incoming fluid stream per kilowatt of low-grade thermal waste heat is a function of its temperature gradient above the dead state:
$$E_{\text{in}} = 1.0 \text{ kW} \cdot \left(1 - \frac{T_0}{T_{\text{source}}}\right)$$

### 3. Exergy Output ($E_{\text{out}}$)
Because the output is cooling capacity, its true thermodynamic value is defined by the minimum electrical work that would be required by a perfect Carnot refrigerator to produce the equivalent cooling rate:
$$E_{\text{out}} = (1.0 \text{ kW} \cdot \text{COP}_{\text{th}}) \cdot \left(\frac{T_0}{T_{\text{chilled}}} - 1\right)$$

### 4. Localized Exergy Efficiency ($\eta_{\text{ex,4}}$)
$$\eta_{\text{ex,4}} = \frac{E_{\text{out}}}{E_{\text{in}}}$$

---

## 🛠️ Boundary Conditions & Real-World Loss Factors

While highly efficient at bypassing electrical conversion limits, Stage 4 performance is restricted by localized physical constraints:

* **Mass Transfer Resistance:** Vapor diffusion rates through thick silica gel beds create a kinetic bottleneck, causing transient drop-offs in adsorption rates as the outermost layers saturate.
* **Bed Thermal Inertia:** Alternating between hot regeneration cycles and cooler adsorption cycles forces the heat exchanger chassis to absorb and dump sensible heat continuously, introducing structural thermal losses.
* **Vapor Velocity Constraints:** Operating under deep vacuum conditions near water's low-pressure triple point requires oversized vapor ducting to prevent sonic choking and boundary friction losses.

---

## 💻 Simulation & Verification Interface

The mathematical engine governing this module is implemented in `variables/stage4_adsorption.py`. Run the internal test suite to verify localized behavior across a shifting condenser baseline:

```bash
python -m variables.stage4_adsorption
