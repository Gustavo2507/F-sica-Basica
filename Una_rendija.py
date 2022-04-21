"""
Intesidad de una onda en una sola rendija
"""

import numpy as np
import matplotlib.pyplot as plt


lamnda = 650e-9
a = 3.5e-6

k = a/lamnda


theta = np.arange(-100,100,0.001)*np.pi/180

phi = (np.pi*k)*np.sin(theta)

I_I_max = ((np.sin(phi))/(phi))**2


# Grafica
plt.plot(theta, I_I_max)
plt.xlabel(r'ang($\theta$)')
plt.ylabel('I/Imax')
plt.grid()