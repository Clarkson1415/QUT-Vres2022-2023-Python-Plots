import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def f(s, t):
    a = 4
    b = 7
    n = s[0]
    c = s[1]
    # Dm dt equation of myelin
    #dndt = a * n - (c/(c+1)) * b * n

    dMdt = a*n - (c/(c+1)) * b * n

    #dcdt = (c/(c+1)) * n - c + 1
    return [dMdt]

t = np.linspace(0,20) # x axis

initial_conditions = [??, ??] # initial condition, can be a vector, i.e. if 2 equations dmdt and dsdt and 2 initial conditions y0 = [m0, s0]
# imma need to solve for C first then


s = odeint(f, M0, t) #integrate f over between s0 and t

plt.plot(t,s[:,0],'r--', linewidth=2.0)
plt.plot(t,s[:,1],'b-', linewidth=2.0)
plt.xlabel("t")
plt.ylabel("S[N,C]")
plt.legend(["N","C"])
plt.show()