# -*- coding: utf-8 -*-

"""
© Copyright 2014. Joon Yang & Jaemin Cheun. All rights reserved.

Deals with creating or reading .csv files to produce flashcards.
"""

import os
import csv
import configure
from expectimaxAgents import ExpectimaxAgent

cwd = os.getcwd()
data_path = os.path.join(cwd, "flashcards.csv")

class reader(object):
    """Reads off .csv file and quizzes user"""
    
    def __init__(self, filename):
        data_path = os.path.join(cwd, "flashcards/%s" %filename)
        self.txt = open(data_path, 'rU')
        self.progress = []
        self.reader = csv.reader(self.txt, delimiter=",")
        self.qna = self.load(data_path)
        print "=" * 100
        print("To Quit at any time, just type in \"quit\"")
        
    def ask(self, message):
        print "="*100
        print message

    def load(self, path):
        """Loads a CSV file returns a dict of answers/questions"""
        db = dict()
        for line in self.reader:
            db[line[0]] = line[1], line[2]
        return db

    def start(self):
        """Protocol for asking questions and verifying"""
        agent = ExpectimaxAgent(depth = '2')
        agent.getPolicy()

        for question in self.qna:
            answer = self.qna[question]
            if not question or not answer:
                continue
            self.ask("Question: %s" % question)
            attempt = raw_input(">> ")
            if attempt == "quit":
                break
            if attempt == answer:
                print "Correct!"
            else:
                print("The correct answer was: %s" % answer)

class writer(object):
    """Appends questions and answers into the csv file."""
    
    def __init__(self, data_path):
        self.txt = open(data_path,'a')
        self.qna = self.get_qna()

    def start(self):
        writer = csv.writer(self.txt)
        for q in self.qna: # group is a tuple of strings
            question = "%s," % q
            answers = "%s," % self.qna[q]
            progress = "0.5"
            row = (question + answers + progress).split(",")
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
