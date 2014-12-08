# -*- coding: utf-8 -*-

"""
© Copyright 2014. Joon Yang & Jaemin Cheun. All rights reserved.

"""
from expectimaxAgents import ExpectimaxAgent
from star1Agents import Star1Agent
from progress import ProgressState

d = '6'
agent = ExpectimaxAgent(depth = d)
initial = ProgressState({"Joon":["Yang",0.8],"Gene":["Chang",0.7], "Jaemin":["Cheun",0.6], "Andrew" : ["Cho",0.62]})
print agent.getPolicy(initial)

initial2 = ProgressState({"Joon":["Yang",0.8],"Gene":["Chang",0.7], "Jaemin":["Cheun",0.6], "Andrew" : ["Cho",0.62]})
star1agent = Star1Agent(depth = d)
print star1agent.getPolicy(initial2)