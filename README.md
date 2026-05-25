# Cascading Hybrid Thermal Scavenger (CHTS)

CHTS is a deterministic and reproducible framework for modeling serial enthalpy cascade thermal recovery. This repository provides a reproducible and internally validated environment for simulating thermal scavenge performance, verifying telemetry against thermodynamic constraints, and auditing recovery metrics.

> **Current Release:** CHTS v1.0

---

## ⚖️ License
Author: 🌻 Emily 🌻 Cheetahs Creations
Licensed under the [CERN Open Hardware Licence v1.2](./License.txt).

---

## 📖 Project Overview
The **Cascading Hybrid Thermal Scavenger (CHTS)** addresses energy inefficiencies in high-density computing and industrial management. CHTS utilizes a decoupled, 4-stage solid-state cascading framework to capture waste heat with minimal parasitic overhead.

### The Innovation
* **Stages 1 & 2 (High/Low TEG):** Solid-state Seebeck conversion modules capturing high and low-grade heat.
* **Stage 3 (Zeotropic Loop):** A binary fluid heat exchange loop capturing residual latent thermal energy.
* **Stage 4 (Adsorption Cycle):** A silica-gel water desiccant cycle utilizing remaining exergy for active cooling offsets.
* **Thermal Management:** Integrated Phase Change Material (PCM) buffer for dynamic load balancing.

---

## 🧭 Project Status
CHTS v1.0 represents a thermodynamically credible and reproducible modeled thermal recovery platform.

* ✅ Controller and analytics internally validated
* ✅ Reproducible ledger and telemetry pipeline
* ✅ Sequential Carnot-limited cascade model
* ⏳ Experimental hardware validation in development

---

## 🔬 Validation & Reproducibility
CHTS includes reproducible controller outputs, telemetry QA validation, and ledger generation workflows designed to support auditability and thermodynamic traceability.

**Core Workflow:** `controller` → `telemetry` → `validation` → `ledger` → `analytics`

---

## 📊 Modeled Thermal Recovery Envelope

| Stage | Modeled Role | Governing Constraints |
| :--- | :--- | :--- |
| **High / Low TEG** | Primary solid-state heat recovery | Junction resistance & thermal gradient |
| **Zeotropic Loop** | Residual latent heat recovery | Pressure losses & exchanger efficiency |
| **Adsorption Cycle** | Cooling offset & low-grade recovery | Thermal inertia & mass transfer |
| **Integrated System** | Sequential Carnot-limited cascade | Remaining enthalpy & operating conditions |

**Current controller models ~25–30% aggregate thermal recovery under nominal operating conditions and temperature gradients.**

*Results represent calibrated model predictions and reproducible software validation; experimental hardware validation remains future work.*

---

## 📂 Repository Directory
| Path | Description |
| :--- | :--- |
| [**.github/workflows/**](./.github/workflows/) | Validated CI/CD for Python 3.11+ thermal verification. |
| [**docs/**](./docs/) | Thermodynamic modeling methodology, validation protocols, and space-adaptation theory. |
| [**hardware/**](./hardware/) | BOM, solid-state signal conditioning, and mechanical tolerances. |
| [**variables/**](./variables/) | Controller logic and PCM Thermal Buffer management. |
| [**analytics/**](./analytics/) | Recovery analysis, visualization, and provenance tooling. |
| [**validation/**](./validation/) | Telemetry QA, ledger generation, and model validation artifacts. |
| [**tests/**](./tests/) | Forensic thermodynamic unit tests and validation suites. |

---

## 🚀 Global & Strategic Impact
* **Data Center Exergy Reclamation:** Modeled pathways to reclaim exhaust heat to offset cooling infrastructure costs.
* **Industrial Decarbonization:** Modeled retrofit pathway for kilns and flues through staged thermal recovery.
* **Space & Aerospace:** Conceptual thermal bus recovery architecture for orbital and constrained thermal systems with modeled potential to reduce radiator mass requirements.
* **Distributed Grid Support:** Modeled pathways for micro-scale thermal energy harvesting in distributed and remote infrastructure.

---
