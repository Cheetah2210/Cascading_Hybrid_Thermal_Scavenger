import logging

# Standardized logging for solid-state performance monitoring
logging.basicConfig(filename='system_alerts.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class CHTSController:
    """
    Manages multi-stage TEG array conversion.
    Efficiency: 18.5% (High), 14.0% (Low), 7.1% (Zeo) = 39.6% total.
    """
    def __init__(self, max_capacity=200.0):
        self.max_capacity = max_capacity
        self.coefficients = {
            "teg_high": 0.185,
            "teg_low": 0.140,
            "zeo": 0.071
        }

    def compute_cascaded_output(self, input_thermal_kw):
        is_saturated = input_thermal_kw > self.max_capacity
        effective_input = min(input_thermal_kw, self.max_capacity)
        
        outputs = {k: round(effective_input * v, 3) for k, v in self.coefficients.items()}
        
        return {
            "outputs": outputs,
            "total_output": sum(outputs.values()),
            "status": "SATURATED" if is_saturated else "OPTIMAL"
        }

def get_optimized_realistic_yield(input_thermal_kw):
    controller = CHTSController()
    result = controller.compute_cascaded_output(input_thermal_kw)
    return result["outputs"]
