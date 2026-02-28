import numpy as np

def mesh_analysis(resistances, voltages):
    """
    Perform mesh analysis to calculate loop currents in a DC circuit.
    
    Parameters:
    resistances (2D list): A square matrix representing the resistances in the circuit.
    voltages (list): A list representing the voltage sources in each mesh.
    
    Returns:
    currents (list): A list of loop currents in amperes.
    """
    # Convert resistances and voltages to numpy arrays
    R = np.array(resistances)
    V = np.array(voltages)

    # Solve the system of linear equations (R * I = V) for I
    currents = np.linalg.solve(R, V)
    return currents

# Example usage
if __name__ == "__main__":
    # Define the circuit parameters
    # Resistances matrix (in ohms)
    # Each row corresponds to the coefficients of the mesh equations
    resistances = [
        [10, -5, 0],   # Mesh 1 equation
        [-5, 15, -10], # Mesh 2 equation
        [0, -10, 20]   # Mesh 3 equation
    ]

    # Voltage sources (in volts)
    # Each value corresponds to the net voltage in each mesh
    voltages = [10, 0, 20]

    # Perform mesh analysis
    currents = mesh_analysis(resistances, voltages)

    # Display the results
    print("Loop Currents (in amperes):")
    for i, current in enumerate(currents, start=1):
        print(f"I{i}: {current:.2f} A")