import csv
import json
import os

def calculate_metrics(row):
    """
    Computes Efficiency (%) and COP for the telemetry row.
    """
    total_power_out = float(row['mhd_output_kw']) + float(row['teg_output_kw']) + float(row['zeo_recovery_kw'])
    input_kw = float(row['input_thermal_kw'])
    
    # Efficiency = Total Output / Total Input
    efficiency = (total_power_out / input_kw) * 100
    
    # COP = Total Output / Parasitic Input (Estimated at 5% of gross input)
    cop = total_power_out / (input_kw * 0.05) if input_kw > 0 else 0
    
    return round(efficiency, 2), round(cop, 2)

def validate_telemetry_data(csv_file_path, tolerance=0.5):
    """
    Parses telemetry data, performs Power Balance check, and computes performance metrics.
    """
    report = []
    
    if not os.path.exists(csv_file_path):
        return None
        
    with open(csv_file_path, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                input_kw = float(row['input_thermal_kw'])
                outputs = float(row['mhd_output_kw']) + float(row['teg_output_kw']) + float(row['zeo_recovery_kw'])
                
                # Efficiency and COP calculation
                eff, cop = calculate_metrics(row)
                
                # Calorimetry check: residual heat (50kW baseline rejection)
                residual = input_kw - outputs
                variance = abs(residual - 50.0)
                
                report.append({
                    "timestamp": row['timestamp'],
                    "valid": variance <= tolerance,
                    "variance_kw": round(variance, 3),
                    "efficiency_pct": eff,
                    "cop": cop
                })
            except (ValueError, KeyError):
                continue
    return report

def export_balance_summary(report, output_file='validation/power_balance_log.json'):
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=4)

if __name__ == "__main__":
    results = validate_telemetry_data('validation/prototype_telemetry.csv')
    
    if results:
        print(f"{'Timestamp':<25} | {'Valid':<5} | {'Eff %':<6} | {'COP':<5}")
        print("-" * 50)
        for entry in results:
            print(f"{entry['timestamp']:<25} | {str(entry['valid']):<5} | "
                  f"{entry['efficiency_pct']:<6} | {entry['cop']:<5}")
        
        export_balance_summary(results)
        print("\nLog updated with efficiency metrics.")
    else:
        print("Error: Could not process telemetry file.")
