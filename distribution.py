#!/usr/local/bin/python

import csv
from math import floor
from random import random

with open('./population.txt', 'rb') as fp:
  lines = fp.readlines()

numbers = [int(l) for l in lines]

fp = open('./distribution.csv', 'wb')
cw = csv.writer(fp)

for i in xrange(0, 5):
  dist = []
  for i in xrange(0, 30):
    index = int(floor(random() * 100))
    n = numbers[index]
    dist.append(n)

  cw.writerow(dist)

fp.close()
