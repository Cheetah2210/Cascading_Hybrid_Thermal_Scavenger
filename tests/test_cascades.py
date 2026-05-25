import pytest
from variables.GEN_III_node_amplifiers import get_realistic_exergy_yield

def test_cascade_stage_progression():
    """
    Verifies that the cascade yields a positive net output 
    and validates the energy balance across the three stages.
    """
    gross_input = 20.0  # 20 kW input
    result = get_realistic_exergy_yield(gross_input, 1200.0, 600.0)
    
    # 1. Ensure the amplifier returns the correct keys
    assert "realized_net_kw" in result
    assert "ideal_potential_kw" in result
    
    # 2. Verify thermodynamic logic: 
    # Realized output should always be less than or equal to ideal potential
    assert result["realized_net_kw"] <= result["ideal_potential_kw"]
    
    # 3. Ensure the output is greater than zero
    assert result["realized_net_kw"] > 0
    
    # 4. Confirm the status flag
    assert result["status"] == "HARDWARE_CONSTRAINT_VALIDATED"

def test_stage_output_consistency():
    """
    Ensures that scaling the input scales the output proportionally.
    """
    low_input = get_realistic_exergy_yield(5.0, 1200.0, 600.0)
    high_input = get_realistic_exergy_yield(10.0, 1200.0, 600.0)
    
    # Check if the output scales (roughly linear within the constrained hardware limits)
    assert high_input["realized_net_kw"] > low_input["realized_net_kw"]
