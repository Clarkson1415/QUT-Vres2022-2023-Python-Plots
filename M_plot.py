import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

K = 1
phi = 1.1
T = 0
Lambda = 2


# M = solution plot
def dMdt(M, t):
    K = 1
    phi = 1
    Lambda = 2
    dMdt = (Lambda * M) - ((Lambda * M * M) / K) - (phi * M * T)
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
    My_sol = (K*phi*T/Lambda + K) / -2 + math.sqrt((-K*phi*T / Lambda - K) ^ 2 + 4*math.exp(t + c)(Lambda - T*phi)) / -2
    plt.plot(t, M, label=f'T={T},M0={M0}')
    plt.plot(t, My_sol, label='mine')
    plt.legend()
    plt.title('M(t)')
    plt.xlabel('t')
plt.show()

# solution
M0 = 1
T = 100
M = odeint(dMdt, M0, t)
plt.plot(t, M, label=f'T={T}')
plt.legend()
plt.title('M(t)')
plt.xlabel('t')
plt.show()

