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
        self.reader = csv.reader(self.txt, delimiter=",")
        self.qna = self.load(data_path)
        empty = self.is_empty()
        if empty:
            print "=" * 100
            print "The .csv file in %s is empty!" % data_path
        
    def ask(self, message):
        print "="*100
        print message

    def load(self, path):
        """Loads a CSV file returns a dict of answers/questions"""
        db = dict()
        for line in self.reader:
            db[line[0]] = line[1]
        return db

    def start(self):
        """Protocol for asking questions and verifying"""
        for question in self.qna:
            answer = self.qna[question]
            if not question or not answer:
                continue
            self.ask("Question: %s" % question)
            attempt = raw_input(">> ")
            if attempt == answer:
                print "Correct!"
            else:
                print("The correct answer was: %s" % answer)

    def is_empty(self):
        """util for checking if file is empty"""
        txt = self.txt.readlines()
        empty = True
        for line in txt:
            if line:
                empty = False
        return empty

class writer(object):
    """Appends questions and answers into the csv file."""
    
    def __init__(self):
        #File IO object in either 'a' or 'w' mode.
        self.txt = open(data_path,'a')
        #KEY is a list of tuples with strings in them. Each tuple is a pair of question and answer.
        self.KEY = self.get_key() #Gets the questions and answers from the user and stores them in self.KEY for self.start()
        #self.start() #Gets the ball rolling. write() is the function that actually writes information to ./data.csv

    def start(self):
        print "To stop adding cards, type exit or end"
        writer = csv.writer(self.txt)
        for q in self.KEY: #group is a tuple of strings
            question = "%s," % q #string+comma
            answers = self.KEY[q] #string
            progress = "0.5"
            format = question + answers + progress# String with comma separated values. First value is question.
            format = format.split(",") #Split the format string at each comma into a list.
            writer.writerow(format)
        self.txt.close()

    def get_key(self):
        qna = {}
        print "="*72
        while True:
            print "="*100
            question = raw_input("Question: ")
            if question == 'exit' or question == 'end':
                break
            answer = raw_input("Answer: ")
            if answer == 'exit' or answer == 'end':
                break
            qna[question] = answer
        print "\n"
        return qna
