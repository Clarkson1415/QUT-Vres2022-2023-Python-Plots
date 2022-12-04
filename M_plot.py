import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math


# M plot - solution
K = 1
O = 1
Lambda = 1.4

t = np.linspace(0,5)

M_0 = 1
# plot T = 0

for T in range(2): # for T = 0, 1, 2
    c = K * math.log((O * T - K / (Lambda * M_0)) + 1) / (O * T - Lambda * K)
    M = (O*T-Lambda*K)/(Lambda*(np.exp((t+c)*(O*T-Lambda*K)/K)-1))
    plt.plot(t, M, 'b', label=f'T={T}')
    plt.legend()
plt.show()
