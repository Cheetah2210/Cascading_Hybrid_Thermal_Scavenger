import logging

logging.basicConfig(filename='system_alerts.log', level=logging.INFO)

class CHTSController:
    """
    Consolidated Controller for 4-Stage Thermal Cascade.
    1. TEG-High (18.5%), 2. TEG-Low (14.0%), 3. Zeotropic (7.1%), 4. Adsorption (5.0%)
    """
    def __init__(self, max_capacity=200.0):
        self.max_capacity = max_capacity
        self.coeffs = {"teg_high": 0.185, "teg_low": 0.140, "zeo": 0.071, "ads": 0.05}

    def compute_cascaded_output(self, input_thermal_kw):
        effective = min(input_thermal_kw, self.max_capacity)
        outputs = {k: round(effective * v, 3) for k, v in self.coeffs.items()}
        return {"outputs": outputs, "total_output": sum(outputs.values()), "status": "OPTIMAL"}

def get_optimized_realistic_yield(input_thermal_kw):
    return CHTSController().compute_cascaded_output(input_thermal_kw)["outputs"]
