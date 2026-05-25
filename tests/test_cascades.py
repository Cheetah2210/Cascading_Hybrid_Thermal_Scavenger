from variables.GEN_III_node_amplifiers import get_optimized_realistic_yield

def test_cascades_energy_balance():
    # Verify 39.6% baseline conversion (0.185+0.140+0.071)
    input_kw = 100.0
    result = get_optimized_realistic_yield(input_kw)
    total = sum(result.values())
    assert abs(total - 39.6) < 0.001

def test_saturation_clamping():
    # Verify the 200kW cap (200 * 0.396 = 79.2)
    input_kw = 300.0
    result = get_optimized_realistic_yield(input_kw)
    total = sum(result.values())
    assert abs(total - 79.2) < 0.001
