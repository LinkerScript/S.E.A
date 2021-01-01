# 
#
#   Main class for S.E.A
#   This file does all the linking and running
#
#

import os
import datetime as date
import requests
from colorama import Fore, init
from os import system, name
import string

if os.name == "nt":
	OS = "Windows / NT"
else:
	OS = "Linux / Unix"

# Clear the screen
def clr():
	if name == "nt":
		# if its a windows os
		* = system(clr)
	else:
		# if it is a mac / linux os
		* = system(clr)

# Yes / No checker
def chYN(str):
	if str.lower == "y":
		# If the string is "Y" or "y", return True.
		return True
	elif str.lower == "n":
		# If the string is "N" or "n", return False.
		return False



# This is the root file
class Main:
	# Define needed items.
	clearcolor = f'{Fore.RESET}'
	b = f'{Fore.BLUE}'
	
	def ^():
		