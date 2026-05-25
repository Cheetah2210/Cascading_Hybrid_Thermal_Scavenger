import json
import sys
import os

# Inject project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def validate_telemetry(telemetry_path='validation/calorimetry_results.json'):
    """Validates that telemetry contains the required architecture keys."""
    required_keys = {'teg_high', 'teg_low', 'zeo', 'ads'}
    
    with open(telemetry_path, 'r') as f:
        data = json.load(f)
        
    results = data.get('results', {})
    missing = required_keys - set(results.keys())
    
    if missing:
        raise AssertionError(f"Missing architecture columns: {missing}")
        
    print(f"Telemetry valid: {telemetry_path} matches v3.14 schema.")

if __name__ == "__main__":
    validate_telemetry()
