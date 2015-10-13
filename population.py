#!/usr/local/bin/python

import os
import numpy as np
from random import random

numbers = []

for i in xrange(0, 500):
  n = int(random() * 100)
  # n = int(((np.random.randn() + 3.5) / 7) * 100)
  # n = int(np.random.weibull(5) * 100)
  # n = int((np.random.exponential() / 8) * 100)
  # n = int(((np.random.gumbel() + 2) / 10) * 100)
  # n = int(((np.random.logistic() + 10) / 20) * 100)
  # n = int((np.random.rayleigh() / 4) * 100)
  # n = int(np.random.uniform() * 100)

  numbers.append(n)

print len(numbers), max(numbers), min(numbers)

if not os.path.exists('./data'):
    os.makedirs('./data')

with open('./data/population.txt', 'wb') as fp:
  num_strings = [str(n) + '\n' for n in numbers]
  fp.writelines(num_strings)
