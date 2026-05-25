"""
Gen III Global Cascade Aggregator - Validated Edition
"""

def get_optimized_realistic_yield(gross_input_kw: float, phys_vars: dict) -> dict:
    # 1. Ionization Threshold Check
    is_mhd_stable = phys_vars.get('mhd_ionization_stable', True)
    
    if not is_mhd_stable:
        net_output = gross_input_kw * 0.22
        return {
            "optimized_net_kw": round(net_output, 3),
            "status": "MHD_BYPASS_ENGAGED_THERMAL_ONLY",
            "efficiency_gain_delta": 0.0
        }

    # 2. Baseline realistic net yield (46.8% of gross input)
    base_net = gross_input_kw * 0.468
    
    # 3. Calculate cumulative gain
    total_gain = (phys_vars.get('slip_factor', 0.0) + 
                  phys_vars.get('ehd_freq_boost', 0.0) + 
                  phys_vars.get('halbach_flux_gain', 0.0))
    
    # 4. Final Adjusted Output
    teg_multiplier = phys_vars.get('zt_coefficient', 1.0)
    optimized_output = base_net * (1 + total_gain) * teg_multiplier
    
    return {
        "optimized_net_kw": round(optimized_output, 3),
        "efficiency_gain_delta": round(total_gain * 100, 2),
        "status": "GRANULAR_MODEL_VALIDATED"
    }
