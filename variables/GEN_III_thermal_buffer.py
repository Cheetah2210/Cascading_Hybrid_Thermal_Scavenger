class ThermalBuffer:
    """
    Manages the secondary thermal storage buffer for the GEN-III system.
    Captures excess exergy during saturation and provides discharge during low-input.
    """
    def __init__(self, capacity_kwh=500.0, melt_point_c=120.0):
        self.capacity_kwh = capacity_kwh
        self.melt_point_c = melt_point_c
        self.current_charge = 0.0  # kWh

    def update_charge(self, storage_potential_kw, dt_hours=1.0):
        """Updates the buffer charge based on excess heat capture."""
        energy_added = storage_potential_kw * dt_hours
        self.current_charge = min(self.capacity_kwh, self.current_charge + energy_added)
        return self.current_charge

    def discharge(self, demand_kw, dt_hours=1.0):
        """Releases energy from the buffer to the system."""
        energy_to_release = min(self.current_charge, demand_kw * dt_hours)
        self.current_charge -= energy_to_release
        return energy_to_release / dt_hours

    def get_status(self):
        """Returns the current charge status."""
        return {
            "charge_level_kwh": self.current_charge,
            "charge_level_pct": (self.current_charge / self.capacity_kwh) * 100,
            "ready_for_discharge": self.current_charge > 0
        }
