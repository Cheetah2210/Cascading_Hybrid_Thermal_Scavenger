"""
GEN_III Node Amplifiers: Thermal Cascade Control Logic
Updated with Saturation Alerting
"""

class CHTSController:
    def __init__(self, max_capacity=200.0):
        self.max_capacity = max_capacity
        self.efficiency_coefficients = {
            "mhd": 0.242,
            "teg": 0.155,
            "zeo": 0.071
        }

    def compute_cascaded_output(self, input_thermal_kw):
        """
        Calculates energy distribution with saturation bypass and status flagging.
        """
        # Determine operational state
        is_saturated = input_thermal_kw > self.max_capacity
        
        effective_input = min(input_thermal_kw, self.max_capacity)
        bypassed_heat = max(0.0, input_thermal_kw - self.max_capacity)

        # Output calculation
        outputs = {
            "mhd": round(effective_input * self.efficiency_coefficients["mhd"], 3),
            "teg": round(effective_input * self.efficiency_coefficients["teg"], 3),
            "zeo": round(effective_input * self.efficiency_coefficients["zeo"], 3)
        }

        return {
            "effective_input": effective_input,
            "outputs": outputs,
            "bypassed_heat": bypassed_heat,
            "total_output": sum(outputs.values()),
            "status": "SATURATED" if is_saturated else "OPTIMAL"
        }

# Instantiate controller for operational verification
node_controller = CHTSController()
