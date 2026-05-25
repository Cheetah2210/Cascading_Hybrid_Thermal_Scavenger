import matplotlib.pyplot as plt
import numpy as np

def plot_performance_with_error(data, temps={'T_hot': 500, 'T_cold': 300}):
    """
    Forensic analysis tool: Plots actual recovery against 
    dynamic theoretical Carnot limits.
    """
    # Calculate Carnot efficiency based on provided temps
    carnot = 1 - (temps['T_cold'] / temps['T_hot'])
    
    # Calculate dynamic ceiling (30% aggregate efficiency of processed load)
    # Ensure inputs are treated as a numpy array for vector math
    input_loads = np.array(data['input_kw'])
    theoretical_limit = input_loads * 0.30 * carnot
    
    plt.figure(figsize=(10, 6))
    
    # Plot experimental results with error bars
    plt.errorbar(
        data['input_kw'], 
        data['total_output_kw'], 
        yerr=data['modeled_sigma'], 
        fmt='o', 
        label='Measured Recovery ± σ'
    )
    
    # Plot the dynamic theoretical limit
    plt.plot(data['input_kw'], theoretical_limit, 'r--', label='Dynamic Thermodynamic Limit')
    
    plt.title("CHTS v3.14 Performance: Dynamic Thermodynamic Limit Analysis")
    plt.xlabel("Input Thermal kW")
    plt.ylabel("Recovery kW")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    print("Visualization module ready. Ensure data source includes 'modeled_sigma'.")
