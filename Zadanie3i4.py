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


import pandas as pd
intro = markdown.markdown("## Karol Wolczyk zadanie 4")
print(intro)

dt = {'Name' : [], 'Surname' : [], 'Age' : [], 'Sex' : []}
name = ["Jacek", "Tomasz", "Sławomir", "Eliza", "Dawid"]
surname = ["Wróbel", "Nowak", "Szczepaniak", "Górecka", "Pasieka"]
age = [58, 34, 24, 27, 13]
sex = ['M', 'M', 'M', "F", 'M']
data_frame = pd.DataFrame({"Name" : name, "Surname" : surname, "Age" : age, "Sex" : sex})
data_frame["Age"] = data_frame["Age"].astype(np.uint8)
data_frame.info()
print(data_frame.describe(include='all'))
data_frame.head(3)
