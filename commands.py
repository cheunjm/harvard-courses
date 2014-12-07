# -*- coding: utf-8 -*-

"""
© Copyright 2014. Joon Yang & Jaemin Cheun. All rights reserved.

This is where we keep entry points that we use in setup.py for creating command line commands.
Generally, if it uses argparse, it belongs here.
"""

from __future__ import unicode_literals
from __future__ import print_function

import csv_controller
import argparse
import os

def menu():
	"""CSV File as Flashcard Base"""
	print("[1] Start Quiz")
	print("[2] Add Quiz")
	print("[3] Exit")
	resp = raw_input(">> ")
	if resp == "1":
		directory = os.listdir(os.path.join(os.getcwd(),"flashcards"))
		for idx, fname in enumerate(directory):
			print(str(idx+1) + " : " + fname)
		print("Type in which flashcard you want to study:")
		filename = directory[int(raw_input(">> ")) - 1]
		csv_controller.reader(filename).start()
	if resp == "2":
		newcards = raw_input(print("What would you like to name your new flashcards?"))
		directory = os.path.join(os.getcwd(), "flashcards/%s.csv" %newcards)
		if os.path.exists():
			print("Error: a deck with that name already exists!")
			break
		else:
			os.makedirs(directory)
			csv_controller.writer(directory).start()
	if resp == "" or '3':
		exit(0)
	print("="*100)
