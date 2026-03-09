import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,100)
mach = 1 + 3*(x**2)

plt.plot(x,mach)
plt.xlabel("Nozzle Length")
plt.ylabel("Mach Number")
plt.title("Mach Number Distribution in Rocket Nozzle")
plt.grid()

plt.savefig("mach_distribution.png", dpi=300)

plt.show()