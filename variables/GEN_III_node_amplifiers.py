class CHTSController:
    """
    HIL-Ready Controller: Dynamically computes cascaded exergy extraction 
    using live sensor telemetry.
    """
    def __init__(self, max_capacity=200.0, discharge_threshold=50.0):
        self.max_capacity = max_capacity
        self.discharge_threshold = discharge_threshold

    def compute_optimized_output(self, input_thermal_kw, live_temps):
        """
        Processes load based on live sensor data (T_hot, T_cold).
        """
        # Determine operational status
        if input_thermal_kw > self.max_capacity:
            status = "SATURATED"
        elif input_thermal_kw < self.discharge_threshold:
            status = "DISCHARGING"
        else:
            status = "OPTIMAL"
            
        # Dynamic Carnot calculation
        carnot = max(0, 1 - (live_temps['T_cold'] / live_temps['T_hot']))
        
        # Cascaded Enthalpy Reduction
        remaining_heat = min(input_thermal_kw, self.max_capacity)
        stages = {"teg_high": 0.35, "teg_low": 0.30, "zeo": 0.20, "ads": 0.15}
        
        outputs = {}
        current_heat = remaining_heat
        for name, eff in stages.items():
            extracted = current_heat * (eff * carnot)
            outputs[name] = round(extracted, 3)
            current_heat -= extracted
            
        return {
            "outputs": outputs,
            "total_recovery_kw": round(sum(outputs.values()), 3),
            "status": status
        }
