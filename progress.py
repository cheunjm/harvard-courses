<<<<<<< HEAD
# -*- coding: utf-8 -*-
=======
import copy
>>>>>>> 60fc1e3c6b7ff0d570140d06a89ace21583c3d31

"""
© Copyright 2014. Joon Yang & Jaemin Cheun. All rights reserved.

"""
class ProgressState:
   
    def __init__(self, progress, word=None):
        self.progress = progress
        self.word = word

    def getLegalActions(self, agentIndex):
        """
        Returns the legal actions for the agent specified.
        """
        if agentIndex == "computer":  # Computer is asking
            #representing which question can be asked
            return list(self.progress.keys())
        else: #Human is answering
            return [0,1]


    def generateSuccessor(self, agentIndex, action):
        if agentIndex == "computer": # Computer is asking    
            return ProgressState(self.progress, action) #remember which action is taken
        else: # Human is answering
            #work with the word that only matters
            progress_copy = copy.deepcopy(self.progress)
            if action == 0: # if the user got the question wrong
                progress_copy[self.word][1] = progress_copy[self.word][1]/2
            if action == 1: # if the user got the question right
                progress_copy[self.word][1] = progress_copy[self.word][1] + (1 - progress_copy[self.word][1])/2
            return ProgressState(progress_copy)


    def getProgress(self):
        return self.progress

    def getWord(self):
        return self.word
<<<<<<< HEAD
=======

    def getProbability(self):
        return self.progress[self.word][1]

>>>>>>> 60fc1e3c6b7ff0d570140d06a89ace21583c3d31
