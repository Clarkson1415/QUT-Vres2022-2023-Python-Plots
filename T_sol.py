import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math


# plot of sol
k = 2
M = 1
gamma_M = 1
delta = 1
T = np.linspace(0,20)
def dTdt(T, t):
    k = 2
    M = 1
    gamma_M = 1
    delta = 1
    dTdt = (k*M*T)/(M+gamma_M) - delta*T
    return dTdt

t = np.linspace(0,2)


# The sol vs my sol matches on top
T0 = 1
delta = 1
gamma_M = 1

M = 1
c = math.log(T0) / (k*M / (M+gamma_M)-delta)
my_sol = np.exp((t+c)*(k*M/(M+gamma_M) - delta))

T = odeint(dTdt, T0, t)
plt.plot(t, T, label=f'T=ODE solver')
plt.plot(t, my_sol, label=r"$T=e^{((t+c)(kM/(M+\gamma_M)-\delta))}$")
plt.legend()
plt.title('T(t) = T-cells over time')
plt.xlabel("'t', time")
plt.ylabel('T-Cells')
plt.show()

# for what M value do we have the sol decreasing
# M < (delta * gamma_m)/k-delta

M = (delta * gamma_M)/(k-delta)
T0 = 1
delta = 1
gamma_M = 1
k = 1
c = math.log(T0) / (k*M / (M+gamma_M)-delta)
my_sol = np.exp((t+c)*(k*M/(M+gamma_M) - delta))
plt.plot(t, my_sol, label=r"$T=e^{((t+c)(kM/(M+\gamma_M)-\delta))}$")
plt.legend()
plt.title('T(t) = T-cells over time')
plt.xlabel("'t', time")
plt.ylabel('T-Cells')
plt.show()