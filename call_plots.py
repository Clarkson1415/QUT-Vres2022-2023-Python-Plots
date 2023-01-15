import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import system_eulers
import system_ode_solver
import M_plot

system_eulers.eulers_approx_both()
system_ode_solver.ode_solve()
M_plot.Mt_sol()



plt.show()

# vs the algebraic
