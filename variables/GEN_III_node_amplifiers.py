"""
GEN_III Node Amplifiers: Thermal Cascade Control Logic
Updated with Saturation Alerting and Legacy Compatibility
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
        is_saturated = input_thermal_kw > self.max_capacity
        
        effective_input = min(input_thermal_kw, self.max_capacity)
        bypassed_heat = max(0.0, input_thermal_kw - self.max_capacity)

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

# Wrapper function for legacy test compatibility
def get_optimized_realistic_yield(input_thermal_kw):
    """
    Maintains compatibility with tests/test_cascades.py and tests/test_realism_check.py
    """
    controller = CHTSController()
    result = controller.compute_cascaded_output(input_thermal_kw)
    return result["outputs"]

# Global controller instance for system-wide access
node_controller = CHTSController()
