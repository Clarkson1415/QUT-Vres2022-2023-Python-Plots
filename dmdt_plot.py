import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

K = 1
O = 1.1
T = 0
Lambda = 1.4
#c = K * math.log((O * T / ( Lambda * M)) - K +1, e) / (O * T - Lambda * K)

M0 = np.linspace(0, 2)
#dmdt = Lambda*M*(1-(M/K)) - O*M*T

dmdt = (Lambda*M0) - ((Lambda*M0*M0)/K) - (O*M0*T)
dmdt_plot = plt.plot(M0, dmdt, 'r-')

# M plot of solution
t = np.linspace(0,20)
c = 5
M = (O*T-Lambda*K)/(Lambda*(np.exp((t+c)*(O*T-Lambda*K)/K)-1))
M_plot = plt.plot(t, M, 'b')

# M plot of solution ODE int solver python to check


plt.show()
