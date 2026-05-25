import matplotlib.pyplot as plt
import numpy as np

def plot_performance_with_error(data, temps={'T_hot': 500, 'T_cold': 300}):
    """
    Forensic analysis tool: Plots actual recovery against 
    an independently derived thermodynamic Carnot boundary.
    """
    # Independent Thermodynamic Boundary
    carnot_efficiency = 1 - (temps['T_cold'] / temps['T_hot'])
    input_loads = np.array(data['input_kw'])
    
    # Boundary: Theoretical limit based strictly on 2nd Law
    theoretical_carnot_limit = input_loads * carnot_efficiency
    
    plt.figure(figsize=(10, 6))
    
    # Experimental Results (Deterministic Sigma)
    plt.errorbar(
        data['input_kw'], 
        data['total_output_kw'], 
        yerr=data['modeled_sigma'], 
        fmt='o', 
        label='Measured Recovery ± σ (Deterministic)'
    )
    
    # Independent Physics Ceiling
    plt.plot(data['input_kw'], theoretical_carnot_limit, 'r--', label='Theoretical Carnot Boundary')
    
    plt.title("CHTS v3.14 Performance: Reproducible Forensic Boundary")
    plt.xlabel("Input Thermal kW")
    plt.ylabel("Recovery kW")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    print("Visualization module using reproducible deterministic sigma.")
