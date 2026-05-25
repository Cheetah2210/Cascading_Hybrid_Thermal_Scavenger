from variables.GEN_III_node_amplifiers import get_optimized_realistic_yield

def test_cascades_energy_balance():
    # Test Normal Operational Range
    gross_input = 100.0 
    result = get_optimized_realistic_yield(gross_input)
    assert sum(result.values()) == 39.6
    
    # Test Saturation Range (Above 200kW)
    # The system should cap at 200kW, so the sum should be 39.6 * 2 = 79.2
    saturation_input = 250.0
    result_sat = get_optimized_realistic_yield(saturation_input)
    assert sum(result_sat.values()) == 79.2
