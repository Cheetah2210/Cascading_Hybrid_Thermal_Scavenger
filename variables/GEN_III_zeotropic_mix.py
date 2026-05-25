class ZeotropicManager:
    """
    Manages the thermodynamic glide recovery for zeotropic mixtures.
    Encapsulates the cycle-specific recovery logic.
    """
    def __init__(self, mixture_type="R410A_equivalent"):
        self.mixture_type = mixture_type

    def calculate_zeotropic_glide_recovery(self, residual_heat_kw, glide_factor=0.85):
        """
        Calculates recovery efficiency accounting for temperature glide 
        characteristics of the mixture.
        """
        # Glide recovery is non-linear; simple multiplier for now
        # acting as a proxy for physical entropy reduction
        return round(residual_heat_kw * glide_factor, 3)

    def process(self, residual_heat_kw):
        """Wrapper method for package consistency."""
        return self.calculate_zeotropic_glide_recovery(residual_heat_kw)
