import pytest
from variables.GEN_III_node_amplifiers import CHTSController

def test_controller_api_consistency():
    """
    Validates that the test suite aligns with the actual 
    CHTSController interface (compute_optimized_output).
    """
    controller = CHTSController()
    input_thermal_kw = 100.0
    
    # Execute actual controller method
    result = controller.compute_optimized_output(input_thermal_kw)
    
    # Assertions match the new return structure (total_recovery_kw)
    assert "total_recovery_kw" in result
    assert result["total_recovery_kw"] > 0
    assert isinstance(result["total_recovery_kw"], float)
    
    # Validate structure of output keys
    expected_stages = ["teg_high", "teg_low", "zeo", "ads"]
    for stage in expected_stages:
        assert stage in result["outputs"]

def test_buffer_integration():
    """
    Validates that the controller correctly communicates with the 
    ThermalBuffer status.
    """
    controller = CHTSController()
    # Force saturation
    controller.compute_optimized_output(300.0)
    
    status = controller.buffer.get_status()
    assert status["charge_level_kwh"] > 0
    assert status["charge_level_pct"] > 0
