import pytest
from variables.GEN_III_node_amplifiers import CHTSController

def test_controller_api_compatibility():
    """Validates that the controller works with and without live_temps."""
    controller = CHTSController()
    
    # Test Fallback Mode
    res_default = controller.compute_optimized_output(100.0)
    assert res_default['total_recovery_kw'] > 0
    
    # Test HIL Mode
    res_hil = controller.compute_optimized_output(100.0, {'T_hot': 550, 'T_cold': 290})
    assert res_hil['total_recovery_kw'] > res_default['total_recovery_kw'] # Higher Carnot = higher recovery

def test_state_consistency():
    controller = CHTSController()
    assert controller.compute_optimized_output(250)['status'] == "SATURATED"
    assert controller.compute_optimized_output(20)['status'] == "DISCHARGING"
