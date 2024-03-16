dx = 0.01

def range_d(x1, x2):
    return (x1 + k*dx
            for k in range(
                int((x2 - x1)/dx)))

def derv(f):
    return lambda x: (f(x + dx) - f(x))/dx

def integral(f):
    return lambda x1, x2: sum((f(x)*dx 
                               for x in range_d(x1, x2)))
