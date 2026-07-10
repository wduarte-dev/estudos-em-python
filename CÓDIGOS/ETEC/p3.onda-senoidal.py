import numpy as np
import matplotlib.pyplot as plt
A = 1                                           # amplitude
f = 0.25                                        # frequência
omega = 2*np.pi*f                   # frequência angular

x = np.linspace(0, 10, 1000)
y = A * np.sin(omega * x)

plt.plot(x, y)
plt.title("Onda Senoidal")
plt.xlabel("Tempo")
plt.ylabel("Amplitude")
plt.grid()
plt.show()