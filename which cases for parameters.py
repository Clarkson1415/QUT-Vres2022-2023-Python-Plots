import system_ode_solver
import numpy as np
import matplotlib.pyplot as plt

# Parameters
M0 = 1
K = 1
Lambda = 1
phi = 1
rho = 1  # k, rho later

gamma_M = 0.01
delta = 1
T0 = 1

h = 0.001 # stepsize
tf = 1000 # final
t = np.arange(0, tf+h, h) #start, stop, step


# final case conditions
# 1 disease free M->K and T->0
# 2 mild M-> non 0 < K, T - > non zero >= 0
# 3 severe disease M->0
# check 3 first, then 2, the else its 1
# also cases when its oscillating


def what_case(M, T):
    error = 0.01
    if M[-1] == 0:
        print("3 severe")
        print(M[-1], T[-1])
        return "red"
    elif (K-error < M[-1] < K+error) & (0-error < T[-1] < 0+error):
        print(f"1 disease free")
        print(M[-1], T[-1])
        return "green"
    else:
        print("2 mild")
        print(M[-1], T[-1])
        return "blue"


# dont for loop it, #
# use 2 vectors for phi and rho x and y axis then plot the case on it.
# for phi in np.arange(0, 2, 0.5):
#     M, T = system_ode_solver.ode_solve_plot(M0, T0, K, Lambda, phi, rho, gamma_M, delta, t, tf, h)
#     case = what_case(M, T)
#     plt.show()
#     print(f"phi = {phi}, rho = {rho}, case: {case}")

rho_values = np.arange(0, 2, 0.1)
phi_values = np.arange(0, 2, 0.1)

for rho in rho_values:
    for phi in phi_values:
        M, T = system_ode_solver.ode_solve_plot(M0, T0, K, Lambda, phi, rho, gamma_M, delta, t, tf, h)
        case_colour = what_case(M, T)
        plt.scatter(rho, phi, c=case_colour)
plt.show()

