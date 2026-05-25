def validate_energy_balance(input_kw, power_outputs, rejected_heat, system_losses):
    """
    Checks if the system energy is conserved.
    Sum of Outputs + Rejection + Losses must equal Input.
    """
    total_measured = sum(power_outputs.values()) + rejected_heat + system_losses
    variance = abs(input_kw - total_measured)
    
    return {
        "is_balanced": variance < 0.5, # Tolerance of 0.5 kW
        "variance_kw": round(variance, 3)
    }
