import pandas as pd
import matplotlib.pyplot as plt

def plot_performance_gap(sim_data, real_data):
    """
    Forensic analysis tool: Visualizes the delta between theoretical 
    efficiency and realized net yield to identify system bottlenecks.
    """
    # Theoretical Max Benchmark
    sim_data['theoretical_max'] = 0.446
    
    # Calculate Realized Yield
    real_data['realized_yield'] = real_data['total_output_kw'] / real_data['input_thermal_kw']
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(real_data['input_kw'], sim_data['theoretical_max'], label='Theoretical Max (44.6%)', linestyle='--')
    plt.plot(real_data['input_kw'], real_data['realized_yield'], label='Realized Yield', marker='o')
    
    # Highlight the 'Realization Gap'
    plt.fill_between(real_data['input_kw'], real_data['realized_yield'], 0.446, color='red', alpha=0.1)
    
    plt.title("CHTS System Realization Gap Analysis")
    plt.xlabel("Input Thermal Load (kW)")
    plt.ylabel("Efficiency Percentage")
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage for forensic validation:
if __name__ == "__main__":
    # Mock-up data for demonstration
    sample_data = pd.DataFrame({
        'input_kw': [50, 100, 150, 200],
        'total_output_kw': [22, 43, 64, 88]
    })
    plot_performance_gap(sample_data, sample_data)
