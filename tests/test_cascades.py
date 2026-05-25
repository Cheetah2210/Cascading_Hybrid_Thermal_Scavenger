import pytest
from variables.GEN_III_node_amplifiers import CHTSController

def test_four_stage_energy_balance():
    """
    Verifies that the controller correctly calculates the 44.6% 
    total system gain (0.185 + 0.140 + 0.071 + 0.05).
    """
    controller = CHTSController()
    input_kw = 100.0
    result = controller.compute_cascaded_output(input_kw)
    
    # Assert total output equals 44.6 kW based on the defined coefficients
    assert abs(result["total_output"] - 44.6) < 0.001
    
    # Verify all four stages are present in the output
    expected_keys = {"teg_high", "teg_low", "zeo", "ads"}
    assert expected_keys.issubset(result["outputs"].keys())

def test_saturation_clamping():
    """
    Verifies that the system output caps at the 200kW limit.
    200kW * 0.446 = 89.2 kW total.
    """
    controller = CHTSController()
    saturation_input = 300.0
    result = controller.compute_cascaded_output(saturation_input)
    
    # The output should be clamped to the 200kW capacity
    assert result["total_output"] == 89.2
    assert result["status"] == "SATURATED"

def test_stage_output_values():
    """
    Ensures that individual stages receive the correct proportional input.
    """
    controller = CHTSController()
    input_kw = 100.0
    result = controller.compute_cascaded_output(input_kw)
    
    assert result["outputs"]["teg_high"] == 18.5
    assert result["outputs"]["teg_low"] == 14.0
    assert result["outputs"]["zeo"] == 7.1
    assert result["outputs"]["ads"] == 5.0
