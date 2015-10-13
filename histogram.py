import os
import csv
import math
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def plot(x, n_bins, name, mu, sigma, var):
  plt.cla()
  n, bins, patches = plt.hist(x, n_bins, normed=1, facecolor='green', alpha=0.5)
  plt.xlim(0, 100)
  plt.title(r'$Mean =' + str(mu) + '$, $SD =' + str(sigma) + '$, $Variance =' + str(var) + '$')

  if not os.path.exists('./data'):
    os.makedirs('./data')
  plt.savefig('./data/' + name + '.png')


with open('./data/population.txt', 'rb') as fp:
  lines = fp.readlines()

numbers = [int(l) for l in lines]
mean = round(np.mean(numbers), 2)
sd = round(np.std(numbers), 2)
var = round(np.var(numbers), 2)

plot(numbers, 25, '500', mean, sd, var)

fp = open('./data/distribution.csv', 'rb')
cr = csv.reader(fp)

index = 0
for row in cr:
  index += 1

  dist = [int(n) for n in row]
  mean = round(np.mean(dist), 2)
  sd = round(np.std(dist), 2)
  var = round(np.var(dist), 2)

  plot(dist, 10, 'Dist ' + str(index), mean, sd, var)

fp.close()
