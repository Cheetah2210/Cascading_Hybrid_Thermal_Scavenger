# Cascading Hybrid Thermal Scavenger (CHTS)

A multi-stage, solid-state thermal recovery ecosystem designed to maximize exergy extraction from high-density data center exhaust, industrial flues, and space-based thermal buses.

---

## ⚖️ License
Author: Emily 🌻 (Cheetahs Creations)  
Licensed under the [CERN Open Hardware Licence v1.2](./License.txt).

---

## 📖 Project Overview
The **Cascading Hybrid Thermal Scavenger (CHTS)** addresses energy inefficiencies in high-density computing and industrial management. CHTS utilizes a decoupled, multi-stage cascading framework to capture waste heat without parasitic mechanical load.

### The Innovation
* **Primary Stage (MHD Core):** Uses an immiscible fluid mixture in a closed circuit, leveraging **Magnetohydrodynamics (MHD)** to generate DC power autonomously.
* **Secondary Stage (Decoupled Retrofit):** A secondary refrigerant vapor loop captures residual heat, ensuring maximum total exergy extraction.

---

## 📂 Repository Directory
| Path | Description |
| :--- | :--- |
| [**.github/workflows/**](./.github/workflows/) | Validated CI/CD for Node.js 24/Python 3.11. |
| [**docs/**](./docs/) | Scaling guides, Sizing math, and **Space Adaptation**. |
| [**hardware/**](./hardware/) | CAD chassis, RF schematics, and material compliance. |
| [**variables/**](./variables/) | Core 46.8% realistic exergy simulation engines. |
| [**tests/**](./tests/) | Forensic thermodynamic unit tests. |

---

## 🚀 Global & Strategic Impact
* **Data Center Exergy Reclamation:** Flagship application for AI compute clusters; reclaims exhaust to offset cooling costs and auxiliary load.
* **Industrial Decarbonization:** Retrofitting blast furnaces and kilns; reducing energy overhead by 15-20%.
* **Space & Aerospace:** Integrated thermal bus recovery for orbital compute, reducing the mass penalty of large radiator arrays.
* **Distributed Grid Support:** Enabling micro-scale energy harvesting for remote infrastructure.

---

## 📊 Performance Matrix (Realized vs. Ideal)

| Phase Node | Ideal Limit | Realistic Net Yield | Governing Loss Factors |
| :--- | :---: | :---: | :--- |
| **Stage 1: MHD** | 53.6% | **24.2%** | RF ionization overhead & Hartmann drag. |
| **Stage 2: TEG** | 20.0% | **15.5%** | 0.15 mΩ contact resistance. |
| **Stage 3: Zeotropic** | 12.0% | **7.1%** | Antoine pressure drops & boundary friction. |
| **Total System** | **80.4%** | **46.8%** | **Validated Net Exergy Yield** |

---

## 🛠️ Implementation Requirements
* [requirements.txt](./requirements.txt): Manifest for NumPy, SciPy, and test dependencies.
* [setup.py](./setup.py): Local package configuration.
* [docs/SPACE_ADAPTATION.md](./docs/SPACE_ADAPTATION.md): Vacuum-rated engineering guide.
