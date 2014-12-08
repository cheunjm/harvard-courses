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
		try:
			directory = os.listdir(os.path.join(os.getcwd(),"flashcards"))
			for idx, fname in enumerate(directory):
				if fname != ".DS_Store":
					print(str(idx) + " : " + fname)
			print("Type in which flashcard you want to study:")
			filename = directory[int(raw_input(">> "))]
			csv_controller.Reader(filename).start()
		except ValueError:
			exit(0)
	if resp == "2":
		print("\n What would you like to name your new flashcards? \n")
		newcards = raw_input(">> ")
		directory = os.path.join(os.getcwd(), "flashcards/%s.csv" %newcards)
		print(directory)
		try:
			if os.path.exists(directory):
				print("Error: a deck with that name already exists!")
				exit(0)
			else:
				csv_controller.Writer(directory).start()
		except TypeError:
			exit(0)
	if resp == "" or '3':
		exit(0)
	print("="*100)
