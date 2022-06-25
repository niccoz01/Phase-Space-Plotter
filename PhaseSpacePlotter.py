import matplotlib.pyplot as plt
from sympy import *
import numpy as np
x = Symbol('x')
y = Symbol('y')

# List of functions to simplify the input
log = np.log
log2 = np.log2
log10 = np.log10
sin = np.sin
sinc = np.sinc
cos = np.cos
tan = np.tan
sec = np.arcsin
csc = np.arccos
cot = np.arctan
sinh = np.sinh
cosh = np.cosh
tanh = np.tanh
arcsinh = np.arcsinh
arccosh = np.arccosh
arctanh = np.arctanh
exp = np.exp
real = np.real
imag = np.imag
conj = np.conj
max = np.maximum
min = np.min
sqrt = np.sqrt

def PSP(der, xmin=-5, xmax=5, ymin=-5, ymax=5, n=20, F=0.002):
    '''Function which plots the phase space portrait of a dynamical system in the phase plane (x,y).
    The two differential equations which make the system have the form:
    dx/dt = f(x,y)
    dy/dt = g(x,y)


    Args:
        der (list of string) : list containing f(x,y) and g(x,y)  
        xmin (float) : minimum value of x
        xmax (float) : maximum value of x
        ymin (float) : minimum value of y
        ymax (float) : maximum value of y
        n (integer) : last polynomial order (n=3 default)
        F (float) : normalization factor
    
    Returns:
        Plot of the corresponding phase space portrait
    '''
    dxdt, dydt = der

    # Parsing the functions and convert them in numpy
    dydt = parse_expr(dydt)
    dxdt = parse_expr(dxdt)
    dxdt_num = lambdify((x,y), dxdt, 'numpy')
    dydt_num = lambdify((x,y), dydt, 'numpy')
    X, Y = np.meshgrid(np.linspace(xmin, xmax, n), np.linspace(ymin, ymax, n))
    u, v = np.zeros(X.shape), np.zeros(Y.shape)
    NI, NJ = X.shape
    for i in range(NI):
        for j in range(NJ):
            x_ = X[i, j]
            y_ = Y[i, j]
            solns = [dxdt_num(x_,y_), dydt_num(x_,y_)]
            u[i,j] = solns[0]
            v[i,j] = solns[1]
            
    # Normalize arrows
    N = np.sqrt( u**2 + v**2 )
    U, V = u/N, v/N
    U *= F
    V *= F

    # Plot the results
    Q = plt.quiver(X, Y, U, V, color='blue')

    plt.xlim([xmin+0.2, xmax+0.2])
    plt.ylim([ymin+0.2, ymax+0.2])
    plt.axvline(0, color='black')
    plt.axhline(0, color='black')
    plt.grid()
    
    plt.show()
