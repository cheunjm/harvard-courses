from expectimaxAgents import ExpectimaxAgent
from progress import ProgressState

agent = ExpectimaxAgent(depth = '3')
initial = ProgressState([0.1,0.7,0.3,0.2,0.4,0.5,0.2,0.3,0.5,0.3,0.1,0.7,0.3,0.2,0.4,0.5,0.2,0.3,0.5,0.3,0.1,0.7,0.3,0.2,0.4,0.5,0.2,0.3,0.5,0.3])
print agent.getAction(initial)