import reprlib

class Sentence:
  def __init__(self, text):
    self.text = text
    self.words = text.split()
    self.index = 0

  def __iter__(self):
    for word in self.words:
      yield word

  def __repr__(self):
      return 'Sentence(%s)' % reprlib.repr(self.text)