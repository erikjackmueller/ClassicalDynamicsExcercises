import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def pend(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

y0 = [np.pi - 0.1, 0.0]

b = 0.25
c = 5.0

t = np.linspace(0, 10, 101)

sol = odeint(pend, y0, t, args=(b, c))

plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()

def EC(y, t, L1, L2, L3, C1, C2, R1, R2, amp, omega):
    x1, x2, x3, x4 = y
    dydt = [(L1 + L3),
            L1,
            L2,
            L3]
    return dydt

L1 = 0.15
L2 = 0.2
L3 = 0.25
C1 = 0.05
C2 = 0.02
R1 = 1
R2 = 2
omega = 3
amp = 1

