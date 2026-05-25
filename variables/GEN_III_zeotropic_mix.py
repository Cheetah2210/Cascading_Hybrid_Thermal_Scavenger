class ZeotropicManager:
    """Manages the thermodynamic glide recovery for zeotropic mixtures."""
    def __init__(self, mixture_type="R410A_equivalent"):
        self.mixture_type = mixture_type

    def calculate_zeotropic_glide_recovery(self, residual_heat_kw, glide_factor=0.85):
        return round(residual_heat_kw * glide_factor, 3)

    def process(self, residual_heat_kw):
        return self.calculate_zeotropic_glide_recovery(residual_heat_kw)
