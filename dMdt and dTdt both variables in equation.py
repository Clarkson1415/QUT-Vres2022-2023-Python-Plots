import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import Eulers

k = 3
M = 1
gamma_M = 1
delta = 1
def dTdt(T, t):
    dTdt = (k*M*T)/(M+gamma_M) - delta*T
    return dTdt

M0 = 1
K = 1
Lambda = 0
phi = 1
T = 1
T0 = 1

# x axis = time
t = np.linspace(0, 2)

# T = odeint(dTdt, T0, t)

def dMdt(M, t):
    dMdt = Lambda*M*(1-(M/K)) - (phi*M*T)
    return dMdt

c1 = -np.log(Lambda - K*(Lambda - T*phi))/(Lambda-T*phi)

mysol = (np.exp((t+c1)*(Lambda-T*phi))*(Lambda-T*phi)*(K*(Lambda-T*phi)))/(1+Lambda*np.exp((t+c1)*(Lambda-T*phi)))

M = odeint(dMdt, M0, t)
plt.plot(t, M, label=f'sol ode', linewidth=6)
plt.plot(t, mysol, label=r"mysol")
plt.legend()
plt.title('')
Eulers.euler(dMdt, 0, 1, 10, 100)

plt.show()
