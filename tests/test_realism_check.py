"""
Test Suite: Realism & Integrity
Validates that the simulation does not exceed physical thermodynamic limits.
"""

from variables.GEN_III_node_amplifiers import get_optimized_realistic_yield

def test_physical_limits():
    # Test with zero remediation to ensure baseline integrity
    base_vars = {
        'slip_factor': 0.0,
        'ehd_freq_boost': 0.0,
        'halbach_flux_gain': 0.0,
        'zt_coefficient': 1.0
    }
    
    result = get_optimized_realistic_yield(100.0, base_vars)
    
    # Base realistic yield should be exactly 46.8%
    assert result["optimized_net_kw"] == 46.8
