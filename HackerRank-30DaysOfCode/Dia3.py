#!/bin/python3

import math
import os
import random
import re
import sys

def par_impar(n):
    if(n%2!=0):
        print('Weird')
    if(n%2==0):
        if(n>=2 and n<=5 or n>20):
            print('Not Weird')
        if(n>=6 and n<=20):
            print('Weird')

def validacion(n):
    if(n>=1 or n<=100):
        par_impar(n)
    
N = int(input())
validacion(N)