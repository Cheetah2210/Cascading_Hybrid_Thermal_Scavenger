import numpy as np

class CHTSController:
    """
    Production-Grade CHTS Controller.
    
    Architecture:
    - Serial Enthalpy Cascade: Each stage processes residual heat.
    - Operational States: OPTIMAL, SATURATED, DISCHARGING.
    - Uncertainty: Modeled stochastic noise and instrument variance.
    """
    def __init__(self, max_capacity=200.0, discharge_threshold=50.0):
        self.max_capacity = max_capacity
        self.discharge_threshold = discharge_threshold
        self.baseline_temps = {'T_hot': 500, 'T_cold': 300}

    def compute_optimized_output(self, input_thermal_kw, live_temps=None):
        """Calculates energy recovery based on cascaded exergy extraction."""
        # Operational State
        if input_thermal_kw > self.max_capacity:
            status = "SATURATED"
        elif input_thermal_kw < self.discharge_threshold:
            status = "DISCHARGING"
        else:
            status = "OPTIMAL"
            
        # Determine effective temps (HIL fallback to baseline)
        temps = live_temps if live_temps is not None else self.baseline_temps
        
        # Physics: Carnot-limited cascaded exergy extraction
        carnot = max(0, 1 - (temps['T_cold'] / temps['T_hot']))
        
        # Empirical Efficiencies (Aggregate ~30%)
        stages = {"teg_high": 0.35, "teg_low": 0.22, "zeo": 0.12, "ads": 0.08}
        
        outputs = {}
        current_heat = min(input_thermal_kw, self.max_capacity)
        total_recovery = 0.0
        
        for name, eff in stages.items():
            extracted = current_heat * (eff * carnot)
            outputs[name] = round(extracted, 3)
            total_recovery += extracted
            current_heat -= extracted
            
        # Statistical Modeling: Return float for analytics compatibility
        base_error = 0.02 * total_recovery
        stochastic_noise = np.random.normal(0, 0.3) 
        modeled_sigma = round(np.sqrt(base_error**2 + stochastic_noise**2), 3)
        
        return {
            "outputs": outputs,
            "total_recovery_kw": round(total_recovery, 3),
            "modeled_sigma": modeled_sigma, 
            "status": status
        }
