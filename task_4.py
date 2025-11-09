from scipy import integrate
import numpy as np

integrl_1 = lambda x: (2*x)/3 + 1/(4*np.sqrt(x))
res1 = integrate.quad(integrl_1, 4, 9)

integrl_2 = lambda y, x: np.sqrt(x + y + 1)
bottom = lambda x: 1
top = lambda x: 7
res2 = integrate.dblquad(integrl_2, 0, 4, bottom, top)

print("Результат первого интеграла:", res1[0])
print("Результат второго интеграла:", res2[0])
