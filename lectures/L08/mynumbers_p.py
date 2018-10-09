import numpy as np

class RealExtensions:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class _Complex(RealExtensions):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def _magnitude(self):
        return np.sqrt(self.real**2.0 + self.imag**2.0)
    
    def _angle(self):
        return np.arctan(self.imag / self.real)
    
    def polar_form(self):
        self.r = self._magnitude()
        self.theta = self._angle()

class Dual(RealExtensions):
    def __init__(self, a, b):
        self.real = a
        self.dual = b
    
    def _magnitude(self):
        return self.real
    
    def _angle(self):
        return self.dual /self. real
    
    def polar_form(self):
        self.r = self._magnitude()
        self.theta = self._angle()
