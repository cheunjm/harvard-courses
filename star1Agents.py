import progress

class Star1Agent:
 
  def __init__(self, depth = '1'):
    self.index = 0 # Computer is agent 0
    self.depth = int(depth)


  def getPolicy(self, initialState):
    """
      Returns the expectimax action using self.depth
    """
 
    #decide later
    def getReward(state):
      return state.getAverage()

    def terminalTest(state, depth):
      return depth == 0

    def Star1Decision(state):
      """returns action that maximizes minValue"""
      alpha = -float('inf')
      # base case: action = None
      max_value, policy = -float('inf'), None
      # get all possible actions of computer, i.e. all possible questions
      actions = state.getLegalActions("computer")
      for act in actions:
        new_value = playerNode(state.generateSuccessor("computer", act), self.depth - 1, alpha)
        if max_value < new_value:
          max_value, policy = new_value, act
        #stop?
        alpha = max(max_value, alpha)
      return policy

    #player Move 
    def playerNode(state, depth, alpha):
      numberWords = state.getnumberWords()
      if terminalTest(state,depth): 
        return getReward(state)      
      QValue = getReward(state)
      actions = state.getLegalActions("human") #human
      if QValue + depth < alpha:
        return QValue
      QValue += state.getProbability() * MaxValue(state.generateSuccessor("human", 1), depth)
      if (QValue + (1- state.getProbability()) * depth) < alpha:
        return QValue
      QValue += (1 - state.getProbability()) * MaxValue(state.generateSuccessor("human", 0), depth)
      if (QValue + (state.getProbability()) * depth) < alpha:
        print("c")
        return QValue 
        #probability of choosing that * value of the State
      return QValue

    #Computer Move
    def MaxValue(state, depth):
      # base case: action = None
      alpha = -float('inf')
      max_value = -float('inf')
      # get all possible actions of computer
      actions = state.getLegalActions("computer")
      for act in actions:
        new_value = playerNode(state.generateSuccessor("computer", act), depth - 1,alpha)
        if max_value < new_value:
           max_value = new_value 
        alpha = max(max_value, alpha)
      return max_value

    # return the result of expectimax algorithm
    return Star1Decision(initialState)
