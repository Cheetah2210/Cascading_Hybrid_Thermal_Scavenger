import pandas as pd

def validate_data(csv_path='validation/prototype_telemetry.csv'):
    df = pd.read_csv(csv_path)
    # Check for correct architecture columns
    required = {'teg_high_kw', 'teg_low_kw', 'zeo_recovery_kw'}
    assert required.issubset(df.columns), "Missing solid-state architecture columns!"
    print("Telemetry structure validated.")

if __name__ == "__main__":
    validate_data()
