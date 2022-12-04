import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

K = 1
O = 1.1
T = 0
Lambda = 1.4

M = np.linspace(0, 1)

for T in range(3): # for = 0, 1, 2
    dmdt = (Lambda * M) - ((Lambda * M * M) / K) - (O * M * T)
    plt.plot(M, dmdt, 'b-', label=f'T={T}')
    plt.legend()
plt.show()

# M plot of solution ODE int solver python to check same as M_plot
dmdt = (Lambda*M) - ((Lambda*M*M)/K) - (O*M*T)
