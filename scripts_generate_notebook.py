"""Generate the project analysis notebook."""
from pathlib import Path
import nbformat

ROOT = Path(__file__).resolve().parent
nb = nbformat.v4.new_notebook()
nb.cells = [
    nbformat.v4.new_markdown_cell("# Quantum Tunneling Problem Solver\n\nThick-barrier approximation; default case is an electron with E=1 eV, V0=2 eV, a=0.5 nm."),
    nbformat.v4.new_code_cell("import sys\nfrom pathlib import Path\nROOT = Path.cwd()\nsys.path.insert(0, str(ROOT / 'src'))\nfrom quantum_tunneling import solve_tunneling\nimport numpy as np\nimport matplotlib.pyplot as plt"),
    nbformat.v4.new_code_cell("result = solve_tunneling('Electron', 1.0, 2.0, 0.5)\nfor key, value in result.items(): print(f'{key}: {value}')"),
    nbformat.v4.new_code_cell("widths=np.linspace(0.1,5,200)\nvalues=[solve_tunneling(width_nm=float(w))['transmission_percent'] for w in widths]\nplt.plot(widths,values); plt.xlabel('Barrier width (nm)'); plt.ylabel('Transmission (%)'); plt.grid(); plt.show()"),
    nbformat.v4.new_code_cell("energies=np.linspace(0.1,1.98,200)\nvalues=[solve_tunneling(energy_eV=float(e))['transmission_percent'] for e in energies]\nplt.plot(energies,values); plt.xlabel('Particle energy (eV)'); plt.ylabel('Transmission (%)'); plt.grid(); plt.show()")
]
nb.metadata = {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}}
nbformat.write(nb, ROOT/"notebook"/"quantum_tunneling_analysis.ipynb")
print("Notebook generated.")
