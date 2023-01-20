import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

M0 = 1
T0 = 1
K = 1
Lambda = 0.1
phi = 0.5
k = 1.5  # rho later
M = 1
gamma_M = 0.01
delta = 1
h = 0.01 # stepsize
tf = 10 # final
t = np.arange(0, tf+h, h) #start, stop, step


def eulers_approx_both(M0, T0, K, Lambda, phi, k, M, gamma_M, delta, t, tf, h):

    #Euler sol for M(t) over t using both equations

    n = len(t)

    Mt = np.ones(n)
    Tt = np.ones(n)

    for i in range(1, n):
        Mt[i] = Mt[i-1] + h * (Lambda*Mt[i-1]*(1-(Mt[i-1]/K)) - (phi*Mt[i-1]*Tt[i-1]))
        Tt[i] = Tt[i-1] + h * ((k*Mt[i-1]*Tt[i-1])/(Mt[i-1]+gamma_M) - delta*Tt[i-1])


    # alg
    #c_1 = (np.log(M0) - np.log(Lambda*M0 - K*(Lambda - T*phi))) / (Lambda-T*phi)
    #algebraic_solution = (K*(Lambda - T*phi)*np.exp(Lambda*(t+c_1)))/(-np.exp(T*phi*(t+c_1))+Lambda*np.exp(Lambda*(t+c_1)))

    #plot

    plt.plot(t, Mt, label='M(t) eulers')
    plt.plot(t, Tt, label='T(t) eulers')
    #plt.plot(t, algebraic_solution, label=r"$\frac{e^{(t+c1)(\lambda-T \phi))}(\lambda-T*phi)(K (\lambda-T*\phi))}{1+\lambda e^{(t+c1) (\lambda- T \phi)}}$")
    plt.legend()
    plt.title('')


# eulers_approx_both(M0, T0, K, Lambda, phi, k, M, gamma_M, delta)
# plt.show()
