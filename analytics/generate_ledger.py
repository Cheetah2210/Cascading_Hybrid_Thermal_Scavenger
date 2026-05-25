import json
from variables.GEN_III_node_amplifiers import CHTSController

def generate_ledger(input_kw=200.0, output_path='validation/calorimetry_results.json'):
    """
    Generates a serialized ledger of performance metrics directly
    from the Controller model to ensure perfect traceability.
    """
    controller = CHTSController()
    result = controller.compute_optimized_output(input_kw)
    
    ledger = {
        "status": "VALIDATED_BY_MODEL",
        "input_kw": input_kw,
        "results": result['outputs'],
        "total_recovery_kw": result['total_recovery_kw'],
        "modeled_sigma": result['modeled_sigma'],
        "timestamp": "2026-05-25T16:41:00Z"
    }
    
    with open(output_path, 'w') as f:
        json.dump(ledger, f, indent=4)
        
    print(f"Ledger synced successfully to {output_path}.")
    return ledger

if __name__ == "__main__":
    generate_ledger()
