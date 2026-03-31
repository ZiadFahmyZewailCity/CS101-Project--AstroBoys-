import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def gravitational_force(state, t, masses):
    G = 6.67430e-11

    # Unpack state vector
    num_bodies = len(masses)
    positions = state[:num_bodies*3].reshape((num_bodies, 3))
    velocities = state[num_bodies*3:].reshape((num_bodies, 3))

    # Initialize accelerations
    accelerations = np.zeros_like(positions)

    for i in range(num_bodies):
        for j in range(num_bodies):
            if i != j:
                r = positions[j] - positions[i]
                r_magnitude = np.linalg.norm(r)
                force_magnitude = G * masses[i] * masses[j] / r_magnitude**2
                force_direction = r / r_magnitude
                accelerations[i] += force_magnitude / masses[i] * force_direction

    # Flatten accelerations for odeint
    return np.concatenate((velocities.flatten(), accelerations.flatten()))

def simulate_trajectory(masses, initial_positions, initial_velocities, t):
    initial_state = np.concatenate((initial_positions.flatten(), initial_velocities.flatten()))
    args = (masses,)
    states = odeint(gravitational_force, initial_state, t, args=args)
    return states

def plot_trajectory(states, num_bodies):
    positions = states[:, :num_bodies*3].reshape((-1, num_bodies, 3))

    for i in range(num_bodies):
        x = positions[:, i, 0]
        y = positions[:, i, 1]
        z = positions[:, i, 2]
        plt.plot(x, y, label=f'Body {i+1}')

    plt.title('Celestial Bodies Trajectory')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()

def on_simulate_button_click():
    masses = [float(mass.get()) for mass in mass_entries]
    initial_positions = np.array([[float(entry.get()) for entry in row] for row in position_entries])
    initial_velocities = np.array([[float(entry.get()) for entry in row] for row in velocity_entries])
    t = np.linspace(0, float(time_entry.get()), 1000)

    states = simulate_trajectory(masses, initial_positions, initial_velocities, t)

    num_bodies = len(masses)
    plt.figure()
    plot_trajectory(states, num_bodies)
    canvas.draw()

# Create Tkinter GUI
root = tk.Tk()
root.title("Celestial Bodies Trajectory Simulator")

# Create input fields for masses
mass_entries = []
mass_label = tk.Label(root, text="Masses:")
mass_label.grid(row=0, column=0, padx=10, pady=5)
for i in range(3):
    entry = tk.Entry(root, width=10)
    entry.grid(row=0, column=i+1, padx=5, pady=5)
    mass_entries.append(entry)

# Create input fields for initial positions
position_entries = []
position_label = tk.Label(root, text="Initial Positions:")
position_label.grid(row=1, column=0, padx=10, pady=5)
for i in range(3):
    row_entries = []
    for j in range(3):
        entry = tk.Entry(root, width=10)
        entry.grid(row=1+i, column=j+1, padx=5, pady=5)
        row_entries.append(entry)
    position_entries.append(row_entries)

# Create input fields for initial velocities
velocity_entries = []
velocity_label = tk.Label(root, text="Initial Velocities:")
velocity_label.grid(row=4, column=0, padx=10, pady=5)
for i in range(3):
    row_entries = []
    for j in range(3):
        entry = tk.Entry(root, width=10)
        entry.grid(row=4+i, column=j+1, padx=5, pady=5)
        row_entries.append(entry)
    velocity_entries.append(row_entries)

# Create input field for simulation time
time_label = tk.Label(root, text="Simulation Time (s):")
time_label.grid(row=7, column=0, padx=10, pady=5)
time_entry = tk.Entry(root, width=10)
time_entry.grid(row=7, column=1, padx=5, pady=5)

# Create simulate button
simulate_button = tk.Button(root, text="Simulate", command=on_simulate_button_click)
simulate_button.grid(row=8, column=0, columnspan=4, pady=10)

# Create Matplotlib figure and canvas
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=4, rowspan=9, padx=10, pady=10)

root.mainloop()
