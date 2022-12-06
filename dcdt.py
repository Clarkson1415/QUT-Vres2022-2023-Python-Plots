import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

# plot of DE
k = 1
r = 1

C = np.linspace(0,20)
dCdt = r*C*(1-(C/k))
plt.plot(C, dCdt)
plt.legend()
plt.title(r'$\frac{dC}{dt} = rC(1-\frac{C}{K}) $')
plt.xlabel('C')
plt.ylabel('dCdt')
plt.show()


# plot of sol

def dCdt(C, t):
    k = 1
    r = 1
    dCdt = r*C*(1-(C/k))
    return dCdt

t = np.linspace(0,2)

# plot sol
for C0 in range(5): # for diff inital conditions of T cells
    C = odeint(dCdt, C0, t)
    plt.plot(t, C, label=f'C0={C0}')
    plt.title('C(t)')
    plt.xlabel('t')
    plt.legend()
plt.show()