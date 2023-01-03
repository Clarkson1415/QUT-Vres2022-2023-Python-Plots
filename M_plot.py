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
#
# M0 = 1
# K = 1
# Lambda = 1
# phi = 1
# T = 0
# #dMdt = (Lambda * M) - ((Lambda * M * M) / K) - (phi * M * T)
# dMdt = Lambda*M*(1 - (M/K)) - (phi*M*T)
# return dMdt
#
# # x axis = time
# t = np.linspace(0,2)
# # solution
# c = 1/Lambda * np.log(abs(M0/(Lambda*(M0-K))))
# My_sol = (K*(Lambda - T*phi)*np.exp((Lambda*(t+c)))) / (Lambda*np.exp((Lambda*(t+c))) - np.exp((T*phi*(t+c))))
#
# c2 = 1/(Lambda-phi*T) * np.log(abs(K*M0 / (K*(Lambda-phi*T)-Lambda*M0)))
# My_sol2 = (K*(Lambda-phi*T)*np.exp((t+c2)*(Lambda-phi*T))) / (K + Lambda * np.exp((t+c2)*(Lambda-phi*T)))
#
#
# M = odeint(dMdt, M0, t)
# plt.plot(t, M, label=f'ode solver', linewidth=6)
# plt.plot(t, My_sol, label=r"$M(t)=\frac{K(\lambda - T\phi)e^{\lambda(t+c)}}{\lambda e^{\lambda(t+c)} - e^{T\phi(t+c)}}$")
# plt.plot(t, My_sol2, label=r"$mine: M(t)=\frac{K(\lambda - T\phi)e^{\lambda(t+c)}}{\lambda e^{\lambda(t+c)} - e^{T\phi(t+c)}}$")
# >>>>>>> Stashed changes
# plt.legend()
# plt.title('M(t)')
# plt.xlabel('t')
# plot with eulers method approx, euler(x0, y0, xn, steps)
Eulers.euler(dMdt, 0,1,2,100)
plt.show()
