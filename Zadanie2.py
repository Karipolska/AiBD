import matplotlib.pyplot as plt
import numpy as np

fn = lambda x: x**2 + 5

x1 = np.linspace(-1, 1)
x2 = np.linspace(-6, 6)
x3 = np.linspace(0, 5)


fig, axs = plt.subplots(1,3,figsize = (12,6))
fig.suptitle("Karol Wolczyk Zadanie 3")
axs[0].plot(x1, fn(x1))
axs[0].set_title("D: -1<x<1")
axs[0].set_xlabel("x")
axs[0].set_ylabel("f(x)")
axs[0].grid()
axs[1].plot(x2, fn(x2))
axs[1].set_title("D: -6<x<6")
axs[1].set_xlabel("x")
axs[1].set_ylabel("f(x)")
axs[1].grid()
axs[2].plot(x3, fn(x3))
axs[2].set_title("D: 0<x<5")
axs[2].set_xlabel("x")
axs[2].set_ylabel("f(x)")
axs[2].grid()

plt.show()
