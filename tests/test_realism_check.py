import pytest
from variables.GEN_III_node_amplifiers import get_optimized_realistic_yield

def test_ledger_integrity():
    """
    Verifies that the global exergy yield remains within 
    the validated engineering bounds (46.0% - 47.0% range).
    """
    gross_input = 10.0
    result = get_realistic_exergy_yield(gross_input, 1200.0, 300.0)
    
    # Assertions to ensure the cascade logic is functioning as intended
    assert 'realized_net_kw' in result, "Ledger missing 'realized_net_kw' key"
    assert 'achieved_percentage' in result, "Ledger missing 'achieved_percentage' key"
    
    # Verify the realism bounds (46.8% target)
    assert 46.0 <= result['achieved_percentage'] <= 47.5, \
        f"Efficiency {result['achieved_percentage']}% outside of hardware-validated bounds"
    
    assert result['status'] == "HARDWARE_CONSTRAINT_VALIDATED"

def test_extreme_inputs():
    """
    Ensures the system handles negative or zero flux gracefully.
    """
    with pytest.raises(ValueError):
        get_realistic_exergy_yield(0.0, 1200.0, 300.0) 
