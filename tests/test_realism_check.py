"""
Test Suite: Realism, Integrity, and Fail-Safe Logic
Validates baseline yields and the MHD-Bypass mode.
"""

from variables.GEN_III_node_amplifiers import get_optimized_realistic_yield

def test_physical_limits():
    # Test with zero remediation to ensure baseline integrity
    base_vars = {
        'mhd_ionization_stable': True,
        'slip_factor': 0.0,
        'ehd_freq_boost': 0.0,
        'halbach_flux_gain': 0.0,
        'zt_coefficient': 1.0
    }
    
    result = get_optimized_realistic_yield(100.0, base_vars)
    
    # Base realistic yield should be 46.8%
    assert result["optimized_net_kw"] == 46.8

def test_mhd_bypass_mode():
    # Test failure mode: MHD ionization fails
    fail_vars = {
        'mhd_ionization_stable': False
    }
    
    result = get_optimized_realistic_yield(100.0, fail_vars)
    
    # When bypassed, yield should drop to the thermal-only recovery floor (22%)
    assert result["optimized_net_kw"] == 22.0
    assert result["status"] == "MHD_BYPASS_ENGAGED_THERMAL_ONLY"
