import pandas as pd
from variables.GEN_III_node_amplifiers import CHTSController

def calculate_system_loss(telemetry_file, controller):
    """
    Calculates Empirical System Loss Coefficient (λ).
    λ = 1 - (Actual / Theoretical)
    """
    df = pd.read_csv(telemetry_file)
    total_theoretical = 0
    total_actual = 0
    
    for _, row in df.iterrows():
        # Using baseline temps for forensic model validation
        theoretical = controller.compute_optimized_output(row['Input_kW'])
        
        total_theoretical += theoretical['total_recovery_kw']
        total_actual += row['Output_kW']
    
    if total_theoretical == 0: return 1.0
    return round(1 - (total_actual / total_theoretical), 4)

if __name__ == "__main__":
    c = CHTSController()
    loss = calculate_system_loss('validation/prototype_telemetry.csv', c)
    print(f"Empirical System Loss Coefficient (λ): {loss}")
