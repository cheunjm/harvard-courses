# -*- coding: utf-8 -*-

"""
© Copyright 2014. Joon Yang & Jaemin Cheun. All rights reserved.

"""
from expectimaxAgents import ExpectimaxAgent
from star1Agents import Star1Agent
from progress import ProgressState

from time import time

d = '3'

t_1 = time()
agent = ExpectimaxAgent(depth = d)
initial = ProgressState({'Limitone': ['Henry Jarvis', 0.7519029376983644], 'Cooper': ['Robert William', 0.9819955842362976], 'Kocsis': ['John Francis Muldoon', 0.033510377679528455], 'Colford': ['John', 0.6819714460545936], 'Rasmussen': ['Benjamin', 0.9711123260391236], 'Li': ['Andy', 0.989048169173938], 'A. Wang': ['Albert', 0.03351046601400199], 'Rozet': ['Alan', 0.9556768], 'Guajardo': ['Eric', 0.9612320335823059], 'Imbrie': ['John', 0.033509721519133936], 'Luo': ['Michael', 0.7], 'Damiano': ['James', 0.8587413721084595], 'Wu': ['Austin', 0.8170919075224992], 'J. Wang': ['Jeff', 0.03346118067297551], 'J. S. Kim': ['Jiseop', 0.9670897383382059], 'Thao': ['Neng', 0.06195669975913981], 'Dragoi': ['Octav', 0.9585212290298462], 'Choi': ['Ian', 0.9918899714682499], 'Meller': ['Artur', 0.9860032], 'Lessard': ['Michael Kevin', 0.033511481075932124], 'Prosky': ['Daniel', 0.8957022223406879], 'Clemans': ['Parker', 0.03349524789940208], 'Feri': ['Jordan Jeffery John', 0.9706731352057661], 'Kata': ['Karwehn', 0.8138110348057892], 'Peterson': ['Dylan', 0.8870609843025208]})
print agent.getPolicy(initial)
print time() - t_1

t_2 = time()
initial2 = ProgressState({'Limitone': ['Henry Jarvis', 0.7519029376983644], 'Cooper': ['Robert William', 0.9819955842362976], 'Kocsis': ['John Francis Muldoon', 0.033510377679528455], 'Colford': ['John', 0.6819714460545936], 'Rasmussen': ['Benjamin', 0.9711123260391236], 'Li': ['Andy', 0.989048169173938], 'A. Wang': ['Albert', 0.03351046601400199], 'Rozet': ['Alan', 0.9556768], 'Guajardo': ['Eric', 0.9612320335823059], 'Imbrie': ['John', 0.033509721519133936], 'Luo': ['Michael', 0.7], 'Damiano': ['James', 0.8587413721084595], 'Wu': ['Austin', 0.8170919075224992], 'J. Wang': ['Jeff', 0.03346118067297551], 'J. S. Kim': ['Jiseop', 0.9670897383382059], 'Thao': ['Neng', 0.06195669975913981], 'Dragoi': ['Octav', 0.9585212290298462], 'Choi': ['Ian', 0.9918899714682499], 'Meller': ['Artur', 0.9860032], 'Lessard': ['Michael Kevin', 0.033511481075932124], 'Prosky': ['Daniel', 0.8957022223406879], 'Clemans': ['Parker', 0.03349524789940208], 'Feri': ['Jordan Jeffery John', 0.9706731352057661], 'Kata': ['Karwehn', 0.8138110348057892], 'Peterson': ['Dylan', 0.8870609843025208]})
star1agent = Star1Agent(depth = d)
print star1agent.getPolicy(initial2)
print time() - t_2