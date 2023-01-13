import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import Eulers

M0 = 1
K = 1
Lambda = 0.5
phi = 1
T = 1
# M = solution plot
def dMdt(M, t):
    dMdt = (Lambda*M*(1-(M/K))) - (phi*M*T)
    return dMdt

# x axis = time
t = np.linspace(0, 2)

c_1 = (np.log(M0) - np.log(Lambda*M0 - K*(Lambda - T*phi))) / (Lambda-T*phi)
the_solution = (K*(Lambda - T*phi)*np.exp(Lambda*(t+c_1)))/(-np.exp(T*phi*(t+c_1))+Lambda*np.exp(Lambda*(t+c_1)))

c2 = np.log(np.abs(M0 / (K*Lambda - M0*Lambda - K*T*phi))) / (Lambda-T*phi)
mysol = (np.exp((t+c2)*(Lambda-T*phi))*(Lambda-T*phi)*(K*(Lambda-T*phi)))/(1+Lambda*np.exp((t+c2)*(Lambda-T*phi)))

M = odeint(dMdt, y0=M0, t=t)
plt.plot(t, M, label=f'sol ode', linewidth=6)
plt.plot(t, the_solution, label=r"the_solution")
#plt.plot(t, mysol, label=r"mysol")
Eulers.euler(dMdt, 0, 1, 2, 50)
plt.show()
