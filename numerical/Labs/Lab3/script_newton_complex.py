import numpy as np
import matplotlib.pyplot as plt
from equation_solvers import newton

# f = lambda x: x**2+1     # Pure imaginary roots: i , -i
# Df = lambda x: 2*x

# f = lambda x: x**3-3*x     # Real roots: -sqrt(3), 0, sqrt(3)
# Df = lambda x: 3*x**2 - 3

# f = lambda x: x**3+x**2+x-3    # Complex roots: -1-i*sqrt(2),-1+i*sqrt(2),1
# Df = lambda x: 3*x**2+2*x+1

f = lambda x: x**6-1
Df = lambda x: 6*x**5

# Complex grid

n = 500

real_points = np.linspace(-5,5,n)
imaginary_points = np.linspace(-5,5,n)

# real_points = np.linspace(-0.5,0.5,n)
# imaginary_points = np.linspace(0.2,1,n)

real_grid, imaginary_grid = np.meshgrid(real_points, imaginary_points)

complex_grid = real_grid + imaginary_grid * 1j

convergence_real_grid = np.zeros(complex_grid.shape)
convergence_imaginary_grid = np.zeros(complex_grid.shape)

iterations_grid = np.zeros(complex_grid.shape)


for iter1 in range(0,complex_grid.shape[0]):
    for iter2 in range(0,complex_grid.shape[1]):
           
        x0 = complex_grid[iter1,iter2]
        
        x_new, xall_new, iters_new = newton(f,Df,x0)
        
        convergence_real_grid[iter1,iter2] = np.real(x_new)
        convergence_imaginary_grid[iter1,iter2] = np.imag(x_new)
        iterations_grid[iter1,iter2] = iters_new
        

fig, (ax1,ax2) = plt.subplots(1,2,figsize=(8, 4))
ax1.matshow(convergence_real_grid)
ax2.matshow(convergence_imaginary_grid)
ax1.set_title('Real part')
ax2.set_title('Imaginary part')
# I'm just removing bars and ticks
plt.setp(ax1.spines.values(), alpha = 0)
plt.setp(ax2.spines.values(), alpha = 0)
ax1.tick_params(which = 'both', size = 0, labelsize = 0)
ax2.tick_params(which = 'both', size = 0, labelsize = 0)
plt.show()

fig, ax = plt.subplots(1,1,figsize=(4,4))
ax.matshow(iterations_grid)
plt.setp(ax.spines.values(), alpha = 0)
ax.tick_params(which = 'both', size = 0, labelsize = 0)
ax.set_title('Number of iterations')
plt.show()