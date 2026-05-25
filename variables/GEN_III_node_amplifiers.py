import numpy as np
import hashlib

class CHTSController:
    """
    Production-Grade CHTS Controller.
    
    Architecture:
    - Serial Enthalpy Cascade: Each stage processes residual heat.
    - Input-Deterministic Uncertainty: Seed derived from input load hashing 
      to ensure stateless, repeatable sigma values.
    """
    def __init__(self, max_capacity=200.0, discharge_threshold=50.0):
        self.max_capacity = max_capacity
        self.discharge_threshold = discharge_threshold
        self.baseline_temps = {'T_hot': 500, 'T_cold': 300}

    def compute_optimized_output(self, input_thermal_kw, live_temps=None):
        """Calculates energy recovery with input-deterministic modeling."""
        if input_thermal_kw > self.max_capacity:
            status = "SATURATED"
        elif input_thermal_kw < self.discharge_threshold:
            status = "DISCHARGING"
        else:
            status = "OPTIMAL"
            
        temps = live_temps if live_temps is not None else self.baseline_temps
        carnot = max(0, 1 - (temps['T_cold'] / temps['T_hot']))
        stages = {"teg_high": 0.35, "teg_low": 0.22, "zeo": 0.12, "ads": 0.08}
        
        outputs = {}
        current_heat = min(input_thermal_kw, self.max_capacity)
        total_recovery = 0.0
        
        for name, eff in stages.items():
            extracted = current_heat * (eff * carnot)
            outputs[name] = round(extracted, 3)
            total_recovery += extracted
            current_heat -= extracted
            
        # Input-Deterministic Stochastic Modeling
        # Hashing the load ensures the same input always produces the same 'random' noise
        seed = int(hashlib.md5(str(input_thermal_kw).encode()).hexdigest(), 16) % (2**32)
        local_rng = np.random.default_rng(seed=seed)
        
        base_error = 0.02 * total_recovery
        stochastic_noise = local_rng.normal(0, 0.3) 
        modeled_sigma = round(np.sqrt(base_error**2 + stochastic_noise**2), 3)
        
        return {
            "outputs": outputs,
            "total_recovery_kw": round(total_recovery, 3),
            "modeled_sigma": modeled_sigma, 
            "status": status
        }
