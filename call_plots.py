import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import system_eulers
import system_ode_solver

system_eulers.eulers_approx_both()
system_ode_solver.ode_solve_plot()
plt.show()

# vs the algebraic
