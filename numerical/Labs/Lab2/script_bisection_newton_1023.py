import numpy as np
import matplotlib.pyplot as plt
from equation_solvers import bisection, newton

f = lambda x: (x+1)*np.log(x**2+1)

# Plot of the function

x = np.linspace(-3,2,500);

plt.figure()
plt.plot(x,f(x),'k-')
plt.grid(True)
plt.show()

## Bisection

z = -1
a = z - np.pi/2
b = z + 0.5
x_true_1 = -1

x_bisec, xall_bisec, iters_bisec = bisection(f,a,b)

print('Relative error with the bisection method:',
      '{:e}'.format(np.abs(x_true_1-x_bisec)/np.abs(x_true_1)))

## Newton

Df = lambda x: np.log(x**2+1) + 2*x*(x+1)/(x**2+1)

x0 = a

x_new, xall_new, iters_new = newton(f,Df,x0)

print('Relative error with the Newton-Raphson method', 
      '{:e}'.format(np.abs(x_true_1-x_new)/np.abs(x_true_1)))

## Comparison bisection-Newton

plt.figure()
plt.semilogy(np.abs(x_true_1-xall_bisec)/np.abs(x_true_1),'k-')
plt.semilogy(np.abs(x_true_1-xall_new)/np.abs(x_true_1),'r-')
plt.title('Comparison bisection-Newton')
plt.legend(['Bisection','Newton'])
plt.grid(True)
plt.show()


## Computing the convergence order. Here, we choose the last iterations of both methods
## Note that indexing starts from 0. 

k_bisec = 28
k_new = 6

print('Estimated convergence order of the bisection method:',
      '{:f}'.format(np.log(np.abs(xall_bisec[k_bisec]-xall_bisec[k_bisec-1])/np.abs(xall_bisec[k_bisec-1]-xall_bisec[k_bisec-2]))/
                    np.log(np.abs(xall_bisec[k_bisec-1]-xall_bisec[k_bisec-2])/np.abs(xall_bisec[k_bisec-2]-xall_bisec[k_bisec-3]))))


print('Estimated convergence order of the Newton-Raphson method:',
      '{:f}'.format(np.log(np.abs(xall_new[k_new]-xall_new[k_new-1])/np.abs(xall_new[k_new-1]-xall_new[k_new-2]))/
                    np.log(np.abs(xall_new[k_new-1]-xall_new[k_new-2])/np.abs(xall_new[k_new-2]-xall_new[k_new-3]))))


