import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

K = 1
phi = 1.1
T = 0
Lambda = 2

M = np.linspace(0, 1)
for T in range(2):
    dmdt = (Lambda * M) - ((Lambda * M * M) / K) - (phi * M * T)
    plt.plot(M, dmdt, label=f'T={T}')
    #show that max pos roots has T < lambda/phi
    plt.legend()
    plt.title(r'$\frac{dM}{dt} = \lambda M(1-\frac{M}{K}) - \o{}MT$')
    plt.xlabel('M')
    plt.ylabel('dMdt')
plt.show()

