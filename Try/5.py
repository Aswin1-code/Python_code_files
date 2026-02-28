import numpy as np
import matplotlib.pyplot as plt

def rc_charging_response(R, C, V, time_duration):
    """
    Analyze and plot the transient response of an RC charging circuit.
    
    Parameters:
    R (float): Resistance in ohms
    C (float): Capacitance in farads
    V (float): Supply voltage in volts
    time_duration (float): Total time duration for the simulation in seconds
    """
    # Time constant (tau = R * C)
    tau = R * C

    # Generate time points
    t = np.linspace(0, time_duration, 1000)

    # Calculate capacitor voltage over time (Vc = V * (1 - exp(-t / tau)))
    vc = V * (1 - np.exp(-t / tau))

    # Plot the response
    plt.figure(figsize=(8, 6))
    plt.plot(t, vc, label=f"R={R}Ω, C={C}F, τ={tau:.2f}s")
    plt.title("RC Charging Circuit: Capacitor Voltage vs Time", fontsize=14)
    plt.xlabel("Time (s)", fontsize=12)
    plt.ylabel("Capacitor Voltage (V)", fontsize=12)
    plt.grid(True)
    plt.legend()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Parameters for the RC circuit
    R = 1000  # Resistance in ohms
    C = 0.001  # Capacitance in farads
    V = 5  # Supply voltage in volts
    time_duration = 5  # Total time duration in seconds

    # Plot the transient response
    rc_charging_response(R, C, V, time_duration)

    # Analyze the effect of changing R or C
    print("Analyzing the effect of changing R or C...")
    rc_charging_response(2000, C, V, time_duration)  # Doubling R
    rc_charging_response(R, 0.002, V, time_duration)  # Doubling C