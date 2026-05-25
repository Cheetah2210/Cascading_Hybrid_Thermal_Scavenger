import logging
from variables.GEN_III_thermal_buffer import ThermalBuffer

class CHTSController:
    """
    Optimized Controller for the 4-Stage Thermal Cascade (CHTS GEN-III).
    Incorporates PCM storage management and automated discharge triggers.
    """
    def __init__(self, max_capacity=200.0, buffer_capacity=500.0, discharge_threshold=50.0):
        self.max_capacity = max_capacity
        self.buffer = ThermalBuffer(capacity_kwh=buffer_capacity)
        self.discharge_threshold = discharge_threshold
        self.coefficients = {
            "teg_high": 0.185,
            "teg_low": 0.140,
            "zeo": 0.071,
            "ads": 0.050
        }

    def compute_optimized_output(self, input_thermal_kw):
        """Processes input load, manages buffer, and returns total recovery."""
        # 1. Determine excess and base input
        excess_input = max(0.0, input_thermal_kw - self.max_capacity)
        effective_input = min(input_thermal_kw, self.max_capacity)
        
        # 2. Charge buffer if saturated
        if excess_input > 0:
            self.buffer.update_charge(excess_input)
            
        # 3. Discharge buffer if input is below threshold
        discharged_kw = 0.0
        if input_thermal_kw < self.discharge_threshold and self.buffer.get_status()['ready_for_discharge']:
            demand_kw = self.discharge_threshold - input_thermal_kw
            discharged_kw = self.buffer.discharge(demand_kw)
            effective_input += discharged_kw
            
        # 4. Calculate yield per stage based on final effective input
        outputs = {k: round(effective_input * v, 3) for k, v in self.coefficients.items()}
        total_recovery = sum(outputs.values())
        
        return {
            "outputs": outputs,
            "total_recovery_kw": total_recovery,
            "buffer_discharged_kw": discharged_kw,
            "buffer_status": self.buffer.get_status(),
            "status": "DISCHARGING" if discharged_kw > 0 else ("SATURATED" if excess_input > 0 else "OPTIMAL")
        }

def get_maximized_yield(input_thermal_kw):
    """Utility to run optimized output logic."""
    controller = CHTSController()
    return controller.compute_optimized_output(input_thermal_kw)
