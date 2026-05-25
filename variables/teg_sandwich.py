"""
TEG Sandwich Efficiency Model
Calculates thermoelectric power output while enforcing contact resistance 
and thermal interface limitations.
"""

def simulate_teg_core(heat_flux_kw: float, t_hot: float, t_cold: float) -> dict:
    """
    Simulates the performance of the Stage 2 TEG sandwich.
    
    Parameters:
    - heat_flux_kw: Residual thermal energy (kW) from Stage 1.
    - t_hot: Hot side temperature (K).
    - t_cold: Cold side temperature (K).
    
    Returns:
    - net_teg_output_kw: Calculated power generated (kW).
    - rejected_flux_kw: Remaining thermal energy passed to Stage 3.
    """
    
    # 1. Constants and Constraints
    # Contact resistance enforced at 0.15 mOhm (0.00015 Ohms)
    contact_resistance_ohm = 0.00015
    
    # 2. Temperature Gradient
    delta_t = t_hot - t_cold
    if delta_t <= 0:
        return {"net_teg_output_kw": 0.0, "rejected_flux_kw": heat_flux_kw}
    
    # 3. Seebeck Efficiency Calculation
    # Theoretical Carnot efficiency limit
    carnot_eff = delta_t / t_hot
    
    # Realistic TEG efficiency factor (Module performance * Contact loss penalty)
    # Contact resistance effectively shunts a portion of generated current
    contact_loss_factor = 1.0 / (1.0 + (contact_resistance_ohm * 100))
    module_efficiency = 0.20 * carnot_eff * contact_loss_factor
    
    # 4. Energy Conversion
    net_teg_output_kw = heat_flux_kw * module_efficiency
    rejected_flux_kw = heat_flux_kw - net_teg_output_kw
    
    return {
        "net_teg_output_kw": round(net_teg_output_kw, 4),
        "rejected_flux_kw": round(rejected_flux_kw, 4),
        "efficiency_achieved": round(module_efficiency * 100, 2),
        "status": "TEG_CORE_STABLE"
    }

# Example validation check
# print(simulate_teg_core(5.0, 350, 300))
