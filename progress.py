
class ProgressState:
   
    def __init__(self, progress, word = None):
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
            copy = self.progress.copy()
            if action == 0: # if the user got the question wrong
                copy[self.word] = copy[self.word]/2
            if action == 1: # if the user got the question right
                copy[self.word] = copy[self.word] + (1 - copy[self.word])/2
            return ProgressState(copy)

    def getProgress(self):
        return self.progress

    def getWord(self):
        return self.word

