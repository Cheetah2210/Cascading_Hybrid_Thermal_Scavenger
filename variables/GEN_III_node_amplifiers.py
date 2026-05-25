import logging

# Configure logger for system health monitoring
logging.basicConfig(filename='system_alerts.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class CHTSController:
    def __init__(self, max_capacity=200.0):
        self.max_capacity = max_capacity
        # Solid-state coefficients: 18.5% High, 14% Low, 7.1% Zeotropic
        self.efficiency_coefficients = {
            "teg_high": 0.185,
            "teg_low": 0.140,
            "zeo": 0.071
        }

    def compute_cascaded_output(self, input_thermal_kw):
        is_saturated = input_thermal_kw > self.max_capacity
        if is_saturated:
            logging.warning(f"Saturation Alert: Input {input_thermal_kw}kW exceeds capacity!")
        
        effective_input = min(input_thermal_kw, self.max_capacity)
        
        outputs = {
            "teg_high": round(effective_input * self.efficiency_coefficients["teg_high"], 3),
            "teg_low": round(effective_input * self.efficiency_coefficients["teg_low"], 3),
            "zeo": round(effective_input * self.efficiency_coefficients["zeo"], 3)
        }
        
        return {
            "outputs": outputs,
            "total_output": sum(outputs.values()),
            "status": "SATURATED" if is_saturated else "OPTIMAL"
        }

def get_optimized_realistic_yield(input_thermal_kw, phys_vars=None):
    """
    Maintains compatibility with test suites using the new TEG architecture.
    """
    controller = CHTSController()
    result = controller.compute_cascaded_output(input_thermal_kw)
    return result["outputs"]

node_controller = CHTSController()
