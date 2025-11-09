import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)

f_x = 5 / (x**2 - 9)

plt.plot(x, f_x, "blue")
plt.title('График функции f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(-10, 10)

plt.tight_layout()
plt.show()