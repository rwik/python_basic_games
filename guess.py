#!/usr/bin/env python3
#import sys 
import random
from termcolor import colored, cprint

minVal = 1
maxVal = 6

validityFlag = True

while validityFlag :
    cprint("Rolling dice...", 'green', 'on_grey')
    cprint("The value is....", 'green', 'on_grey')
    cprint(random.randint(minVal, maxVal), 'green', 'on_red')
    if(input("Roll the dices again?")=='y') :
        validityFlag = True
    else:
        validityFlag = False    