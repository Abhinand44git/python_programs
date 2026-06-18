'''
import math

print(math.pi)
print(math.sqrt(49))
print(math.pow(2,10))

from math import sqrt

print(sqrt(121))

import random
import string

print(random.randint(1,30))
random_letter=random.choice(string.ascii_letters)
print(random_letter)
small_letter=random.choice(string.ascii_lowercase)
print(small_letter)
capital_letter=random.choice(string.ascii_uppercase)
print(capital_letter)

list1=[1,2,3,4,5]
print(random.choice(list1)) #tryout multiple random generation
print(random.sample(list1,k=2))
#tryout secret module

import datetime
print(datetime.date.today()-datetime.timedelta(1))
#tryout random dates in between specific dates


import sys

print(sys.platform)
print(sys.version)

import os

print(os.getcwd())
print(os.listdir())

#ALIASING given temporary name to imported packaging

import datetime as dt
print(dt.datetime.now())

import requests

url=requests.get('https://jsonplaceholder.typicode.com/users/1')
print(url.json())
'''
