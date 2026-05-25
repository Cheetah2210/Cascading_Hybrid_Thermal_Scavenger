import matplotlib.pyplot as plt

def plot_performance_with_error(data):
    """
    Forensic analysis tool: Plots actual recovery with 
    statistical error bars (Modeled Sigma).
    """
    # Updated efficiency ceiling to 0.30 (30%)
    EFFICIENCY_CEILING = 0.30
    
    plt.figure(figsize=(10, 6))
    plt.errorbar(
        data['input_kw'], 
        data['total_output_kw'], 
        yerr=data['sigma_values'], 
        fmt='o', 
        label='Measured Recovery ± Modeled Sigma'
    )
    plt.axhline(y=EFFICIENCY_CEILING * data['input_kw'].max(), color='r', linestyle='--', label='Theoretical 30% Ceiling')
    plt.title("CHTS v3.14 Performance: Experimental Confidence Intervals")
    plt.xlabel("Input Thermal kW")
    plt.ylabel("Recovery kW")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    print("Visualization module ready. Ensure data source provides 'modeled_sigma'.")
