"""Copyright Joon Yang & Jaemin Cheun"""

from copy import deepcopy
import timeit

class Sudoku:
  def __init__(self, board):
    self.board = board

  def __str__(self):
    boardString = '\n'
    for row in self.board:
      boardString += str(row) + '\n'
    return boardString

  def _getFirstEmptySquare(self):
    for x in xrange(0,9):
      for y in xrange(0,9):
        if not self.board[x][y]:
          return (x, y)
    return None

  # Returns all empty squares
  def _getAllEmptySquares(self):
    emptySquares = []
    for x in xrange(0,9):
      for y in xrange(0,9):
        if not self.board[x][y]:
          emptySquares.append((x, y))
    return emptySquares

  def _getMostConstrainedEmptySquare(self):
    # Part 3 goes here.
    emptySquares = self._getAllEmptySquares()
    if not(emptySquares):
      return None
    PossibleVals = map(len,map(self._getPossibleValsFor, emptySquares))
    return emptySquares[PossibleVals.index(min(PossibleVals))]

  # PART 3: Swap out the implementation after implementing part 3
  def _getEmptySquare(self):
    # return self._getFirstEmptySquare()
    return self._getMostConstrainedEmptySquare()

  def _getRow(self, x):
    return list(self.board[x])

  def _getCol(self, y):
    return [row[y] for row in self.board]

  def _getBox(self, x, y):
    rowmin, rowmax = x / 3 * 3, x / 3 * 3 + 3
    colmin, colmax = y / 3 * 3, y / 3 * 3 + 3
    nums = [] 
    for x in xrange(rowmin, rowmax):
      for y in xrange(colmin, colmax):
        nums.append(self.board[x][y])
    return nums

  def _crossOff(self, values, nums):
    for n in nums:
      if n: values[n-1] = None

  def _getPossibleValsFor(self, emptySquare):
    x = emptySquare[0]
    y = emptySquare[1]
    values = range(1,10)
    row = self._getRow(x)
    col = self._getCol(y)
    box = self._getBox(x, y)
    self._crossOff(values, row)
    self._crossOff(values, col)
    self._crossOff(values, box)
    return [v for v in values if v]

  def _fillEmptySquare(self, emptySquare, val):
    newBoard = deepcopy(self.board)
    newBoard[emptySquare[0]][emptySquare[1]] = val
    return Sudoku(newBoard)

  def _forwardCheck(self):
    # PART 2 goes here.
    for emptySquare in self._getAllEmptySquares():
      if not(self._getPossibleValsFor(emptySquare)):
        return False
    return True

  def _getAllSuccessors(self):
    # PART 1 goes here.
    # repeat until all squares are filled
    successors = []
    emptySquare = self._getEmptySquare()
    if emptySquare is not None:
      possibleVals = self._getPossibleValsFor(emptySquare)
      for val in possibleVals:
        successor = self._fillEmptySquare(emptySquare, val)
        successors.append(successor)
    return successors


  def _getSuccessorsWithForwardChecking(self):
    return [s for s in self._getAllSuccessors() if s._forwardCheck()]

  # PART 2: Swap out the implementation after implementing part 2
  def getSuccessors(self):
    # return self._getAllSuccessors()
    return self._getSuccessorsWithForwardChecking()

  def isFinalState(self):
    return self._getFirstEmptySquare() == None

def solveCSP(problem):
  statesExplored = 0
  fringe = [problem]
  while fringe:
    state = fringe.pop()
    statesExplored += 1
    if state.isFinalState():
      print 'Number of explored: ' + str(statesExplored)
      return state
    else:
      successors = state.getSuccessors()  
      fringe.extend(successors)
  return None

if __name__ == "__main__":
  setup = '''
from __main__ import Sudoku
from __main__ import solveCSP

mySudokuBoard = [[None, None, None, None, None, 8, 9, None, 2],
          [6, None, 4, 3, None, None, None, None, None],
          [None, None, None, 5, 9, None, None, None, None],
          [None, None, 5, 7, None, 3, None, None, 9],
          [7, None, None, None, 4, None, None, None, None],
          [None, None, 9, None, None, None, 3, None, 5],
          [None, 8, None, None, None, 4, None, None, None],
          [None, 4, 1, None, None, None, None, 3, None],
          [2, None, None, 1, 5, None, None, None, None]]
mySudokuPuzzle = Sudoku(mySudokuBoard)


mySudokuPuzzle = Sudoku(mySudokuBoard)
'''

  solveSudoku = '''
print 'Solution: ' + str(solveCSP(mySudokuPuzzle))
'''

  print 'Time elapsed: ' + str(timeit.timeit(solveSudoku, setup = setup, number = 1))
