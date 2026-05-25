# CHTS Space Adaptation Guide: Radiative Exergy Harvesting

When transitioning the Cascading Hybrid Thermal Scavenger (CHTS) from terrestrial exhaust paths to space-based thermal bus integration, the primary thermodynamic constraint shifts from convective airflow to **radiative rejection**.

---

## 🛰️ Physical Constants & Simulation Overrides

To adapt the `variables/` engines for vacuum-rated environments, the following parameter shifts must be implemented in your configuration scripts:

### 1. Thermal Sink Constant ($T_{\text{sink}}$)
In terrestrial mode, $T_{\text{sink}}$ is bounded by ambient air ($298\text{K}$). In vacuum, $T_{\text{sink}}$ becomes a function of the radiator's Stefan-Boltzmann emissive power:
$$Q_{\text{rad}} = \epsilon \sigma A (T^4 - T_{\text{space}}^4)$$
* **Simulation Override:** In `teg_sandwich.py`, redefine `t_cold` to be dynamically linked to the radiator panel temperature, which typically fluctuates between $200\text{K}$ and $350\text{K}$ depending on solar orientation.

### 2. MHD Loop Pressure Regulation
* **Terrestrial:** Relies on gravity-assisted flow and atmospheric backpressure.
* **Space:** Requires an active electromagnetic pump or vapor-pressure-driven loop (Capillary Pumped Loop). The absence of buoyancy necessitates a move toward higher flow velocities to maintain MHD induction without convective assistance.

---

## 🛠️ Simulation Engine Adjustments

To maintain the **46.8% Realistic Net Yield** in a space environment, you must update your `variables/` files with these logic gates:

### Updated Logic for `variables/GEN_III_node_amplifiers.py`
```python
def adapt_for_vacuum(gross_input_kw: float, radiator_temp: float):
    # Adjust efficiency constant based on radiative sink efficiency
    # Radiative sink is significantly lower than ambient air, 
    # increasing potential Carnot efficiency (theoretical)
    # but increasing radiator mass penalty (realistic).
    
    # Placeholder for the updated radiative-sink math
    carnot_max = 1 - (radiator_temp / t_hot)
    # ... logic to scale output based on radiative flux ...
