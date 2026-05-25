import numpy as np

def calculate_stage4_exergy(t_stage3_condenser_c, cop_thermal=0.60, t_ambient_c=25.0, t_chilled_out_c=7.0):
    """
    Calculates the localized exergy efficiency and net system yield contribution
    for Stage 4 (Adsorption Chilling Loop) bottoming stage.
    """
    # Convert all inputs to Kelvin
    T0 = t_ambient_c + 273.15
    T_source = t_stage3_condenser_c + 273.15
    T_chilled = t_chilled_out_c + 273.15
    
    # 1. Exergy input per kW of low-grade thermal fluid entering Stage 4
    exergy_in_per_kw = 1.0 * (1.0 - (T0 / T_source))
    
    # 2. Equivalent refrigeration work value (Exergy output of produced cooling capacity)
    q_cooling = 1.0 * cop_thermal
    exergy_out_per_kw = q_cooling * ((T0 / T_chilled) - 1.0)
    
    # 3. Localized Exergy Efficiency of Stage 4
    if exergy_in_per_kw > 0:
        stage4_local_efficiency = exergy_out_per_kw / exergy_in_per_kw
    else:
        stage4_local_efficiency = 0.0
        
    # 4. Net System Yield Added (Assuming Stage 3 leftover exergy share is ~12% of total ideal limit)
    stage3_leftover_share = 0.12
    net_yield_added = stage3_leftover_share * stage4_local_efficiency
    
    return {
        "exergy_in_kw": round(exergy_in_per_kw, 4),
        "exergy_out_kw": round(exergy_out_per_kw, 4),
        "stage4_local_efficiency_pct": round(stage4_local_efficiency * 100, 2),
        "net_system_yield_added_pct": round(net_yield_added * 100, 2)
    }

# Quick test verification for 70°C output
if __name__ == "__main__":
    results = calculate_stage4_exergy(70.0)
    print(f"Stage 4 Local Efficiency: {results['stage4_local_efficiency_pct']}%")
    print(f"Net System Yield Added: {results['net_system_yield_added_pct']}%")
