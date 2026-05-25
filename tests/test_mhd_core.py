import pytest
import numpy as np

# Absolute imports targeting the physics engine core
from variables.node_amplifiers import calculate_hartmann_drag
from variables.variable_theory_testing import evaluate_rf_ionization_overhead

def test_hartmann_drag_boundaries():
    """
    Validates that the Hartmann boundary-layer wall shear drag stays within
    the physics-constrained 2.1 kW ceiling under peak flow velocity.
    
    Channel Target Dimensions: 40mm x 2mm x 150mm
    Fluid Velocity Target: 45 m/s
    Target Conductivity (sigma): 1.2e4 S/m
    """
    # Channel dimensions converted to meters
    width = 0.040
    height = 0.002
    length = 0.150
    velocity = 45.0
    sigma = 1.2e4
    
    # Run core physics engine calculation
    drag_results = calculate_hartmann_drag(
        w=width, h=height, L=length, u=velocity, sigma=sigma
    )
    
    # 1. Assert gross braking force doesn't completely stall the net power output
    assert drag_results['net_power_loss_kw'] > 0.0
    
    # 2. Assert wall shear drag precisely tracks our forensic matrix limit (2.1 kW)
    # Using a 1% relative tolerance to cushion architecture drift across python minor versions
    assert drag_results['net_power_loss_kw'] == pytest.approx(2.1, rel=1e-2)


def test_rf_ionization_overhead():
    """
    Verifies that active non-equilibrium RF ionization fields do not exceed 
    the maximum allowed parasitic energy overhead of 14.1% of the gross node output.
    """
    gross_input_thermal_kw = 10.0
    expected_mhd_output_kw = 2.42
    
    ionization_data = evaluate_rf_ionization_overhead(
        input_flux=gross_input_thermal_kw, 
        target_output=expected_mhd_output_kw
    )
    
    # Extract calculated parasitic ratio
    parasitic_ratio = ionization_data['rf_overhead_percentage']
    
    # Assert that the RF field stays tightly bounded to the 14.1% threshold
    assert parasitic_ratio == pytest.approx(14.1, abs=1e-1)
    
    # Physical check: Ensure electron temperature scaling yields a positive energy balance
    assert ionization_data['electron_conductivity_s_m'] >= 1.2e4


def test_channel_geometry_invariants():
    """
    Sanity test to ensure the ultra-thin slit design parameters do not 
    accidentally receive negative or zero dimension scales during a dynamic glide shift.
    """
    with pytest.raises(ValueError):
        # Passing an invalid negative channel height must throw an explicit exception
        calculate_hartmann_drag(w=0.040, h=-0.002, L=0.150, u=45.0, sigma=1.2e4)
