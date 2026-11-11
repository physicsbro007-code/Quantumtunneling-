"""Run the full quantum-tunneling analysis and save tables and figures."""
from pathlib import Path
import csv
import numpy as np
import matplotlib.pyplot as plt
from quantum_tunneling import solve_tunneling

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
RESULTS = ROOT / "results"
DATA.mkdir(exist_ok=True)
RESULTS.mkdir(exist_ok=True)

params = solve_tunneling("Electron", 1.0, 2.0, 0.5)
with (RESULTS / "summary.txt").open("w", encoding="utf-8") as f:
    f.write("QUANTUM TUNNELING ANALYSIS\\n")
    f.write("Model: thick-barrier approximation T = exp(-2*kappa*a)\\n\\n")
    for key, value in params.items():
        f.write(f"{key}: {value}\\n")
    T = params["transmission_probability"]
    f.write("\\nInterpretation: " + (
        "Significant tunneling probability." if T > 0.01 else
        "Tunneling occurs with a small probability." if T > 1e-6 else
        "Tunneling probability is extremely small."
    ) + "\\n")

# Barrier width sweep
widths = np.linspace(0.1, 5.0, 200)
width_data = [solve_tunneling(width_nm=float(w)) for w in widths]
with (DATA / "transmission_vs_width.csv").open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f); writer.writerow(["barrier_width_nm", "transmission_probability", "transmission_percent"])
    writer.writerows((d["width_nm"], d["transmission_probability"], d["transmission_percent"]) for d in width_data)

# Particle energy sweep, keeping E below V0
energies = np.linspace(0.1, 2.0*0.99, 200)
energy_data = [solve_tunneling(energy_eV=float(e)) for e in energies]
with (DATA / "transmission_vs_energy.csv").open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f); writer.writerow(["particle_energy_eV", "transmission_probability", "transmission_percent"])
    writer.writerows((d["energy_eV"], d["transmission_probability"], d["transmission_percent"]) for d in energy_data)

# Potential profile
x = np.linspace(-1.5, 2.0, 500) # nm
potential = np.where((x >= 0) & (x <= 0.5), 2.0, 0.0)
plt.figure(figsize=(9, 5)); plt.plot(x, potential, label="Potential barrier")
plt.axhline(1.0, linestyle="--", label="Particle energy")
plt.xlabel("Position (nm)"); plt.ylabel("Energy (eV)")
plt.title("Quantum Tunneling: Potential Barrier"); plt.grid(True); plt.legend()
plt.tight_layout(); plt.savefig(RESULTS/"potential_barrier.png", dpi=180); plt.close()

plt.figure(figsize=(9, 5)); plt.plot(widths, [d["transmission_percent"] for d in width_data])
plt.xlabel("Barrier width (nm)"); plt.ylabel("Transmission probability (%)")
plt.title("Transmission Probability vs Barrier Width"); plt.grid(True)
plt.tight_layout(); plt.savefig(RESULTS/"transmission_vs_width.png", dpi=180); plt.close()

plt.figure(figsize=(9, 5)); plt.plot(energies, [d["transmission_percent"] for d in energy_data])
plt.xlabel("Particle energy (eV)"); plt.ylabel("Transmission probability (%)")
plt.title("Transmission Probability vs Particle Energy"); plt.grid(True)
plt.tight_layout(); plt.savefig(RESULTS/"transmission_vs_energy.png", dpi=180); plt.close()

print("Analysis complete. See results/ and data/.")
print(f"Transmission probability: {params['transmission_probability']:.6e}")
