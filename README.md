QUANTUM TUNNELING PROBLEM SOLVER
1. Project Information
DetailsInformationProject TitleQuantum Tunneling Problem SolverStudent NameRAHUL KISHORE MRoll NumberRA2411019010102DepartmentAerospace EngineeringInstitutionSRM Institute of Science and Technology, KattankulathurCoursePython Programming
2. Abstract
The Quantum Tunneling Problem Solver is a Python-based simulation project developed to demonstrate the phenomenon of quantum tunneling through a rectangular potential barrier.
In classical mechanics, a particle cannot cross a potential barrier when its energy is lower than the barrier height. However, according to quantum mechanics, a particle has a finite probability of penetrating and passing through the barrier. This phenomenon is known as quantum tunneling.
This project uses Python libraries such as NumPy and Matplotlib to calculate transmission probability, reflection probability, wave number and decay constant. It also generates graphical visualizations to demonstrate the effect of particle energy and barrier width on quantum tunneling probability.
The project provides a computational understanding of quantum mechanical behaviour through numerical calculations and graphical analysis.
3. Problem Statement
To develop a Python-based simulation program that calculates and visualizes the quantum tunneling probability of a particle passing through a one-dimensional rectangular potential barrier.
The program evaluates the particle's energy, mass, barrier height and barrier width to determine the approximate transmission and reflection probabilities.
4. Objectives
• To understand the fundamental concept of quantum tunneling.
• To calculate the wave number and decay constant.
• To determine transmission and reflection probabilities.
• To visualize the potential energy barrier.
• To plot the wavefunction and probability density.
• To study the variation of transmission probability with barrier width.
• To investigate the effect of particle energy on tunneling probability.
• To implement scientific calculations using Python.
5. Introduction and Background
Quantum tunneling is an important phenomenon in quantum mechanics in which a particle passes through a potential energy barrier even when its energy is lower than the barrier height.
The phenomenon occurs because particles exhibit wave-like properties at the quantum scale.
In this project, a one-dimensional rectangular potential barrier is considered. The particle approaches the barrier with energy E, while the barrier has a potential height V₀.
For quantum tunneling to occur:
E < V₀
The decay constant inside the barrier is calculated using:
κ = √[2m(V₀ − E)] / ℏ
The wave number is:
k = √(2mE) / ℏ
The approximate transmission probability using the thick-barrier approximation is:
T ≈ e^(-2κa)
The reflection probability is calculated using:
R = 1 − T
Where:
• m = Mass of the particle
• E = Particle energy
• V₀ = Potential barrier height
• ℏ = Reduced Planck constant
• a = Barrier width
• κ = Decay constant
• k = Wave number
• T = Transmission probability
• R = Reflection probability
6. Methodology / Algorithm
The project follows the following algorithm:
1. Import the required Python libraries, NumPy and Matplotlib.
2. Define the physical constants such as Planck's reduced constant, electron mass and electronvolt conversion factor.
3. Select the particle type: electron, proton or custom particle.
4. Define the particle energy, barrier height and barrier width.
5. Convert energy and width into SI units.
6. Check whether the tunneling condition E < V₀ is satisfied.
7. Calculate the decay constant (κ).
8. Calculate the transmission probability (T).
9. Calculate the reflection probability (R).
10. Calculate the wave number (k).
11. Generate the position arrays and calculate the illustrative wavefunction.
12. Calculate the probability density.
13. Generate graphs using Matplotlib.
14. Display the calculated results and final interpretation.
7. Python Implementation and Programming Concepts Used
The project is implemented using Python programming.
Libraries Used
NumPy
Used for:
• Mathematical calculations.
• Square root operations.
• Exponential functions.
• Numerical arrays.
• Probability calculations.
Matplotlib
Used for:
• Plotting graphs.
• Visualizing the potential barrier.
• Displaying wavefunctions.
• Plotting probability density.
• Comparing transmission probability.
Python Programming Concepts
The following programming concepts are implemented:
1. Variables and constants.
2. Conditional statements (if, elif and else).
3. Mathematical expressions.
4. NumPy arrays.
5. Numerical computations.
6. Unit conversions.
7. Formatted output using f-strings.
8. Data visualization using Matplotlib.
8. Default Input Parameters
The following default values are used in the demonstration:
ParameterValueParticleElectronElectron Mass9.1093837 × 10⁻³¹ kgParticle Energy1.0 eVBarrier Height2.0 eVBarrier Width0.5 nmReduced Planck Constant1.054571817 × 10⁻³⁴ J·sNote: These values are predefined in the current notebook. The program displays the particle selection, but the demonstration parameters must be changed directly in the code to test other values.
9. Results and Data Visualizations
The program generates five graphical outputs.
9.1 Quantum Tunneling Potential Barrier
This graph represents the rectangular potential barrier and the particle energy level. It illustrates the condition in which particle energy is lower than the barrier height.
9.2 Quantum Wavefunction During Tunneling
This graph displays the real part of the illustrative wavefunction before, inside and after the potential barrier.
9.3 Quantum Probability Density
This graph represents the probability density |ψ|² of the particle along the position coordinate.
9.4 Transmission Probability vs Barrier Width
This graph demonstrates how transmission probability decreases exponentially as the barrier width increases.
9.5 Transmission Probability vs Particle Energy
This graph illustrates the increase in estimated transmission probability as particle energy approaches the barrier height from below.
The program also displays:
• Particle mass.
• Particle energy.
• Barrier height.
• Barrier width.
• Wave number.
• Decay constant.
• Transmission probability.
• Reflection probability.
• Final interpretation.
10. Discussion and Observations
From the simulation, the following observations can be made:
1. Quantum tunneling allows a particle to pass through a potential barrier even when its energy is below the barrier height.
2. Transmission probability decreases as barrier width increases.
3. Transmission probability increases as particle energy approaches the barrier height.
4. The reflection probability represents the remaining probability after accounting for transmission.
5. The graphical results help understand the relationship between particle properties and tunneling behaviour.
Model limitations:
The program uses the thick-barrier exponential approximation for transmission probability rather than the exact solution for a finite rectangular barrier. The plotted wavefunction is illustrative and is not a fully boundary-matched quantum-mechanical wavefunction. Therefore, the results are intended to demonstrate the physical trends and concepts.
11. Conclusion
The Quantum Tunneling Problem Solver successfully demonstrates the basic concept of quantum tunneling using Python programming.
The project calculates the approximate transmission and reflection probabilities and visualizes the behaviour of a particle interacting with a rectangular potential barrier.
Through this project, numerical computation, conditional statements, mathematical operations, NumPy arrays and graphical visualization techniques were applied.
The simulation provides a better understanding of quantum tunneling and demonstrates how Python can be used to solve and visualize scientific engineering problems.
12. Requirements
The following software and libraries are required:
• Python 3.9 or above.
• NumPy.
• Matplotlib.
• Jupyter Notebook / JupyterLab.
Install the required libraries using:
pip install numpy matplotlib jupyter
13. How to Execute the Project
Using Jupyter Notebook
1. Download or clone the GitHub repository.
2. Install Python on your computer.
3. Install the required libraries.
4. Open the project folder.
5. Launch Jupyter Notebook.
6. Open the project .ipynb file.
7. Run all cells sequentially.
8. Observe the calculated output and generated graphs.
Using Google Colab
1. Open Google Colab.
2. Upload the project notebook.
3. Execute all cells.
4. View the numerical results and graphical outputs.
14. Repository Structure
Quantum-Tunneling-Problem-Solver/
│
├── README.md
│
├── quantum_tunneling_solver.ipynb
│
├── requirements.txt
│
└── outputs/
    ├── potential_barrier.png
    ├── wavefunction.png
    ├── probability_density.png
    ├── transmission_vs_width.png
    └── transmission_vs_energy.png
Note: The output image files and requirements.txt are suggested additions. Save the generated graphs from the notebook before including them in the outputs folder. No external dataset is required.
15. References
1. Griffiths, D. J., Introduction to Quantum Mechanics, 2nd Edition, Pearson Prentice Hall, 2005.
2. Zettili, N., Quantum Mechanics: Concepts and Applications, 2nd Edition, Wiley, 2009.
3. NumPy Official Documentation: https://numpy.org/doc/
4. Matplotlib Official Documentation: https://matplotlib.org/stable/

Student Declaration
Name: RAHUL KISHORE M
Roll Number: RA2411019010102
Department: Aerospace Engineering
Project Title: Quantum Tunneling Problem Solver
Institution: SRM Institute of Science and Technology, Kattankulathur
Course: Python Programming
