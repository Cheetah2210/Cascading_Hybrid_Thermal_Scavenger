import pandas as pd
from variables.GEN_III_node_amplifiers import CHTSController

def run_sensitivity_analysis():
    """
    Forensic sensitivity analysis: Evaluates how the cascaded system 
    responds to thermal load variations.
    """
    controller = CHTSController()
    results = []
    
    # Test across a range of thermal inputs
    for load in [50, 100, 150, 200, 250]:
        report = controller.compute_optimized_output(load)
        results.append({
            "load_kw": load,
            "total_recovery": report["total_recovery_kw"],
            "status": report["status"],
            "modeled_sigma": report["modeled_sigma"]
        })
    
    return pd.DataFrame(results)

if __name__ == "__main__":
    df = run_sensitivity_analysis()
    print("Sensitivity Analysis Results (v3.14 Sync):")
    print(df)
    
    if df['total_recovery'].isnull().any():
        raise ValueError("Sensitivity Analysis failed: Key mismatch detected.")
    print("Analysis complete. API alignment verified.")
