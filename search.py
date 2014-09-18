import util
import sets
from operator import itemgetter
COST_MATTERS = ["ucs", "aStar", "Greedy"]
## Abstract Search Classes

class SearchProblem:
  """
  Abstract SearchProblem class. Your classes
  should inherit from this class and override 
  all the methods below
  """
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def genericTreeSearch(problem, frontier, algorithm, heuristic = None):
  # initilaize frontier to initial state (state, actions, visited_states), priority)
  visited_states = []
  actions = {}
  actions[problem.getStartState()] = []
  if algorithm in COST_MATTERS:
    frontier.push(problem.getStartState(), 0)
  # no need for total cost in DFS and BFS
  else: 
    frontier.push(problem.getStartState())
  # if frontier is empty, then return failure
  while not frontier.isEmpty(): 
    # node <- remove-first (frontier)
    current_state = frontier.pop()
    visited_states.append(current_state)
    # if goal-test succeeds, then return solution
    if problem.isGoalState(current_state):
      return actions[current_state]
    else:
      # expand(node) to get its children
      for successor, action, stepCost in problem.getSuccessors(current_state):
        # add children into the frontier
        if not successor in visited_states:
          actions[successor] = actions[current_state] + [action]
          if algorithm == "ucs":
            frontier.push(successor, problem.getCostOfActions(actions[successor]))
          elif algorithm == "Greedy":
            frontier.push(successor, heuristic(successor))
          elif algorithm == "aStar":
            frontier.push(successor, problem.getCostOfActions(actions[successor]) + heuristic(successor))
          else:
            frontier.push(successor)
  return []

def tinyMazeSearch(problem):
  """Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze"""
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first. [p 74].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  
  """
  "*** YOUR CODE HERE ***"
  #LIFO
  return genericTreeSearch(problem, util.Stack(), "dfs")

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 74]"
  "*** YOUR CODE HERE ***"
  #frontier is FIFO
  return genericTreeSearch(problem, util.Queue(), "bfs")
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  return genericTreeSearch(problem, util.PriorityQueue(), "ucs")

def nullHeuristic(state):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided searchProblem.  This one is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  return genericTreeSearch(problem, util.PriorityQueue(), "aStar", heuristic)
    
def greedySearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest heuristic first."
  "*** YOUR CODE HERE ***"
  return genericTreeSearch(problem, util.PriorityQueue(), "Greedy", heuristic)

