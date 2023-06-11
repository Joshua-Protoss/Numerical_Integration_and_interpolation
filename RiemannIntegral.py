import numpy as np

a = 0
b = np.pi
n = 11
h = (b-a) / (n - 1)
x = np.linspace(a, b, n)
f = np.sin(x)

riemannL = h * sum(f[:n-1])
err_riemannL = 2 - riemannL

riemannR = h * sum(f[1:])
err_riemannR = 2 - riemannR

riemannMid = h * sum(np.sin((x[:n-1] + x[1:])/2))
err_riemannMid = 2 - riemannMid

trapz = h/2*(f[0] + 2 * sum(f[1:n-1]) + f[n-1])
err_trapz = 2 - trapz

print(riemannL)
print(err_riemannL)

print(riemannR)
print(err_riemannR)

print(riemannMid)
print(err_riemannMid)

print(trapz)
print(err_trapz)
