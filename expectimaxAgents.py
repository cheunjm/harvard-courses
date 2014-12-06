import progress

class ExpectimaxAgent:

  def __init__(self, depth = '1'):
    self.index = 0 # Computer is agent 0
    self.depth = int(depth)


  def getPolicy(self, initialState):
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
      max_value, policy = -float('inf'), None
      # get all possible actions of computer, i.e. all possible questions
      actions = state.getLegalActions("computer")
      for act in actions:
        new_value = playerNode(state.generateSuccessor("computer", act), self.depth)
        if max_value < new_value:
           max_value, policy = new_value, act
      return policy

    #player Move 
    def playerNode(state, depth):
      if terminalTest(state,depth): 
        return getReward(state)      
      QValue = getReward(state)
      actions = state.getLegalActions("human") #human
      for act in actions:
        QValue = QValue + state.getProgress()[state.getWord()] * MaxValue(state.generateSuccessor("human", act), depth )
        #probability of choosing that * value of the State
      return QValue

    #Computer Move
    def MaxValue(state, depth):
      # base case: action = None
      max_value, max_action = -float('inf'), None
      # get all possible actions of computer
      actions = state.getLegalActions("computer")
      for act in actions:
        new_value = playerNode(state.generateSuccessor("computer", act), depth - 1)
        if max_value < new_value:
           max_value, max_action = new_value, act
      return max_value

    # return the result of expectimax algorithm
    return ExpectimaxDecision(initialState)
