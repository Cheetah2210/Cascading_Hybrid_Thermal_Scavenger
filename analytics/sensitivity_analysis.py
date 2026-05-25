from variables.GEN_III_node_amplifiers import CHTSController

def run_sensitivity_analysis():
    controller = CHTSController()
    baseline = 0.242
    degraded = 0.218 # 10% performance drop
    
    print(f"{'Input (kW)':<12} | {'Base Out':<10} | {'Degraded Out':<12}")
    for load in [100, 150, 200]:
        base_out = controller.compute_cascaded_output(load)['total_output']
        controller.efficiency_coefficients['mhd'] = degraded
        degraded_out = controller.compute_cascaded_output(load)['total_output']
        controller.efficiency_coefficients['mhd'] = baseline
        print(f"{load:<12} | {base_out:<10.2f} | {degraded_out:<12.2f}")

if __name__ == "__main__":
    run_sensitivity_analysis()
