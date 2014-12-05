import progress

class Star1Agent:

  def __init__(self, depth = '1'):
    self.index = 0 # Computer is agent 0
    self.depth = int(depth)


  def getAction(self, initialState):
    """
      Returns the expectimax action using self.depth
    """

    #decide later
    def getReward(state):
      return (1 - state.getProgress()[state.getWord()])/2

    def terminalTest(state, depth):
      return depth == 0

    def ExpectimaxDecision(state):
      """returns action that maximizes minValue"""
      # base case: action = None
      max_value, max_action = -float('inf'), None
      # get all possible actions of computer
      actions = state.getLegalActions(0)
      for act in actions:
        new_value = playerMove(state.generateSuccessor(0, act), self.depth)
        if max_value < new_value:
           max_value, max_action = new_value, act
      return max_action

    #player Move 
    def chanceNode(state, depth):
      if terminalTest: then return get Reward(state)      
      QValue = getReward(state)
      actions = state.getLegalActions(1) #human
      for act in actions:
        QValue = QValue + probability * value of the State
      return QValue

    #Computer Move
    def MaxValue(state, depth):
      # base case: action = None
      max_value, max_action = -float('inf'), None
      # get all possible actions of computer
      actions = state.getLegalActions(0)
      for act in actions:
        new_value = playerMove(state.generateSuccessor(0, act), self.depth)
        if max_value < new_value:
           max_value, max_action = new_value, act
      return max_value

    # return the result of minimax algorithm
    return ExpectimaxDecision(initialState)
