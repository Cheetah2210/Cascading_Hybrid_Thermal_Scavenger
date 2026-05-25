"""
Antoine Vapor Pressure Glide Math
"""
import numpy as np

def calculate_zeotropic_glide(t_inlet: float, t_sink: float) -> float:
    """
    Computes the phase-change glide entropy reduction.
    """
    # Antoine constants for Gen III fluid
    A, B, C = 4.0, 1500.0, 273.15
    pressure_drop = B / (t_inlet + C)
    return pressure_drop
