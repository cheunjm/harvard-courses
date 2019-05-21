"""
Created on Oct 20, 2013

@author: Ofra
"""
from action import Action
from actionLayer import ActionLayer
from util import Pair
from proposition import Proposition
from propositionLayer import PropositionLayer
from itertools import combinations

class PlanGraphLevel(object):
  """
  A class for representing a level in the plan graph.
  For each level i, the PlanGraphLevel consists of the actionLayer and propositionLayer at this level in this order!
  """
  independentActions = []  # updated to the independentActions of the propblem GraphPlan.py line 31 
  actions = []             # updated to the actions of the problem GraphPlan.py line 32 and planningProblem.py line 25
  props = []               # updated to the propositions of the problem GraphPlan.py line 33 and planningProblem.py line 26
  
  @staticmethod
  def setIndependentActions(independentActions):
    PlanGraphLevel.independentActions = independentActions
  
  @staticmethod  
  def setActions(actions):
    PlanGraphLevel.actions = actions
  
  @staticmethod    
  def setProps(props):
    PlanGraphLevel.props = props   
  
  def __init__(self):
    """
    Constructor
    """
    self.actionLayer = ActionLayer()    		# see actionLayer.py
    self.propositionLayer = PropositionLayer()	# see propositionLayer.py

  
  def getPropositionLayer(self):
    return self.propositionLayer
  
  def setPropositionLayer(self, propLayer):
    self.propositionLayer = propLayer  
  
  def getActionLayer(self):
    return self.actionLayer
    
  def setActionLayer(self, actionLayer):
    self.actionLayer = actionLayer

  def updateActionLayer(self, previousPropositionLayer):
    """ 
    Updates the action layer given the previous proposition layer (see propositionLayer.py)
    allAction is the list of all the action (include noOp in the domain)
    """ 
    allActions = PlanGraphLevel.actions
    previousProps = previousPropositionLayer.getPropositions()
    previousMutexProps = previousPropositionLayer.getMutexProps()
    "*** YOUR CODE HERE ***"
    for action in allActions:
      if (all(precond in previousProps for precond in action.getPre()) and 
        all(pair not in previousMutexProps for pair in combinations(action.getPre(), 2))):
        self.actionLayer.addAction(action)

  def updateMutexActions(self, previousLayerMutexProposition):
    """
    Updates the mutex list in self.actionLayer,
    given the mutex proposition from the previous layer.
    currentLayerActions are the actions in the current action layer
    """
    currentLayerActions = self.actionLayer.getActions()
    "*** YOUR CODE HERE ***"
    for a1, a2 in combinations(currentLayerActions, 2):
      if a1 != a2 and mutexActions(a1, a2, previousLayerMutexProposition):
        self.actionLayer.addMutexActions(a1, a2)

  def updatePropositionLayer(self):
    """
    Updates the propositions in the current proposition layer,
    given the current action layer.
    don't forget to update the producers list!
    """
    currentLayerActions = self.actionLayer.getActions()
    "*** YOUR CODE HERE ***"
    for prop in PlanGraphLevel.props:
      if any(action.isPosEffect(prop) for action in currentLayerActions):
        self.propositionLayer.addProposition(prop)

  def updateMutexProposition(self):
    """
    updates the mutex propositions in the current proposition layer
    """
    currentLayerPropositions = self.propositionLayer.getPropositions()
    currentLayerMutexActions =  self.actionLayer.getMutexActions()
    "*** YOUR CODE HERE ***"
    for p1, p2 in combinations(currentLayerPropositions, 2):
      if p1 != p2 and mutexPropositions(p1, p2, currentLayerMutexActions):
        self.propositionLayer.addMutexProp(p1, p2)

  def expand(self, previousLayer):
    """
    Your algorithm should work as follows:
    First, given the propositions and the list of mutex propositions from the previous layer,
    set the actions in the action layer. 
    Then, set the mutex action in the action layer.
    Finally, given all the actions in the current layer, set the propositions and their mutex relations in the proposition layer.   
    """
    previousPropositionLayer = previousLayer.getPropositionLayer()
    previousLayerMutexProposition = previousPropositionLayer.getMutexProps()

    "*** YOUR CODE HERE ***"   
    self.updateActionLayer(previousPropositionLayer)
    self.updateMutexActions(previousLayerMutexProposition)
    self.updatePropositionLayer()
    self.updateMutexProposition()
    
  def expandWithoutMutex(self, previousLayer):
    """
    Questions 11 and 12
    You don't have to use this function
    """
    previousLayerProposition = previousLayer.getPropositionLayer()
    "*** YOUR CODE HERE ***"
    self.updateActionLayer(previousLayerProposition)
    self.updatePropositionLayer()
		
def mutexActions(a1, a2, mutexProps):
  """
  Complete code for deciding whether actions a1 and a2 are mutex,
  given the mutex proposition from previous level (list of pairs of propositions).
  Your updateMutexActions function should call this function
  """
  "*** YOUR CODE HERE ***"
  if Pair(a1,a2) not in PlanGraphLevel.independentActions:
    return True
  for p1 in a1.getPre():
    for p2 in a2.getPre():
      if Pair(p1,p2) in mutexProps:
        return True
  return False

def mutexPropositions(prop1, prop2, mutexActions):
  """
  complete code for deciding whether two propositions are mutex,
  given the mutex action from the current level (list of pairs of actions).
  Your updateMutexProposition function should call this function
  """
  "*** YOUR CODE HERE ***"
  for a1 in prop1.getProducers():
    for a2 in prop2.getProducers():
      if Pair(a1, a2) not in mutexActions:
        return False
  return True
