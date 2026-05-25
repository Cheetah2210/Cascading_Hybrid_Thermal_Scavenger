import pytest
from variables.GEN_III_node_amplifiers import CHTSController

def test_controller_volatility():
    """
    Forensic stress test: validates controller behavior under 
    erratic thermal load patterns (Surge, Dip, Saturation).
    """
    controller = CHTSController()
    
    # Simulate a chaotic load pattern: surge, then drop, then sustained saturation
    load_pattern = [50, 250, 10, 300, 20]
    
    for input_kw in load_pattern:
        result = controller.compute_optimized_output(input_kw)
        
        # 1. Safety Constraint: Recovery must not exceed total physical capacity
        assert result['total_recovery_kw'] <= 200.0, f"System exceeded capacity at {input_kw}kW"
        
        # 2. Forensic Logic Validation: Buffering vs. Discharge
        if input_kw > 200:
            assert result['status'] == "SATURATED", f"Failed to detect saturation at {input_kw}kW"
        elif input_kw < 50:
            assert result['status'] == "DISCHARGING", f"Failed to trigger discharge at {input_kw}kW"
        else:
            assert result['status'] == "OPTIMAL", f"Unexpected state at {input_kw}kW"

if __name__ == "__main__":
    pytest.main([__file__])
