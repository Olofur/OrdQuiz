###############################################################################
##-##-##.............,....+...!..¤|'''''''''|¤..!...+....,.............##-##-##
##-##-##.............{_.~*^*~.&*^%| main.py |%^*&.~*^*~._}.............##-##-##
##-##-##.............~'^-....<'."?|,,,,,,,,,|?".'>....-^'~.............##-##-##
###############################################################################
# Main script of the OrdQuiz program.
#
# author:oh
 
#!/usr/bin/python

import os
import sys

import time
import random as rd

import numpy as np
import pandas as pd

import nltk

# Implement gui
#import tkinter as tk
#from tkinter import ttk

LANGDIR="Languages"

class OrdQuiz:
	def __init__(self):	
		self.timesup = 30	

		# Load all available languages into list	
		self.langlist = []
		for lang in os.listdir(LANGDIR):
			self.langlist.append(lang)
		
		self.wordlist = {} 		

		self.mainmenu = ["Play", "Settings", "Exit"]
		self.gamemodes = ["Regular"]	
	
		self.start()

	def choicemenu(self):
		pass

	def populate_wordlist(self, language, mode):
		langfile = LANGDIR + "/" + language + "/" + language + ".csv"
		with open(langfile, encoding="utf-8") as f:
			for line in f:
				word, plurmod, gender, translation = line.split(sep=",", maxsplit=3)
				print(word)			
		
	def start(self):
		print("OrdQuiz!")
		
		print("Choose option")
		
		n=1
		for choice in self.mainmenu:	
			print(str(n) + "." + choice)
			n += 1
	
		reply = input()
		
		if reply == "1":
			self.setup()
		elif reply == "2":
			self.settings()
		elif reply == "3":
			self.quit()
		else:
			print("Please choose a valid option")
	
	def setup(self):
		print("Choose language")

		n=1
		for lang in self.langlist:
			print(str(n) + "." + lang)
			n += 1
		print(str(n) + ".Back")

		reply = input()
		quizlang = self.langlist[int(reply)-1]	
		
		print("Choose game mode")
		
		m=1
		for mode in self.gamemodes:
			print(str(m) + "." + mode)
			m += 1
		print(str(m) + ".Back")

		reply = input()
		mode = self.gamemodes[int(reply)-1]	

		self.populate_wordlist(quizlang, mode)

		#self.play(self.wordlist)
	
	def play(self, wordlist):
		os.system('clear')
	
		pass
	
	def settings(self):
		pass

	# Add words to language list
	# Remove words from list
	# Edit words in list
	def managewords(self):
		pass
	
	def quit(self):
		print("Exiting program...")
		exit

if __name__ == "__main__":
	program = OrdQuiz()
else:
	# We are not running at top-level
	pass
