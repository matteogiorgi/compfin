import numpy as np
import matplotlib.pyplot as plt
from equation_solvers import fixed_point

f = lambda x: np.sin(np.pi*x) - 4*x - 1

# Plot of the function

x = np.linspace(-2,3,500);

plt.figure()
plt.plot(x,f(x),'k-')
plt.grid(True)
plt.show()

## Fixed point

x0 = 0

g = lambda x: (np.sin(np.pi*x) - 1)/4
# g = lambda x: x + f(x)

x_fp, xall_fp, iters_fp = fixed_point(g,x0)

