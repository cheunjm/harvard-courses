from expectimaxAgents import ExpectimaxAgent
from progress import ProgressState

agent = ExpectimaxAgent()
initial = ProgressState([0.7,0.3])
print agent.getAction(initial)