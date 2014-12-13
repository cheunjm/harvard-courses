"""
© Copyright 2014. Joon Yang & Jaemin Cheun. All rights reserved.

Significantly cuts down the computation by not evaluating a QValue 
when we discover that it is worse than a previously examined Q value

"""
import progress

class ExpectipruneAgent:
 
  def __init__(self, depth = '1'):
    self.index = 0 # Computer is agent 0
    self.depth = int(depth)


  def getPolicy(self, initialState):
    """
      Returns the expectimax action using self.depth
    """
 
    def getReward(state):
      return state.getAverage()

    def terminalTest(state, depth):
      return depth == 0

    def ExpectipruneDecision(state):
      """returns action that maximizes minValue"""
      # base case: action = None
      max_value, policy = -float('inf'), None
      # get all possible actions of computer, i.e. all possible questions
      actions = state.getLegalActions("computer")
      for act in actions:
        new_value = playerNode(state.generateSuccessor("computer", act), self.depth - 1, max_value)
        if max_value < new_value:
          max_value, policy = new_value, act
      return policy

    #player Move 
    def playerNode(state, depth, alpha):
      """Nodes where player makes the move"""
      if terminalTest(state,depth): 
        return getReward(state)      
      QValue = getReward(state)
      QValue += state.getProbability() * MaxValue(state.generateSuccessor("human", 1), depth)
      #if the highest possible Q value after calculating the first child is less than alpha, we prune the branch
      if (QValue + (1- state.getProbability()) * depth) < alpha:
        return QValue
      QValue += (1 - state.getProbability()) * MaxValue(state.generateSuccessor("human", 0), depth)
      return QValue


    #Computer Move
    def MaxValue(state, depth):
      """Nodes where computer asks a question"""
      max_value = -float('inf')
      # get all possible actions of computer
      actions = state.getLegalActions("computer")
      for act in actions:
        new_value = playerNode(state.generateSuccessor("computer", act), depth - 1,max_value)
        if max_value < new_value:
           max_value = new_value 
      return max_value

    # return the result of expectimax algorithm
    return ExpectipruneDecision(initialState)
