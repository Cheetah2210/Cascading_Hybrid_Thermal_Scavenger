import logging
from variables.GEN_III_thermal_buffer import ThermalBuffer

class CHTSController:
    """
    Optimized Controller for the 4-Stage Thermal Cascade (CHTS GEN-III).
    Incorporates dynamic load balancing and PCM thermal storage management.
    """
    def __init__(self, max_capacity=200.0, buffer_capacity=500.0):
        self.max_capacity = max_capacity
        self.buffer = ThermalBuffer(capacity_kwh=buffer_capacity)
        self.coefficients = {
            "teg_high": 0.185,
            "teg_low": 0.140,
            "zeo": 0.071,
            "ads": 0.050
        }

    def compute_optimized_output(self, input_thermal_kw):
        """
        Processes input load, handles saturation via buffer routing, 
        and calculates total system recovery.
        """
        # Determine saturation and potential for storage
        excess_input = max(0.0, input_thermal_kw - self.max_capacity)
        effective_input = min(input_thermal_kw, self.max_capacity)
        
        # Capture excess into storage buffer
        if excess_input > 0:
            self.buffer.update_charge(excess_input)
        
        # Calculate yield per stage based on effective input
        outputs = {k: round(effective_input * v, 3) for k, v in self.coefficients.items()}
        total_recovery = sum(outputs.values())
        
        # Efficiency index calculation
        efficiency_index = round(total_recovery / input_thermal_kw, 4) if input_thermal_kw > 0 else 0
        
        return {
            "outputs": outputs,
            "total_recovery_kw": total_recovery,
            "storage_potential_kw": excess_input,
            "buffer_status": self.buffer.get_status(),
            "efficiency_index": efficiency_index,
            "status": "SATURATED" if excess_input > 0 else "OPTIMAL"
        }

def get_maximized_yield(input_thermal_kw):
    controller = CHTSController()
    return controller.compute_optimized_output(input_thermal_kw)
