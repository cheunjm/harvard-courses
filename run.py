from expectimaxAgents import ExpectimaxAgent
from star1Agents import Star1Agent
from progress import ProgressState

d = '8'
agent = ExpectimaxAgent(depth = d)
initial = ProgressState([0.7,0.4])
print agent.getPolicy(initial)

star1agent = Star1Agent(depth = d)
print star1agent.getPolicy(initial)