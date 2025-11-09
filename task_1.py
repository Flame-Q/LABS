import numpy as np
import matplotlib.pyplot as plt

x_degrees = np.linspace(-360, 360, 1000)
x_radians = np.radians(x_degrees)

cos_x = np.cos(x_radians)
cos_06x = np.cos(0.6 * x_radians)
f_x = np.exp(cos_x) + np.log(cos_06x**2 + 1) * np.sin(x_radians)

h_x = -np.log((cos_x + np.sin(x_radians))**2 + 2.5) + 10

plt.subplot(2, 1, 1)
plt.plot(x_degrees, f_x, color="blue")
plt.title('График функции f(x)')
plt.xlabel('Градусы')
plt.ylabel('f(x)')
plt.xlim(-360, 360)

plt.subplot(2, 1, 2)
plt.plot(x_degrees, h_x, color="red")
plt.title('График функции h(x)')
plt.xlabel('Градусы')
plt.ylabel('h(x)')
plt.xlim(-360, 360)

plt.tight_layout()
plt.show()