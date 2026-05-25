class ThermalBuffer:
    """Handles transient thermal lag in the GEN-III system."""
    def __init__(self, capacity_kj=500.0):
        self.capacity_kj = capacity_kj
        self.current_stored_heat = 0.0

    def update(self, heat_flux_kw, delta_t_sec):
        self.current_stored_heat += (heat_flux_kw * delta_t_sec)
        return min(self.current_stored_heat, self.capacity_kj)
