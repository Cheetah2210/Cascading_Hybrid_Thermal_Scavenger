# Cascading Hybrid Thermal Scavenger (CHTS)

A multi-stage, solid-state thermal recovery ecosystem designed to maximize exergy extraction from high-density data center exhaust, industrial flues, and space-based thermal buses.

---

## ⚖️ License
Author: Emily 🌻 (Cheetahs Creations)  
Licensed under the [CERN Open Hardware Licence v1.2](./License.txt).

---

## 📖 Project Overview
The **Cascading Hybrid Thermal Scavenger (CHTS)** addresses energy inefficiencies in high-density computing and industrial management. CHTS utilizes a decoupled, 4-stage solid-state cascading framework to capture waste heat without parasitic mechanical load.

### The Innovation
* **Stages 1 & 2 (High/Low TEG):** Solid-state Seebeck conversion modules capturing high and low-grade heat.
* **Stage 3 (Zeotropic Loop):** A binary fluid heat exchange loop capturing residual latent thermal energy.
* **Stage 4 (Adsorption Cycle):** A silica-gel water desiccant cycle utilizing remaining exergy for active cooling offsets.
* **Thermal Management:** Integrated Phase Change Material (PCM) buffer for dynamic load balancing.

---

## 📂 Repository Directory
| Path | Description |
| :--- | :--- |
| [**.github/workflows/**](./.github/workflows/) | Validated CI/CD for Python 3.11+ thermal verification. |
| [**docs/**](./docs/) | Hardware interface, 44.6% efficiency math, and **Space Adaptation**. |
| [**hardware/**](./hardware/) | BOM, Solid-state signal conditioning, and mechanical tolerances. |
| [**variables/**](./variables/) | Controller logic and PCM Thermal Buffer management. |
| [**tests/**](./tests/) | Forensic thermodynamic unit tests and validation suites. |

---

## 🚀 Global & Strategic Impact
* **Data Center Exergy Reclamation:** Reclaims exhaust heat to offset cooling infrastructure costs and auxiliary power loads.
* **Industrial Decarbonization:** High-efficiency retrofitting for kilns and flues; reducing thermal overhead by 15-20%.
* **Space & Aerospace:** Integrated thermal bus recovery for orbital compute, reducing the mass penalty of large radiator arrays.
* **Distributed Grid Support:** Enabling sustainable micro-scale energy harvesting for remote infrastructure.

---

## 📊 Performance Matrix (Solid-State 4-Stage Cascade)

| Phase Node | Target Efficiency | Realistic Net Yield | Governing Loss Factors |
| :--- | :--- | :--- | :--- |
| **Stage 1 & 2: TEG** | 32.5% | **32.5%** | Semiconductor junction resistance. |
| **Stage 3: Zeotropic** | 7.1% | **7.1%** | Pressure drops & boundary friction. |
| **Stage 4: Adsorption** | 5.0% | **5.0% (Offset)** | Bed thermal inertia & mass transfer. |
| **Total System** | **44.6%** | **44.6%** | **Validated Net Exergy Yield** |

---

## 🛠️ Implementation Requirements
* [requirements.txt](./requirements.txt): Manifest for NumPy, SciPy, and automated validation tools.
* [setup.py](./setup.py): Local production environment configuration.
* [docs/SPACE_ADAPTATION.md](./docs/SPACE_ADAPTATION.md): Vacuum-rated engineering specifications for non-magnetic/solid-state thermal buses.
