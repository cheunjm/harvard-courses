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


class Reader(object):
    """Reads off .csv file and quizzes user"""
    
    def __init__(self, filename, timer):
        self.data_path = os.path.join(os.getcwd(), "flashcards/%s" % filename)
        self.txt = open(self.data_path, 'rU')
        self.progress = []
        self.timer = timer
        self.reader = csv.reader(self.txt, delimiter=",")
        self.qna, self.prev_knwdge = self.load(self.data_path)
        print "=" * 100
        print("To Quit at any time, just type in \"quit\" or press Enter")
        
    def ask(self, message):
        print "=" * 100
        print message

    def load(self, path):
        """Loads a CSV file returns a dict of answers/questions"""
        self.db = {}
        total = 0 # previous overall understanding level
        entries = 0
        for line in self.reader:
            entries += 1
            total += float(line[2]) * 100
            self.db[line[0]] = [line[1], float(line[2])]
        return self.db, round(total / entries, 2)

    def start(self):
        """
        Protocol for asking questions and verifying. Integrates dyanamic horizon allocation,
        as well as pruning cards that share similar levels of understanding. Multiple choice
        option is also implemented.

        :print: User's improvement of understanding of the deck of flashcards         
        """

        def run_random():
            """Util for generating random multiple choice options"""
            opt1 = random.choice(self.db.values())[0]
            opt2 = random.choice(self.db.values())[0]
            return opt1, opt2

        def update_csv():
            """Update csv file with new understanding levels"""
            with open(self.data_path, 'w') as txt:
                writer = csv.writer(txt, delimiter=',')
                data = []
                total = 0 # new overall understanding level
                for q in self.qna:
                    total += float(self.qna[q][1]) * 100
                    data.append([q, self.qna[q][0], self.qna[q][1]])
                writer.writerows(data)
            return round(total / len(data), 2)

        def prune_likes(orig_dict):
            """
            Before using expectimax on every single Q&A, prune by first traversing
            the list of words and grouping ones that have similar levels of understanding
            and choose one from each group at random to pass onto the algorithm
            """
            # new output dict
            new_dict = {}
            # utility to code in random choice from list (dict is troubling here)
            temp_list = []
            # keep note of which knowledge_level 'class' we've seen 
            pseu_memoizer = []
            for e in orig_dict.items():
                temp_list.append([e[0], e[1][0], e[1][1]])
            random.shuffle(temp_list)
            for item in temp_list:
                knowledge_level = round(float(item[2]), 2) # yields the rounded values
                if knowledge_level not in pseu_memoizer:
                    pseu_memoizer.append(knowledge_level)
                    new_dict[item[0]] = [item[1], item[2]]
            return new_dict

        try:
            init_time = time()
            new_time = 0
            while new_time - init_time < self.timer:
                dict_copy = copy.deepcopy(self.qna)
                print(dict_copy)
                pruned_copy = prune_likes(dict_copy)
                print "pruned length {} / {}".format(len(pruned_copy), len(dict_copy))
                # choose the horizon based on how many nodes we're looking at
                if 30 <= len(pruned_copy):
                    agent = Star1Agent(depth = '2')
                elif 20 <= len(pruned_copy) < 30:
                    agent = Star1Agent(depth = '3')
                elif 10 <= len(pruned_copy) < 20:
                    agent = Star1Agent(depth = '4')
                elif len(pruned_copy) < 10:
                    agent = Star1Agent(depth = '5')
                question = agent.getPolicy(ProgressState(pruned_copy))
                answer = self.qna[question][0]
                if not question or not answer:
                    continue
                self.ask("Question: %s" % question)
                answer_start = time()
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
                answer_end = time()
                time_taken = answer_end - answer_start
                if attempt == "quit" or "":
                    break
                if options[int(attempt) - 1] == answer:
                    self.qna = ProgressState(self.qna,question).generateSuccessor("human", 1, time_taken).getProgress()
                    print "Correct!"
                else:
                    self.qna = ProgressState(self.qna,question).generateSuccessor("human", 0, time_taken).getProgress()
                    print("The correct answer was: %s" % answer)
                new_time = time()
        finally:
            # update csv file
            new_knwdge = update_csv()
            # tells the user improvement since last time
            print "IMPROVEMENT: {} points".format(round((new_knwdge - self.prev_knwdge) / self.prev_knwdge * 1000), 2)


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
