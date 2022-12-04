import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

K = 1
O = 1.1
T = 0
Lambda = 1.4

M = np.linspace(0, 1)
for T in range(10): # for = 0, 1, 2
    dmdt = (Lambda * M) - ((Lambda * M * M) / K) - (O * M * T)
    plt.plot(M, dmdt, label=f'T={T}')
    plt.legend()
    plt.title('dMdt')
plt.show()

# M = solution plot
def dMdt(M, t):
    K = 1
    O = 1
    Lambda = 1.4
    dMdt = (Lambda * M) - ((Lambda * M * M) / K) - (O * M * T)
    return dMdt


# initial condition
# M0 = 1

# x axis time
t = np.linspace(0,2)

# solve ode
#M = odeint(dMdt, M0, t)

# plot
for T in range(5):
    M0 = 1
    M = odeint(dMdt, M0, t)
    plt.plot(t, M, label=f'T={T},M0={M0}')
    plt.legend()
    plt.title('M(t)')
plt.show()

for M0 in range(5):
    T = 1
    M = odeint(dMdt, M0, t)
    plt.plot(t, M, label=f'T={T},M0={M0}')
    plt.legend()
    plt.title('M(t)')
plt.show()


T=100
M = odeint(dMdt, M0, t)
plt.plot(t, M, label=f'T={T}')
plt.legend()
plt.title('M(t)')
plt.show()
