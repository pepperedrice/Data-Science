
#Analysing world cup data from 1930 - 2018
#teams, goals, group stages and all
#objectives:
#-practice python algorithms and syntax
#practice data alayisis concepts: numpy, matplotlib, and also using some math and statistics modules 


import csv
import pandas as pd

dataFile = pd.read('world_cups.csv')
print(dataFile)