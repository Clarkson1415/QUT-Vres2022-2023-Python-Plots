import matplotlib.pyplot as plt
import Eulers

def dMdt(t, M):
    dMdt = M
    return dMdt

Eulers.euler(dMdt,0, 1, 1.2, 4)