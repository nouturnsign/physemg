import sys

import matplotlib.pyplot as plt
import numpy as np

array = np.loadtxt("data/" + sys.argv[1])
plt.plot(array)
plt.show()
