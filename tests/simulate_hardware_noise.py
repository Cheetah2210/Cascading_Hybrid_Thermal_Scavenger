import numpy as np

def generate_noisy_telemetry(input_val, theoretical_output):
    """
    Simulates real-world hardware noise, sensor drift, and thermal lag.
    """
    noise = np.random.normal(0, 0.5)  # Gaussian noise
    drift = 0.01 * input_val          # Time-dependent drift
    lag = 0.95 if input_val > 150 else 1.0  # Thermal lag factor
    
    return round((theoretical_output * lag) + noise + drift, 2)
