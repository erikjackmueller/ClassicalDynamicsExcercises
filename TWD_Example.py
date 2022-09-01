import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# 1.2, 1.2, 0.9, 0.4, 0.8, 0.4
def system_2_1(a, t, m1, m2, k1, k2, b1, b2):
    """ 2 mass translational system ex.2.1 """
    if t < 0:
        f = 0
    else:
        f = 1
    return np.array([a[2],
                     a[3],
                     (-(k1 + k2) * a[0] - b1 * a[2] + f + k2 * a[1]) * (1 / m1),
                     (-k2 * a[1] + k2 * a[0] - b2 * a[3]) * (1 / m2)])


#  m1=2.2, m2=2.5, k1=1.1, k2=1.5, b=1.4
def system_2_15(a, t, m1, m2, k1, k2, b):
    """ 2 mass translational system ex.2.15 """
    if t < 0:
        f = 0
    else:
        f = 1
    return np.array([a[2],
                     a[3],
                     (-k1 * (a[0] - a[1]) - b * (a[2] - a[3])) * (1 / m1),
                     ((-k2 * a[1]) - k1 * (a[1] - a[0]) - b * (a[3] - a[2]) + f) * (1 / m2)])


def system_2_18(a, t, m1, m2, m3, k, b):
    """ 3-mass translational system ex.2.18 """
    if t <= 0.0:
        f = 0
    else:
        f = 1
    return np.array([a[3],
                     a[4],
                     a[5],
                     (-k * a[0] - k * (a[0] - a[1]) - b * (a[3] - a[4])) * (1 / m1),
                     (-k * (a[1] - a[0]) - k * a[1] - b * (a[4] - a[3]) - k * (a[1] - a[2])) * (1 / m2),
                     (-k * (a[2] - a[1]) - f) * (1 / m3)])


# (-2 * k * a[0] - 2 * b * a[3] + k * a[1] + b * a[4]) * (1 / m1),
# (-3 * k * a[1] - 3 * b * a[4] + k * a[0] + b * a[3] + k * a[2] + b * a[5]) * (1 / m2),
# (-k * a[2] - b * a[5] + k * a[1] + b * a[4] - f) * (1 / m3)

# ==============================================================
# simulation harness

# time step
h = 0.01

# simulation time
time = np.arange(0, 300, h)

# initial conditions
# y0 = np.array([2, 0, 1.5, 0.1, 0.3, 0.1])
y0 = np.zeros(4)

# initialize yk
yk = y0

# solve system of equations args=(m1, m2, m3, k, b)
y = odeint(system_2_15, y0, time, args=(1.2, 2, 1.1, 1.2, 1.2))

# convert list to numpy array
y = np.array(y)

# ==============================================================
# plot result

fig, ax = plt.subplots()
ax.plot(time, y[:, 0])
ax.plot(time, y[:, 1])
ax.plot(time, y[:, 2])
ax.set(xlabel='time (s)', ylabel='x1, x2, x3 (m)', title='Translational Mechanical System 3 Unit Step Response')
ax.legend(['m1 Displacement', 'm2 Displacement', 'm3 Displacement'], loc='lower right')
ax.grid()
plt.show()