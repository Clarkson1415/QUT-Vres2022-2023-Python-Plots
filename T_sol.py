import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
import Eulers

def T_plot():
    # plot of sol
    k = 1
    M = 1
    gamma_M = 1
    delta = 1

    def dTdt(T, t):
        dTdt = (k*M*T)/(M+gamma_M) - delta*T
        return dTdt

    # eulers
    # y[n+1] = y[n] + delta_t*f(y[n])
    h = 0.1
    tf = 10
    t = np.arange(0, tf+h, h) #start, stop, step
    n = len(t)
    Tt = np.ones(n)

    for i in range(1, n):
        Tt[i] = Tt[i-1] + h * ((k*M*Tt[i-1])/(M+gamma_M) - delta*Tt[i-1])

    # The sol vs my sol matches on top
    T0 = 1
    c = math.log(T0) / (k*M / (M+gamma_M)-delta)
    my_sol = np.exp((t+c)*((k*M/(M+gamma_M)) - delta))


    T = odeint(dTdt, T0, t)
    plt.plot(t, T, label=f'T ODE solver, M={M}', linewidth=6)
    plt.plot(t, my_sol, label=r"$T=e^{(t+c)(\frac{kM}{M+\gamma_M} - \delta)}$ with M={M}")
    plt.plot(t, Tt, label=f'T(t) Eulers M={M}')
    # plt.title('T(t) = T-cells over time')
    # plt.xlabel("'t', time")
    # plt.ylabel('T-Cells')
    plt.legend()

T_plot()
plt.show()