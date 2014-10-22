#! /usr/bin/env python

import numpy as np
import scipy.stats
import sys

# Takes a file and prints out the average of all the columns (skipping the first column)

def average(infile, outfile):
  data = np.loadtxt(infile)
  outfile = open(outfile, 'w')
  for x in range(1, data.shape[1]):
    segment = data[:,x]
    outfile.write(repr(np.mean(segment)) + ' ')

def main():
  average(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
  main()
