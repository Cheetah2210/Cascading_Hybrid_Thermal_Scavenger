file_content = """# CHTS Theoretical Limits: Realistic vs. Maximum Potential

This document outlines the gap between our current granular realistic efficiency (**46.8%**) and the theoretical thermodynamic maximum (**~85%**).

---

## 📊 Efficiency Gap Analysis

| Stage | Realistic Yield (%) | Theoretical Limit (%) | Primary Loss Source |
| :--- | :--- | :--- | :--- |
| **MHD Core** | 24.2% | 45.0% | Hartmann drag, RF ionization noise |
| **TEG Sandwich** | 15.5% | 25.0% | Contact resistance, phonon scattering |
| **Zeotropic Glide** | 7.1% | 15.0% | Pressure-drop losses, heat exchanger inefficiency |
| **Total System** | **46.8%** | **85.0%** | **Integrated Entropy Generation** |

---

## 🚀 The Path to Maximum Potential

To approach the **85% theoretical limit**, the system must transition from passive remediation to active entropy suppression.

### 1. MHD: Superconducting Magnetic Focusing
* **Current Limitation:** Permanent magnet dipole flux density is limited by the physical size of the magnets.
* **Maximum Potential:** Implementing **High-Temperature Superconductors (HTS)** allows for magnetic field densities > 5T, virtually eliminating Lorentz-force-related slip and reducing Hartmann drag toward the theoretical limit of zero friction.

### 2. TEG: Phonon-Glass Electron-Crystal (PGEC)
* **Current Limitation:** $0.15 \text{ m}\Omega$ contact resistance creates a thermal shunt.
* **Maximum Potential:** Moving to **Quantum-Well Superlattices** enables PGEC behavior. This decouples electron conductivity from thermal conductivity, allowing for ZT values > 4.0, which nearly doubles the Carnot conversion limit.

### 3. Zeotropic: Isentropic Expansion
* **Current Limitation:** Passive vapor expansion through nozzles leads to turbulent entropy generation.
* **Maximum Potential:** Replacing the expansion valve with a **Micro-Turbo-Expander** allows the system to recover the energy of the expanding vapor as shaft work, turning a pressure-loss stage into a power-generation stage.

---

## 🧠 Governing Math: Entropy Suppression

The maximum potential is defined by the reduction of entropy generation ($S_{gen}$):

$$S_{gen} = \int \frac{\delta Q}{T_{res}} \geq 0$$

In our current realistic model, we accept $S_{gen}$ as a constant penalty. To reach the **85% maximum**, we must replace our passive components with active recovery mechanisms that satisfy:

$$\Delta S_{system} \rightarrow 0$$

---

*For technical specifications on the HTS and Turbo-Expander integration, refer to the [Physical Reference Matrix](PHYSICS_REFERENCE.md).*
"""

# Use python to create the file
with open('docs/THEORETICAL_LIMITS.md', 'w') as f:
    f.write(file_content)
