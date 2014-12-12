# -*- coding: utf-8 -*-

"""
© Copyright 2014. Joon Yang & Jaemin Cheun. All rights reserved.

"""
from expectimaxAgents import ExpectimaxAgent
from star1Agents import Star1Agent
from progress import ProgressState

from time import time

d = '6'

t_1 = time()
agent = ExpectimaxAgent(depth = d)
initial = ProgressState({"Joon":["Yang",0.9],"Gene":["Chang",0.7], "Jaemin":["Cheun",0.1], "Andrew" : ["Cho",0.8]})
print agent.getPolicy(initial)
print time() - t_1

t_2 = time()
initial2 = ProgressState({"Joon":["Yang",0.9],"Gene":["Chang",0.7], "Jaemin":["Cheun",0.1], "Andrew" : ["Cho",0.8]})
star1agent = Star1Agent(depth = d)
print star1agent.getPolicy(initial2)
print time() - t_2