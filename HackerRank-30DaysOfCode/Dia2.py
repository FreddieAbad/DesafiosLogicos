import math
import os
import random
import re
import sys
 
# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
   meal_cost=float(meal_cost)
   tip_percent=float(tip_percent)
   tax_percent=float(tax_percent)
   tip=meal_cost*tip_percent/100
   tax=meal_cost*tax_percent/100
   finalR=round(meal_cost+tip+tax)
   return finalR
 
meal_cost = input()
tip_percent = input()
tax_percent =input()
 
ol=solve(meal_cost, tip_percent, tax_percent)
print (ol)