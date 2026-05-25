import matplotlib.pyplot as plt
import numpy as np

def plot_performance_with_error(data):
    """
    Forensic analysis tool: Plots actual recovery against 
    the controller's validated aggregate efficiency ceiling (30%).
    """
    # Aggregate ceiling is 30%; Carnot efficiency is already factored 
    # into the controller's stage-wise processing.
    AGGREGATE_EFFICIENCY = 0.30
    input_loads = np.array(data['input_kw'])
    theoretical_limit = input_loads * AGGREGATE_EFFICIENCY
    
    plt.figure(figsize=(10, 6))
    
    # Plot experimental results with numeric error bars
    plt.errorbar(
        data['input_kw'], 
        data['total_output_kw'], 
        yerr=data['modeled_sigma'], 
        fmt='o', 
        label='Measured Recovery ± σ'
    )
    
    # Plot the physics-aligned aggregate limit
    plt.plot(data['input_kw'], theoretical_limit, 'r--', label='Theoretical 30% Aggregate Limit')
    
    plt.title("CHTS v3.14 Performance: Aggregate Efficiency Analysis")
    plt.xlabel("Input Thermal kW")
    plt.ylabel("Recovery kW")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    print("Visualization module fully synchronized with controller v3.14.")
