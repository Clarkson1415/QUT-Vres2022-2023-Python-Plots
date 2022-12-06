import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

K = 1
O = 1.1
T = 0
Lambda = 1.4

M = np.linspace(0, 1)
for T in range(10):
    dmdt = (Lambda * M) - ((Lambda * M * M) / K) - (O * M * T)
    plt.plot(M, dmdt, label=f'T={T}')
    plt.legend()
    plt.title(r'$\frac{dM}{dt} = \lambda M(1-\frac{M}{K}) - \o{}MT$')
    plt.xlabel('M')
    plt.ylabel('dMdt')
plt.show()

# M = solution plot
def dMdt(M, t):
    K = 1
    O = 1
    Lambda = 1.4
    dMdt = (Lambda * M) - ((Lambda * M * M) / K) - (O * M * T)
    return dMdt


# x axis = time
t = np.linspace(0,2)

for T in range(5):
    M0 = 1
    M = odeint(dMdt, M0, t)
    plt.plot(t, M, label=f'T={T},M0={M0}')
    plt.legend()
    plt.title('M(t)')
    plt.xlabel("t")
    plt.ylabel("M(t)")
plt.show()

for M0 in range(5):
    T = 1
    M = odeint(dMdt, M0, t)
    plt.plot(t, M, label=f'T={T},M0={M0}')
    plt.legend()
    plt.title('M(t)')
    plt.xlabel('t')
plt.show()


T=100
M = odeint(dMdt, M0, t)
plt.plot(t, M, label=f'T={T}')
plt.legend()
plt.title('M(t)')
plt.xlabel('t')
plt.show()

