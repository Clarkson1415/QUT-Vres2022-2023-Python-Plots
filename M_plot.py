import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

t = np.linspace(0,5)

M_0 = 1

T = 1
K = 1
O = 1
Lambda = 1.4
c = (math.log(abs(1 - (K + (K*O*T)/M_0)) / (Lambda - O*T)))
M = (K + K*O*T)/(1 - math.exp((t+c)*(Lambda - O*T)))
plt.plot(t, M)
plt.title('M')
