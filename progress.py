# -*- coding: utf-8 -*-
"""
© Copyright 2014. Joon Yang & Jaemin Cheun. All rights reserved.

"""
import copy

class ProgressState:
   
    def __init__(self, progress, word=None):
        self.progress = progress
        self.word = word

    def getProgress(self):
        return self.progress

    def getWord(self):
        return self.word

    def getProbability(self):
        return float(self.progress[self.word][1])

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
            if time < 5:
                penalty = time * - 0.05
            elif time >= 5:
                penalty = - 0.3
            progress_copy = copy.deepcopy(self.progress)

            def floor_value():
                if progress_copy[self.word][1] < 0.05:
                    progress_copy[self.word][1] = 0.05

            if action == 0: # if the user got the question wrong
                progress_copy[self.word][1] = progress_copy[self.word][1]/2 + penalty
                floor_value()
            if action == 1: # if the user got the question right
                progress_copy[self.word][1] = progress_copy[self.word][1] + (1 - progress_copy[self.word][1])/2 + penalty
                floor_value()
            return ProgressState(progress_copy)

    def getProgress(self):
        return self.progress

    def getWord(self):
        return self.word

    def getProbability(self):
        return self.progress[self.word][1]
