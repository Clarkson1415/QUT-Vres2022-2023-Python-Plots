import system_ode_solver
import numpy as np
import matplotlib.pyplot as plt

M0 = 1
K = 1
Lambda = 0.1
phi = 0.5
k = 1.5  # rho later

gamma_M = 0.01
delta = 1
T0 = 1
h = 0.001 # stepsize
tf = 1000 # final
t = np.arange(0, tf+h, h) #start, stop, step

M, T = system_ode_solver.ode_solve_plot(M0, T0, K, Lambda, phi, k, gamma_M, delta, t, tf, h)
# conditions
# 1 disease free M->K and T->0
# 2 mild M-> non 0 < K, T - > non zero >= 0
# 3 severe disease M->0
# check 3 first, then 2, the else its 1
if M[-1] == 0:
    print("3 severe")
elif (M[-1] != 0) & (T[-1] >= 0):
    print("2 mild")
else:
    print(f"1 disease free{M[-1]}")

print(M[-1], T[-1])

# plot it
plt.show()

