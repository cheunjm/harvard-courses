from expectimaxAgents import ExpectimaxAgent
from progress import ProgressState

agent = ExpectimaxAgent(depth = '5')
initial = ProgressState([0.1,0.7,0.3])
print agent.getAction(initial)