# -*- coding: utf-8 -*-

"""
© Copyright 2014. Joon Yang & Jaemin Cheun. All rights reserved.

Finds an optimal policy using expectimax search

"""

import progress

class ExpectimaxAgent:

  def __init__(self, depth='2'):
    self.index = 0 # Computer is agent 0
    self.depth = int(depth)

  def getPolicy(self, initialState):
    """Returns the expectimax action using self.depth"""

    def getReward(state):
      return state.getAverage()

    def terminalTest(state, depth):
      return depth == 0

    def ExpectimaxDecision(state):
      """returns action that maximizes minValue"""
      # base case: action = None
      max_value, policy = -float('inf'), None
      # get all possible actions of computer, i.e. all possible questions
      actions = state.getLegalActions("computer")
      for act in actions:
        new_value = playerNode(state.generateSuccessor("computer", act), self.depth - 1)
        if max_value < new_value:
          max_value, policy = new_value, act
      return policy

    def playerNode(state, depth):
      """Nodes where player makes the move"""
      if terminalTest(state, depth): 
        return getReward(state)    
      QValue = getReward(state)
      actions = state.getLegalActions("human")
      for act in actions:
        if act == 0:
          QValue +=  (1 - state.getProbability()) * MaxValue(state.generateSuccessor("human", act), depth)
        else:
          QValue += state.getProbability() * MaxValue(state.generateSuccessor("human", act), depth)
      return QValue

    def MaxValue(state, depth):
      """Nodes where computer asks a question"""
      max_value = -float('inf')
      # get all possible actions of computer
      actions = state.getLegalActions("computer")
      for act in actions:
        new_value = playerNode(state.generateSuccessor("computer", act), depth - 1)
        if max_value < new_value:
           max_value = new_value
      return max_value

    # return the result of expectimax algorithm
    return ExpectimaxDecision(initialState)
