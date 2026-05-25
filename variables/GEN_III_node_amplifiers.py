import logging

class CHTSController:
    """
    Optimized Controller for the 4-Stage Thermal Cascade (CHTS GEN-III).
    Incorporates dynamic load balancing for peak thermal input.
    """
    def __init__(self, max_capacity=200.0):
        self.max_capacity = max_capacity
        # Baseline conversion efficiencies
        self.coefficients = {
            "teg_high": 0.185,
            "teg_low": 0.140,
            "zeo": 0.071,
            "ads": 0.050
        }

    def compute_optimized_output(self, input_thermal_kw):
        """
        Calculates recovery and captures excess exergy for thermal storage.
        """
        # Determine saturation status and storage potential
        is_saturated = input_thermal_kw > self.max_capacity
        effective_input = min(input_thermal_kw, self.max_capacity)
        
        # Calculate yield per stage
        outputs = {k: round(effective_input * v, 3) for k, v in self.coefficients.items()}
        total_recovery = sum(outputs.values())
        
        # Capture excess for secondary thermal storage (PCM/buffer)
        storage_potential = max(0.0, input_thermal_kw - self.max_capacity)
        
        # Calculate performance index
        efficiency_index = round(total_recovery / input_thermal_kw, 4) if input_thermal_kw > 0 else 0
        
        return {
            "outputs": outputs,
            "total_recovery_kw": total_recovery,
            "storage_potential_kw": storage_potential,
            "efficiency_index": efficiency_index,
            "status": "SATURATED" if is_saturated else "OPTIMAL"
        }

def get_maximized_yield(input_thermal_kw):
    controller = CHTSController()
    return controller.compute_optimized_output(input_thermal_kw)
