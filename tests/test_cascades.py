import pytest
import numpy as np
from variables.teg_sandwich import simulate_teg_core
from variables.zeotropic_mix import calculate_zeotropic_glide, calculate_cascade

def test_second_law_compliance():
    """
    Validates that the cumulative system cascade does not cross the theoretical
    maximum efficiency cap defined by the Carnot limit.
    """
    t_hot = 1200.0  # Source peak temperature (Kelvin)
    t_cold = 300.0  # Environmental sink temperature (Kelvin)
    
    # Max Carnot Limit = 1 - (T_cold / T_hot)
    carnot_limit = 1.0 - (t_cold / t_hot)  # Evaluates to 0.75 (75.0%)
    
    # Extract total calculated cascade efficiency
    calculated_efficiency = calculate_cascade(source_temp=t_hot, sink_temp=t_cold)
    
    # Assert that the real-world net yield sits safely underneath the Carnot ceiling
    assert calculated_efficiency < carnot_limit
    assert calculated_efficiency == pytest.approx(0.468, abs=1e-4)


def test_electrode_contact_resistance():
    """
    Verifies that the Stage 2 TEG layer recognizes laser-textured 
    contact thresholds and does not drop to an ideal zero-resistance state.
    """
    teg_data = simulate_teg_core(residual_flux_kw=7.58)
    
    # Check that contact layer resistance is tracked at exactly 0.15 mOhm
    assert teg_data['contact_resistance_ohms'] == 1.5e-4
    assert teg_data['net_teg_output_kw'] == pytest.approx(1.17, abs=1e-2)


def test_zeotropic_glide_mismatch():
    """
    Validates Stage 3 glide parsing to ensure environmental runoff calculations
    account for non-zero thermodynamic losses.
    """
    stage3_data = calculate_zeotropic_glide(source_flux_kw=6.41)
    
    # Verify realistic net yield matches the ledger (7.1%)
    assert stage3_data['realistic_net_efficiency'] == 7.1
    assert stage3_data['net_zeotropic_output_kw'] == pytest.approx(0.45, abs=1e-2)
