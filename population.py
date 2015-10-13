#!/usr/local/bin/python

from random import random

numbers = []

for i in xrange(0, 500):
  n = int(random() * 100)
  numbers.append(n)

print len(numbers)

with open('./population.txt', 'wb') as fp:
  num_strings = [str(n) + '\n' for n in numbers]
  fp.writelines(num_strings)
