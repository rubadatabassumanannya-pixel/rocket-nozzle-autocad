# NexNoz - Rocket Nozzle Pre-optimizer
# Day 1 - Understanding Variables

chamber_pressure = 3000000      # in pascles
chamber_temperature = 3500      # in kelvin
gamma = 1.4
gas_constant = 287              # J/kgK (example vale)
throat_area = 0.0005            # in square meters

print("Chamber Pressure:", chamber_pressure)
print("Chamber Temperature:", chamber_temperature)
print("gamma:", gamma)
print("Gas Constant:", gas_constant)
print("Throat Area:", throat_area)
print("Pressure divided by temperature:", chamber_pressure / chamber_temperature)

# Baic Math Operations
Pressure_times_area = chamber_pressure * throat_area
Velocity_estimated = (2 * chamber_pressure * gas_constant * chamber_temperature) ** 0.5

print("Pressure times Area:", Pressure_times_area)
print("Estimated Velocity:", Velocity_estimated)

# Simple Mass Flow Estimate
mass_flow_rate = (chamber_pressure * throat_area / (gas_constant * chamber_temperature) ** 0.5)
print(" Estimated Mass Flow Rate:", mass_flow_rate)

#Improved Mass Flow Calculation
mass_flow_real = (chamber_pressure * throat_area / (gas_constant * chamber_temperature) **0.5)
print("Realistic Mass Flow Rate:", mass_flow_real)

#Simple Exit Velocity Estimate
exit_velocity = (2 * chamber_pressure * gas_constant * chamber_temperature) **0.5
print("Estimated Exit Velocity:", exit_velocity)

#First Thrust Estimated
Thrust = mass_flow_real * exit_velocity
print("Estimated Thrust:", Thrust)

# Simple conical nozzle generator
import math
import csv

length = 0.5          # nozzle length in meters
throat_radius = 0.012  # meters
exit_radius = 0.05     # meters
num_points = 20

x_coords = []
y_coords = []

for i in range(num_points + 1):
    x = i * (length / num_points)
    y = throat_radius + i * ((exit_radius - throat_radius) / num_points)
    x_coords.append(x)
    y_coords.append(y)

# Save to CSV
with open("nozzle_coords.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x", "y"])
    for xi, yi in zip(x_coords, y_coords):
        writer.writerow([xi, yi])

print("Nozzle coordinates saved to nozzle_coords.csv")