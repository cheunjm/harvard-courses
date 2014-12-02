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
	print("*"*100)


def parse_args():
	parser = argparse.ArgumentParser()
	parer.add_argument('-v', '--version', action='version', version='1.0')
	parser.add_argument('-ls', '--list', dest='list')
	parser.add_argument('-rm', '--remove', dest='remove')
	parser.add_argument('-l', '--load', dest='load')
	parser.add_argument('-u', '--use', dest='use')
	parser.add_argument('-m', '--make', dest='make')
	parser.add_argument('-a', '--add', dest='add')
	
	args = parser.parse_args()
	
	list_ = args.list
	add_ = args.add
	remove_ = args.remove
	load_ = args.load
	use_ = args.use

	make_args.make

	return(list_, add_, remove_, make_, load_, use_)

def main():
	menu()

if __name__ == "__main__":
	main()