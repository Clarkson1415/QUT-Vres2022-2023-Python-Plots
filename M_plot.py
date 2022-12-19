import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

M0 = 1
K = 2
Lambda = 1
phi = 1
T = 1
# M = solution plot
def dMdt(M, t):
    dMdt = (Lambda * M) - ((Lambda * M * M) / K) - (phi * M * T)
    return dMdt


# x axis = time
t = np.linspace(0,2)

# solution

c = 1/Lambda * np.log(abs(M0/(Lambda*(M0-K))))
My_sol = (K*(Lambda - T*phi)*np.exp((Lambda*(t+c)))) / (Lambda*np.exp((Lambda*(t+c))) - np.exp((T*phi*(t+c))))

M = odeint(dMdt, M0, t)
plt.plot(t, M, label=f'sol ode', linewidth=6)
plt.plot(t, My_sol, label=r"$M(t)=\frac{K(\lambda - T\phi)e^{\lambda(t+c)}}{\lambda e^{\lambda(t+c)} - e^{T\phi(t+c)}}$")
plt.legend()
plt.title('M(t)')
plt.xlabel('t')
plt.show()

