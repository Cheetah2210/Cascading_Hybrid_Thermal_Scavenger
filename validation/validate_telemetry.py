import csv

def validate_telemetry_data(csv_file_path, tolerance=0.5):
    """
    Parses telemetry data and performs a Power Balance check:
    Input_KW = (MHD + TEG + ZEO) + Rejection_Loss + Losses
    """
    results = []
    
    try:
        with open(csv_file_path, mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Extract and cast inputs
                input_kw = float(row['input_thermal_kw'])
                mhd = float(row['mhd_output_kw'])
                teg = float(row['teg_output_kw'])
                zeo = float(row['zeo_recovery_kw'])
                
                # Calculate total measured output
                outputs = mhd + teg + zeo
                
                # Calorimetry check: residual heat (assuming 50kW baseline rejection)
                residual = input_kw - outputs
                
                # Check variance against target rejection
                variance = abs(residual - 50.0)
                is_valid = variance <= tolerance
                
                results.append({
                    "timestamp": row['timestamp'],
                    "valid": is_valid,
                    "variance": round(variance, 3),
                    "efficiency_gap": round(input_kw - outputs, 3)
                })
    except FileNotFoundError:
        return "Error: File not found. Please ensure prototype_telemetry.csv exists."
        
    return results

if __name__ == "__main__":
    # Path should be relative to the root of your repository
    path = 'validation/prototype_telemetry.csv'
    validation_results = validate_telemetry_data(path)
    
    if isinstance(validation_results, list):
        for entry in validation_results:
            print(f"Time: {entry['timestamp']} | Valid: {entry['valid']} | "
                  f"Variance: {entry['variance']} kW | Gap: {entry['efficiency_gap']} kW")
    else:
        print(validation_results)
