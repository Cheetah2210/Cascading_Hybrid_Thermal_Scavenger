class CHTSController:
    def __init__(self, max_capacity=200.0, discharge_threshold=50.0):
        self.max_capacity = max_capacity
        self.discharge_threshold = discharge_threshold
        self.temps = {"T_source": 500, "T_sink": 300}

    def compute_optimized_output(self, input_thermal_kw):
        # 1. Determine Operational State
        if input_thermal_kw > self.max_capacity:
            status = "SATURATED"
        elif input_thermal_kw < self.discharge_threshold:
            status = "DISCHARGING"
        else:
            status = "OPTIMAL"
            
        # 2. Physics-based cascaded recovery calculation
        remaining_heat = min(input_thermal_kw, self.max_capacity)
        carnot = 1 - (300 / 500)
        
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
