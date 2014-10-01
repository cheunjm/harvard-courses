# multiAgents.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from util import manhattanDistance
from game import Directions
import random, util
from math import sqrt, log

from game import Agent

class ReflexAgent(Agent):
  """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
  """


  def getAction(self, gameState):
    """
    You do not need to change this method, but you're welcome to.

    getAction chooses among the best options according to the evaluation function.

    Just like in the previous project, getAction takes a GameState and returns
    some Directions.X for some X in the set {North, South, West, East, Stop}
    """
    # Collect legal moves and successor states
    legalMoves = gameState.getLegalActions()

    # Choose one of the best actions
    scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best

    "Add more of your code here if you want to"

    return legalMoves[chosenIndex]

  def evaluationFunction(self, currentGameState, action):
    """
    Design a better evaluation function here.

    The evaluation function takes in the current and proposed successor
    GameStates (pacman.py) and returns a number, where higher numbers are better.

    The code below extracts some useful information from the state, like the
    remaining food (newFood) and Pacman position after moving (newPos).
    newScaredTimes holds the number of moves that each ghost will remain
    scared because of Pacman having eaten a power pellet.

    Print out these variables to see what you're getting, then combine them
    to create a masterful evaluation function.
    """
    # Useful information you can extract from a GameState (pacman.py)
    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = successorGameState.getPacmanPosition()
    newFood = successorGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    "*** YOUR CODE HERE ***"
    food_score, ghost_score = 0, 0
    for food in newFood.asList():
      # choose the option that's closer to the food
      food_score = min(manhattanDistance(newPos, food), food_score)**2
    for ghost in newGhostStates:
      ghost_score = max(manhattanDistance(newPos, ghost.getPosition()), ghost_score)
    if newScaredTimes[0] > 0 or newScaredTimes[0] > 0 or food_score < 10 and ghost_score > 3:
      if food_score < 2:
        return food_score**10
      else:
        return food_score**2
    else:
      return food_score + ghost_score**2

def scoreEvaluationFunction(currentGameState):
  """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
  """
  return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
  """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
  """

  def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
    self.index = 0 # Pacman is always agent index 0
    self.evaluationFunction = util.lookup(evalFn, globals())
    self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
  """
    Your minimax agent (question 2)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action from the current gameState using self.depth
      and self.evaluationFunction.

      Here are some method calls that might be useful when implementing minimax.

      gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

      Directions.STOP:
        The stop direction, which is always legal

      gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

      gameState.getNumAgents():
        Returns the total number of agents in the game
    """
    "*** YOUR CODE HERE ***"
    num_agents = gameState.getNumAgents()

    def minimaxDecision(state):
      """returns action that maximizes minValue"""
      # base case: action = stop
      max_value, max_action = -float('inf'), Directions.STOP
      # get all possible actions of pacman
      actions = gameState.getLegalActions(0)
      actions.remove(Directions.STOP)
      for act in actions:
        # query min values of ghost decisions
        new_value = minValue(gameState.generateSuccessor(0, act), 1, self.depth)
        if max_value < new_value:
           max_value, max_action = new_value, act
      return max_action

    def maxValue(state, index, depth):
      """returns util value"""
      if state.isWin() or state.isLose() or depth == 0:
        return self.evaluationFunction(state)
      max_value = -float('inf')
      actions = state.getLegalActions(index)
      actions.remove(Directions.STOP)
      for act in actions:
        # take the maximum of min values
        new_value = minValue(state.generateSuccessor(index, act), index + 1, depth)
        max_value = max(max_value, new_value)
      return max_value

    def minValue(state, index, depth):
      """returns util value"""
      if state.isWin() or state.isLose() or depth == 0:
        return self.evaluationFunction(state)
      min_value = float('inf') 
      actions = state.getLegalActions(index)
      for act in actions:
        if (index == num_agents - 1):
          # pacman's turn
          new_value = maxValue(state.generateSuccessor(index, act), 0, depth - 1)
        else:
          # ghost's turn
          new_value = minValue(state.generateSuccessor(index, act), index + 1, depth)
        min_value = min(min_value, new_value)
      return min_value
    # return the result of minimax algorithm
    return minimaxDecision(gameState)

class AlphaBetaAgent(MultiAgentSearchAgent):
  """
    Your minimax agent with alpha-beta pruning (question 3)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action using self.depth and self.evaluationFunction
    """
    "*** YOUR CODE HERE ***"
    num_agents = gameState.getNumAgents()

    def alphabetaDecision(state):
      """returns action that maximizes minValue"""
      alpha = -float('inf')
      beta = float('inf')
      # base case: action = stop
      max_value, max_action = -float('inf'), Directions.STOP
      # get all possible actions of pacman
      actions = gameState.getLegalActions(0)
      actions.remove(Directions.STOP)
      for act in actions:
        # query min values of ghost decisions, now with alpha & beta
        new_value = minValue(gameState.generateSuccessor(0, act), 1, self.depth, alpha, beta)
        if max_value < new_value:
          max_value, max_action = new_value, act
        # stop if lower limit beta isn't reached
        if max_value >= beta:
          return max_value
        # update alpha
        alpha = max(max_value, alpha)
      print(max_value)
      return max_action

    def maxValue(state, index, depth, alpha, beta):
      """returns util value"""
      if state.isWin() or state.isLose() or depth == 0:
        return self.evaluationFunction(state)
      max_value = -float('inf')
      actions = state.getLegalActions(index)
      actions.remove(Directions.STOP)
      for act in actions:
        # take the maximum of min values
        new_value = minValue(state.generateSuccessor(index, act), index + 1, depth, alpha, beta)
        max_value = max(max_value, new_value)
        if max_value >= beta:
          return max_value
        # update alpha
        alpha = max(max_value, alpha)
      return max_value

    def minValue(state, index, depth, alpha, beta):
      """returns util value"""
      if state.isWin() or state.isLose() or depth == 0:
        return self.evaluationFunction(state)
      min_value = float('inf')
      actions = state.getLegalActions(index)
      for act in actions:
        if (index == num_agents - 1):
          # pacman's turn
          new_value = maxValue(state.generateSuccessor(index, act), 0, depth - 1, alpha, beta)
        else:
          # ghost's turn
          new_value = minValue(state.generateSuccessor(index, act), index + 1, depth, alpha, beta)
        min_value = min(min_value, new_value)
        if min_value <= alpha:
          return min_value
        # update beta
        beta = min(min_value, beta)
      return min_value
    # return the result of minimax algorithm
    return alphabetaDecision(gameState)

