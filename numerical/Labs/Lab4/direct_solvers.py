import numpy as np
from scipy.linalg import lu, cholesky, solve

def lu_solver(A,b):
    
    """
    ----------- Inputs ---------
    A   : the matrix
    b : the right-hand term
    ------------ Outputs ---------
    x   : the solution found
    ----------------------------------
    """

    if A.shape[0] != A.shape[1]:
        raise ValueError('The matrix is not square!')

    if np.linalg.det(A) == 0:
        raise ValueError('The matrix is not invertible')

    P, L, U = lu(A)
    
    y = solve(L,P@b)
    x = solve(U,y)
    
    return x

def chol_solver(A,b):
    
    """
    ----------- Inputs ---------
    A   : the matrix
    b : the right-hand term
    ------------ Outputs ---------
    x   : the solution found
    ----------------------------------
    """

    if A.shape[0] != A.shape[1]:
        raise ValueError('The matrix is not square!')

    if np.linalg.det(A) == 0:
        raise ValueError('The matrix is not invertible')

    L = cholesky(A)
    
    y = solve(L.T,b)
    x = solve(L,y)
    
    return x
