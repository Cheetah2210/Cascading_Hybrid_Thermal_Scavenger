from variables.GEN_III_node_amplifiers import get_optimized_realistic_yield

def test_cascades_energy_balance():
    # Helper to calculate expected yield based on 200kW cap
    def get_expected(input_kw):
        effective = min(input_kw, 200.0)
        return effective * (0.185 + 0.140 + 0.071) # 0.396 total efficiency

    # Test points
    for i in [100.0, 200.0, 250.0]:
        result = get_optimized_realistic_yield(i)
        assert abs(sum(result.values()) - get_expected(i)) < 0.001
