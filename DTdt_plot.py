import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

# plot of DE
k = 1
M = 1
gamma_M = 1
delta = 1
M = 1

T = np.linspace(0,20)
for M in range(5):
    dTdt = (k * M * T) / (M + gamma_M) - delta * T
    plt.plot(T, dTdt, label=f'M={M}')
    plt.legend()
    plt.title(r'$\frac{dT}{dt} = \frac{kMT}{M + \gamma_M} - \delta T $')
    plt.xlabel('T')
    plt.ylabel(r'$\frac{dT}{dt}$')
plt.show()


# plot of sol
M = 1
def dTdt(T, t):
    dTdt = (k*M*T)/(M+gamma_M) - delta*T
    return dTdt

t = np.linspace(0,2)
# plot
for T0 in range(5): # for diff inital conditions of T cells
    T = odeint(dTdt, T0, t)
    plt.plot(t, T, label=f'M={M},T0={T0}')
    plt.legend()
    plt.title('T(t) = T-cells over time')
    plt.xlabel("'t', time")
    plt.ylabel('T-Cells')
plt.show()

# plot dTdt vs T with different

#The sol vs my sol
T0 = 1
delta = 1
gamma_M = 1
k = 1
M = 1


T = odeint(dTdt, T0, t)
plt.plot(t, T, label=f'M={M},T0={T0}')
my_sol = np.exp(t+1)
plt.legend()
plt.title('T(t) = T-cells over time')
plt.xlabel("'t', time")
plt.ylabel('T-Cells')
plt.show()