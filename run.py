from expectimaxAgents import ExpectimaxAgent
from star1Agents import Star1Agent
from progress import ProgressState

d = '6'
agent = ExpectimaxAgent(depth = d)
initial = ProgressState({"Joon":0.8,"Gene":0.7, "Jaemin":0.6, "Andrew" : 0.62})
print agent.getPolicy(initial)

initial2 = ProgressState({"Joon":0.8,"Gene":0.7,"Jaemin":0.6,"Andrew" : 0.62})
star1agent = Star1Agent(depth = d)
print star1agent.getPolicy(initial2)