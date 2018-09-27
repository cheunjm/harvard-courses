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
