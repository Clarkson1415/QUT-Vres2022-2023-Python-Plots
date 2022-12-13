import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math


t = np.linspace(0, 2)
k = 3
M = 1
gamma_M = 1
delta = 1
M = 1

def dTdt(T, t):
    dTdt = (k*M*T)/(M+gamma_M) - delta*T
    return dTdt

T0 = 1
# for what M value do we have the sol decreasing
# M < (delta * gamma_m)/k-delta

M = (delta * gamma_M)/(k-delta) + 0.5
T = odeint(dTdt, T0, t)
plt.plot(t, T, label=f'M={M}')

M = (delta * gamma_M)/(k-delta)
T = odeint(dTdt, T0, t)
plt.plot(t, T, label=fr"$M=\frac{{\delta \gamma_m}}{{(k-\delta)}}$ ={M}")

M = (delta * gamma_M)/(k-delta)-0.5
T = odeint(dTdt, T0, t)
plt.plot(t, T, label=f'M={M}')

plt.legend()
plt.title('T(t) = T-cells over time')
plt.xlabel("'t', time")
plt.ylabel('T-Cells')
plt.show()