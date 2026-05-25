import matplotlib.pyplot as plt
import pandas as pd

def plot_performance_curve(csv_path='validation/prototype_telemetry.csv'):
    df = pd.read_csv(csv_path)
    # Calculate efficiency percentage
    df['total_output'] = df['mhd_output_kw'] + df['teg_output_kw'] + df['zeo_recovery_kw']
    df['efficiency'] = (df['total_output'] / df['input_thermal_kw']) * 100
    
    plt.figure(figsize=(10, 6))
    plt.plot(df['input_thermal_kw'], df['efficiency'], marker='o', linestyle='-', color='b')
    plt.title('CHTS System Efficiency vs. Thermal Input')
    plt.xlabel('Input Thermal (kW)')
    plt.ylabel('Conversion Efficiency (%)')
    plt.grid(True)
    plt.savefig('analytics/performance_curve.png')
    print("Graph generated: analytics/performance_curve.png")

if __name__ == "__main__":
    plot_performance_curve()
