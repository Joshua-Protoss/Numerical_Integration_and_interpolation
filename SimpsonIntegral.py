import numpy as np
from scipy.integrate import quad

a = 0
b = np.pi
n = 11
h = (b - a) / (n-1)
x = np.linspace(a, b, n)
f = np.sin(x)

SimpI = (h/3) * (f[0] + 2*sum(f[:n-2:2]) + 4*sum(f[1:n-1:2]) + f[n-1])
err_SimpI = 2 - SimpI

quad, est_err_quad = quad(np.sin, 0, np.pi)
err_quad = 2 - quad

print(SimpI)
print(err_SimpI)
print(quad)
print(est_err_quad, err_quad)
