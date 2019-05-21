from util import Pair
import copy
from propositionLayer import PropositionLayer
from planGraphLevel import PlanGraphLevel
from Parser import Parser
from action import Action

try:
  from search import SearchProblem
  from search import aStarSearch

except:
  from  CPF.search import SearchProblem
  from  CPF.search import aStarSearch

class PlanningProblem():
  def __init__(self, domain, problem):
    """
    Constructor
    """
    p = Parser(domain, problem)
    self.actions, self.propositions = p.parseActionsAndPropositions()	# list of all the actions and list of all the propositions
    self.initialState, self.goal = p.pasreProblem() 					# the initial state and the goal state are lists of propositions
    self.createNoOps() 													# creates noOps that are used to propagate existing propositions from one layer to the next
    PlanGraphLevel.setActions(self.actions)
    PlanGraphLevel.setProps(self.propositions)
    self._expanded = 0
   
    
  def getStartState(self):
    "*** YOUR CODE HERE ***"
    return self.initialState
    
    
  def isGoalState(self, state):
    "*** YOUR CODE HERE ***"
    return all(s in state for s in self.goal)
  

  def getSuccessors(self, state):
    """   
    For a given state, this should return a list of triples, 
    (successor, action, stepCost), where 'successor' is a 
    successor to the current state, 'action' is the action
    required to get there, and 'stepCost' is the incremental 
    cost of expanding to that successor
    Hint:  check out action.allPrecondsInList 
    """
    self._expanded += 1
    "*** YOUR CODE HERE ***"
    successors = []
    # for all actions that have all its preconditions satisfied 
    for action in self.actions:
      #NoOp cannot be in an optimal plan
      if not action.isNoOp() and action.allPrecondsInList(state):
        #add positive effects
        successor = state + [prop for prop in action.getAdd() if prop not in state]
        #delete negative effects
        successor = [prop for prop in successor if prop not in action.getDelete()]
        #the cost is one in this case: 1 action
        successors.append((successor, action, 1))
    return successors

  def getCostOfActions(self, actions):
    return len(actions)
    
  def goalStateNotInPropLayer(self, propositions):
    """
    Helper function that returns true if all the goal propositions 
    are in propositions
    """
    for goal in self.goal:
      if goal not in propositions:
        return True
    return False

  def createNoOps(self):
    """
    Creates the noOps that are used to propagate propositions from one layer to the next
    """
    for prop in self.propositions:
      name = prop.name
      precon = []
      add = []
      precon.append(prop)
      add.append(prop)
      delete = []
      act = Action(name,precon,add,delete, True)
      self.actions.append(act)  
      
def maxLevel(state, problem):
  """
  The heuristic value is the number of layers required to expand all goal propositions.
  If the goal is not reachable from the state your heuristic should return float('inf')
  For each state, expand the planning graph omitting the computation of mutex relations, 
  until you reach a level that includes all goal propositions. 
  """
  "*** YOUR CODE HERE ***"
  level = 0
  levelList = []

  #create first layer of graph with proposition layer consisting of that of the state
  propLayerInit = PropositionLayer()
  for prop in state:
      propLayerInit.addProposition(prop)
  pglevelInit = PlanGraphLevel()
  pglevelInit.setPropositionLayer(propLayerInit)
  levelList.append(pglevelInit)

  #check if we are at goal state
  while problem.goalStateNotInPropLayer(levelList[level].getPropositionLayer().getPropositions()):
    # check if stalled
    if isFixed(levelList, level):
      return float('inf')
    # create a new plan graph level
    else:
      level += 1
      pglevelNew = PlanGraphLevel()
      pglevelNew.expandWithoutMutex(levelList[level-1])
      levelList.append(pglevelNew)
  return level

def levelSum(state, problem):
  """
  The heuristic value is the sum of sub-goals level they first appeared.
  If the goal is not reachable from the state your heuristic should return float('inf')
  """
  "*** YOUR CODE HERE ***"


  
def isFixed(Graph, level):
  """
  Checks if we have reached a fixed point,
  i.e. each level we'll expand would be the same, thus no point in continuing
  """
  if level == 0:
    return False
  
  if len(Graph[level].getPropositionLayer().getPropositions()) == len(Graph[level - 1].getPropositionLayer().getPropositions()):
    return True
  return False  
      
      
if __name__ == '__main__':
  import sys
  import time
  if len(sys.argv) != 1 and len(sys.argv) != 4:
    print "Usage: PlanningProblem.py domainName problemName heuristicName(max, sum or zero)"
    exit()
  domain = 'dwrDomain.txt'
  problem = 'dwrProblem.txt'
  heuristic = lambda x,y: 0
  if len(sys.argv) == 4:
    domain = str(sys.argv[1])
    problem = str(sys.argv[2])
    if str(sys.argv[3]) == 'max':
      heuristic = maxLevel
    elif str(sys.argv[3]) == 'sum':
      heuristic = levelSum
    elif str(sys.argv[3]) == 'zero':
      heuristic = lambda x,y: 0
    else:
      print "Usage: PlanningProblem.py domainName problemName heuristicName(max, sum or zero)"
      exit()

  prob = PlanningProblem(domain, problem)
  start = time.clock()
  plan = aStarSearch(prob, heuristic)  
  elapsed = time.clock() - start
  if plan is not None:
    print "Plan found with %d actions in %.2f seconds" % (len(plan), elapsed)
  else:
    print "Could not find a plan in %.2f seconds" %  elapsed
  print "Search nodes expanded: %d" % prob._expanded
 
