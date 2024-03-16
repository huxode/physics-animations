from math import sqrt

class vector:
    def __init__(self, v):
        self.core = tuple(v)
    
    @property
    def dim(self):
        return len(self.core)
    def __getitem__(self, j):
        return self.core[j]
    def __repr__(self):
        return repr(self.core)
    
    def __add__(self, v2):
        if(self.dim != v2.dim):
            raise ValueError("Different Dimensions in Vector Addition")
        return vector(a + b for a, b in zip(self.core, v2.core))
    
    def __mul__(self, s):
        return vector(s*a for a in self.core)
    def __rmul__(self, s):
        return self*s
    
    def __neg__(self):
        return -1*self
    def __sub__(self, v2):
        return self + (-v2)
    
    def dot(self, v2):
        if(self.dim != v2.dim):
            raise ValueError("Different Dimensions in Vector Inner Products")
        return sum(a*b for a, b in zip(self.core, v2.core))

    @property
    def form(self):
        return self.dot(self)
    @property
    def length(self):
        return sqrt(self.form)
    def __abs__(self):
        return self.length

    def cross(self, v2):
        if(self.dim != v2.dim):
            raise ValueError("Different Dimensions in Vector External Products")
        if(self.dim != 3):
            raise ValueError("Dimensions in Vector External Products is not 3")
        return self.__init__((self[1]*v2[2] - self[2]*v2[1],
                              self[2]*v2[0] - self[0]*v2[2],
                              self[0]*v2[1] - self[1]*v2[0]))
        
def dot(v1, v2):
    return v1.dot(v2)

def cross(v1, v2):
    return v1.cross(v2)
        