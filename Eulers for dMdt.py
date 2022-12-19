import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

M0 = 2
K = 1
Lambda = 1
phi = 1
T = 1

def dMdt(M, t):
    dMdt = (Lambda * M) - ((Lambda * M * M) / K) - (phi * M * T)
    return dMdt

tlist = []
Mlist = []
h = 0.1 # step size
t0 = 0
for i in range(20):
    tlist.append(t0)
    Mlist.append(M0)
    # calc next
    Mn = M0 + dMdt(M0, t0)
    M0 = Mn
    t0 = t0 + h
    print(tlist, Mlist)

plt.plot(tlist, Mlist)
plt.show()