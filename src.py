"""Quantum tunneling solver using the thick-barrier approximation."""
import numpy as np

HBAR = 1.054571817e-34       # J s
ELECTRON_MASS = 9.1093837e-31 # kg
PROTON_MASS = 1.6726219e-27   # kg
EV_J = 1.602176634e-19        # J/eV

def solve_tunneling(particle="Electron", energy_eV=1.0, barrier_eV=2.0,
                    width_nm=0.5, custom_mass_kg=None):
    """Return tunneling quantities for E < V0 using T ~= exp(-2*kappa*a)."""
    masses = {"Electron": ELECTRON_MASS, "Proton": PROTON_MASS}
    if particle == "Custom Particle":
        if custom_mass_kg is None or custom_mass_kg <= 0:
            raise ValueError("custom_mass_kg must be a positive value.")
        mass = float(custom_mass_kg)
    elif particle in masses:
        mass = masses[particle]
    else:
        raise ValueError("particle must be Electron, Proton, or Custom Particle")
    if energy_eV <= 0 or barrier_eV <= 0 or width_nm <= 0:
        raise ValueError("Energy, barrier height, and width must be positive.")
    if energy_eV >= barrier_eV:
        raise ValueError("Tunneling approximation requires particle energy E < barrier V0.")
    energy_j = energy_eV * EV_J
    barrier_j = barrier_eV * EV_J
    width_m = width_nm * 1e-9
    k = np.sqrt(2 * mass * energy_j) / HBAR
    kappa = np.sqrt(2 * mass * (barrier_j - energy_j)) / HBAR
    transmission = float(np.exp(-2 * kappa * width_m))
    return {
        "particle": particle, "mass_kg": mass, "energy_eV": energy_eV,
        "barrier_eV": barrier_eV, "width_nm": width_nm,
        "wave_number_per_m": float(k), "decay_constant_per_m": float(kappa),
        "transmission_probability": transmission,
        "transmission_percent": transmission * 100,
        "reflection_probability_approx": 1 - transmission,
        "reflection_percent_approx": (1 - transmission) * 100
    }
