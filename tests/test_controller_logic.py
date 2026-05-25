import pytest
from variables.GEN_III_node_amplifiers import CHTSController

def test_controller_volatility():
    controller = CHTSController()
    # Simulate a chaotic load pattern: surge, then drop, then sustained saturation
    load_pattern = [50, 250, 10, 300, 20]
    
    for input_kw in load_pattern:
        result = controller.compute_optimized_output(input_kw)
        # Ensure total recovery never exceeds the system's thermal capacity
        assert result['total_recovery_kw'] <= 200.0
        # Check that buffering is active during surges
        if input_kw > 200:
            assert result['status'] == "SATURATED"
        # Check that discharge is active during dips
        if input_kw < 50:
            assert result['status'] == "DISCHARGING"

if __name__ == "__main__":
    pytest.main([__file__])
