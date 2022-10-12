import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def v1(t):
    return 1

def sys(t, u):
    # L = 2e-12
    # Ic = 1e-3
    # C = 1.3e-12
    # R = 250
    # Phi_0 = 2e-15

    L = 2
    Ic = 3e6
    C = 1.3
    R = 2e6
    Phi_0 = 2e-3



    du = np.zeros_like(u)
    du[0] = u[1]
    du[1] = u[2]
    du[2] = (2*np.pi*L*Ic/(C * Phi_0))*np.cos(u[0])*u[1] + u[1] - (L/(R*C)) * u[2] - (2*np.pi / Phi_0)*v1(t)
    return du



# p = np.array([L, Ic, C, R, Phi_0])
u0 = np.zeros(3)
# t = np.linspace(0, 1e-8, 100) not working with actual values... None type for sol.sol object from ivp
t = np.linspace(0, 1, 100)
sol = solve_ivp(sys, [0, 1], u0)
y = sol.sol(t)

plt.plot(t, y[0])
plt.plot(t, y[1])