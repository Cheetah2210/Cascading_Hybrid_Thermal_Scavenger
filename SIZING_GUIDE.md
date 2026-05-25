# CHTS Engineering Sizing Guide

## 1. MHD Core Scaling (Stage 1)
The core simulation utilizes the Hartmann number ($Ha$) to define fluidic power loss.
- **Channel Geometry:** 40mm x 2mm x 150mm.
- **Drag Equation:** $Ha = B \cdot h \cdot \sqrt{\sigma / \mu}$
  - Where $B=1.5T$ (Halbach Array flux), $\sigma=1.2e4 S/m$, and $\mu=4.5e-5 Pa \cdot s$.
- **Boundary Constraint:** Power loss must track the 2.1 kW design limit.

## 2. Thermoelectric Compounding (Stage 2)
The TEG sandwich utilizes laser-textured interface contacts.
- **Contact Resistance:** $0.15 m\Omega$ (Threshold for 1.17 kW net yield).
- **Thermal Gradient:** $\Delta T = 600K$ ($1200K$ to $600K$).

## 3. Zeotropic Glide (Stage 3)
The final stage utilizes an Antoine-compliant zeotropic mixture to mitigate entropy generation.
- **Temperature Glide:** Operates on a $600K \rightarrow 300K$ gradient.
- **Efficiency Cap:** Net efficiency of 7.1% constrained by parasitic friction within the vapor manifold.
