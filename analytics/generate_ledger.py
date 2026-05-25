import sys
import os
import json
import datetime

# Inject project root into path if run as a script
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from variables.GEN_III_node_amplifiers import CHTSController

def generate_ledger(input_kw=200.0, output_path='validation/calorimetry_results.json'):
    """Generates an authoritative ledger with dynamic ISO-8601 timestamps."""
    controller = CHTSController()
    result = controller.compute_optimized_output(input_kw)
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
        
    print(f"Ledger synced: {output_path} generated at {timestamp}")
    return ledger

if __name__ == "__main__":
    generate_ledger()
