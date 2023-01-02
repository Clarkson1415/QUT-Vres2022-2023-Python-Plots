import matplotlib.pyplot as plt
import Eulers

def dMdt(M, t):
    dMdt = M*t
    return dMdt

Eulers.euler(dMdt,0, 1, 2, 20)