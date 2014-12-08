# -*- coding: utf-8 -*-

"""
© Copyright 2014. Joon Yang & Jaemin Cheun. All rights reserved.

Deals with creating or reading .csv files to produce flashcards.
"""

from expectimaxAgents import ExpectimaxAgent
from star1Agents import Star1Agent
from progress import ProgressState

from time import time
import os
import csv
import configure
import random
import copy

cwd = os.getcwd()
data_path = os.path.join(cwd, "flashcards.csv")

class Reader(object):
    """Reads off .csv file and quizzes user"""
    
    def __init__(self, filename, timer):
        data_path = os.path.join(cwd, "flashcards/%s" % filename)
        self.txt = open(data_path, 'rU')
        self.progress = []
        self.timer = timer
        self.reader = csv.reader(self.txt, delimiter=",")
        self.qna = self.load(data_path)
        print "=" * 100
        print("To Quit at any time, just type in \"quit\" or press Enter")
        
    def ask(self, message):
        print "="*100
        print message

    def load(self, path):
        """Loads a CSV file returns a dict of answers/questions"""
        self.db = {}
        for line in self.reader:
            self.db[line[0]] = [line[1], float(line[2])]
        return self.db

    def start(self):
        """Protocol for asking questions and verifying"""

        def run_random():
            opt1 = random.choice(self.db.values())[0]
            opt2 = random.choice(self.db.values())[0]
            return opt1, opt2

        def update_csv():
            with open(data_path, 'w') as txt:
                for q in self.qna:
                    new_row = "{0},{1},{2}".format(q, self.qna[q][0], self.qna[q][1]).split(",")
                    print(new_row)
                    csv.writer(txt).writerow(new_row)

        init_time = time()
        new_time = 0
        while new_time - init_time < self.timer:
            agent = Star1Agent(depth = '1')
            dict_copy = copy.deepcopy(self.qna)
            question = agent.getPolicy(ProgressState(dict_copy))
            answer = self.qna[question][0]
            print(self.qna)
            if not question or not answer:
                continue
            self.ask("Question: %s" % question)
            # assuring mutex options
            opt1, opt2 = run_random()
            while opt1 == answer or opt2 == answer:
                opt1, opt2 = run_random()
                while opt1 == opt2:
                    opt1, opt2 = run_random()
            # answer choice is from 1~3
            ans_idx = random.randrange(3)
            # the other (wrong) answer choices
            opt1_idx = (ans_idx + 1) % 3
            opt2_idx = (ans_idx + 2) % 3
            # mechanism for mixing order of options
            options = [1, 2, 3]
            options[ans_idx] = answer
            options[opt1_idx] = opt1
            options[opt2_idx] = opt2
            options.sort()
            for x, option in enumerate(options):
                print("[{0}]: {1}".format(x + 1, option)) 
            attempt = raw_input(">> ")
            if attempt == "quit" or "":
                break
            if options[int(attempt) - 1] == answer:
                self.qna = ProgressState(self.qna,question).generateSuccessor("human", 1).getProgress()
                print "Correct!"
            else:
                self.qna = ProgressState(self.qna,question).generateSuccessor("human", 0).getProgress()
                print("The correct answer was: %s" % answer)
            new_time = time()
        # update csv file
        update_csv()

class Writer(object):
    """Appends questions and answers into the csv file."""
    
    def __init__(self, data_path):
        self.txt = open(data_path,'a')
        self.qna = self.get_qna()

    def start(self):
        writer = csv.writer(self.txt)
        for q in self.qna: # group is a tuple of strings
            question = "%s," % q
            answer = "%s," % self.qna[q]
            progress = "0.5"
            row = (question + answer + progress).split(",")
            writer.writerow(row)
        self.txt.close()

    def get_qna(self):
        print("To stop adding cards, type quit")
        qna = {}
        print "="*100
        while True:
            print "="*100
            question = raw_input("Question: ")
            if question == "quit":
                break
            answer = raw_input("Answer: ")
            if answer == "quit":
                break
            qna[question] = answer
        print "\n"
        return qna
