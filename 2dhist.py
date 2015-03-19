#!/usr/bin/python

import numpy as np

tor1 = np.loadtxt('internalTorsions.gra1', usecols=[1])
tor3 = np.loadtxt('internalTorsions.gra1', usecols=[3])

H, xedges, yedges = np.histogram2d(tor1, tor3, bins=100)

outfile = open('2dhistogram.txt', 'w')

for x in range(0,len(xedges)-1):
  for y in range(0,len(yedges)-1):
    outfile.write('%s %s %s \n' % (57.2957795*xedges[x], 57.2957795*yedges[y], H[x][y]))
  outfile.write('\n')
