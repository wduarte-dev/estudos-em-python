import numpy as np
import matplotlib.pyplot as plt
Ap = 6                                                           # amplitude da portadora
fp = 750                                                         # frequência da portadora
fm = 40                                                          # frequência do modulante
µ = 1/3                                                          # razão entre a amplitude do modulante e da amplitude da moduladora
offset = 4
omega_p = 2*np.pi*fp                             # frequência angular da portadora
omega_m = 2*np.pi*fm                           # frequência angular do modulante
cmd = input('1 -> Domínio do tempo\n2 -> Domínio da frequência ')

if cmd == '1':
    x = np.linspace(0, 0.1, 1000)
    y = (Ap) * np.cos(omega_p * x) + Ap * µ/2 * np.cos((omega_p + omega_m) * x) + Ap * µ/2 * np.cos((omega_p - omega_m) * x)
    y = y + offset
    plt.xlabel("Tempo")
    plt.plot(x, y)
else:
    x = [fp - fm, fp, fp + fm]
    y = [Ap*µ/2, Ap, Ap*µ/2]
    plt.stem(x, y, basefmt="black")
    plt.xlabel("Frequência")
    
plt.title("Modulação AM")
plt.ylabel("Amplitude")
plt.grid()
plt.show()