import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import Eulers

M0 = 1
K = 1
Lambda = 0
phi = 1
T = 1
# M = solution plot
def dMdt(M, t):
    dMdt = Lambda*M*(1-(M/K)) - (phi*M*T)
    return dMdt

# x axis = time
t = np.linspace(0, 2)

# solution?
#c = 1/(T*phi - Lambda) * np.log((K*(T*phi))/M0 + 1)
#the_sol = (K*(Lambda - T*phi)*np.exp(Lambda*(t+c))) / (-np.exp(T*phi*(t+c)) + Lambda*np.exp(Lambda*(t+c)))

c_1 = -np.log(Lambda - K*(Lambda - T*phi))/(Lambda-T*phi)
the_sol_wolf = (K*(Lambda - T*phi)*np.exp(Lambda*(t+c_1)))/(-np.exp(T*phi*(t+c_1))+Lambda*np.exp(Lambda*(t+c_1)))
#another = -K*np.exp(Lambda*(t+c_1))*(Lambda-T*phi) / (np.exp(T*phi*(c_1+t) - Lambda * np.exp(Lambda*(t+c_1))))

c2 = np.log(np.abs(Lambda*(K-1)-K*T*phi)) / (T*phi - Lambda)
mysol = (np.exp((t+c2)*(Lambda-T*phi))*(Lambda-T*phi)*(K*(Lambda-T*phi)))/(1+Lambda*np.exp((t+c2)*(Lambda-T*phi)))

M = odeint(dMdt, M0, t)
plt.plot(t, M, label=f'sol ode', linewidth=6)
plt.plot(t, the_sol_wolf, label=r"wolfram")
plt.plot(t, mysol, label=r"mysol")
plt.legend()
plt.title('M(t)')
plt.xlabel('t')
# plot with eulers method approx, euler(x0, y0, xn, steps)
Eulers.euler(dMdt, 0,1,2,100)
plt.show()
