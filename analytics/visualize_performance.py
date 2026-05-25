import pandas as pd
import matplotlib.pyplot as plt

def plot_performance_gap(sim_data, real_data):
    # Calculate the 'Efficiency Gap'
    sim_data['theoretical_max'] = 0.446
    real_data['realized_yield'] = real_data['total_output_kw'] / real_data['input_thermal_kw']
    
    plt.plot(sim_data['input_kw'], sim_data['theoretical_max'], label='Theoretical')
    plt.plot(real_data['input_kw'], real_data['realized_yield'], label='Realized')
    plt.fill_between(real_data['input_kw'], real_data['realized_yield'], 0.446, color='red', alpha=0.1)
    plt.title("CHTS System Realization Gap")
    plt.show()
