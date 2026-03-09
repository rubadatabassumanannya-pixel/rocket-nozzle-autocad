import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,100)
y = 0.2 + 0.8*(x**1.5)

plt.plot(x,y)
plt.xlabel("Nozzle Length")
plt.ylabel("Radius")
plt.title("Rocket Nozzle Profile")
plt.grid()

plt.savefig("python_nozzle_plot.png", dpi=300)

plt.show()