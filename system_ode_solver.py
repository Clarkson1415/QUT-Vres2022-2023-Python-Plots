
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def ode_solve_plot():
    # solve with ODE solver
    def odes(x, t):
        # constants
        M0 = 1
        K = 1
        Lambda = 0
        phi = 1
        k = 1
        M = 1
        gamma_M = 1
        delta = 1

        # assign each ode to a vector element
        M = x[0]
        T = x[1]

        # define ode
        dMdt =  (Lambda * M) - ((Lambda * M * M) / K) - (phi * M * T)
        dTdt = (k*M*T)/(M+gamma_M) - delta*T
        return [dMdt, dTdt]

    # initial conditions
    x0 = [1, 1] # [M(0) = 1, T(0) = 1] if they are 0 then the plot is flat

    # print(odes(x=x0, t=0))

    # declare time vector time window
    t = np.linspace(0, 10, 1000)
    x = odeint(odes, x0, t)

    # the results of the solved odes
    M = x[:, 0]
    T = x[:, 1]

    # plot
    plt.plot(t, M, label='M(t) ode solver')
    plt.plot(t, T, label='T(t) ode solver')
    plt.legend()



