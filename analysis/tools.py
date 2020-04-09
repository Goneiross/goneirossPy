import math

def differentiate(f, method, x0, h):
    """
    @param f: function to differentiate)
    @param method: FDF, BDF, centered, BDF2
    @param x0: point to differentiate at
    @return: f'(x0)
    """
    if method == "FDF":
        df = (f(x0+h)-f(x0))/h
        return df
    elif method == "BDF":
        df = (f(x0)-f(x0-h))/h
        return df
    elif method == "centered":
        df = (f(x0+h/2)-f(x0-h/2))/h
        return df
    elif method == "BDF2":
        df = (3*f(x0)-4*f(x0-h)+f(x0-2*h))/(2*h)
        return df
    else :
        print("Please provide a valid method")
        return 

def differentiateTwice(f, x0, h):
    """
    @param f: function to differentiate)
    @param method: FDF, BDF, centered
    @param x0: point to differentiate at
    @return: f'(x0)
    """
    df = (f(x0+h)-2*f(x0)+f(x0-h))/(h*h)
    return df

def integrate(f, a, b, N, method):
    """
    @param f: function to integrate
    @param a: initial point
    @param b: end point
    @param N: number of intervals for precision
    @param method: trapeze, rectangle, Simpson, Gauss2
    @return: integral from a to b of f(x)
    """
    h = (b-a)/(N)
    if method == "trapeze":
        for i in range(0,n-1):
            xi = a+i*h
            Lhf += f(xi)+f(xi+h)
        Lhf *= h/2
    elif method == "rectangle":
        for i in range(0,n-1):
            xi = a+i*h
            Lhf += f(xi)+h/2
        Lhf *= h
    elif method == "Simpson":
        for i in range(0,n-1):
            xi = a+i*h
            Lhf += f(xi)+4*f(xi+h/2)+f(xi+h)
        Lhf *= h/6
    elif method == "Gauss2"
        for i in range(0,n-1):
            xi = a+i*h
            Lhf += f(xi+h*(1/2)*(1-(1/sqrt(3))))+f(xi+h*(1/2)*(1-(1/sqrt(3))))
        Lhf *= h/2
    return Lhf