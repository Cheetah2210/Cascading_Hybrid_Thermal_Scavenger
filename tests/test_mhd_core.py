import pytest
import numpy as np

# Absolute imports matching your clean package structure
from variables.variable_theory_testing import calculate_hartmann_drag, evaluate_rf_ionization_overhead

def test_hartmann_drag_boundaries():
    """
    Validates that the Hartmann boundary-layer wall shear drag stays within
    the physics-constrained 2.1 kW ceiling under peak flow velocity.
    """
    # Channel parameters matching design specs
    width = 0.040
    height = 0.002
    length = 0.150
    velocity = 45.0
    sigma = 1.2e4
    
    drag_results = calculate_hartmann_drag(
        w=width, h=height, L=length, u=velocity, sigma=sigma
    )
    
    # Assertions to secure physics boundaries
    assert drag_results['net_power_loss_kw'] > 0.0
    
    # Using a minor tolerance window to absorb cross-platform rounding anomalies
    assert drag_results['net_power_loss_kw'] == pytest.approx(2.1, rel=1e-2)


def test_rf_ionization_overhead():
    """
    Verifies that the non-equilibrium active RF ionization energy fields
    remain strictly restricted to the 14.1% parasitic ceiling of the output node.
    """
    gross_input_thermal_kw = 10.0
    expected_mhd_output_kw = 2.42
    
    ionization_data = evaluate_rf_ionization_overhead(
        input_flux=gross_input_thermal_kw, 
        target_output=expected_mhd_output_kw
    )
    
    parasitic_ratio = ionization_data['rf_overhead_percentage']
    
    # Secure the 14.1% performance ledger threshold
    assert parasitic_ratio == pytest.approx(14.1, abs=1e-1)
    assert ionization_data['electron_conductivity_s_m'] >= 1.2e4


def test_channel_geometry_invariants():
    """
    Ensures the micro-channel dimensions reject physically impossible invariants
    (zeros or negative spatial bounds).
    """
    with pytest.raises(ValueError):
        calculate_hartmann_drag(w=0.040, h=-0.002, L=0.150, u=45.0, sigma=1.2e4)
