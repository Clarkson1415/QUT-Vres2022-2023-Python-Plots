import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

def f(M, t):
    K = 1
    O = 2
    T = 1
    M0 = initial_conditions[0]
    Lambda = 1
    c = K*math.log((O*T/(Lambda*M0)) - K +1)/(O*T - Lambda*K)

    #a = 4
    #b = 7
    #n = s[0]
    #c = s[1]
    # Dm dt equation of myelin
    #dndt = a * n - (c/(c+1)) * b * n

    dMdt = Lambda*M*(1-(M/K)) - O*M*T

    #dcdt = (c/(c+1)) * n - c + 1
    print(dMdt)
    return [dMdt]

t = np.linspace(0,20) # x axis

initial_conditions = [1] # initial condition, can be a vector, i.e. if 2 equations dmdt and dsdt and 2 initial conditions y0 = [m0, s0]
# imma need to solve for C first then
# plot for a bunch of different initial conditions. so many lines plotted for dmdt equation
M0 = 1
M = odeint(f, M0, t) #integrate f over between s0 and t

plt.plot(t,s[:,0],'r--', linewidth=2.0)
#plt.plot(t,s[:,1],'b-', linewidth=2.0)
plt.xlabel("t")
plt.ylabel("S[N,C]")
plt.legend(["N","C"])
plt.show()