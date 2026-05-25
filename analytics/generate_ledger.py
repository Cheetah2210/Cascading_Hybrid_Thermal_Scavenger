import json
import datetime
from variables.GEN_III_node_amplifiers import CHTSController

def generate_ledger(input_kw=200.0, output_path='validation/calorimetry_results.json'):
    """
    Generates an authoritative ledger with dynamic timestamps.
    This ensures provenance remains accurate to the time of generation.
    """
    controller = CHTSController()
    result = controller.compute_optimized_output(input_kw)
    
    # Dynamic UTC timestamping for forensic accuracy
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    ledger = {
        "status": "AUTHORITATIVE_MODEL_OUTPUT",
        "input_kw": input_kw,
        "results": result['outputs'],
        "total_recovery_kw": result['total_recovery_kw'],
        "modeled_sigma": result['modeled_sigma'],
        "timestamp": timestamp
    }
    
    with open(output_path, 'w') as f:
        json.dump(ledger, f, indent=4)
        
    print(f"Ledger updated: {output_path} generated at {timestamp}")
    return ledger

if __name__ == "__main__":
    generate_ledger()
