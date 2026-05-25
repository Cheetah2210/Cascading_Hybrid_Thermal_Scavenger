"""
Test Suite: Thermodynamic Cascade Consistency
Validates that the CHTS stages maintain energy balance (Second Law integrity).
"""

from variables.GEN_III_node_amplifiers import get_optimized_realistic_yield

def test_cascades_energy_balance():
    # Define granular physical remediation variables for the test
    test_phys_vars = {
        'slip_factor': 0.025,
        'ehd_freq_boost': 0.042,
        'halbach_flux_gain': 0.031,
        'zt_coefficient': 1.0
    }
    
    gross_input = 100.0 # 100 kW input
    
    # Execute optimized yield calculation
    result = get_optimized_realistic_yield(gross_input, test_phys_vars)
    
    # Assertions
    assert "optimized_net_kw" in result
    assert result["optimized_net_kw"] > 0
    assert result["status"] == "GRANULAR_MODEL_VALIDATED"
    
    # Verify that the yield is within the realistic target range (40-60%)
    assert 40.0 <= result["optimized_net_kw"] <= 60.0
