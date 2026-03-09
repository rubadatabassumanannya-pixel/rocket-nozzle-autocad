# NexNoz Inline Plot Version
import matplotlib.pyplot as plt
import math
import csv

# --- Inputs ---
chamber_pressure = 3e6      # Pa
chamber_temperature = 3500  # K
gamma = 1.4
gas_constant = 287
throat_radius = 0.012
exit_radius = 0.05
nozzle_length = 0.5
num_points = 50

# --- Mass Flow Calculation ---
mass_flow = (chamber_pressure * math.pi * throat_radius**2) / ( (chamber_temperature * gas_constant) ** 0.5 ) * (gamma ** 0.5)

# --- Exit Velocity ---
exit_velocity = (2 * gamma / (gamma - 1) * gas_constant * chamber_temperature * (1 - (0.1)**((gamma - 1)/gamma))) ** 0.5

# --- Thrust ---
thrust = mass_flow * exit_velocity

print(f"Mass Flow Rate: {mass_flow:.2f} kg/s")
print(f"Exit Velocity: {exit_velocity:.2f} m/s")
print(f"Estimated Thrust: {thrust:.2f} N")

# --- Rao Bell Nozzle Coordinates ---
x_coords = []
y_coords = []

for i in range(num_points + 1):
    theta = i * math.pi / (2 * num_points)
    x = nozzle_length * (theta / (math.pi / 2))
    y = throat_radius + (exit_radius - throat_radius) * math.sin(theta)
    x_coords.append(x)
    y_coords.append(y)

# --- Save CSV ---
with open("nexnoz_coords.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x", "y"])
    for xi, yi in zip(x_coords, y_coords):
        writer.writerow([xi, yi])

# --- Inline Plot (VS Code Friendly) ---
plt.figure(figsize=(6,3))
plt.plot(x_coords, y_coords, label="Rao Bell Nozzle", color='red')
plt.fill_between(x_coords, 0, y_coords, color='lightgrey')
plt.title("Rao Bell Nozzle Shape")
plt.xlabel("Length (m)")
plt.ylabel("Radius (m)")
plt.legend()
plt.grid(True)
plt.show()

