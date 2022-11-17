import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import scipy as sp

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

import sympy as sp
x1, x2, x3, x4 = sp.symbols('x1:5')
l1, l2, l3 = sp.symbols('l1:4')
r1, r2 = sp.symbols('r1:3')
c1, c2 = sp.symbols('c1:3')
o = sp.symbols('o')
amp = sp.symbols('amp')
u = sp.symbols('u')
a1, a2, a3, a4 = sp.symbols('a1:5')

A = sp.zeros(4)
A[0, 0] = 1
A[2, 2] = 1
A[1, 1] = l1+l3
A[1, 3] = -l3
A[3, 1] = -l3
A[3, 3] = l2+l3
b = sp.zeros(4, 1)
b[0] = a2
b[1] = -(1/c1)*a1 - r1*a2 + u
b[2] = a4
b[3] = -r2*a4 - (1/c2)*a3
A2 = sp.Matrix([[0, 1, 0, 0], [-(1/c1), -r1, 0, 0], [0, 0, 0, 1], [0, 0, -(1/c2), -r2]])
A3 = sp.quick_inv(A) * A2