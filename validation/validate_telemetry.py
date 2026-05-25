import csv

def validate_telemetry_data(csv_file_path, tolerance=0.5):
    """
    Parses telemetry data and checks if the Power Balance holds:
    Input_KW = (MHD + TEG + ZEO) + Rejection_Loss
    """
    results = []
    with open(csv_file_path, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Cast inputs to float
            input_kw = float(row['input_thermal_kw'])
            outputs = float(row['mhd_output_kw']) + float(row['teg_output_kw']) + float(row['zeo_recovery_kw'])
            
            # Simple approximation for calorimetry: Input - Output = Residual Heat
            residual = input_kw - outputs
            
            # Here we assume a theoretical rejection target of ~50.0 kW
            # Variance checks if measured rejection matches theoretical expectations
            is_valid = abs(residual - 50.0) <= tolerance
            
            results.append({"timestamp": row['timestamp'], "valid": is_valid, "variance": round(abs(residual - 50.0), 3)})
            
    return results

# Example execution output
if __name__ == "__main__":
    validation = validate_telemetry_data('validation/prototype_telemetry.csv')
    for entry in validation:
        print(f"Time: {entry['timestamp']} | Valid: {entry['valid']} | Variance: {entry['variance']} kW")
