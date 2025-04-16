import numpy as np 
import matplotlib.pyplot as plt
x=np.arange(1,13)
y=x**2
plt.title("line graph")
plt.xlabel("X axis")
plt.ylabel("y axis")
plt.plot(x,y,color="blue")
plt.show()
