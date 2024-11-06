import numpy as np

def bisection(f,a,b,tol=1e-8,max_it=1000):

    """
    ----------- Inputs ---------
    f   : function
    a,b : extrema of the interval
    tol : tolerance 
    max_it: maximum number of iterations
    ------------ Outputs ---------
    x   : the solution found
    xall: all the approximations computed in the iterations
    iters: number of iterations
    ----------------------------------
    """
    
    if f(a)*f(b) > 0:
        
       raise ValueError('Bisection not applicable')
       
    elif f(a)*f(b) == 0:
        
       raise ValueError('The root is an extremum of the interval')
       
    xall = []
    
    iters = 1        
    x = ???    
    xall.append(x)
       
    while (np.abs(a-b) ??? tol) and (iters <= max_it):
        
        if f(x) == 0:   
            
           return x, np.array(xall), iters
       
        elif f(x)*f(a) < 0:
            
           b = x
           
        elif f(b)*f(x) ??? 0:
            
           a = x                              
        
        iters += 1                       
        x = ???                            
        xall.append(x)
        
    return x, np.array(xall), iters

def fixed_point(g,x0,tol=1e-8,max_it=1000):

    """    
    ----------- Inputs ---------
    g:        fixed point function
    x0:       initial guess
    tol : tolerance 
    max_it: maximum number of iterations
    ------------ Outputs ---------
    x   : the solution found
    xall: all the approximations computed in the iterations
    iters: number of iterations
    ----------------------------------
    """
    
    xall = []

    x = g(x0)
    xall.append(x)
    iters = 1
    
    while (np.abs(x-x0) > tol*???) and (iters <= max_it):
        
      x0 = ???
      x = g(x0)

      iters += 1
      xall.append(x)
    
    return x, np.array(xall), iters



def newton(f,Df,x0,tol=1e-8,max_it=1000):

    """    
    ----------- Inputs ---------
    f:        function
    Df:       derivative of function
    x0:       initial guess
    tol : tolerance 
    max_it: maximum number of iterations
    ------------ Outputs ---------
    x   : the solution found
    xall: all the approximations computed in the iterations
    iters: number of iterations
    ----------------------------------
    """
    
    xall = []

    dx = ???
    x = x0+dx
    iters = 1
    xall.append(x)

    
    while (np.abs(x-x0) > tol*???) and (iters <= max_it):
        
      x0 = x
      dx = ???
      x = x0 + dx
      iters += 1
      xall.append(x)
    
    return x, np.array(xall), iters




