import pytest
from variables.GEN_III_node_amplifiers import CHTSController

def test_controller_state_transition():
    """
    Validates that the controller correctly transitions between 
    operational states under cascaded thermodynamic loads.
    """
    controller = CHTSController(max_capacity=200.0)
    
    # Test cases: (input_kw, expected_state)
    scenarios = [
        (250, "SATURATED"),    # Above max
        (30, "DISCHARGING"),   # Below threshold
        (100, "OPTIMAL")       # Nominal operation
    ]
    
    for input_kw, expected_state in scenarios:
        result = controller.compute_optimized_output(input_kw)
        assert result['status'] == expected_state, f"State mismatch at {input_kw}kW"
        assert result['total_recovery_kw'] > 0
