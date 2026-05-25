import pytest
# Absolute import from the repository root
from variables.zeotropic_mix import calculate_cascade 

def test_second_law_compliance():
    # Run your dynamic glide simulation
    calculated_efficiency = calculate_cascade(source_temp=1200, sink_temp=300)
    
    # ✅ FIX: Use an approximation window for floating-point safety
    assert calculated_efficiency == pytest.approx(0.468, abs=1e-4)
