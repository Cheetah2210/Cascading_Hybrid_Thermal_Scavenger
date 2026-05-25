"""
Test Suite: Thermodynamic Cascade Consistency
Validates that the CHTS stages maintain energy balance (Second Law integrity).
"""
from variables.GEN_III_node_amplifiers import get_optimized_realistic_yield

def test_cascades_energy_balance():
    # 100 kW input * (0.185 + 0.140 + 0.071) = 39.6 kW total
    gross_input = 100.0 
    result = get_optimized_realistic_yield(gross_input)
    
    assert sum(result.values()) == 39.6
    assert "teg_high" in result
    assert "teg_low" in result
    assert "zeo" in result
