import logging

# Configure logger to capture saturation events
logging.basicConfig(filename='system_alerts.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class CHTSController:
    def __init__(self, max_capacity=200.0):
        self.max_capacity = max_capacity
        self.efficiency_coefficients = {
            "mhd": 0.242,
            "teg": 0.155,
            "zeo": 0.071
        }

    def compute_cascaded_output(self, input_thermal_kw):
        is_saturated = input_thermal_kw > self.max_capacity
        
        if is_saturated:
            logging.warning(f"Saturation Alert: Input {input_thermal_kw}kW exceeds capacity!")
        
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

def get_optimized_realistic_yield(input_thermal_kw, phys_vars=None):
    """
    Maintains compatibility with tests/test_cascades.py and tests/test_realism_check.py
    while applying physics-based remediation variables.
    """
    controller = CHTSController()
    
    # Apply remediation physics if variables are provided
    if phys_vars:
        # Handle MHD stability failure
        if phys_vars.get('mhd_ionization_stable') is False:
            controller.efficiency_coefficients["mhd"] = 0.0
        
        # Apply performance adjustments
        slip = phys_vars.get('slip_factor', 0.0)
        flux_gain = phys_vars.get('halbach_flux_gain', 0.0)
        
        # Adjust MHD performance based on slip and flux
        controller.efficiency_coefficients["mhd"] = (controller.efficiency_coefficients["mhd"] * (1 - slip)) + flux_gain

    result = controller.compute_cascaded_output(input_thermal_kw)
    return result["outputs"]

# Global controller instance for system-wide access
node_controller = CHTSController()
