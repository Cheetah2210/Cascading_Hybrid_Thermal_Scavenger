import logging

# Configure logging for thermal performance monitoring
logging.basicConfig(
    filename='system_alerts.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class CHTSController:
    """
    Consolidated Controller for the 4-Stage Thermal Cascade (CHTS GEN-III).
    
    Stages:
    1. TEG-High (18.5% efficiency)
    2. TEG-Low (14.0% efficiency)
    3. Zeotropic Recovery (7.1% efficiency)
    4. Adsorption Cooling Offset (5.0% efficiency)
    
    Total Baseline Efficiency: 44.6%
    """
    def __init__(self, max_capacity=200.0):
        self.max_capacity = max_capacity
        self.coefficients = {
            "teg_high": 0.185,
            "teg_low": 0.140,
            "zeo": 0.071,
            "ads": 0.050
        }

    def compute_cascaded_output(self, input_thermal_kw):
        """
        Calculates power recovery across all 4 stages based on thermal input.
        """
        # Determine if system is at capacity
        is_saturated = input_thermal_kw > self.max_capacity
        effective_input = min(input_thermal_kw, self.max_capacity)
        
        # Calculate yield per stage
        outputs = {k: round(effective_input * v, 3) for k, v in self.coefficients.items()}
        
        total_recovery = sum(outputs.values())
        
        status = "SATURATED" if is_saturated else "OPTIMAL"
        
        if is_saturated:
            logging.warning(f"System saturation reached at {input_thermal_kw}kW")
            
        return {
            "outputs": outputs,
            "total_output": total_recovery,
            "status": status
        }

def get_optimized_realistic_yield(input_thermal_kw):
    """Utility function to interface with telemetry validation."""
    controller = CHTSController()
    result = controller.compute_cascaded_output(input_thermal_kw)
    return result["outputs"]
