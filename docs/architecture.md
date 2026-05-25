# System Architecture Specification

**Status:** Stable Release (v1.0)  
**Date:** 2026-05-25  
**Author:** Emily – Cheetahs Creations

---

# 1. Overview

The Cascading Hybrid Thermal Scavenger (CHTS) architecture is defined by a serial enthalpy cascade designed to model staged thermal exergy extraction across four distinct recovery layers.

Unlike parallel extraction approaches, CHTS employs sequential thermodynamic recovery in which downstream stages process only the residual thermal potential remaining after upstream extraction. This design prevents exergy double-counting and maintains thermodynamic consistency across the modeled system.

The architecture prioritizes:

- Deterministic modeling
- Reproducibility
- Sequential recovery
- Thermodynamic traceability
- Minimal parasitic overhead

---

# 2. Cascade Stages

CHTS models four thermodynamic recovery stages.

## Stage 1: High-Grade Thermoelectric Conversion

**Mechanism:**  
Solid-state Seebeck-effect thermoelectric modules.

**Input:**  
Primary thermal flux.

**Governing Constraints:**

- Junction resistance
- Thermal interface losses
- High-grade temperature differential ($\Delta T_{high}$)

This stage provides primary high-grade thermal recovery and establishes the initial reduction in available enthalpy.

---

## Stage 2: Low-Grade Thermoelectric Conversion

**Mechanism:**  
Secondary Seebeck conversion modules.

**Input:**  
Thermal rejection from Stage 1.

**Governing Constraints:**

- Moderate temperature differential ($\Delta T_{low}$)
- Thermal interface impedance
- Reduced remaining thermal gradient

This stage recovers additional thermal potential from residual heat unavailable to the primary TEG layer.

---

## Stage 3: Zeotropic Latent Heat Recovery

**Mechanism:**  
Binary-fluid heat exchange loop.

**Input:**  
Residual thermal energy following Stage 2 extraction.

**Governing Constraints:**

- Fluid pressure losses
- Cross-flow exchanger efficiency
- Thermal glide behavior

This stage models latent and residual heat recovery through staged fluid interaction and exchanger behavior.

---

## Stage 4: Adsorption-Assisted Cooling Offset

**Mechanism:**  
Silica-gel / water adsorption cycle.

**Input:**  
Final residual exergy.

**Governing Constraints:**

- Adsorption kinetics
- Bed thermal inertia
- Mass transfer efficiency

Rather than primary electrical generation, this stage models low-grade exergy utilization through cooling-offset and adsorption-assisted thermal recovery.

---

# 3. Control & Thermal Buffering

## Deterministic Controller

The CHTS controller provides deterministic, stage-by-stage thermodynamic modeling.

Core controller responsibilities include:

- Operating-state evaluation
- Carnot-limited recovery bounding
- Sequential stage interaction
- Recovery aggregation
- Deterministic uncertainty modeling

The controller enforces serial recovery logic and ensures reproducible system outputs across modeled operating environments.

---

## PCM Thermal Buffering

Integrated Phase Change Material (PCM) nodes provide modeled thermal stabilization and transient mitigation.

PCM buffering supports:

- Thermal smoothing
- Load balancing
- Temperature stabilization
- Recovery continuity during transient thermal states

The PCM subsystem acts as a supporting thermal management layer rather than a primary extraction stage.

---

# 4. Modeling Methodology

The CHTS architecture employs serial enthalpy depletion logic.

Residual thermal potential is modeled as:
