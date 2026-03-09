import math
import csv

# Inputs
throat_radius = 0.012
exit_radius = 0.05
length = 0.5
num_points = 50

x_coords = []
y_coords = []

# Rao bell shape parameters
for i in range(num_points + 1):
    theta = i * math.pi / (2 * num_points)  # angle from throat to exit
    x = length * (theta / (math.pi / 2))    # linear x
    y = throat_radius + (exit_radius - throat_radius) * math.sin(theta)  # bell curve
    x_coords.append(x)
    y_coords.append(y)

# Save to CSV
with open("rao_nozzle_coords.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x", "y"])
    for xi, yi in zip(x_coords, y_coords):
        writer.writerow([xi, yi])

print("Rao bell nozzle coordinates saved to rao_nozzle_coords.csv")