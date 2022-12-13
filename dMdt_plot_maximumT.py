import numpy as np
import matplotlib.pyplot as plt

K = 1
phi = 1.1
Lambda = 2

M = np.linspace(-1, 1)

#show that max pos roots has T < lambda/phi
T = 0
dmdt = (Lambda * M) - ((Lambda * M * M) / K) - (phi * M * T)
ax = plt.plot(M, dmdt, label=f'T={T}')

T = Lambda/phi - 0.5
dmdt = (Lambda * M) - ((Lambda * M * M) / K) - (phi * M * T)
ax = plt.plot(M, dmdt, label=f'T={T}')

T = Lambda/phi
dmdt = (Lambda * M) - ((Lambda * M * M) / K) - (phi * M * T)
ax = plt.plot(M, dmdt, label=fr'$T = \frac{{\lambda}}{{\phi}}$ = {T}')

T = Lambda/phi + 0.5
dmdt = (Lambda * M) - ((Lambda * M * M) / K) - (phi * M * T)
ax = plt.plot(M, dmdt, label=fr'T = {T}')

plt.legend()
plt.title(r'$\frac{dM}{dt} = \lambda M(1-\frac{M}{K}) - \o{}MT$')
plt.xlabel('M')
plt.ylabel('dMdt')
plt.show()