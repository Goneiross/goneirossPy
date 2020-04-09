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