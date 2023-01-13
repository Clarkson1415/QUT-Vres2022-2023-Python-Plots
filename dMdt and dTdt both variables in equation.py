import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import Eulers

k = 1
M = 1
gamma_M = 1
delta = 1

M0 = 1
K = 1
Lambda = 0
phi = 1
T = 1

def dTdt(T, t):
    dTdt = (k*M*T)/(M+gamma_M) - delta*T
    return dTdt


def dMdt(M, t):
    dMdt = Lambda*M*(1-(M/K)) - (phi*M*T)
    return dMdt


# eulers for M solution
# y[n+1] = y[n] + delta_t*f(y[n])
h = 0.05
tf = 10
t = np.arange(0, tf+0.01, h) #start, stop, step
n = len(t)

Mt = np.ones(n)
Tt = np.ones(n)

for i in range(1, n):
    Mt[i] = Mt[i-1] + h * (Lambda*Mt[i-1]*(1-(Mt[i-1]/K)) - (phi*Mt[i-1]*Tt[i-1]))
    Tt[i] = Tt[i-1] + h * ((k*Mt[i-1]*Tt[i-1])/(Mt[i-1]+gamma_M) - delta*Tt[i-1])


c_1 = (np.log(M0) - np.log(Lambda*M0 - K*(Lambda - T*phi))) / (Lambda-T*phi)
algebraic_solution = (K*(Lambda - T*phi)*np.exp(Lambda*(t+c_1)))/(-np.exp(T*phi*(t+c_1))+Lambda*np.exp(Lambda*(t+c_1)))

M = odeint(dMdt, M0, t)
plt.plot(t, M, label=f'sol ode', linewidth=6)
plt.plot(t, Mt, label='M(t) eulers')
plt.plot(t, Tt, label='T eulers')
plt.plot(t, algebraic_solution, label=r"$\frac{e^{(t+c1)(\lambda-T \phi))}(\lambda-T*phi)(K (\lambda-T*\phi))}{1+\lambda e^{(t+c1) (\lambda- T \phi)}}$")
plt.legend()
plt.title('')
plt.show()
