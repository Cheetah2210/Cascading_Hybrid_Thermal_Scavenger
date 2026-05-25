from variables.GEN_III_node_amplifiers import get_realistic_exergy_yield

def test_ledger_integrity():
    # Test at 10kW baseline
    result = get_realistic_exergy_yield(10.0, 1200.0, 300.0)
    assert 46.0 <= result['achieved_percentage'] <= 47.0, "Efficiency outside of validated bounds"
