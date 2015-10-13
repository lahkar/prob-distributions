#!/usr/local/bin/python

import csv
import math
import numpy as np

lines = [['LABEL', 'MEAN', 'SD', 'VARIANCE']]

with open('./data/population.txt', 'rb') as fp:
  nums = fp.readlines()

numbers = [int(l) for l in nums]

mean = round(np.mean(numbers), 2)
sd = round(np.std(numbers), 2)
var = round(np.var(numbers), 2)
print "500 :: Mean = {}, SD = {}, Var = {}".format(mean, sd, var)

lines.append(['500', mean, sd, var])

fp = open('./data/distribution.csv', 'rb')
cr = csv.reader(fp)

index = 0
for row in cr:
  index += 1

  dist = [int(n) for n in row]
  mean = round(np.mean(dist), 2)
  sd = round(np.std(dist), 2)
  var = round(np.var(dist), 2)
  print "Dist {} :: Mean = {}, SD = {}, Var = {}".format(index, mean, sd, var)

  lines.append(['Dist ' + str(index), mean, sd, var])

fp.close()

with open('./data/mean-variance.csv', 'wb') as fp:
  cw = csv.writer(fp)
  for line in lines:
    cw.writerow(line)
