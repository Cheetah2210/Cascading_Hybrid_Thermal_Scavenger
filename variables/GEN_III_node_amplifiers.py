import logging

class CHTSController:
    """
    Thermodynamic Controller for the 4-Stage Thermal Cascade.
    Implements a serial energy cascade where each stage processes the 
    residual enthalpy of the previous stage.
    """
    def __init__(self, max_capacity=200.0):
        self.max_capacity = max_capacity
        self.temps = {"T_source": 500, "T_sink": 300}

    def _calculate_carnot_limit(self, T_hot, T_cold):
        return max(0, 1 - (T_cold / T_hot))

    def compute_optimized_output(self, input_thermal_kw):
        """Processes input load through a serial thermodynamic chain."""
        remaining_heat = min(input_thermal_kw, self.max_capacity)
        carnot = self._calculate_carnot_limit(self.temps["T_source"], self.temps["T_sink"])
        
        # Efficiencies per stage (fraction of available residual heat)
        # These are no longer multipliers of the total input, but of the current state
        stages = {
            "teg_high": 0.35 * carnot, # Extracting 35% of available
            "teg_low": 0.30 * carnot,
            "zeo": 0.20 * carnot,
            "ads": 0.15 * carnot
        }
        
        outputs = {}
        current_heat = remaining_heat
        
        for name, efficiency in stages.items():
            extracted = current_heat * efficiency
            outputs[name] = round(extracted, 3)
            current_heat -= extracted # Cascading reduction
            
        return {
            "outputs": outputs,
            "total_recovery_kw": round(sum(outputs.values()), 3),
            "status": "CASCADED_PHYSICS_MODEL"
        }
