import glob
import os
import sys

maxRuleLen = 5
start = ""

if len(sys.argv) > 1: maxRuleLen = int(sys.argv[1])
if len(sys.argv) > 2: start = sys.argv[2]

def recur(rule):
    print(rule)
    os.system("python langtonsant.py 0 " + rule + " 2 51 51")
    if len(rule) < maxRuleLen:
        for i in range(6):
            recur(rule + str(i))

if start == "":
    recur("1")
    recur("2")
    recur("3")
else:
    recur(start)
