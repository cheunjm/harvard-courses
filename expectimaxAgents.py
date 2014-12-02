import progress

class ExpectimaxAgent:

  def __init__(self, depth = '1'):
    self.index = 0 # Computer is agent 0
    self.depth = int(depth)


  def getAction(self, initialState):
    """
      Returns the expectimax action using self.depth
    """

    def getReward(state):
      return sum(state.getProgress())

    def terminalTest(state, depth):
      return depth == 0

    def ExpectimaxDecision(state):
      """returns action that maximizes minValue"""
      # base case: action = None
      max_value, max_action = -float('inf'), None
      # get all possible actions of computer
      actions = state.getLegalActions(0)
      for act in actions:
        new_value = weightedValue(state.generateSuccessor(0, act), 1, self.depth)
        if max_value < new_value:
           max_value, max_action = new_value, act
      return max_action

    def maxValue(state, index, depth):
      if terminalTest(state,depth):
        return getReward(state)
      max_value = -float('inf')
      actions = state.getLegalActions(index)
      for act in actions:
        # take the maximum of min values
        new_value = weightedValue(state.generateSuccessor(index, act), index + 1, depth)
        max_value = max(max_value, new_value)
      return max_value

    def weightedValue(state, index, depth):
      """returns util value"""
      if terminalTest(state,depth):
        return getReward(state)
      weighted_avg = 0
      actions = state.getLegalActions(index)
      for act in actions:
        prob = 0
        if act == 0: #user got the question wrong
          prob = 1 - state.getProgress()[state.getWord()]
        else: 
          prob = state.getProgress()[state.getWord()]
        # last ghost agent
        weighted_avg += prob * maxValue(state.generateSuccessor(index, act), 0, depth - 1)
      return weighted_avg
    # return the result of minimax algorithm
    return ExpectimaxDecision(initialState)
