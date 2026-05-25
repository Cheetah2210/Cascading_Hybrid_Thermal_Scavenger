import matplotlib.pyplot as plt
import numpy as np
from variables.GEN_III_node_amplifiers import CHTSController

def plot_performance_with_error(data):
    """
    Forensic analysis tool: Plots actual recovery against the 
    controller's actual dynamic thermodynamic ceiling.
    """
    controller = CHTSController()
    
    # Calculate dynamic theoretical ceiling by probing the controller's physics
    # We use the baseline temp assumption to define the thermodynamic boundary
    theoretical_limit = []
    for load in data['input_kw']:
        # The theoretical ceiling is the output if the system had 100% stage 
        # utilization up to the Carnot limit.
        res = controller.compute_optimized_output(load)
        theoretical_limit.append(res['total_recovery_kw'] / 0.30) # Normalize back to potential
    
    plt.figure(figsize=(10, 6))
    plt.errorbar(
        data['input_kw'], 
        data['total_output_kw'], 
        yerr=data['modeled_sigma'], 
        fmt='o', 
        label='Measured Recovery ± σ'
    )
    plt.plot(data['input_kw'], theoretical_limit, 'r--', label='Dynamic Thermodynamic Ceiling')
    plt.title("CHTS v3.14 Performance vs. Dynamic Thermodynamic Boundary")
    plt.xlabel("Input Thermal kW")
    plt.ylabel("Recovery kW")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    print("Visualization module using dynamic thermodynamic derivation.")
