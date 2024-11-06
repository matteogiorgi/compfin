import numpy as np
from scipy.linalg import hilbert, invhilbert
import matplotlib.pyplot as plt
from direct_solvers import lu_solver, chol_solver

lu_errors = []
chol_errors = []

for n in range(2,13):
    
    A = hilbert(n)
    invA = invhilbert(n)
    b = np.ones((n,1))
    x_true = invA@b
    
    x_lu = lu_solver(A,b)
    x_chol = chol_solver(A,b)
    
    lu_errors.append(np.linalg.norm(x_lu-x_true,2)/np.linalg.norm(x_true,2))
    chol_errors.append(np.linalg.norm(x_chol-x_true,2)/np.linalg.norm(x_true,2))

plt.figure()
plt.semilogy([i for i in range(2,13)],lu_errors,'k-')
plt.semilogy([i for i in range(2,13)],chol_errors,'r-')
plt.title('Gauss and Cholesky errors')
plt.legend(['LU','Cholesky'])
plt.grid(True)
plt.show()
