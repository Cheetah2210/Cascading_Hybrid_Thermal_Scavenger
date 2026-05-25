import csv
import json
import os

def validate_telemetry_data(csv_file_path, tolerance=0.5):
    """
    Parses telemetry data and performs a Power Balance check:
    Input_KW = (MHD + TEG + ZEO) + Rejection_Loss + Losses
    """
    report = []
    
    if not os.path.exists(csv_file_path):
        return None
        
    with open(csv_file_path, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                # Extract and cast inputs from telemetry
                input_kw = float(row['input_thermal_kw'])
                mhd = float(row['mhd_output_kw'])
                teg = float(row['teg_output_kw'])
                zeo = float(row['zeo_recovery_kw'])
                
                # Total conversion output
                outputs = mhd + teg + zeo
                
                # Calorimetry check: residual heat (assuming 50kW baseline rejection)
                residual = input_kw - outputs
                
                # Check variance against target rejection baseline
                variance = abs(residual - 50.0)
                is_valid = variance <= tolerance
                
                report.append({
                    "timestamp": row['timestamp'],
                    "valid": is_valid,
                    "variance": round(variance, 3),
                    "efficiency_gap": round(input_kw - outputs, 3)
                })
            except (ValueError, KeyError) as e:
                print(f"Skipping malformed row: {e}")
                continue
                
    return report

def export_balance_summary(report, output_file='validation/power_balance_log.json'):
    """
    Exports the validation report to a JSON log for long-term tracking.
    """
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=4)

if __name__ == "__main__":
    # Define file paths
    input_path = 'validation/prototype_telemetry.csv'
    log_path = 'validation/power_balance_log.json'
    
    # Process the data
    results = validate_telemetry_data(input_path)
    
    if results:
        # Print summary report to console
        print(f"{'Timestamp':<25} | {'Valid':<5} | {'Variance':<10} | {'Gap (kW)':<8}")
        print("-" * 60)
        for entry in results:
            print(f"{entry['timestamp']:<25} | {str(entry['valid']):<5} | "
                  f"{entry['variance']:<10} | {entry['efficiency_gap']:<8}")
        
        # Export log file
        export_balance_summary(results, log_path)
        print(f"\nSuccessfully generated power balance log at: {log_path}")
    else:
        print(f"Error: Could not process file at {input_path}. Please verify path and structure.")
