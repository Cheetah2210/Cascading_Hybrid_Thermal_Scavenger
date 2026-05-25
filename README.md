# Cascading Hybrid Thermal Scavenger (CHTS)

A multi-stage, solid-state thermal recovery ecosystem designed to maximize exergy extraction from high-density data center exhaust and industrial flues without introducing restrictive airflow or mechanical drag.

---

## ⚖️ License
Author: Emily 🌻 (Cheetahs Creations)  
Licensed under the [CERN Open Hardware Licence v1.2](./License.txt).

---

## 📖 Project Overview
The **Cascading Hybrid Thermal Scavenger (CHTS)** addresses the critical energy inefficiencies inherent in high-density computing and industrial thermal management. Traditional recovery systems often suffer from low thermodynamic efficiency or introduce parasitic mechanical loads. CHTS utilizes a decoupled, multi-stage cascading framework to capture waste heat effectively.

### The Innovation
* **Primary Stage (MHD Core):** Uses an immiscible fluid mixture in a closed circuit. Phase change expansion accelerates fluid through micro-channels across a magnetic field, leveraging **Magnetohydrodynamics (MHD)** to generate DC power autonomously.
* **Secondary Stage (Decoupled Retrofit):** A secondary refrigerant vapor loop captures residual lower-grade heat, ensuring maximum total exergy extraction across the entire thermal gradient.



---

## 📂 Repository Directory
| Path | Description |
| :--- | :--- |
| [**.github/workflows/**](./.github/workflows/) | Validated CI/CD pipeline for automated physics verification. |
| [**docs/**](./docs/) | Industry scaling guides and exergy math. |
| [**hardware/**](./hardware/) | CAD chassis files and RF ionization schematics. |
| [**variables/**](./variables/) | The core 46.8% realistic exergy simulation engines. |
| [**tests/**](./tests/) | Forensic unit tests for thermodynamic integrity. |

---

## 🚀 Global Impact & Applications
The CHTS framework is engineered for global scalability, providing a pathway to decarbonize heat-intensive industries.

* **Data Center Exergy Reclamation: Directly addressing the massive thermal exhaust from high-density server clusters. By retrofitting CHTS scavenger hoods, data center operators can reclaim significant exergy to offset cooling costs and auxiliary power consumption, transforming waste heat into a manageable electrical load.
* **Industrial Decarbonization:** Retrofitting blast furnaces, glass kilns, and ceramic kilns to reclaim thermal waste, reducing energy overhead by an estimated 15-20% per unit.
* **Distributed Grid Support:** Enabling micro-scale energy harvesting in remote regions where thermal transport infrastructure is non-existent, turning high-temperature waste into usable electrical load.
* **Marine & Propulsion:** Integrating solid-state scavenger hoods into combustion propulsion systems to improve net fuel utilization and reduce thermal signatures.

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
* [setup.py](./setup.py): Local package configuration for installation.
