import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import system_eulers
import system_ode_solver

M0 = 1
K = 1
Lambda = 0.1
phi = 0.5
k = 1.5  # rho later

gamma_M = 0.01
delta = 1
T0 = 1
h = 0.001 # stepsize
tf = 100 # final
t = np.arange(0, tf+h, h) #start, stop, step


system_eulers.eulers_approx_both(M0, T0, K, Lambda, phi, k, M, gamma_M, delta, t, tf, h)
system_ode_solver.ode_solve_plot(M0, T0, K, Lambda, phi, k, M, gamma_M, delta, t, tf, h)
plt.show()
# shows matching eulers to ode solver