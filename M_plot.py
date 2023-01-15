import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import Eulers

def Mt_sol():

    M0 = 1
    K = 1
    Lambda = 0
    phi = 1
    T = 1
    # M = solution plot
    def dMdt(M, t):
        dMdt = (Lambda*M*(1-(M/K))) - (phi*M*T)
        return dMdt


    # eulers for M solution
    # y[n+1] = y[n] + delta_t*f(y[n])
    h = 0.1
    tf = 10
    t = np.arange(0, tf+h, h) #start, stop, step
    n = len(t)

    Mt = np.ones(n)
    Tt = np.ones(n)

    for i in range(1, n):
        Mt[i] = Mt[i-1] + h * (Lambda*Mt[i-1]*(1-(Mt[i-1]/K)) - (phi*Mt[i-1]*Tt[i-1]))


    c_1 = (np.log(M0) - np.log(Lambda*M0 - K*(Lambda - T*phi))) / (Lambda-T*phi)
    the_solution = (K*(Lambda - T*phi)*np.exp(Lambda*(t+c_1)))/(-np.exp(T*phi*(t+c_1))+Lambda*np.exp(Lambda*(t+c_1)))

    c2 = np.log(np.abs(M0 / (K*Lambda - M0*Lambda - K*T*phi))) / (Lambda-T*phi)
    mysol = (np.exp((t+c2)*(Lambda-T*phi))*(Lambda-T*phi)*(K*(Lambda-T*phi)))/(1+Lambda*np.exp((t+c2)*(Lambda-T*phi)))


    M = odeint(dMdt, y0=M0, t=t)
    plt.plot(t, M, label=f'ODE solver', linewidth=6)
    #plt.plot(t, the_solution, label=r"$M = \frac{K(\lambda - T \phi)e^{\lambda(t+c_1)}} {-e^{T\phi(tc_1)} + \lambda e^{\lambda(t+c_1)}}$")
    plt.plot(t, Mt, label='Eulers')
    plt.legend(fontsize=20)
    plt.show()

