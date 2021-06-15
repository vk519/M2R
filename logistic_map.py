import numpy as np
import matplotlib.pyplot as plt


def map(r, x):
    return r * x * (1 - x)


t = 10000
r = np.linspace(1, 4.0, t)

iterations = 1000
last = 100

x = 1e-5 * np.ones(t)

lyapunov = np.zeros(t)


fig, (ax1, ax2) = plt.subplots(2,1, sharex=False)
for i in range(iterations):
    x = map(r, x)
    lyapunov += np.log(abs(r - 2 * r * x))
    if i >= (iterations - last):
        ax1.plot(r, x, ',b', alpha=.25)
        ax1.set_title("Bifurication Diagram")
        ax1.set_xlim(3, 4)



ax2.plot(r[lyapunov < 0], lyapunov[lyapunov < 0] / iterations, ',k')
ax2.plot(r[lyapunov > 0], lyapunov[lyapunov > 0] / iterations, ',r')
ax2.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax2.set_xlim(3, 4)
ax2.set_ylim(-1, 1)
ax2.set_title("Lyapunov exponent")

plt.show()
