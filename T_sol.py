import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
import Eulers

# plot of sol
k = 3
M = 1
gamma_M = 1
delta = 1

t = np.linspace(0,20)
def dTdt(T, t):
    dTdt = (k*M*T)/(M+gamma_M) - delta*T
    return dTdt

# The sol vs my sol matches on top
T0 = 1
c = math.log(T0) / (k*M / (M+gamma_M)-delta)
my_sol = np.exp((t+c)*(k*M/(M+gamma_M) - delta))

T = odeint(dTdt, T0, t)
plt.plot(t, T, label=f'T=ODE solver', linewidth=6)
plt.plot(t, my_sol, label=r"$T=e^{((t+c)(kM/(M+\gamma_M)-\delta))}$")
plt.legend()
plt.title('T(t) = T-cells over time')
plt.xlabel("'t', time")
plt.ylabel('T-Cells')
# Eulers
Eulers.euler(dTdt, 0, T0, 20, 10)
plt.show()