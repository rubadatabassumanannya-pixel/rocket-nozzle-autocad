import math
import csv

# --- Inputs ---
chamber_pressure = 3e6
chamber_temperature = 3500
gamma = 1.4
gas_constant = 287
throat_radius = 0.012
nozzle_length = 0.5
num_points = 50
ambient_pressure = 101325  # sea-level

# --- Optimization Loop ---
best_exit_radius = throat_radius
best_thrust = 0

for i in range(20, 101):  # 20 mm to 100 mm
    exit_radius = i / 1000  # convert mm to meters

    # Mass flow (same as before)
    mass_flow = (chamber_pressure * math.pi * throat_radius**2) / ( (chamber_temperature * gas_constant) ** 0.5 ) * (gamma ** 0.5)

    # Exit velocity (simple estimate with exit pressure)
    pe_pc_ratio = (ambient_pressure / chamber_pressure)
    exit_velocity = (2 * gamma / (gamma - 1) * gas_constant * chamber_temperature * (1 - pe_pc_ratio**((gamma - 1)/gamma))) ** 0.5

    # Thrust
    thrust = mass_flow * exit_velocity

    if thrust > best_thrust:
        best_thrust = thrust
        best_exit_radius = exit_radius

print(f"Optimal Exit Radius: {best_exit_radius:.3f} m")
print(f"Maximum Estimated Thrust: {best_thrust:.2f} N")

# --- Generate CSV for Optimal Nozzle ---
x_coords = []
y_coords = []

for i in range(num_points + 1):
    theta = i * math.pi / (2 * num_points)
    x = nozzle_length * (theta / (math.pi / 2))
    y = throat_radius + (best_exit_radius - throat_radius) * math.sin(theta)
    x_coords.append(x)
    y_coords.append(y)

with open("nexnoz_opt_coords.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x", "y"])
    for xi, yi in zip(x_coords, y_coords):
        writer.writerow([xi, yi])

print("Optimal Rao bell nozzle coordinates saved to nexnoz_opt_coords.csv")

# --- Wall Thickness Estimation ---
sigma = 503e6        # Pa (Aluminum 7075-T6)
safety_factor = 2

wall_thickness = []
for radius in y_coords:
    t = (chamber_pressure * radius) / (sigma * safety_factor)
    wall_thickness.append(t)

# Save thickness with coordinates
with open("nexnoz_opt_coords_wall.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x", "y", "wall_thickness"])
    for xi, yi, ti in zip(x_coords, y_coords, wall_thickness):
        writer.writerow([xi, yi, ti])

print("Nozzle coordinates with wall thickness saved to nexnoz_opt_coords_wall.csv")

# --- Material Database ---
materials = {
    "Aluminum 7075-T6": 503e6,  # Pa
    "Titanium Ti-6Al-4V": 880e6,
    "Inconel 718": 1240e6
}

safety_factor = 2

for material, sigma in materials.items():
    wall_thickness_mat = []
    for radius in y_coords:
        t = (chamber_pressure * radius) / (sigma * safety_factor)
        wall_thickness_mat.append(t)
    
    filename = f"nexnoz_{material.replace(' ', '_')}_wall.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["x", "y", "wall_thickness"])
        for xi, yi, ti in zip(x_coords, y_coords, wall_thickness_mat):
            writer.writerow([xi, yi, ti])
    
    print(f"Nozzle wall thickness saved for {material} → {filename}")