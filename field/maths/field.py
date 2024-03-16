import numpy as np







class scalar_field:
    def __init__(self, func):
        self.f= func
        
    def point(self, r):
        return self.f(r)
    
    def line_integral(self, L, t1, t2):
        return integral(lambda t: self.f(L(t))*derv(L)(t))(t2, t1)
    
    def line_integral(self, L, t1, t2):
        return integral(lambda t: self.f(L(t))*derv(L)(t))(t2, t1)

class vector_field:
    def __init__(self, func):
        self.V = func
        
    def point(self, r):
        return self.V(r)
    