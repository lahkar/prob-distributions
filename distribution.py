#!/usr/local/bin/python

import os
import csv
from math import floor
from random import random

if not os.path.exists('./data'):
    os.makedirs('./data')

with open('./data/population.txt', 'rb') as fp:
  lines = fp.readlines()

numbers = [int(l) for l in lines]

fp = open('./data/distribution.csv', 'wb')
cw = csv.writer(fp)

for i in xrange(0, 5):
  dist = []
  for i in xrange(0, 30):
    index = int(floor(random() * 100))
    n = numbers[index]
    dist.append(n)

  cw.writerow(dist)

fp.close()
