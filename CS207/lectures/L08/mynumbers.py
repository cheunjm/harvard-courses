<<<<<<< HEAD
import math

class RealExtensions():
  def __init__(self, a, b):
    self.a = a
    self.b = b
  def _magnitude(self):
    raise NotImplementedError()
  def _angle(self):
    raise NotImplementedError()
  def polar(self):
    raise NotImplementedError()

class Complex(RealExtensions):
  def _magnitude(self):
    return math.sqrt(self.a ** 2 + self.b ** 2)
  def _angle(self):
    return math.atan2(self.b, self.a)
  def polar(self):
    return (self._magnitude(), self._angle())

class Dual(RealExtensions):
  def _magnitude(self):
    return self.a
  def _angle(self):
    return self.b / self.a
  def polar(self):
    return (self._magnitude(), self._angle())
=======
import numpy as np

class RealExtensions:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Complex(RealExtensions):
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
>>>>>>> f7a463f5438eefd4c5b5cfeb1747aa04db69a11c
