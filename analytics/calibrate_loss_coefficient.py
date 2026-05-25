import pandas as pd

def calculate_system_loss(telemetry_file, controller):
    """
    Forensic analysis: Compares actual telemetry vs. cascaded physics 
    to derive the empirical loss coefficient.
    """
    df = pd.read_csv(telemetry_file)
    total_theoretical = 0
    total_actual = 0
    
    for _, row in df.iterrows():
        # Re-run the controller model using live historical temperatures
        # Assuming HIL controller inputs are T_hot and T_cold
        live_temps = {'T_hot': 500, 'T_cold': 300} # Replace with actual sensor data if logged
        theoretical = controller.compute_optimized_output(row['Input_kW'], live_temps)
        
        total_theoretical += theoretical['total_recovery_kw']
        total_actual += row['Output_kW']
    
    # Calculate System Loss Coefficient
    loss_coefficient = 1 - (total_actual / total_theoretical)
    return round(loss_coefficient, 4)

# Usage
if __name__ == "__main__":
    from variables.GEN_III_node_amplifiers import CHTSController
    c = CHTSController()
    loss = calculate_system_loss('validation/prototype_telemetry.csv', c)
    print(f"Empirical System Loss Coefficient: {loss}")
