#! /usr/bin/env python

import numpy as np
import scipy.stats
import sys

# Takes a file and prints out the average and std dev of each column, skipping the first column
# Uncomment the SEM part to print out the 

def average(infile):
  data = np.loadtxt(infile)
  outfile = open(infile + '.stats', 'w')
  for x in range(1,data.shape[1]):
    segment = data[:x]
    outfile.write(repr(x) + ' ' + repr(np.mean(segment)) + ' ')
    outfile.write(repr(np.std(segment)) + '\n')
    #outfile.write(repr(scipy.stats.sem(segment)) + '\n')

def main():
  average(sys.argv[1])


if __name__ == '__main__':
  main()
