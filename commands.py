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

def menu():
	"""CSV File as Flashcard Base"""
	print("[1] Start Quiz")
	print("[2] Add Quiz")
	print("[3] Exit")
	resp = raw_input(">> ")
	if resp == "1":
		csv_controller.reader().start()
	if resp == "2":
		csv_controller.writer().start()
	if resp == "" or '3':
		exit(0)
	print("="*100)