class ExpectimaxAgent(MultiAgentSearchAgent):
  """
    Your expectimax agent (question 4)
  """

  def getAction(self, gameState):
    """
      Returns the expectimax action using self.depth and self.evaluationFunction

      All ghosts should be modeled as choosing uniformly at random from their
      legal moves.
    """
    "*** YOUR CODE HERE ***"
    num_agents = gameState.getNumAgents()

    def ExpectimaxDecision(state):
      """returns action that maximizes minValue"""
      # base case: action = stop
      max_value, max_action = -float('inf'), Directions.STOP
      # get all possible actions of pacman
      actions = gameState.getLegalActions(0)
      actions.remove(Directions.STOP)
      for act in actions:
        # query min values of ghost decisions
        new_value = weightedValue(gameState.generateSuccessor(0, act), 1, self.depth)
        if max_value < new_value:
           max_value, max_action = new_value, act
      return max_action

    def maxValue(state, index, depth):
      """returns util value"""
      if state.isWin() or state.isLose() or depth == 0:
        return self.evaluationFunction(state)
      max_value = -float('inf')
      actions = state.getLegalActions(index)
      actions.remove(Directions.STOP)
      for act in actions:
        # take the maximum of min values
        new_value = weightedValue(state.generateSuccessor(index, act), index + 1, depth)
        max_value = max(max_value, new_value)
      return max_value

    def weightedValue(state, index, depth):
      """returns util value"""
      if state.isWin() or state.isLose() or depth == 0:
        return self.evaluationFunction(state)
      weighted_avg = 0
      actions = state.getLegalActions(index)
      for act in actions:
        if (index == num_agents - 1):
          # pacman's turn
          weighted_avg += maxValue(state.generateSuccessor(index, act), 0, depth - 1)
        else:
          # ghost's turn
          weighted_avg += weightedValue(state.generateSuccessor(index, act), index + 1, depth)
      return weighted_avg
    # return the result of minimax algorithm
    return ExpectimaxDecision(gameState)

def betterEvaluationFunction(currentGameState):
  #higher score the better#
  """

  1. Higher the score, the better
  2. Further the food is, the worse
  3. If there are ghosts that can be eaten, the futher the worse
  4. If there are no ghosts to eat, the further the capsules are, the worse


    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION:

    If scared ghosts exists (for all ghosts, check scaredTimer != 0):
      scared_ghost_list.append(manhattanDistance(pacman, ghost) <= ghost.scaredTimer)
      If scared_ghost_list != []:
        new_target = min(scared_ghost_list)
        score =
        return score
    If there is a capsule:
      capsule_list.append(manhattanDistance(pacman, capsule))
      new_target = min(capsule_list)
      if manhattanDistance(pacman, ghost) < 3:
        do standard_eval_func
      score =
      return score
    Else (simple world of no scared ghosts or capsules):
      do standard_eval_func
  """
  "*** YOUR CODE HERE ***"
  constant1 = 1
  constant2 = 5
  constant3 = 10000000
  #make sure not to lose
  if currentGameState.isLose():
    return float("-inf")

  # base case #
  score = scoreEvaluationFunction(currentGameState)
  score -= constant1 * foodHeuristic(currentGameState)
  pacPosition = currentGameState.getPacmanPosition()
  ghostStates = currentGameState.getGhostStates()
  noReachableScared = True
  #for each ghost
  for ghostState in ghostStates:
    distance = manhattanDistance(pacPosition, ghostState.getPosition())
    if ghostState.scaredTimer > distance:
      noReachableScared = False
      score -= constant2 * distance

  #There are no scared Ghosts within range: get the closest capsule
  capPositions = currentGameState.getCapsules()
  capDis = [manhattanDistance(pacPosition, capPosition) for capPosition in capPositions]
  if noReachableScared and capDis:
    score -= constant3 * min(capDis)
  return score

def foodHeuristic(state):

  heur = 0
  foodGrid = state.getFood()
  curr_pos = state.getPacmanPosition()
  for x_idx, rows in enumerate(foodGrid):
    for y_idx, is_food in enumerate(rows):
      # if there is a food in a given location
      if is_food:
        # calculate the manhattan distance between current position and food
        # while considering weight using square root
        # analagous to adding misplaced tiles by their manhattan distance
        heur += sqrt(manhattanDistance(curr_pos, [x_idx, y_idx]))
  return heur

# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
  """
    Your agent for the mini-contest
  """

  def getAction(self, gameState):
    """
      Returns an action.  You can use any method you want and search to any depth you want.
      Just remember that the mini-contest is timed, so you have to trade off speed and computation.

      Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
      just make a beeline straight towards Pacman (or away from him if they're scared!)
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

