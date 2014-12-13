# -*- coding: utf-8 -*-
"""
© Copyright 2014. Joon Yang & Jaemin Cheun. All rights reserved.

"""
import copy
from math import log
from cmath import e

class ProgressState:
   
    def __init__(self, progress, word=None):
        self.progress = progress
        self.word = word

    def getLegalActions(self, agentIndex):
        """
        Returns the legal actions for the agent specified.
        """
        if agentIndex == "computer":  # Computer is asking
            # representing which question can be asked
            return list(self.progress.keys())
        else: # Human is answering
            return [0,1]

    def generateSuccessor(self, agentIndex, action, time = 0):
        if agentIndex == "computer": # Computer is asking    
            return ProgressState(self.progress, action) #remember which action is taken
        else: # Human is answering
            # work with the word that only matters
            penalty = 0
            if 2 <time < 5:
                penalty = time * - 0.03
            elif time >= 5:
                penalty = - 0.3
            progress_copy = copy.deepcopy(self.progress)

            def limit_value():
                if progress_copy[self.word][1] < 0.05:
                    progress_copy[self.word][1] = 0.05
                elif progress_copy[self.word][1] > 0.95:
                    progress_copy[self.word][1] = 0.95

            var = progress_copy[self.word][1]
            inner = - pow((var - 0.55), 2)
            middle = pow(e, inner)
            outer = pow(middle, 8)
            if action == 0: # if the user got the question wrong
                progress_copy[self.word][1] -= (outer * -log(var))/2
                limit_value()
            if action == 1: # if the user got the question right
                progress_copy[self.word][1] += (outer * -log(var))/2 + penalty
                limit_value()
            return ProgressState(progress_copy)

    def getnumberWords(self):
        return len(list(self.progress.keys()))

    def getProgress(self):
        return self.progress

    def getWord(self):
        return self.word

    def getProbability(self):
        return self.progress[self.word][1]

    def getAverage(self):
        sumProgress = 0
        for key in self.progress.keys():
            sumProgress = self.progress[key][1] + sumProgress
        return sumProgress/len(list(self.progress.keys()))

