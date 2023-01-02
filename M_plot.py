import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

M0 = 3
K = 2
Lambda = 5
phi = 1
T = 1
# M = solution plot
def dMdt(M, t):
    dMdt = Lambda*M*(1-(M/K)) - phi*M*T
    return dMdt


# x axis = time
t = np.linspace(0, 2)

# solution?
c = 1/(T*phi - Lambda) * np.log((K*(T*phi))/M0 + 1)
the_sol = (K*(Lambda - T*phi)*np.exp(Lambda*(t+c))) / (-np.exp(T*phi*(t+c)) + Lambda*np.exp(Lambda*(t+c)))

#c2 = 1/(Lambda - phi*T) * np.log((K*M0)/(Lambda-phi*T*K-M0*K))
#mysol = (K*np.exp((t+c2)*(Lambda-phi*T))*(Lambda - phi*T))/(K+Lambda*np.exp((t+c2)*(Lambda-phi*T)))

M = odeint(dMdt, M0, t)
plt.plot(t, M, label=f'sol ode', linewidth=6)
plt.plot(t, the_sol, label=r"$M(t)=\frac{K(\lambda - T\phi)e^{\lambda(t+c)}}{\lambda e^{\lambda(t+c)} - e^{T\phi(t+c)}}$")
plt.legend()
plt.title('M(t)')
plt.xlabel('t')
plt.show()