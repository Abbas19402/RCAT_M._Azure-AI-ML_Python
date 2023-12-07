import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
data= np.random.randint(0,100,40)

plt.hist(data, bins=[0,10,20,30,40,50,60,70,80,90,100], rwidth=0.9)

plt.xlabel('Values')
plt.ylabel('freq')
plt.title("histogram")

plt.show()