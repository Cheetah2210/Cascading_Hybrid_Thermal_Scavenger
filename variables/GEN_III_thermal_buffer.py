class ThermalBuffer:
    """
    Manages the secondary thermal storage buffer for the GEN-III system.
    """
    def __init__(self, capacity_kwh=100.0, melt_point_c=120.0):
        self.capacity_kwh = capacity_kwh
        self.melt_point_c = melt_point_c
        self.current_charge = 0.0 # kWh

    def update_charge(self, storage_potential_kw, dt_hours=1.0):
        """
        Updates the buffer charge based on excess heat capture.
        """
        energy_added = storage_potential_kw * dt_hours
        self.current_charge = min(self.capacity_kwh, self.current_charge + energy_added)
        return self.current_charge

    def get_status(self):
        return {
            "charge_level_pct": (self.current_charge / self.capacity_kwh) * 100,
            "ready_for_discharge": self.current_charge > 0
        }
