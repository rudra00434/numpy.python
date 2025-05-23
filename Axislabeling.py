import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots(ncols=2, figsize=(7, 2.5), layout='constrained')
np.random.seed(19680801)
t = np.arange(200)
x = np.cumsum(np.random.randn(200))
axs[0].plot(t, x)
axs[0].set_title('aspect="auto"')
axs[1].plot(t, x)
axs[1].set_aspect(3)
axs[1].set_title('aspect=3')
plt.show()